FROM python:3.9
WORKDIR /app
COPY service_payment.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "service_payment.py"]
