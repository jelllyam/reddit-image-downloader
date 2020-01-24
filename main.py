import requests
import os
import sys
from lxml import html

def main():
    try:
        subr = sys.argv[1]
    except IndexError:
        print("Please follow the instructions from the README file")
        exit(0)

    page = requests.get(f"https://www.reddit.com/r/{subr}/top/",stream=True,headers={'User-Agent': 'Mozilla/5.0'})
    webpage = html.fromstring(page.content)

    imgs = webpage.xpath('//img[@alt="Post image"]/@src')

    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        os.mkdir(dir_path+r"\images")
    except FileExistsError:
        print("Images folder already present\n")
    count = 1
    for url in imgs:
        if "external" not in url:
            response = requests.get(url,stream=True,headers={'User-Agent': 'Mozilla/5.0'} )
            with open(dir_path+r"\images"+"\\img"+str(count)+".jpg","wb") as f:
                f.write(response.content)
            count += 1

if __name__ == "__main__":
    main()
