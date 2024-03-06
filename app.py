from fastapi import FastAPI, Query
from typing import List
from fastapi import FastAPI, HTTPException
import logging
from uvicorn import Config, Server
from main import search

# Creating an instance of the FastAPI app
app = FastAPI()


# Defining the search endpoint
@app.get("/search")
async def search_endpoint(query: str = Query(..., title="Query string")):

    # Call the search function with the provided query
    results = search(query)

    # Return the results
    return {"results": results}


# Main block to run the server
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    config = Config(app, host='0.0.0.0', port=8000, log_level='info')
    server = Server(config)
    server.run()


# http://127.0.0.1:8000/docs