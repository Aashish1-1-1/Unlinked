FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install spacy
RUN python -m spacy download en_core_web_md
COPY . .

CMD ["python","main.py"]
