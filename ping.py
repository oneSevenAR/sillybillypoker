import time
import requests

url = "https://yourusername.github.io/reponame/"  # to be replaced

while True:
    try:
        r = requests.get(url)
        print("called", url, "status", r.status_code)
    except Exception as e:
        print("error", e)
    time.sleep(5)  # 600 sec = 10 min
