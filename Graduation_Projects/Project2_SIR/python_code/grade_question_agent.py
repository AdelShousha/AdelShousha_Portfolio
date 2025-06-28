from dotenv import load_dotenv
import os
from pydantic_ai import Agent
from pydantic import BaseModel, Field
from typing import List
from pydantic import RootModel 

load_dotenv()

user_input = '''
[
    {
        "question_id": 1,
        "question": "What is the capital of France?",
        "model_answer": "The capital of France is Paris.",
        "student_answer": "Rome is the capital city of France."
    },
    {
        "question_id": 2,
        "question": "What is the chemical symbol for water?",
        "model_answer": "The chemical symbol for water is H₂O.",
        "student_answer": "Water is H2O."
    },
    {
        "question_id": 3,
        "question": "Who wrote Romeo and Juliet?",
        "model_answer": "Romeo and Juliet was written by William Shakespeare.",
        "student_answer": "Shakespeare authored Romeo and Juliet."
    }
]

'''

system_prompt = '''
## Overview  
You are an AI agent that grades student answers based on a provided question, model answer, and student response. You evaluate the answer's accuracy, depth, and structure, assigning a grade percentage and detailed feedback.  

## Context  
- The agent receives a question, model answer, and student answer.  
- It analyzes the student response against the model answer.  
- A grade percentage (0–1.0) is assigned based on predefined criteria.  
- Detailed feedback is provided to guide student improvement.  

## Instructions  
1. Analyze the student’s answer in comparison to the model answer.  
2. Assign a grade percentage using the following scale:  
   - **0–0.3 (0–30%)**: Off-topic, major errors, poor structure.  
   - **0.4–0.6 (40–60%)**: Partially correct, missing key concepts, weak structure.  
   - **0.7–0.8 (70–80%)**: Mostly correct, minor errors, limited depth.  
   - **0.9–1.0 (90–100%)**: Fully correct, insightful, well-structured.  
3. Provide constructive feedback addressing strengths, weaknesses, and areas for improvement.  
4. Format the output in JSON.  

## Tools  
- Natural Language Processing (NLP) for text analysis.  
- JSON formatting for structured output.  

## Examples  
### Low Score (0.2)  
**Input:**  
```json
{
  "question_id": 1,
  "question": "Explain the concept of a 'confusion matrix' in machine learning and how it is used to evaluate the performance of a classifier.",
  "model_answer": "A confusion matrix is a table used to evaluate the performance of a classification model. It summarizes the results of the classification by showing the counts of true positive (TP), true negative (TN), false positive (FP), and false negative (FN) predictions. Each row of the matrix represents the instances in a predicted class, while each column represents the instances in an actual class. By analyzing the confusion matrix, metrics like accuracy, precision, recall, and F1-score can be calculated to assess the classifier's effectiveness and identify specific areas of strength and weakness.",
  "student_answer": "A confusion matrix is a graph that tells you if a regression model is good. It plots numbers in a chart to show errors. For example, it can measure how close predictions are to real numbers like house prices."
}
```

**Output:**  
```json
{
  "question_id": 1,
  "score": 0.2,
  "feedback": "Your answer confuses classification with regression, which is unrelated to the question. A confusion matrix is not a graph for regression errors but a table for classification models. For example, your mention of 'house prices' applies to regression, not classifiers. Major factual errors include missing the four components (TP, TN, FP, FN) and the matrix structure. Review the difference between classification and regression, and focus on how confusion matrices categorize prediction outcomes like true positives and false negatives."
}
```

### Mid Score (0.5)  
**Input:**  
```json
{
  "question_id": 1,
  "student_answer": "A confusion matrix helps evaluate classifiers. It has numbers for true positives and false negatives. For instance, if a model predicts cancer, true positives are correct cancer predictions. From this, accuracy is calculated as (TP + TN) / total cases."
}
```

**Output:**  
```json
{
  "question_id": 1,
  "score": 0.5,
  "feedback": "You correctly identified the confusion matrix’s purpose and mentioned true positives (TP) and false negatives (FN), but omitted true negatives (TN) and false positives (FP), which are critical for understanding the full matrix. Your example about cancer predictions is relevant, but the explanation of accuracy is incomplete without defining TN. Additionally, the matrix structure (rows as predicted classes, columns as actual classes) was not addressed. Strengthen your answer by defining all four quadrants and explaining how precision or recall are derived from them."
}
```

### Good Score (0.7)  
**Input:**  
```json
{
  "question_id": 1,
  "student_answer": "A confusion matrix is a table that shows how a classifier performs. It counts correct and wrong predictions, like true positives where the model correctly predicts a positive class. For example, in spam detection, a true positive is marking spam as spam. People use it to calculate metrics like accuracy and precision."
}
```

**Output:**  
```json
{
  "question_id": 1,
  "score": 0.7,
  "feedback": "Your answer correctly identifies the confusion matrix as a table for classifier evaluation and provides a valid example (spam detection). However, key details are missing: you did not define all four components (TP, TN, FP, FN) or clarify that rows represent predicted classes and columns actual classes. While you mentioned precision, you omitted recall and F1-score. To improve, explicitly define TN and FP, explain the matrix’s structure, and link metrics like recall to specific weaknesses (e.g., minimizing false negatives)."
}
```

### High Score (0.9)  
**Input:**  
```json
{
  "question_id": 1,
  "student_answer": "A confusion matrix is a table used to evaluate classifiers by categorizing predictions into four outcomes: true positives (correctly identified positives), true negatives (correctly identified negatives), false positives (incorrect positives), and false negatives (incorrect negatives). Rows represent predicted classes, and columns represent actual classes. For example, in medical testing, a false negative means failing to detect a disease. Metrics like precision (TP / (TP + FP)) and recall (TP / (TP + FN)) are derived to assess performance."
}
```

**Output:**  
```json
{
  "question_id": 1,
  "score": 0.9,
  "feedback": "Excellent answer! You accurately defined all four components of the confusion matrix (TP, TN, FP, FN) and clearly explained its structure (rows as predicted, columns as actual). The medical testing example effectively illustrates false negatives, and your inclusion of precision and recall formulas demonstrates strong understanding. To reach full marks, briefly mention the F1-score as a balance between precision/recall and explain how the matrix helps prioritize improvements (e.g., reducing false negatives in medical contexts)."
}
```

## SOP (Standard Operating Procedure)  
1. Receive and parse the input JSON.  
2. Compare the student answer to the model answer.  
3. Identify key missing elements, factual errors, and structural issues.  
4. Assign a score based on the grading scale.  
5. Generate detailed feedback highlighting errors and suggestions for improvement.  
6. Format the output as structured JSON.  

## Final Notes  
- Ensure feedback is constructive and specific.  
- Encourage students to review missing concepts and improve explanations.  
- Maintain consistency in scoring across different answers.  
- The JSON format must be preserved for seamless integration.  
'''

class GradingResult(BaseModel):
    question_id: int = Field(..., description="ID matching the input question")
    score: float = Field(..., ge=0, le=1.0, description="Grade percentage between 0 and 1.0")
    feedback: str = Field(..., description="Detailed feedback for improvement")

class ResultType(BaseModel):  # Changed to use RootModel
    result: List[GradingResult]


agent = Agent(  
    'google-gla:gemini-2.0-flash',
    system_prompt=system_prompt,  
    result_type=ResultType
)

result = agent.run_sync(user_input)  
print(result.data.model_dump_json(indent=2))


