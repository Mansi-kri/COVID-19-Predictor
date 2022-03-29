# COVID_19_Predictor

A web-app that uses M.L to predict the probability of COVID-19 in a person.

## Requirements and Installation

-> Install [Python](https://www.python.org/)

-> Open Powershell (Windows)/ Terminal (MacOS/ Linux) and then type:

### For Windows
```bash
pip install -r path/to/requirements.txt/
```
### For MacOS/ Linux
```bash
pip3 install -r path/to/requirements.txt/
```

## Usage 

-> Navigate to the repository's directory using Powershell/ Terminal and then type:

### For Windows
```bash
python model.py
python app.py
```
### For MacOS/ Linux
```bash
python3 model.py
python3 app.py
```
#### The above commands will run a flask server at [localhost](http://127.0.0.1:5000) and the web-app will become functional.


## NOTE
1. Keep all the directories and files together ( and also do not rename any files/directories ). Failure of this may lead to errors.
2. The dataset used to train the model is *imaginary* and hence the model gives inaccurate results. Using real world dataset will definitely fetch good outcomes.
3. The code of model training is also provided in a python notebook.
