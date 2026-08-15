from helper import sync_check_website

URL_LIST = [
    "https://www.google.com/",
    "https://hydrocalc.in.ua/",
]

for url in URL_LIST:
   print(sync_check_website(url))