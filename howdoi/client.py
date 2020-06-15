import os
import logging
import requests

SERVER_URL = os.getenv("HOWDOI_SERVER_URL",
                       default="http://localhost:8000/plugins/")


if __name__ == '__main__':
    query = input("Type query: ")
    response = requests.post(SERVER_URL, json={"query_str": query})
    print(response.json()["answer_str"])
    # for key, value in response.json().items():
    #     print(key, value)
    feedback = input("Answer your question? (Y/N): ")
    pos = query.lower().find("howdoi")
    query = query[pos+len("howdoi"):]
    data = {'question': query, 'answer': response.json(
    )["answer_str"], 'feedback': feedback}
    logging.basicConfig(filename="logs/test.csv", format='%(asctime)s,%(question)s,%(answer)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info(data['feedback'], extra=data)

