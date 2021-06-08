import praw
from markdown import markdown
from praw.reddit import Submission
from datetime import datetime
from pytz import timezone
import re
import requests
from bs4 import BeautifulSoup, Tag
import waybackpy
import os.path
from os import path
from waybackpy.exceptions import WaybackError
import json
from shutil import copy2, Error
from markdownify import markdownify


ua = "Praw Python Script - russlamb.eth - @devdevgoat"
# rank = ["","mvk5dv","nlwaxv","nlwqyv"]
rank = [""]
archives = {}

tz = timezone('EST') 

reddit = praw.Reddit(
    client_id="thisclientisdead...uhg",
    client_secret="welpIfuckedthatup.hadtodeletetheappbcicommitedit",
    user_agent=ua,
)


def getArchiveTag(link, created_on, soup):
    archive = False
    if link['href'] not in archives:
        if 'youtu.be' in link['href'] or 'youtube.com' in link['href']:
            with open("youtube-list.txt","a") as ytf:
                ytf.write(link["href"])
                ytf.write("\n")
                ytf.close()
            archives[link['href']] = link['href']
            return archives[link['href']]
        if 'reddit.com/r/' in link['href']:
            aprarsed = link['href'].split('?')[0].split('#')[0]
            # if it's a linked post, we want the archive of the target
            try:
                subsub = reddit.submission(url=aprarsed)
                if not subsub.is_self:
                    aprarsed = subsub.url
                aWB = waybackpy.Url(aprarsed, ua)
                print(f'Reddit url found, replaced with {aprarsed} instead')
            except:
                print('unable to get sub submission, likely a link to a subreddit')
                return link['href']
        else:
            aWB = waybackpy.Url(link['href'], ua)
        try:
            archive = aWB.near(year=created_on.year, month=created_on.month, day=created_on.day)
            # print(f"year={created_on.year}, month={created_on.month}, day={created_on.day})
            print(f'Found archive from: {archive.archive_url}')
        except WaybackError as e:
            print("Nothing found for created on. Getting oldest")
            try:
                archive = aWB.oldest()
            except:
                print("Nothing found for oldest. Archiving")
                try:
                    archive = aWB.save()
                except:
                    print(f"This link is jacked, can't archive:{aWB.url}")
                    archives[link['href']] = link['href']
        if(archive): 
            archives[link['href']] = archive.archive_url
        else: 
            archives[link['href']] = link['href']
    return archives[link['href']]

def backupImg(link,type):
    l = link.get('href')
    if type == 'redd.it':
        name = l[24:l.find('?',24)]
        url = l
    elif type == 'imgur':
        name = l.split("/")[3]
        name = name[:name.find('?',0)]
        print(name)
        url = f'https://i.imgur.com/{name}.gif'
        name = f'imgur_{name}.gif'
    else:
        print("Unknown type.. unable to backup image")
        return
    img_data = requests.get(url).content
    localLink = f"img/{name}"
    with open(f'dd/{localLink}', 'wb') as handler:
        handler.write(img_data)
        handler.close()
    return localLink

def getSub(submission):
    print(f'{submission.id}:{submission.title}')
    cts = datetime.utcfromtimestamp(submission.created_utc)
    ats = datetime.now()
    html = markdown(submission.selftext)
    soup = BeautifulSoup(html, 'html.parser')
    if submission.id in rank:
        weight = rank.index(submission.id)
    else: 
        weight = 0
    suburltmp={
        'href':f'http://reddit.com{submission.permalink}'
    }
    suburl = getArchiveTag(suburltmp,cts,soup)
    aId = 0
    #find inline preivews with no html:
    for p in soup.find_all("p")[2:]:
        t = p.getText()
        if "//preview.redd.it/" in t:
            try:
                img_data = requests.get(t).content
                name = t[24:t.find("?",0)]
                # print(f'found image {t}')
                localLink = f"img/{name}"
                tag = soup.new_tag("img",src=localLink)
                # print(tag)
                p.replace_with(tag)
                with open(f'dd/{localLink}', 'wb') as handler:
                    handler.write(img_data)
                    handler.close()
                # print("URL is valid and exists on the internet")
            except:
                continue
    for a in soup.findAll('a'):
        if 'web.archive.org' in a:
            print("Can't wayback a wayback link... skipping")
            continue
        if "preview.redd.it" in a['href']:
            localLink = backupImg(a,'redd.it')
            tag = soup.new_tag("img",src=localLink)
            a.replace_with(tag)
            print(f"Replacing preview link with {tag}")
            continue
        if "imgur.com" in a['href']:
            if "gallery" in a['href'] or "imgur.com/a/" in a['href']:
                print('waybacking gallary/album link')
                pass
            else:
                localLink=backupImg(a, 'imgur')
                if len(a.getText()) >0 and a.getText() != a['href']:
                    a['href'] = localLink
                else:
                    tag = soup.new_tag("img",src=localLink)
                    a.replace_with(tag)
                continue
        # for all other links (and imgur gallaries/albums):
        archive_url = getArchiveTag(a,cts,ats)
        tag = soup.new_tag("a",href=archive_url)
        tag.append(" (wb)")
        a.insert_after(tag)      
        
    with open(f"dd/{submission.id}.html", 'w', encoding='utf-8') as f:
        title = submission.title.replace('"','\\"')
        f.write(f'''<yaml>---
title: "{title} "
author: "{submission.author.name}"
date: "{cts.strftime("%Y-%m-%d %H:%M:%S")}"
archived: "{ats.strftime("%Y-%m-%d %H:%M:%S")}"
permalink: "http://reddit.com{submission.permalink}"
waybackpermalink: "{suburl}"
weight: {weight}
---</yaml>''')
        f.write('\n')
        f.write('<content>')
        f.write(str(soup))
        f.write('</content>')
        f.write('</body>')
        f.close()
    with open("archives.json", 'w', encoding='utf-8') as ar:
        ar.write(json.dumps(archives,indent=4))

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

print(f'I can access reddit: {reddit.read_only}')
with open('archives.json') as json_file:
    archives = json.load(json_file)

for submission in reddit.subreddit("superstonk").search('flair:"DD"', limit = 1000, syntax='lucene', sort='top'):
    rank.append(submission.id)
    if (path.exists(f"dd/{submission.id}.html")):
        print(f"Already archived {submission.id}")
        continue
    else:
        getSub(submission)
    try:
        createMd(f'{submission.id}.html')
    except:
        print(f'Failed converting dd/{submission.id}.html')