import gradio as gr
from google.cloud import speech
import io
from scipy.io.wavfile import write
import numpy as np
import os
from pydub import AudioSegment

# Set up Google Cloud authentication
google_credentials = os.path.join(os.getcwd(), "service_account_speech_to_text.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials

client = speech.SpeechClient()

def transcribe_audio(sound):
    print("Received sound:", sound)
    sample_rate, audio_data = sound  # Unpack the audio data

    # for local testing the audio has two channels, for production use 1 channel
    # gradio live link interface doesn't work with any type of audio 

    # Keep it for production and remove it for local testing
    # if audio_data.ndim > 1:
    #     audio_data = audio_data.mean(axis=1)

    # Ensure audio_data is in int16 format for LINEAR16 encoding
    if audio_data.dtype != np.int16:
        audio_data = (audio_data * 32767).astype(np.int16)

    # Create an in-memory buffer to hold the WAV data
    with io.BytesIO() as wav_buffer:
        write(wav_buffer, sample_rate, audio_data)
        wav_buffer.seek(0)
        content = wav_buffer.read()

    # Prepare the audio data for the API
    audio = speech.RecognitionAudio(content=content)

    # Configure the transcription settings
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="ar-EG",  # Change to your target language code
        audio_channel_count = 2 # for production use 1 for local testing use 2
    )

    # Perform the transcription
    response = client.recognize(config=config, audio=audio)

    # Extract the transcribed text
    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript + ' '

    print("Transcript:", transcript)

        # Convert the audio to MP3
    audio_segment = AudioSegment.from_wav(io.BytesIO(content))
    mp3_file_path = "recorded_audio.mp3"
    audio_segment.export(mp3_file_path, format="mp3")

    if transcript.strip().lower() in ['سهلة', 'سهله']:
        video_file_path = "sahla.mp4"
    else:
        video_file_path = "hand.mp4" 

    return transcript.strip(), mp3_file_path, video_file_path

# Create the Gradio interface
demo = gr.Interface(
    fn=transcribe_audio, 
    inputs=gr.Audio(type="numpy"), 
    outputs=[gr.Textbox(), gr.Audio(), gr.Video()],
    title="Speech-to-Text Transcription",
    description="Record your voice and get a transcription using Google Cloud Speech-to-Text API."
)

demo.launch(share=True, show_error=True)
