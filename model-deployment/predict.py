from flask import Flask
from flask import request
import pickle



app = Flask('flask-app')

# with open(".\model1.bin", 'rb') as model_file:
with open("model2.bin", 'rb') as model_file:

    model = pickle.load(model_file)

# with open(".\dv.bin", 'rb') as vectorizer:
with open("dv.bin", 'rb') as vectorizer:
    dict_vectorizer = pickle.load(vectorizer)


@app.route('/predict', methods = ['POST'])
def get_predictions():

    df = request.get_json()
    df_transformed = dict_vectorizer.transform([df])

    prediction = model.predict_proba(df_transformed)[0, 1]

    churn  = prediction >= 0.5

    return {'probability': float(prediction), 'churn': bool(churn)}


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
    

## Can also use waitress-serve --listen=0.0.0.0:5000 predict:app to avoid the error message: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.

# docker run -it --rm -p 5000:5000 --entrypoint=bash test