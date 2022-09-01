psql "public-api-v2" < resetData.sql
rm ./db.sqlite3
python3 manage.py migrate
locust --config .locust.conf