
FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]


RUN pipenv install --system --deploy

COPY ["model-deployment/predict.py", "./"]

EXPOSE 5000

# docker build -t test .
# docker run -it --rm -p 5000:5000 --entrypoint=bash test
#python predict.py


