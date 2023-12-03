### Move Hbase table data to s3 using Minio
Create venv using `virtualenv venv`.
Then install packages `pip install -r requirements.txt`.
After that using `docker compose up -d` build images for hbase and Minio s3.
Hbase run shell script and create s3 bucket in Minio.
Run `python3 hbase_reader_to_s3.py` to move table from Hbase to s3.