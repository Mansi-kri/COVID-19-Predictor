from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

loaded_model_file = open('covid_predict.sav', 'rb')
model = pickle.load(loaded_model_file)
loaded_model_file.close()

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            data = request.form
            input_features = [int(data[i]) for i in data]
            # print(input_features)
            probability = model.predict_proba([input_features])[0][0]
        except ValueError:
            probability = 0.0
        # print(probability)
        return render_template('predict.html', probability=str(round(probability,4)*100)+" %")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
