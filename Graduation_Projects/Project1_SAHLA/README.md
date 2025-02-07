# 👐 SAHLA - Speech And Hearing Language Assistant

SAHLA is a **mobile application** designed to facilitate communication for **non-hearing** and **non-speaking** individuals. It provides a real-time solution that transforms **Arabic Sign Language (ArSL) into text and speech, and vice versa**. Our goal is to create an **inclusive world** where everyone, regardless of their hearing or speaking abilities, can connect, communicate, and thrive with ease.

## 💪 My Role in SAHLA
I was the **project lead** for SAHLA and I was responsible for designing  **system architecture** of SAHLA. I created the technical system diagrams to showcase the app’s structure, workflow, and integration of various components.

Additionally, I developed the **machine learning** components, including:
- **Speech-to-Text and Sign Language Translation**
- **Sign Language to Speech and Text Translation**

This involved working with **OpenCV, MediaPipe, Different APIs such as Google speech to text and text to speech and Elevenlabs API**, and deploying the models using **Gradio and Hugging Face**.



---

## 🚀 SAHLA Features
- **🛠️ Translation between Arabic Sign Language (ArSL) and text & speech**
- **🎨 3D hand model integration for sign visualization**
- **📱 Mobile-friendly interface** for easy accessibility.

---

## 🏰 Tech Stack
- **Mobile Development:** [React Native](https://github.com/Project1-Sahla/sahla) *(SAHLA mobile app repository)*
- **Machine Learning:** OpenCV, MediaPipe
- **Speech-to-Text:** Google Speech-to-Text API
- **Text-to-Speech:** Google Text-to-Speech API, ElevenLabs API
- **3D Hand Model Creation:** Blender
- **Deployment:** Gradio, Hugging Face

---
## 🗂️ Project Resources
All project-related materials, including **demo videos, screenshots, documentation, and presentations**, can be found in the [`Project_Resources`](Project_Resources/) folder.

### 📂 Folder Contents:
- 🎥 **Demo Video** (`SAHLA_Demo.mp4`)
- 📸 **App Screenshots** (`screenshots/`)
- 📖 **Project Book** (`SAHLA_Project_Book.pdf`)
- 📜 **Brochure** (`SAHLA_Brochure.pdf`)
- 🖼️ **Project Banner** (`SAHLA_Banner.png`)
- 📊 **Presentation Slides** (`SAHLA_Slides.pptx`)
- 🏗 **System Diagrams** (`system_diagrams/`) – Contains system architecture and other technical diagrams.
---
## 📂 Dataset
We utilized the following dataset for training the sign language recognition models:
- **Original Dataset:** [RGB Arabic Alphabets Sign Language Dataset (Kaggle)](https://www.kaggle.com/datasets/muhammadalbrham/rgb-arabic-alphabets-sign-language-dataset/data)
- **Edited Dataset (Compatible with MediaPipe Training Architecture):** [Google Drive Link](https://drive.google.com/drive/folders/1GN4GCYEovlZytrDVBL_V5Wa1uBgTCOsK?usp=share_link)

---
## 📸 Screenshots & Demo
🚀 **[Demo Video](INSERT_YOUTUBE_OR_GOOGLE_DRIVE_LINK_HERE)**  
🎨 **Screenshots:**  
| Splash | Home Screen | Output Screen | loading screen |
|------------|---------------|-------------|------|
| ![Screenshot 1](INSERT_IMAGE_LINK_HERE) | ![Screenshot 2](INSERT_IMAGE_LINK_HERE) | ![Screenshot 3](INSERT_IMAGE_LINK_HERE) | ![Screenshot 4](INSERT_IMAGE_LINK_HERE) |

---
## 🎯 **System Architecture Explanation**
![System Architecture](INSERT_IMAGE_LINK_HERE)


#### **1️⃣ Sign Language to Speech Translation**
1. **Sign Language video is recorded** by the mobile app.
2. The **video frames are sent** to the **first Python script** in the backend.
3. The **Python script processes the video frames** and sends them to the **MediaPipe model**, which converts the sign language into text.
4. The **text is then sent to Google TTS**, which converts it into spoken audio.
5. **Both the generated text and audio are sent back to the mobile app** for display to the user.



#### **2️⃣ Speech to Sign Language Translation**
1. **User records an audio message** in the mobile app.
2. The **audio is sent to the second Python script** in the backend.
3. The **audio is processed and sent to Google STT**, which converts it into text.
4. The **text is then converted into sign language** using a **3D hand model**.
5. **Both the generated text and the sign language animation (video) are sent back to the mobile app** for display to the user.

---









## 🔧 Installation & Setup

### Step 1: Create a Virtual Environment

First, navigate to the specific folder (`sign2speech` or `speech2sign`) you want to run. Open your terminal or command prompt and run the following command to create a virtual environment.

#### On Windows:
```bash
python -m venv env
```

#### On Linux/MacOS:
```bash
python3 -m venv env
```

### Step 2: Activate the Virtual Environment

Activate the virtual environment you just created:

#### On Windows:
```bash
.\env\Scripts\activate
```

#### On Linux/MacOS:
```bash
source env/bin/activate
```

Once the virtual environment is activated, your command prompt or terminal should show the environment name (e.g., `(env)`).

### Step 3: Install Dependencies

install the necessary Python packages listed in `requirements.txt` by running:

```bash
pip install -r requirements.txt
```

This will install all the dependencies required for the project.


### Step 4: 
### For `sign2speech` :

- **`gradio_elevenlabs_video_to_speech_and_text.py`**: A Python script that uses Gradio to create a web interface. It takes a video of sign language and converts it to text and speech using the ElevenLabs API.
- **`gradio_google_video_to_speech_and_text.py`**: A Python script similar to the one above, but it uses Google Text-to-Speech for speech synthesis.
- **`Amiri-Regular.ttf`**: A font file used in the code for text rendering.
- **`Arsl_gesture_recognizer.task`**: A MediaPipe gesture recognition model that recognizes Arabic language letters.

    ### Usage

    1. Navigate to the `sign2speech` folder and activate the virtual environment and .
    2. Run one of the Python scripts:
    - For ElevenLabs speech synthesis:
        ```bash
        python gradio_elevenlabs_video_to_speech_and_text.py
        ```
    - For Google Text-to-Speech:
        ```bash
        python gradio_google_video_to_speech_and_text.py
        ```
    3. Access the web interface by clicking on the link provided in the terminal or by navigating to `http://localhost:7860` in your web browser.

### For `speech2sign`

- **`gradio_speech_to_text_and_video.py`**: A Python script that uses Gradio to create a web interface. It takes speech input, converts it to text using Google Speech-to-Text, and then converts the text to a video of sign language.

    ### Usage
    1. Activate the virtual environment and navigate to the `speech2sign` folder.
    2. Run the Python script:
    ```bash
    python gradio_speech_to_text_and_video.py
    ```
    3. Access the web interface by clicking on the link provided in the terminal or by navigating to `http://localhost:7860` in your web browser.
---
## 🔗 Dependencies

Make sure you have the following installed:

- ElevenLabs API key (for `gradio_elevenlabs_video_to_speech_and_text.py`)
- Google Cloud Speech-to-Text and Text-to-Speech API keys (for `gradio_speech_to_text_and_video.py` and `gradio_google_video_to_speech_and_text.py`)

---
## 🛠️ Development Notebooks

This section provides an overview of the Jupyter notebooks used in the development of the project.

### `data_prep.ipynb`

This notebook is used for data preparation, including data cleaning, preprocessing, and splitting the data into training and testing sets. It ensures that the data is in the correct format and ready for model training.

### `train_gesture_recognizer.ipynb`

In this notebook, the gesture recognizer model is trained. It includes setting up the model architecture, defining training parameters, and running the training loop. This notebook is essential for developing the model's ability to recognize gestures accurately.

### `test_gesture_recognizer.ipynb`

This notebook is used to evaluate the performance of the trained gesture recognizer model. It involves testing the model on a validation dataset to assess its accuracy and effectiveness.


## Instructions for Running Notebooks

1. **Environment Setup**: Make sure you have a Python environment set up with all dependencies installed.
2. **Running Notebooks**: Open the notebooks in Jupyter or any compatible notebook interface and run them in the specified order.
---
## 🤗 Deployment

Explore the live demos of the projects on Hugging Face Spaces:

- [Sahla-speech2sign](https://huggingface.co/spaces/AdelShousha/Sahla-speech2sign)
- [Sahla-sign2speech](https://huggingface.co/spaces/AdelShousha/Sahla-sign2speech)

This allows you to experience the functionality without setting up the environment locally.


