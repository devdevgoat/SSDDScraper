# The (DD)uplicator

Hello apes. I come bulling gifts! 

u/Corporate_Greed [posted](https://www.reddit.com/r/Superstonk/comments/nt54j9/save_it_all/) a bit ago something I've been worried about since Feb: info supression/removal/curation during/after the MOASS. I had had tried to develop a nifty solution to this problem with a focus on preserving comments and enabling future comments on archived post using a complicated combination of orbitdb/ipfs/custom dhts... and then my kid got rsv and you know how it goes... life! But the post made me realize it's worth revisiting, and I decided to lower my scope!

Like many of you, I can't contribute actual stock analysis... hell, evem my memes are shit! But, I can whip up some mean data extraction/migration scripts! I'm an ETL developer by trade, and with the NFT news I've been looking for many excuses to tinker with IPFS/Distributed architectures! So I built a thing. It's perfect, but it has a few key features:

* Stores our precious DD on the distributed web, so no one 'owns' it and thus can't take it down
* Stores images (reddit and imgur currently) on the Dweb as well, so they can't be lost/deleted by their owners at a later date
* Hosts a homepage of the content on the Dweb as well where anyone can fork in case the creator (me in this case) is compromised ()
* Create wayback archives on all posts today, but collect their original ones if they exist (backup of our backup)

Whoah whoah whoah, what are you talking about DevDevGoat?? You want to copy all our DD and expect us to come to you to get it back?? *pulls shill alarm*

Fuck no! I don't trust anyone, not even myself! (am I shill meme here) That's why I'm putting everything up on IPFS. [What is IPFS](http://docs.ipfs.io.ipns.localhost:8080/concepts/what-is-ipfs/)? The Inter-Plantetary File System is like blockchain meets your downloads folder with touch of bittorrent. Simply put, the files don't go to *a* sever, they go to a BUNCH (img) of different "servers" called "nodes" that can be run by anyone (if you're using Brave Browser you can even [host a node just by surfing the web](https://brave.com/ipfs-support/)!!), even shills!! Take that shills! Also, the files can't change! That's right, no more, \[deleted\] when you open a link. Changing the content in the file will actually generate a NEW file with a new url and both are accessible! (for you IPFS nerds out there, yes we'll pin the directory as well, ain't no garbage collection getting our dd!)

# FAQ

## How does it work?

I use a couple of different python scripts to do the following:

* Copy all top DD flaired posts (~250) from SuperStonk to IPFS (explained below) using PRAW
* Search for WayBack Machine copies of all linked evidence and imgur posts and imbed them inline
* If no WayBack is found at time of posting, get the latest wayback. If that's missing too, make one at runtime and link that!
* Download all reddit preview images and store them on IPFS as well, replacing the inline reddit link with a local refernce
* Ditto for imgur, but gallaries and albulms pose a problem, so we'll just use wayback links for these
* Create an inventory of all IPFS links into a simple homepage, hosted on.. you guessed it, IPFS
* Whenever we see a youtube link, save it to a file so we can comeback and back those up later (would love opinion on this, not sure ipfs would be good for it, maybe a .torrent? saved to ipfs?)


##Yeah, well why does the site look like you're trying to own it?? 

gme.russlamb.eth and gme.russlamb.eth.link (for dns users) are just the first easy to remember point of entry. You can "host" it on your site (.eth, or even dns) as well. I tried to get SuperStonk and Gamestop eth addresses, but both were taken. If they owners wanted to, they could also point to the DSite simply by copying the content tag of the ethereum address. You can also just bookmark the CID (Qxxx) but it will never show updates... which brings me to the next faq.

Well if you can't change it how will you add more dd?? 

The only file that will change is the index file, that lists all the backed up dd links. The dd links themselves will remain untouched (by design, not just because 'I pRoMisE!' I literally can't change them, only linked to altered versions), but if I want to link to more I have to upload a new index file, then I'd change my content address at gme.russlamb.eth. The obvious solution to this is to inject some sort of mutable datastore like an OrbitDB node (or maybe a smart contract?? hmmm) into the site and collect links there, then dynamically render the page... but I don't really have time to do all that atm. Anyway, here's how I envision updates will have to go:

* Public index.html with links to HOC I and HOC II
* HOC II comes out
* Backup post and publish to ipfs, getting Q-link
* Update index.html to include Q-link to HOC III
* Publish index.html to get new q-link
* Update gme.russlamb.eth with new q-link to new index.html. All other old q-links still work, no need to change, can be bookmarked.


## Why not just use WayBack machine

I mean.. yeah... I could... but what if some shitty hedgefunds just... buys it?? Srsly, wayback is good, but it's still a centralized server owned by one entity. I wanted a solution that will work even from the moon (IPFS + GME pun activated!)

## Any plans for extending this?

Yeah, I have a bunch of wishlist items already:

* youtube download and archival
* Wayback actually lets you copy down the source code of their snapshot, I wrote code to do this but it slooooooooooowed way to to far down, might add this back later
* Comment archival, this is what requires DHT's or some form of distributed db
* Other flairs: would be cool if we had a mod-only 'preserve-me' flair that I could monitor for in real time and archive on the fly
* any idea's welcome, but I warn you, I get bored easily and if gme starts mooning I doubt i'll come back to this project very quickly haha

