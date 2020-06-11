import os
import requests


SERVER_URL = os.getenv("HOWDOI_SERVER_URL",
                       default="http://localhost:8000/plugins/")


if __name__ == '__main__':
    query = input("Type query: ")
    response = requests.post(SERVER_URL, json={"query_str": query})
    print(response.json()["answer_str"])
    # for key, value in response.json().items():
    #     print(key, value)
