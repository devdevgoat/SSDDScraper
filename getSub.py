import praw
from markdown import markdown
from praw.reddit import Submission
from datetime import datetime
import sys
import re
import requests
from bs4 import BeautifulSoup, Tag
import waybackpy
from waybackpy.exceptions import WaybackError

ua = "Praw Python Script - russlamb.eth - @devdevgoat"

reddit = praw.Reddit(
    client_id="6yG-inADUv27Hg",
    client_secret="B7UX329CtbMdFTMun4gbk1T4k-qjjw",
    user_agent=ua,
)


def getArchiveTag(link, created_on, soup):
    if 'youtu.be' in link['href'] or 'youtube.com' in link['href']:
        with open("youtube-list.txt","a") as ytf:
            ytf.write(link["href"])
            ytf.close()
    if 'reddit.com/r/' in link['href']:
        aprarsed = link['href'].split('?')[0].split('#')[0]
        # if it's a linked post, we want the archive of the target
        subsub = reddit.submission(url=aprarsed)
        if not subsub.is_self:
            aprarsed = subsub.url
        aWB = waybackpy.Url(aprarsed, ua)
        print(f'Reddit url found, replaced with {aprarsed} instead')
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
    return archive.archive_url

def backupImg(link,type):
    l = link.get('href')
    if type == 'redd.it':
        name = l[24:l.find('?',24)]
        url = l
    elif type == 'imgur':
        name = l.split("/")[3]
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

def getSub(ID):
    submission = reddit.submission(id=ID)
    print(f'{submission.id}:{submission.title}')
    cts = datetime.utcfromtimestamp(submission.created_utc)
    ats = datetime.now()
    html = markdown(submission.selftext)
    soup = BeautifulSoup(html, 'html.parser')
    #clean up reddit previews:
    aId = 0
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
        f.write('<body>')
        f.write(f'<h1>{submission.title}</h1>')
        f.write('\n')
        f.write(f'<h3>By: {submission.author.name}</h3>')
        f.write('\n')
        f.write(f'<p>Submitted On: {cts.strftime("%Y-%m-%d %H:%M:%S")}')
        f.write('\n')
        f.write(f'<p>Archived On: {ats.strftime("%Y-%m-%d %H:%M:%S")}')
        f.write('\n')
        suburl = f'http://reddit.com{submission.permalink}'
        f.write(f'<a href="{suburl}">Permalink</a>')
        subwb = waybackpy.Url(suburl, ua)
        try:
            a = subwb.save()
            f.write(f'<a href="{a.archive_url}"> (wayback)</a>')
        except:
            print('Failed saving submission to wayback')
        f.write('\n')
        f.write('<content>')
        f.write(str(soup))
        f.write('</content>')
        f.write('</body>')
        f.close()
    # print(f'Saved to {submission.id}.html')


    
    
getSub(sys.argv[1])