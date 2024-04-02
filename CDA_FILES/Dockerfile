FROM python

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN  pip install --verbose -r requirements.txt

RUN echo $PYTHONPATH

CMD ["python", "src/app.py"]

