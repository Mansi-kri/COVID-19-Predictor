import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('covid_data.csv')
# data.head()

# 1-> Above 50%, 0-> Below 50% (Infection Probability)
# -1-> Little, 0-> Mediocre, 1-> Severe

features = data.iloc[:,0:-1]
labels = data['infection_prob']
features.tail()

### Model Training
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

### Model Training and Prediction
model = LogisticRegression()
model.fit(X_train, y_train)

model.score(X_test, y_test) # Accuracy is 50% due to random data;(

infection_prob = model.predict_proba(X_test)

# ### Saving the Model using Pickle
model_name = 'covid_predict.sav'
file = open(model_name,'wb')
pickle.dump(model, file)
file.close()

