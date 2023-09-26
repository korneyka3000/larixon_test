FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

COPY db_health_check.sh /db_health_check.sh

RUN chmod +x /db_health_check.sh

COPY start.sh /start.sh

RUN chmod +x /start.sh

ENTRYPOINT ["sh", "./db_health_check.sh"]

CMD ["sh", "./start.sh"]