FROM python:3.8-alpine as builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY invoke.py ./

RUN chmod +x invoke.py

FROM python:3.8-alpine

WORKDIR /app

COPY --from=builder /app/invoke.py ./

CMD ["./invoke.py"]
