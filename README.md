# Patdel_GenAI_Assignment


Problem Statement:
The task involves creating a REST API system that facilitates searching through documents stored in JSON format. The system should expose a single endpoint named "search" which accepts a query parameter. Upon receiving a query, the API should return the most relevant documents based on the provided query.

Solution Overview:
The provided code initializes a FastAPI application that implements the required functionality. It loads documents from JSON files, preprocesses the text data, computes embeddings using the SentenceTransformer model, and sets up a Faiss index for efficient similarity search. When a query is received, the system computes embeddings for the query, finds the nearest neighbors in the embedding space, and returns the relevant documents along with their distances from the query.

GitHub README Information:
1. Overview: This system provides a REST API endpoint named "search" for searching through documents stored in JSON format.
2. Functionality: Users can submit a query through the API, and the system returns the most relevant documents based on the query.
3. Setup: Ensure that Python 3.11 or later is installed. Install the required dependencies listed in the requirements.txt file using pip install -r requirements.txt.
4. Usage: Start the server by running the provided script. Access the API documentation at http://0.0.0.0:8000/docs for information on how to interact with the API.
5. Dataset: The documents used by the system are stored in JSON format and should be placed in the specified directory before running the application.
6. Docker Deployment: The FastAPI application can be deployed using a Docker container with given docker file and requirements file for easy management and scalability.
