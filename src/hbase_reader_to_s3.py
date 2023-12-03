import happybase
from typing import List
from minio import Minio
import json
import io

def read_hbase_data(host: str, port: int, table: str, rows: List):
    connection = happybase.Connection(host, port)
    table = connection.table(table)
    hbase_data = table.rows(rows)
    return hbase_data

def read_credentials(credential_file: str):
    with open(credential_file) as cf:
        credentials = json.load(cf)
    return credentials

def main():
    credentials = read_credentials("credentials.json")
    access_key = credentials["accessKey"]
    secret_key = credentials["secretKey"]
    client = Minio(
        endpoint="127.0.0.1:9000",
        access_key=access_key,
        secret_key=secret_key,
        secure=False
    )

    hbase_data = read_hbase_data(
        '127.0.0.1', 9090, "books", [b"In Search of Lost Time"]
        )
    json_data = str(hbase_data).encode("utf-8")
    json_as_a_stream = io.BytesIO(json_data)
   
    client.put_object(
        "test-bucket",
        "books.json",
        data=json_as_a_stream,
        length=len(json_data)
    )


if __name__ == "__main__":
    main()
