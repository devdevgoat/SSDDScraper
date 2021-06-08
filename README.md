# SSDDScraper:  A DD Archiver for Superstonk... or anything I guess, just edit some praw info

Hello my dear Apes, HAPPY 300!!!! I come bulling gifts!! 

TLDR: Go here for DD, it can't be taken down now. Triple backed up and decentralized:  

- ipfs://Qma6rwZ4nM79MS62ZQBsE8q26dr2CKeMFBbceoL14b3gLx
- http://gme.russlamb.eth/
- https://github.com/rlamb2/SSDDScraper

Also, maybe we should use a decentralized chat app like iris.to ([invite link](https://iris.to/?channelId=fa88c760-c1d1-4cc6-ab97-fa125296168a&inviter=eVG59A0lM_xoTmDC-6KHe_knfuy8BAmVfIh9GPNJZf0.pDiCCkNp8GYw8fES089y4YOITmV03r8VpG9CPvYJdyg&s=fEUAO58l3zQv4SEuDvVrX5DgD_rCFZM5gieaW77Z1m0&k=X9kKDXMdYvVT
))

--- TLDR done ---
As we all saw this morning, one little snip here, or fat check there, and our entire network crumbles. This is not acceptable, and this WILL happen when the MOASS starts. So what is there to do?? 
I know I know, everyone is all "go gingham style!!" but when that goes down too, and we're scattered amongst twitter trying to share Dropbox links, people will get nervous. Did that DD ever actually exists?!?! HOW DO I KNOW FOR SURE?!?! IT"S BEEN 10 MINUTES!!!
We need something safer, more robust, and more importantly, not owned by anyone who can go shill at the drop of a dime... especially me!! 

So here's what I built. I'm not some fancy smancy financial analyst, or a badass micro-expression expert, but I can scrub web content with cobbled together code snippets from StackOverflow! So I copy and pasted my way to a V1 one of a DWeb site that supports the following features:

- Hosted and pinned on IPFS, which means the content is spread across hundreds of nodes, you can even host your own in Brave Browser. I can delete it off my machine and it won't matter, someone else has already replicated the content and it can't be modified!! 
- All (or nearly all) evidence downloaded and stored on IPFS locally, so if someone deletes shit from imgur or reddit images, fuck 'em, we got our copy and that shits INLINE! (except for albums/gallery's, that shits complicated, but see last bullet for workaround) 
- While copying the content I went ahead and re-published all DD to Wayback machine, and grabbed the links closest to original posting time! Seriously, this made the export soooooo much longer... worth it!
- And since I was spamming wayback anyway, I did the same for ALL embedded links, creating a new wayback archive (unless one near posting existed already)! However, I still need a solution for YouTube links, I backed up all the youtube links to a file so we can scrub those separately... maybe use a web-torrent video solution for these?? Suggestions welcome! 
- Oh, and I injected the wayback links inline to the post as well, so if you're readding HOCII and the fuckers tried to edit Investing.com's definition of "fuk'd" you can see the original


Couple things to note: 
- You can access the site via my eth url, but it's just a helpful alias for me. You can use the direct Qxx links, but one problem with the immutability concept, we can't add NEW DD to that Qxxx page, so I have to build a new one and republish with the updated list of DD, which means a new CID. Thus, if I update with new DD, I'll try to periodically update the .eth URL, though it costs like 5-10$ each time, so wont' be updating often.  Not sure if we can use an OrbitDB node in browser to solve this or not?? 
- Would love it if the owners of superstonk.eth updated their content record to the site as well, but I have no control of that. If anyone knows who owns it let them know, pretty sure they're an ape... or a squatter?
- Also, linking via ens is not the same as DNS, anyone can do it, you can host the same site at 'badadddddick.eht' it doesn't matter, it's just a link to the IPFS CID... I don't own this data anymore, it out in the wild forever! It's like a human readable bookmark, if that makes sense.
