import pickle
# import dv


with open("model-deployment\model1.bin", 'rb') as model_file:
    model = pickle.load(model_file)

with open("model-deployment\dv.bin", 'rb') as vectorizer:
    dict_vectorizer = pickle.load(vectorizer)

data = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
data_transformed = dict_vectorizer.transform(data)


prediction = model.predict_proba(data_transformed)[:, 1]

print(prediction)
