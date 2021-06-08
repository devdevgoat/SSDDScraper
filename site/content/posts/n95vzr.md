---
title: "Someone is turding in the dark pools again! "
author: "Pubertus"
date: "2021-05-10 14:26:17"
archived: "2021-06-08 09:17:38"
permalink: "http://reddit.com/r/Superstonk/comments/n95vzr/someone_is_turding_in_the_dark_pools_again/"
waybackpermalink: "https://web.archive.org/web/20210510143225/https://www.reddit.com/r/Superstonk/comments/n95vzr/someone_is_turding_in_the_dark_pools_again/"
weight: 182
---Typical disclaimer: I am retrieving Finra ADF (OTC dark pool) data from Fidelity using Time & Sales and running it through some spaghetti code I threw together for analysis purposes. As always, if you notice any errors in my data please point them out as **I am prone to making mistakes and I'm no wrinkle brain**.


For additional information, and understanding how I am doing all this, [please read my post from last week.](https://www.reddit.com/r/Superstonk/comments/n7ahcl/found_something_funky_on_the_dark_pools/?utm_source=share&utm_medium=web2x&context=3) [(wb)](https://web.archive.org/web/20210508065659/https://www.reddit.com/r/Superstonk/comments/n7ahcl/found_something_funky_on_the_dark_pools/) I highly recommend reading my last post because it will better frame what I'm about to present.


**SOMEONE IS FUCKING AROUND WITH DARK POOL TRANSACTIONS!**


**A large amount of 1 share size transactions are being channeled to the dark pools outside the NBBO and sometimes in excess of $3!!!!!**


Here is GME Finra ADF data:


![](/img/kdu1zgiwxay61.png)
![](/img/fdkicgiryay61.png)
Here is GME from 9:30-10am for NYSE exchange.


![](/img/9c49x1b8cby61.png)
u/dlauer Since you may have missed my post from Thursday, I invite you to shed some light on what is happening. Currently, this appears to be evidence of price suppression combined with price gouging of customers through the use of OTC dark pools. At minimum, someone is executing trades through the dark pools outside of the NBBO and in violation of reg NMS. It happened for the first time (that I've ever witnessed) on Thursday 5-6 and is again actively happening right now!


~~I have not verified whether~~ Other stocks are being manipulated the same way they were last Thursday.


Edit:


I checked AMC to see if it's happening again to other stocks and found that it is:


![](/img/vjt9k79p9by61.png)
Edit3:


![](/img/yqqlbb87pdy61.png)
Here is the cumulative data for today (5-10). **It appears whatever was happening ceased before 12:00ET.** Suspicious that the timing coincides with when my post started getting traction. I'm not gonna jump to conclusions though.


Here's a chart with the corresponding impacts outlined:


![](/img/3qmnaevrpdy61.png)
Large frequency transaction prices:


9:30AM-11:00AM - Above Asks


* $161.755 (9:30:12ET - 9:43:11ET)
* $157.525 (9:43:21ET - 9:43:22ET)
* $157.31 (9:43:27ET - 9:58:22ET)
* $154.09 (9:58:44ET - 10:13:10ET)
* $154.02 (10:13:27ET - 10:28:20ET)
* $153.845 (10:28:39ET - 10:43:22ET)
* $151.155 (10:44:05ET - 10:58:08ET)


11:00AM-12:00PM - Below Bids


* $154.02 (10:16:05ET - 10:22:05ET)
* $150.955 (10:58:34ET - 11:13:20ET)
* $151.38 (11:13:46ET - 11:28:18ET)
* $152.25 (11:29:23ET - 11:37:57ET)


Here's the number of transactions at each of the above price points. I may need to look further into $154.02 since it appears on both sides and is almost a wash in transaction count.


![](/img/700s34mfwdy61.png)
Edit4: Analyzing delay from NBBO.


[Here is my google doc for analyzing time delay from closest NBBO price vs execution](https://docs.google.com/spreadsheets/d/1PQPaQSRMHMPT20hYVKKTG7_QIGG1WIXKoR-6X1G8B6I/edit?usp=sharing) [(wb)](https://web.archive.org/web/20210511024924/https://docs.google.com/spreadsheets/d/1PQPaQSRMHMPT20hYVKKTG7_QIGG1WIXKoR-6X1G8B6I/edit?usp=sharing)


The 1st tab contains all the transaction data from 9:30am-10am including all exchanges. Use this to confirm what I'm reporting and verify if I'm making any mistakes.


The following tabs contain data from the closest NBBO timestamp and then the corresponding batch of transactions including all the outside NBBO orders in order to match that NBBO.


* $161.755
* Row 56 - 9:30:02ET - Begin NBBO
* Row 409 - 9:30:36ET - Last entry within that NBBO
* 34 second delay
* $157.525
* This batch appears to have a corresponding supply of matching NBBO range
* $157.31 (The Dark orange highlights are NBBO price ranges permissible for $157.31)
* 1st noticeable gap
	+ Row 682 - 9:43:53ET - Begin NBBO
	+ Row 3601 - 9:47:37ET - Latest entry within that NBBO
	+ 3:44 delay
* 2nd gap
	+ Row 4095 - 9:48:24ET - Begin NBBO
	+ Row 13590 - 9:58:22ET - Last entry within that NBBO
	+ 9:58 delay (almost 10 minutes!)


Edit5: I'll pick this up in the morning. I'm exhausted.


​


Edit2:


[Dave confirms manipulation is "without a doubt" happening and is "shockingly rampant"](https://youtu.be/AYct0XX0uTU?t=1949) [(wb)](https://youtu.be/AYct0XX0uTU?t=1949)


[Dave states in regards to dark pools "You cannot trade outside the NBBO. That is the rule in US markets."](https://youtu.be/AYct0XX0uTU?t=3502) [(wb)](https://youtu.be/AYct0XX0uTU?t=3502) It's either 610 or 611 and is the "backstop for best execution" & "you cannot get outside of the protected quote."


[242.610 Reg NMS - Access to Quotations](https://www.law.cornell.edu/cfr/text/17/242.610) [(wb)](https://web.archive.org/web/20210511013259/https://www.law.cornell.edu/cfr/text/17/242.610)


[242.611 Reg NMS - Order Protection Rule](https://www.law.cornell.edu/cfr/text/17/242.611) [(wb)](https://web.archive.org/web/20141225100338/http://www.law.cornell.edu/cfr/text/17/242.611)


I have now watched Dave's AMA 10 times and probably will need to watch it another 10 times.


~~I am beginning to suspect, since he says that he "cannot say a ton about that" (when discussing manipulation), that he may not be able to provide insight or clarity into this situation due to other reasons. I hope that I am wrong and I sincerely hope that he chimes in eventually. For now, however,~~ **I will begin compiling my data to prepare a submission to both the SEC & Finra.**


Edit6:


I've spoken with Dave and he does not see these trades outside the NBBO in their data. He suspects the transaction data that Fidelity is providing is probably inaccurate. My next step is going to be calling Fidelity and inquiring about the quality of their data. I'm sure Dave is correct, but I still intend to do the due diligence of learning how Fidelity acquires their data and the accuracy of it. Per his recommendation, getting quality SIP data will cost \~$750/month - which is something I'm honestly not prepared to fork up at the moment. Thanks again, u/dlauer & team, for taking the time to investigate this for me and for providing suggestions. I greatly appreciate the help.


​


I'd also like to sincerely thank everyone for commenting & awarding this post to help get traction. I will be updating it throughout the day once I finish with the data.


[Here is my post from last week covering the first occurrence of this market-wide manipulation](https://www.reddit.com/r/Superstonk/comments/n7ahcl/found_something_funky_on_the_dark_pools/?utm_source=share&utm_medium=web2x&context=3) [(wb)](https://web.archive.org/web/20210508065659/https://www.reddit.com/r/Superstonk/comments/n7ahcl/found_something_funky_on_the_dark_pools/)


​

