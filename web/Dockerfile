FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN ls -la # 현재 디렉토리의 내용을 확인
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV NAME dockertest
CMD ["python", "app.py"]
