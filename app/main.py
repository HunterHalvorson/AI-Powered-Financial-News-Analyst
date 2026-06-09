"""
  Entry Point
    - This file creates and configures the FastAPI app
    - front-door of the backend
  
  API
    - a set of URLs your frontend can call to get or send data
    - Instead of the react front-end doing all the work it can 
      say to the backend, give me this data
  
  FastAPI
    - Python framework that makes building these URLs easy
    - define a function, slap a decorator on it (@app.post, @app.get) and FastAPI turns it into something the browser can call over HTTP

  Middleware
    - code that runs on every single request before it reaches the route functions
    - CORS middleware checks "is this request coming from an allowed origin"
  
  REST
    - set of conventions for how to design your API URLs and use HTTP methods
      --> GET, POST< PUT, DELETE
    - So instead of naming endpoints whatever you want. REST says name them after the resources and use the HTTP method to describe the action
  
  Endpoints
    - A URL your app exposes that does something when you hit it.
    - /health is an endpoint. /query will be an endpoint. Each one has a specific job — you call it, something happens, you get a response back.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# fast api instantiation
app = FastAPI(title="Financial News Analysis", version="0.1.0")

# add middleware
# Link: https://youtu.be/1oWPUpMheGk?si=a7N_dB7RYo9JyGtG
# Link: https://youtu.be/5uq5wCCXvwU?si=SnHHjF-ah-leRqY6

# 

"""
  A browser has a rule, you cannot make a request to a different origion
  than the page you are on.

  React runs on localhost:5173, FastAPI runs on localhost:8000
    - different ports = different origins so the browser will block
      react from talking to FastAPI by default
    - CORS middleware allows us to tell FastAPI to permit the request
  
  When React makes a request to Fast, it will check that requests from
  that origion are valid 'preflight request'
    - allows origion - tristed URLs
    - allow methods - all (i.e. GET, ...)
    - allow headers -  which headers the request is allowed to carry. "*" means all. The one you actually need is Content-Type, because your React app sends Content-Type: application/json with every POST request.
  
  MiddleWare: Code that runs between the request arriving and your endpoint handling it.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/health")
# def health():
#     return {"status": "ok"}
