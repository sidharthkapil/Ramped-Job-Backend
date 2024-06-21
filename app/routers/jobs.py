from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from app import schemas
from app.database import Jobs
from app.oauth2 import require_user
from app.serializers.jobsSerializers import jobEntity, jobListEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()


@router.get('/')
def get_jobs(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
    skip = (page - 1) * limit
    jobs = jobListEntity(Jobs.find({'job_name':{'$regex':search, '$options': 'm' }}))
    return {'status': 'success', 'results': len(jobs), 'jobs': jobs}
  

#Comment

# Expanded implementation for semantic matches
#from sklearn.metrics.pairwise import cosine_similarity
#import numpy as np
#import gensim.downloader as api

# Load a pre-trained model (e.g., Word2Vec)
#model = api.load("word2vec-google-news-300")

# Function to get the vector representation of a job title
#def get_vector(text):
    #words = text.split()
    #vectors = [model[word] for word in words if word in model]
    #if vectors:
        #return np.mean(vectors, axis=0)
    #else:
        #return np.zeros(model.vector_size)

# Compute the vector for the search term
#search_vector = get_vector(search)

# Retrieve and process jobs from the database
#all_jobs = list(Jobs.find({}))
#job_vectors = [(job, get_vector(job['job_name'])) for job in all_jobs]

# Calculate similarity scores
#similarity_scores = [(job, cosine_similarity([search_vector], [vector])[0][0]) for job, vector in job_vectors]

# Filter jobs based on a similarity threshold
#similarity_threshold = 0.7
#similar_jobs = [job for job, score in similarity_scores if score >= similarity_threshold]

# Convert the list of similar jobs to the desired format
#jobs = jobListEntity(similar_jobs)


