import json
import os
from sentence_transformers import SentenceTransformer
import torch
import pickle

# Specify the path to the directory containing your JSON files
json_directory = 'C:\\Users\\karan.kadam\\Desktop\\Patdel_ML_Assignment\\patent_jsons'

# Initialize an empty list to store the text data from each document
text_data = []

# Iterate over each JSON file in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        # Construct the full path to the JSON file
        json_file_path = os.path.join(json_directory, filename)
        
        # Open the JSON file and read its content
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            for key, value in data.items():
                text_data.append(str(value))
            # text_data.append(str(data['patent_number']))
            # text_data.append(str(data['publication_id']))
            # text_data.append(str(data['family_id']))
            # text_data.append(str(data['publication_date']))
            # text_data.append(str(data['titles']))
            # text_data.append(str(data['abstracts']))
            # text_data.append(str(data['claims']))
            # text_data.append(str(data['descriptions']))
            # text_data.append(str(data['inventors']))
            # text_data.append(str(data['assignees']))
            # text_data.append(str(data['ipc_classes']))
            # text_data.append(str(data['locarno_classes']))
            # text_data.append(str(data['national_classes']))
            # text_data.append(str(data['ecla_classes']))
            # text_data.append(str(data['cpc_classes']))
            # text_data.append(str(data['f_term_classes']))
            # text_data.append(str(data['legal_status']))
            # text_data.append(str(data['priority_date']))
            # text_data.append(str(data['application_date']))
            # text_data.append(str(data['family_members']))

            

# Print debug information
print("Text data from JSON files:")
print(len(text_data))


model = SentenceTransformer('LaBSE')
print("Encode the corpus. This might take a while")
corpus_embeddings = model.encode(text_data[:200], show_progress_bar=True, convert_to_tensor=True)

# Store the corpus embeddings in a pickle file
with open('corpus_embeddings2.pickle', 'wb') as f:
    pickle.dump(corpus_embeddings, f)

