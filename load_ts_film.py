# python3
import urllib.request
import os
from time import time

URL = '...' # put it here

os.makedirs("downloaded_film", exist_ok=True)
with open("downloaded_film/film.ts", "wb") as f:
    t = time()
    for i in range(1, 10**10):
        if i % 120 == 0:
            print("~{} minutes downloaded, spent {} min {} sec".format((i // 120) * 10, (t - time()) // 60, (t - time()) % 60))
        try:
            response = urllib.request.urlopen("{}/segment{}.ts".format(URL, i))
            data = response.read()
        except Exception:
            print("downloaded {} segments. downloading finished.".format(i))
            break
        f.write(data)

