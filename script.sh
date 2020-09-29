#!/bin/bash
#if exists already; else need to create a new environement
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt

#test: 
#python -m pytest -vv