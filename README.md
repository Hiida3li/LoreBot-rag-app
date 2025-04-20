# rag-app

# requirements
    - python
    
# Installation

### Install the requirements packages

'''bash
$ pip install -r requirements.txt

'''
### setup the environment variables 

'''bash
$ cp .env.example .env

'''
set your environment variables in the '.env' file, like 'OPEN_API_KEY' value.

## run the FastApi server 

'''bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5001
'''
 
 ## POSTMAN  Collection
 Download the POSTMAN collection from [/assests/rag-app.postman_collection.json](/assets/rag-app.postman_collection.json) 