FROM --platform=linux/amd64 python:3.9

WORKDIR /app
COPY .. .

ENV FLASK_DEBUG 1
ENV FLASK_APP app.py
ENV SECRET_KEY yXzB0lEGphwTYfKenExHmNqMmpFJJRjI
ENV SECRET_EMAIL a@a.cu
ENV SECRET_PASSW A1@A1.cu

RUN apt update

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python3","app.py"]