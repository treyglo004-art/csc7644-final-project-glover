# RAG-Based AI System for Engineering Questions

## Overview
This project is my final project for CSC 7644: Applied LLM Development. It is a simple Retrieval-Augmented Generation (RAG) style system that answers engineering questions using course materials.

The goal is to reduce incorrect or made-up AI responses by first retrieving relevant document content and then generating an answer based on that information.

## Key Features
- Answers engineering related questions
- Searches course materials for relevant information
- Displays retrieved content
- Provides a grounded answer based on the documents
- Uses a simple Streamlit interface

## Tech Stack
- Python
- Streamlit
- Basic document retrieval
- Course material text file

## Architecture
User Question → Document Search → Retrieved Course Material → Answer Output

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/treyglo004-art/csc7644-final-project-glover.git