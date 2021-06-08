import os
from markdownify import markdownify
from bs4 import BeautifulSoup
from shutil import copy2, Error
import requests

rank = ["","mvk5dv","nlwqyv","nlwaxv"]

# def fixPreviewInline(content,src):
#     soup = BeautifulSoup(content, 'html.parser')
#     count = 0
#     for p in soup.find_all("p")[2:]:
#         t = p.getText()
#         if "//preview.redd.it/" in t:
#             try:
#                 img_data = requests.get(t).content
#                 count += 1
#                 name = t[24:t.find("?",0)]
#                 # print(f'found image {t}')
#                 localLink = f"img/{name}"
#                 tag = soup.new_tag("img",src=localLink)
#                 # print(tag)
#                 p.replace_with(tag)
#                 with open(f'dd/{localLink}', 'wb') as handler:
#                     handler.write(img_data)
#                     handler.close()
#                 # print("URL is valid and exists on the internet")
#             except:
#                 continue
#         if count > 0:
#             with open(f"dd/{filename}",'w', encoding='utf-8') as f:
#                 f.write(str(soup))
#     return str(soup)

def createMd(filename):
    basename = filename.split(".")[0]
    with open(f"dd/{filename}",'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        pics = soup.find_all("img")
        for pic in pics:
            try:
                copy2(f'dd/{pic["src"]}', 'site/static/img') #
            except Error as err:
                print(f"missing file {pic['src']}:{err}")
                continue

        content = soup.find("content")
        with open(f"site/content/posts/{filename.split('.')[0]}.md","w", encoding="utf-8") as nf:
            nf.write(soup.find("yaml").getText())
            if len(str(content.getText())) > 0:
                nf.write(markdownify(str(content).replace('src="img/','src="/img/')))
            else:
                nf.write("This is likely a gallary/media post. Check perma/wb links. I'll add support for this later.")
            nf.close()
        f.close()

for filename in os.listdir("dd/"):
    # if filename == "mvk5dv.html":
        if filename.endswith(".html"):
            try:
                print(filename)
                createMd(filename)
            except Error as err:
                print(f"failed to convert {filename}: {err}")
                continue
