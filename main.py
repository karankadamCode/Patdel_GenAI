import json
from sentence_transformers import SentenceTransformer, util
import os
import csv
import time
import torch
import pickle


# Specifying the path to the directory containing your JSON files
json_directory = 'C:\\Users\\karan.kadam\\Desktop\\Patdel_ML_Assignment\\patent_jsons'

# Initializing an empty list to store the text data from each document
text_data = []

# Iterating over each JSON file in the directory
for filename in os.listdir(json_directory):
    
    if filename.endswith('.json'):
        # Construct the full path to the JSON file
        json_file_path = os.path.join(json_directory, filename)
        
        # Open the JSON file and read its content
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            text_data.append(str(data['descriptions']))


# Specifying the path to the pickle file containing the corpus embeddings
pickle_file_path = 'corpus_embeddings2.pickle'

# Loading the corpus embeddings from the pickle file
with open(pickle_file_path, 'rb') as f:
    corpus_embeddings = pickle.load(f)


# printing its shape to verify the loaded embeddings
print("Shape of corpus embeddings:", corpus_embeddings.shape)

if not torch.cuda.is_available():
   print("Warning: No GPU detected. Processing will be slow. Please add a GPU to this notebook")

# model initialization
model = SentenceTransformer('LaBSE')


# Function that searches the corpus and prints the results
def search(inp_question):

    start_time = time.time()
    question_embedding = model.encode(inp_question, convert_to_tensor=True)

    hits = util.semantic_search(question_embedding, corpus_embeddings)
    end_time = time.time()

    hits = hits[0]  #Get the hits for the first query

    print("Input question:", inp_question)
    print("Results (after {:.3f} seconds):".format(end_time-start_time))

    for hit in hits[0:3]:
        # print("\t{:.3f}\t{}".format(hit['score'], text_data[hit['corpus_id']]))
        response = "\t{:.3f}\t{}".format(hit['score'], text_data[hit['corpus_id']])

    return response



