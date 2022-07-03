FROM python:3.9

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cach -r requirements.txt

COPY . .

CMD ["sh", "entrypoint.sh"]