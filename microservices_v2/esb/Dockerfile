FROM python:3.9
WORKDIR /app
COPY esb.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "esb.py"]
