FROM prefecthq/prefect:2-python3.11
COPY requirements.txt .
RUN python pip install -r requirements.txt