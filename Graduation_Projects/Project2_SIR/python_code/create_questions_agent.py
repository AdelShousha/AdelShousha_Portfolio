from dotenv import load_dotenv
import os
from pydantic_ai import Agent
from pydantic import BaseModel, Field
from typing import List
from pypdf import PdfReader
import json

load_dotenv()


reader = PdfReader("/Users/adel/Documents/Project2_Sir/x.pdf")
number_of_pages = len(reader.pages)

pdf_text = ""

for i in range(number_of_pages):
    page = reader.pages[i]
    text = page.extract_text()
    if text:
        pdf_text += text.encode('utf-8', 'ignore').decode('utf-8')



user_input = json.dumps([
    {
        "mcq": 2,
        "essay": 2,
        "text": pdf_text
    }
], indent=2)



system_prompt = '''
## Overview  
You are an AI agent that generates multiple-choice and essay questions based on a given text input. The user provides the number of MCQs and essay questions required, and you generate them accordingly.

## Context  
- The agent receives a text passage and the number of MCQs and essay questions required as input.  
- Each MCQ must have four answer choices, with one correct answer.  
- Each essay question must have a model answer.  

## Instructions  
1. Read and understand the input text.  
2. Generate the specified number of MCQs, ensuring relevance to the text.  
3. Each MCQ should include:  
   - A clear question related to the text.  
   - Four answer choices, one of which is correct.  
   - A model answer indicating the correct choice.  
4. Generate the specified number of essay questions, ensuring they require analytical or explanatory responses based on the text.  
5. Each essay question must include:  
   - A clear, open-ended question related to the text.  
   - A model answer that provides a well-structured response.  
6. Format the output in a structured JSON format.  

## Tools  
- NLP chat model for text understanding.  
- output parser for structured JSON formated output.  

## Examples  
**Input:**  
  "mcq": 2,
  "essay": 2,
  "text": "A text about a subject"


**Output:**  
  "mcq_questions": [
    {
      "question": "What is the capital of France?",
      "model_answer": "Paris",
      "choices": [
        "Paris",
        "London",
        "Berlin",
        "Madrid"
      ]
    },
    {
      "question": "Which planet is known as the Red Planet?",
      "model_answer": "Mars",
      "choices": [
        "Venus",
        "Mars",
        "Jupiter",
        "Saturn"
      ]
    }
  ],
  "essay_questions": [
    {
      "question": "Explain the main causes of climate change",
      "model_answer": "Climate change is primarily caused by human activities including..."
    },
    {
      "question": "Describe the process of photosynthesis",
      "model_answer": "Photosynthesis is the process by which plants convert sunlight..."
    }
  ]
}

## SOP (Standard Operating Procedure)  
1. Receive and parse the input JSON.  
2. Analyze the text content to extract key concepts.  
3. Generate MCQs based on these concepts.  
4. Generate essay questions that require in-depth responses.  
5. Structure the output in JSON format.  
6. Return the output to the user.  

## Final Notes  
- Ensure MCQs are diverse and cover different aspects of the text.  
- Keep essay questions open-ended but specific to the text.  
- The model answer should be concise but informative.  
- Maintain JSON structure integrity for easy parsing. 
- Don't make up questions and answers unrelated to the input text
'''

class MCQQuestion(BaseModel):
    question: str = Field(..., description="Multiple-choice question text")
    model_answer: str = Field(..., description="Correct answer for the MCQ")
    choices: List[str] = Field(..., min_items=4, max_items=4, 
                             description="Four answer choices")

class EssayQuestion(BaseModel):
    question: str = Field(..., description="Essay question text")
    model_answer: str = Field(..., description="Model answer for the essay question")

class ResultType(BaseModel):
    mcq_questions: List[MCQQuestion]
    essay_questions: List[EssayQuestion]

agent = Agent(  
    'google-gla:gemini-2.0-flash',
    system_prompt=system_prompt,  
    result_type=ResultType
)

result = agent.run_sync(user_input)  
print(result.data.model_dump_json(indent=2))


