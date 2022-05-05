from flask import Flask, render_template, request
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model("final_model")

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            data = request.form
            input_features = [float(data[i]) for i in data]
            # print(input_features)
            probability = str(float(model.predict([input_features])))
            idx = probability.index(".")
            probability = probability[0] + probability[idx+1] + "." + probability[idx+2:idx+4]
        except ValueError:
            probability = 0.0
        # print(probability)
        return render_template('predict.html', probability=probability+" %")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
