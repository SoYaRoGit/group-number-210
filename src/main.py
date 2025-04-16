import requests

from os import system
from sys import platform
from url import url_site

def main() -> None:
    data = requests.get(url_site)
    print(data.text)


if __name__ == "__main__":
    if platform == "linux":
        system("clear")
    else:
        system("cls")

    main()
