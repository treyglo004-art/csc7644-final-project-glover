# RAG-Based AI System for Engineering Questions

## Overview
This project is my final project for CSC 7644: Applied LLM Development. It is a simple Retrieval-Augmented Generation (RAG) style system that answers engineering questions using course materials.

The goal is to reduce incorrect or made-up AI responses by first retrieving relevant document content and then generating an answer based on that information.

## Key Features
- Answers engineering-related questions  
- Searches course materials for relevant content  
- Displays retrieved document content  
- Generates grounded responses based on retrieved information  
- Uses a simple Streamlit interface for user interaction  
- Reduces hallucinations compared to traditional LLM-only responses

## Tech Stack
### Technologies Used
- Python  
- Streamlit  
- Text document retrieval  
- Local engineering notes dataset  

## Architecture
User Question → Document Search → Retrieved Course Material → Answer Output

## Setup Instructions

Before running the project, make sure you have:

Python 3.10 or newer
pip installed
Git installed

1. Clone the repository:
   ```bash
   git clone https://github.com/treyglo004-art/csc7644-final-project-glover.git
2. Install Dependencies:
pip install -r requirements.txt

## Running the Application
Run the application using:

streamlit run app.py

After running this command, Streamlit will open in your browser (typically at http://localhost:8501).

Users can type engineering-related questions into the text box and receive grounded responses based on the engineering notes dataset. To keep it simple I only inputted three questions and answers, I have listed the questions that can be asked:

Example Questions:
- What is Ohm’s Law?
- What is stress in materials engineering?
- What is a control system?

## Repository Organization

Main Files
- app.py → Main Streamlit application
- README.md → Project documentation
- requirements.txt → Python dependencies
- .env.example → Example environment variables
- .gitignore → Prevents sensitive files from being uploaded

Data Folder
- data/sample_engineering_notes.txt → Engineering notes used for retrieval

Source Folder
- src/data_loader.py → Document loading logic
- src/retriever.py → Retrieval logic
- src/llm_client.py → Future LLM integration
- src/rag_pipeline.py → Future pipeline orchestration

Evaluation Folder
- evaluation/test_questions.py → Testing questions

## Evaluation

The application was tested using:

- What is Ohm’s Law?
- What is stress?
- What is a control system?

Evaluation focused on:

- Accuracy
- Relevance of retrieved content
- Reduced hallucination
- User experience

## Attributions and Citations


This project was inspired by concepts learned in CSC 7644: Applied LLM Development.

Research Reference

Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. arXiv.
https://arxiv.org/abs/2005.11401





















