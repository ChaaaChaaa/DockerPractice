#!/bin/sh
# web 서비스가 준비될 때까지 기다림
while ! curl -s http://web:5000/health > /dev/null; do
  echo "Waiting for the web service..."
  sleep 1
done

# web 서비스가 준비되면 nginx 시작
echo "Starting nginx..."
exec nginx -g 'daemon off;'
