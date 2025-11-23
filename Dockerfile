FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m playwright install --with-deps

CMD ["pytest", "tests", "--alluredir=results"]