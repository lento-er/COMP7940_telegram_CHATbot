FROM python:3.8

WORKDIR ./telegram_chatgpt_bot

ADD . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]