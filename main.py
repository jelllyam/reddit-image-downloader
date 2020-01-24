
def main():
    try:
        subr = sys.argv[1]
    except IndexError:
        print("Please follow the instructions from the README file")

    page = requests.get(f"https://www.reddit.com/r/{subr}/top/",stream=True,headers={'User-Agent': 'Mozilla/5.0'})
    webpage = html.fromstring(page.content)

    imgs = webpage.xpath('//img[@alt="Post image"]/@src')


if __name__ == "__main__":
    import requests
    import os
    import sys
    from lxml import html
    main()
