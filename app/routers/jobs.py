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
"""
To expand this implementation to include semantic matches, we can integrate a natural language processing (NLP) model that understands and processes synonyms and related terms. One approach is to use a pre-trained model like Word2Vec, GloVe, or BERT to find semantic similarities between job titles. Here's a step-by-step outline and an example comment in your code:

Pre-process the job titles in the database: Compute vector representations for each job title using an NLP model and store them.
Compute vector for the search term: Convert the user's search term into a vector representation using the same NLP model.
Calculate similarity scores: Use cosine similarity or another similarity measure to find jobs in the database that are semantically similar to the search term.
Filter results based on similarity threshold: Retrieve jobs that have a similarity score above a certain threshold.
Here's how we can incorporate these steps into your code:
"""
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




 """
  Another method to search the database for jobs is by using an n-gram technique. An n-gram is a sequence of characters taken from a string. N-grams are commonly used in statistical text analysis problems, such as measuring text similarity (e.g., plagiarism checks) or even in speech recognition.


find(
    {
        "$text": {
            "$search": make_ngrams(unicode(search_input))
        }
    },
    {
        "job_name": True,
        "company_name": True,
        "score": {
            "$meta": "textScore"
        }
    }
).sort([("score", {"$meta": "textScore"})])


In this MongoDB query, we convert the incoming search query into a space-separated list of n-grams so that MongoDB can perform whole-word matches in the documents indexed for text search. We instruct MongoDB to use text search on our collection with n-grams from the search query and sort the results by the text match score.
    """



