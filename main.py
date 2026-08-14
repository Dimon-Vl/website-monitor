import requests

URL_LIST=["https://www.google.com/","https://hydrocalc.in.ua/","https://docs.python.org/"]
REQUESTS_LIST=[]

for url in URL_LIST:
    try:
        REQUESTS_LIST.append(requests.get(url))
    except requests.exceptions.ConnectionError:
        REQUESTS_LIST.append(False)

for i,url in enumerate(REQUESTS_LIST):
    print(URL_LIST[i])
    if url:
        print(f"Status: {url.status_code}")
        print(f"Response time: {url.elapsed.microseconds/1000:.0f}")
    else:
        print("Status: DOWN")
        print("Error: Timeout")
    print()