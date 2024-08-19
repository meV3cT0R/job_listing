from bs4 import BeautifulSoup

with open("home.html","r") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")
    # print(*map(lambda x : x.text,soup.find_all("h1")),sep="\n")
    print(*map(lambda x : f'{x.h1.text} costs {x.button.text.split()[-1]}',soup.find_all("div",class_="w-[500px]")),sep="\n")
