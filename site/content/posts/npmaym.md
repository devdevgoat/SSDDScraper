---
title: "Some accurate data, straight from eToro API calls. "
author: "taranasus"
date: "2021-06-01 05:08:12"
archived: "2021-06-08 09:41:42"
permalink: "http://reddit.com/r/Superstonk/comments/npmaym/some_accurate_data_straight_from_etoro_api_calls/"
waybackpermalink: "https://web.archive.org/web/20210601095219/https://www.reddit.com/r/Superstonk/comments/npmaym/some_accurate_data_straight_from_etoro_api_calls/"
weight: 207
---Hello all! Sorry to beat the drum about this but I feel like it should be summed up one last time as I'm a stickler for accurate data and I have confirmation on some of the numbers that have been floating around the sub yesterday with regards to eToro.


**Short version (TL;DR): I have confirmed by combing through the eToro APIs that there are exactly 96,660 GME holders on the eToro platform. Then, by applying lots of math and removing the top 10 GME institutional holders, as well as RC himself, it resulted that, on average, apes should be holding 6.22 shares each. However, we know from various other sources (Nordnet, Avanza, some private trader groups I'm a part of) that the average is SIGNIFICNATLY higher than that, anywhere between 14 and 19 shares per ape. Soooooo hedgies R fuk.**


**So if ape should be holding 6 shares, but ape actually holding 14 shares, what are the extra 8 shares made of? Fairy dust of course!**


Long version:
=============


Seeing so many people post screenshots from eToro with various numbers of holders lead me to believe that this data should be hiding somewhere in the API calls (spoiler, IT IS).


The call we're most interested about is:


"<https://www.etoro.com/sapi/insights/insights/uniques?client_request_id=> [(wb)](https://www.etoro.com/sapi/insights/insights/uniques?client_request_id=)" (I removed my ID because, you know, it's mine)


So that call will give back data on ALL of the instruments within eToro, but we're only interested in instrument id 1699, because that's our boy.


![](/img/8bpgwy37wk271.png)
And this is to verify that it's our boy:


![](/img/1s73s2d9wk271.png)
So going back to the first screencap we have a few interesting fields


- API URL: /insights/uniques  

- Percentage: 6.372391  

- Total: 96,660


It doesn't take a rocket surgeon to figure out what these numbers are. Total of eToro accounts that hold GME: 96,660. Percentage of eToro accounts this represents: 6.372%.


So if we're to do a 96660 / 0.06372 = 1,516,949 eToro accounts.


Yeah, so what? Well let's do the same math for a different stock.... why not NVIDIA Corp since I have a GPU in my computer:


![](/img/0n4a7ps8xk271.png)
Let's find instrument 1137


![](/img/8b4ftr4exk271.png)
154,056 eToro accounts hold NVIDIA stock, with a percentage of 10.15589, which means if I do the same math again:


154056 / 0.1015589 = 1,516,912


Would you look at this then! Almost identical number! Let's do it for one more, without screenshots so this post is not 10 miles long. Let's pick something completely random: "Imerys" - ID: 5768 - Total: 172 - Percentage: 0.011338825192232642


172 / 0.011338825192232642 = (guess what) 1,516,912


So we've established with a pretty high level of certainty that there are:


1,516,912 eToro users, but more importantly, **that 96,660 of these users hold GME.**


We also know, with a high level of certainty (information not yet 100% confirmed, currently taking eToro at face value with this), that 1.5% of all GME holders are on eToro. [We know this from eToro themselves](https://www.reddit.com/r/Superstonk/comments/nmos5k/what_the_actual_fuck_did_etoro_just_say/) [(wb)](https://web.archive.org/web/20210531173907/https://i.redd.it/hkk1b5937s171.jpg) which [know it from GameStop](https://www.reddit.com/r/Superstonk/comments/np4wwu/etoro_got_their_15_of_all_gme_holder_straight/) [(wb)](https://web.archive.org/web/20210531211802/https://www.reddit.com/r/Superstonk/comments/np4wwu/etoro_got_their_15_of_all_gme_holder_straight/). So that means that the total number of GME holders is:


**96,660 / 0.015 = 6,440,000 holders**


**So there are a total of almost 6.5 million GME shareholders.** It's very important to note that BlackRock (with their 8.5 mill shares) probably also counts as only 1 shareholder. Same probably goes for RC and his 9.whatever million shares.


I'm almost done with the math just bare with me. According to yahoo finance, the marketcap of GME is 15.711Billion USD, and with a closing price of 222 USD last Friday this means that there should be around (15.711B / 222) = 70.7 Million shares in existence.


**So 70.7M shares / 6,440,000 shareholders = 11 shares per holder on average.**


Does that sound right? I mean at first glance it sound fairly reasonable but let's mull this data a little more! Let's start by removing [the top 10 institutional shareholders](https://money.cnn.com/quote/shareholders/shareholders.html?symb=GME&subView=institutional) [(wb)](https://web.archive.org/web/20210605132941/https://money.cnn.com/quote/shareholders/shareholders.html?symb=gme&subView=institutional), which total 21,434,968 shares between them:


(70.7M - 21.4M) / (6.44M - 10) = 7.655 shares per holder


This starts to not look right considering there are plenty of retail investors with xxxx, xxxxx, shares.


But there's more, we also know that RC [owns around 13% of GS shares](https://www.forbes.com/sites/jonathanponciano/2021/04/08/gamestop-taps-billionaire-investor-ryan-cohen-as-board-chair-sending-shares-surging-anew/?sh=3b48faf04db6) [(wb)](https://web.archive.org/web/20210601190957/https://www.forbes.com/sites/jonathanponciano/2021/04/08/gamestop-taps-billionaire-investor-ryan-cohen-as-board-chair-sending-shares-surging-anew/?sh=3b48faf04db6). So if we do a:


(70.7M * (1-0.13) - 21.4M) / (6.44M - (10 (Hedgefunds) + 1 (Ryan))) =


6.22811 shares per holder on average
====================================


That is complete nonsense. We know for a fact [from this post](https://www.reddit.com/r/Superstonk/comments/nnngl6/update_dd_i_did_the_math_latest_nordnet_and/) [(wb)](https://web.archive.org/web/20210601190957/https://www.reddit.com/r/Superstonk/comments/nnngl6/update_dd_i_did_the_math_latest_nordnet_and/) that, on average, there are 15.82 shares / ape. From some other Telegram investor groups that have done counts, they've reported back an average of 19 shares per person.


This thing is nakeder than a sphynx cat.


Okay I'm done, hope you found this useful. I've spent way too much time putting this post together... Please feel free to poke holes in this post, but I'm fairly confident in the accuracy of this data, especially since most of it is verifiable.


Hedgies


B


FUKKDSJAD:JSAKLDJSAKLDJLSAKDSA


EDIT: ***Considering that the average should be 6, but the average appears to actually be between 14 and 19, that means the stock is oversold between 230 % and 316%. OH SWEET NELLY THIS IS GOING TO HURT WHEN IT COMES UNDONE.***


Edit 2: loads of people pointing out that the 1.5% number is from April 15th, while the rest of the data I used is from today. More people have been getting into GME side April 15th and more people have been increasing their positions. There's no evidence to suggest that the 1.5 has changed in any significant way since that time as there's no reason to believe that people's choices for trading platforms has shifted in any way. The only thing that has probably increased since then is the average number of shares held per ape which just raises the SI. 


Based on the data above it's fairly safe to say we're living with at least 200%SI, but I feel like the exact number past this point is just morbid curiosity since it's not like the hedges can save themselves in this situation.

