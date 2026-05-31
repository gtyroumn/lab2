FROM python:3.11-slim
RUN mkdir /Tkalych
COPY translate.py /Tkalych/
WORKDIR /Tkalych
RUN pip install googletrans==3.1.0a0
CMD ["python", "translate.py"]
