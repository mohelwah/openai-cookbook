[![MLOPs Template](https://github.com/mohelwah/MLOps_template/actions/workflows/main.yml/badge.svg)](https://github.com/mohelwah/MLOps_template/actions/workflows/main.yml)

# Project Type: CHATGPT BOT Template
# Project Name : CHATGPT Template
this is scaffold template for chatgpt 
 Create the following:
 - Makefile
 - requirement.txt
 -Linux system:
    - virtial enviroment: python -m venv ~/.chatgpt
    - activate venv envi: source ~/.chatgpt/bin/activate
 - Windows system:
    - virtial enviroment: python -m venv c:\venv\chatgpt
    - activate venv envi:   C:\venv\chatgpt\Scripts\activate.ps1
 - hello.py file
 - test_hello.py file 
 - to check the python version:
    - in linux : which python  
    - in windows: Get-Command python | fl *
 - get pack version:
    - pip freeze | grep packName 
 - chanage bash to run venv :
    - vim ~/.bashrc
    - shift G to button, esc to command mode, i to insert mode 
    -# Setup Virtual Env
    - source ~/.chatgpt/bin/activate
    cd chatgpt/
      - esc to command mode, :wq to save and quit


## run jupyter notebook
    - jupyter noteboke: - install ipykernel
  - run command: - ipython kernel install --user --name=chatgpt

## setup api keys variables:
Store your API key as an environment variable: To hide your API key, you can store it as an environment variable within your virtual environment. In your terminal, run the following command to set your API key as an environment variable:

        export OPENAI_KEY='your_api_key_here'
        export PINECONE_KEY='your_api_key_here'
Access your API key in your Python code: In your Python code, you can access your API key using the os module. Here's an example:

        import os
        openai_key = os.environ.get('OPENAI_KEY')
        pinecone_key = os.environ.get('PINECONE_KEY')