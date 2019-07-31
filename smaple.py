import requests
import json


def main():
    r = requests.get(url='https://httpbin.org/json')
    upper_author = r.json()["slideshow"]["author"].upper()
    with open('test.txt', 'w') as output_file:
        output_file.write(upper_author)


if __name__ == "__main__":
    main()
