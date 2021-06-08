---
title: "RIP /u/leavemeanon - WHERE ARE THE SHARES (Part 1) Resurrected "
author: "VoxUmbra"
date: "2021-06-05 23:50:27"
archived: "2021-06-08 09:06:08"
permalink: "http://reddit.com/r/Superstonk/comments/nt8ot8/rip_uleavemeanon_where_are_the_shares_part_1/"
waybackpermalink: "https://web.archive.org/web/20210605235049/https://www.reddit.com/r/Superstonk/comments/nt8ot8/rip_uleavemeanon_where_are_the_shares_part_1/"
weight: 138
---[[Part 2]](https://www.reddit.com/r/Superstonk/comments/nt8qzj/rip_uleavemeanon_where_are_the_shares_part_2/) [(wb)](https://web.archive.org/web/20210605235414/https://www.reddit.com/r/Superstonk/comments/nt8qzj/rip_uleavemeanon_where_are_the_shares_part_2/)


[[Part 3]](https://www.reddit.com/r/Superstonk/comments/nt8t9n/rip_uleavemeanon_where_are_the_shares_part_3/) [(wb)](https://web.archive.org/web/20210605235801/https://www.reddit.com/r/Superstonk/comments/nt8t9n/rip_uleavemeanon_where_are_the_shares_part_3/)


​


Hi all,


There were a lot of apes in the daily discussion thread wondering why the DD by /u/leavemeanon was gone. Turns out they've deleted their account for some reason, along with their posts. I did a bit of digging and managed to recover their posts (shoutout to <https://camas.github.io/reddit-search> [(wb)](https://web.archive.org/web/20200119041526/https://camas.github.io/reddit-search/)), which I'll be shamelessly reposting as there seems to be some demand:


​


![](/img/mowgrrt7bj371.png)
So, without further ado:


​


-----


​


This post is the first of (at least) 3. I’ve been writing it for a few days now, so it’s pretty long. Some parts are a little repetitive, but this stuff is complicated (for a reason) and I really want people to understand how it works. Clarity is important to me because 1) I want to know when I’m wrong, and 2) obscurity and complexity are pretty much the only things supporting the House of Cards.


Oh and I hate to ask but - even if you just read the TLDR (or can’t read all) but think the post is at least worth looking at, please upvote. I’ve seen the power of the bots and all the words are scary to begin with. Save the award money for more GME 🚀🚀


//


TLDR:
-----


APs, like Citadel, use ETFs to provide liquidity. When there are lots of buyers (GME in January), it’s their job to make sure those buyers have sellers to reduce volatility. Yes, stopping squeezes is a large part of their job. They do this by buying ETF shares and selling the GME inside. **BUT** the SEC has made a series of exemptions for APs that allows them to sell ETF shares up to 6 days before depositing the securities needed for creation. It’s selling before buying, and not locating shares to borrow. That’s naked shorting, up to 50,000 shares at a time. And the securities needed for deposit within 6 days, the ones naked shorted? They go unreported as part of *bona fide* market making. That’s where (some of) the shares are. In this post, I go looking for them.


//


ELIA:
-----


ETFs trade on the market like stocks, but they actually represent some proportion of underlying securities. Authorized Participants (APs are big banks and Citadel) trade ETFs in groups of 50,000 shares called “creation baskets” - and these creation baskets can be exchanged with the underlying securities in the ETFs proportions. (lol it’s actually *any* proportion, but more on that later)


**For an AP: 50,000 shares of ETF = “creation basket” = 50,000 shares of underlying securities.**


They’re interchangeable, for a small fee.


This process allows APs to profit from arbitrage: the process of creating or redeeming creation baskets to profit from differences in an ETF’s market price and the Net-Asset-Value (NAV) of the securities underlying it. A presentation given at Wharton (linked below) showed that APs can make higher and more “predictable” returns by exploiting an exemption that allows them to **sell ETF shares that they do not own up to 6 days before purchasing the securities needed to create them.**


This is effectively short selling via ETF, **and** they are legally exempt from locating a valid share to borrow. So it’s naked short selling via ETF.


Also, the shares deposited (short, naked, or otherwise) for ETF creation are not recorded on the APs books, so any short interest involved in arbitrage will not show up in FINRA numbers. Per the [Securities Act of 1933](https://sec.report/Form/Securities-Act-of-1933.pdf) [(wb)](https://web.archive.org/web/20210503104609/https://sec.report/Form/Securities-Act-of-1933.pdf).


*However*, as the presentation explains, evidence of this activity would include creation of ETF shares without redemption, particularly in ETFs that are more liquid than their underlying securities. *cough, GME, cough*


This would result in consistently increased ownership in the ETF, so evidence of this process can be found in ETF ownership anomalies.


I discuss this data and more, which ultimately suggest, in my opinion, overwhelming evidence of heinous levels of naked short selling across multiple securities, systemically linked through these ETFs and hidden by *bona fide* market making arbitrage provisions. Due to liquidity, or lack thereof, and GME’s 60+ ETFs, it was the perfect target for this activity. This is why GME is the black hole.


*Whoopsie*


I argue that Citadel and friends tried bankrupting GME with this system by hiding naked shorts and FTDs across these ETFs, hoping to dilute share price all the way to bankruptcy. I discuss mechanism behind this, HFT’s role, how BoA, GS, and JP got involved, how RC pretty much handed Citadel’s balls over to BlackRock, and what all the footprints left behind might reveal about the scope of this whole thing.


Spoiler, they’re fucked^(fucked)


//


Preface
-------


(( **I’m skeptical by nature. Like any tool, skepticism isn’t inherently good or bad - it’s just useful. In some cases more than others.** ))


As a disclaimer, not only am I **not** a financial advisor. 6 months ago I had virtually **no** financial background whatsoever. The entirety of my relevant knowledge has come from months of independent research and personal interviews. I believe it’s fair to say I have a proficiency for puzzles and a nose for bullshit - and the dynamic between the two has served me well in the past.


I attempt to discuss an *incredibly* complex system here, the depth of which I’m certainly ignorant to. I decided the “Great Wall of Text” approach just was too much. Plus, I’ve been so close to putting things together for such a long time, I’m eager to have it reviewed. So I’d like present the story as soon as possible it to encourage more apes to dig deeper into this stuff.


I’m sure many of you have years of experience beyond me, but I’ve gone to great lengths in trying to understand the mechanics and regulations at a granular level - as well as their context in the events we’ve hodled through - so I hope you’ll at least give me a chance. I *really* hope you can correct me where I’m mistaken. I’ll try to answer all questions I can in the comments. I just like to figure stuff out.


It took months of notes and connecting dots to put this together, and I’ll eventually discuss mechanics and examples of arbitrage, creation/redemption, liquidity provisions, ex-clearing, synthetic options positions, gamma-delta hedging, disclosure laws, exemptions, Repos, RRPs, APs/MMs/BDs, FTDs, ETFs, ETNs, and all the regulations supposedly governing this whole fiasco. I try to stick to the official facts and documents, and I hope you glance at the sources I linked.


I’ll try keeping it to 3 chapters, though. This post will be the first - on ETF Arbitrage and it’s importance to GME.


Introduction
============


The true beginning of this story has been diligently and beautifully covered in the last few weeks by u/autobitt, u/dlauer, Dr. T, Wes Christian, and more. It starts with greedy and malicious short sellers making fortunes at the expense of companies, their employees, and their shareholders. This problem has existed for decades but was able to scale around 1990 - with the emergence of High Frequency Trading (HFT), Exchange Traded Funds (ETFs) and Options trading. Together, they allowed shares sold short and FTDs to essentially be scattered in various places, as [this 2019 video](https://youtu.be/ncq35zrFCAg) [(wb)](https://youtu.be/ncq35zrFCAg) and [this 2013 SEC risk alert](https://www.sec.gov/news/press-release/2013-151) [(wb)](https://web.archive.org/web/20210517195739/https://www.sec.gov/news/press-release/2013-151) explain.


I urge you, at some point, to look closely at both of those. Based on everything we’ve seen, I believe they are very pertinent and I’ll be leaning heavily on them to explain my reasoning.


ETFs and options trading allow short positions in many individual securities to aggregate, roll forward, and be dispersed (and hidden) in index funds and derivatives. This is, effectively, refurbishing FTDs to manipulate the supply and drive price down. The potential consequences of this scheme was [forewarned in 2006 by Patrick Byrne](https://youtu.be/nLnw2_q5iMk) [(wb)](https://youtu.be/nLnw2_q5iMk) when his company, Overstock, was victimized by this process. Byrne worked with Wes Christian in 2006 to bring attention to the issue, but traction was soon lost in 2008 when a… *more immediate disaster*… popped up.


In the 2000’s, High-Frequency-Trading (HFT) began dominating the markets. Citadel, possibly the world’s largest HFT trading firm, AND FRIENDS got involved when realized that “predictable” returns can be made through ETF arbitrage.


Index funds like ETFs hold securities in certain proportions to track some index. To an Authorized Participant (AP) like Citadel, ETF shares are traded in baskets of 50,000, and they’re exchangeable with securities in the proportions of the ETFs holdings. This is called creation (buying shares and creating ETF) and redemption (redeeming ETF for shares inside).


If there are differences in an ETFs trading price and it’s Net-Asset-Value (NAV), even for a fraction of a second, this is a profitable opportunity for an AP. If NAV > ETF price, then the 50,000 underlying securities are worth more individually than as an ETF. APs can buy ETF, redeem ETF shares for its underlying shares, then sell for a profit. If NAV < ETF price, APs can create ETF shares by depositing the underlying securities into the ETF fund, which provides the AP with ETF shares to sell for profit.


**APs are also allowed to sell ETF shares up to 6 days before creating them**, as explained in the linked video. This is effectively a short position, and *because **there is no supply limit for ETFs** (and ETF creation/redemption has less regulation than in short selling equities) **this can theoretically be repeated and hidden in perpetuity.**


And they don’t even need a locate. This is essentially legal naked shorting renamed *providing liquidity*.


So, for example, if the AP has reason the believe the NAV will decrease within 6 days, they can redeem ETF shares and delay creation, hoping to profit from the decreased NAV. The video calls this “directional short selling” - basically a euphemism for legal naked short selling.


In most cases, this process is effective in reducing volatility by moving the “noise trading” into various ETFs. GME, clearly, is not most cases. I don’t think the system considered what happens when there are more shares owed than should be owned.


But does this really even happen? Or to a significant degree? From the Wharton presentation:


“ *Directional short selling is the strongest indicator of both short interest percentage and FTDs in ETFs.* “


This was likely practiced in a number of stocks. Or entire ETFs, such as XRT, which the presentation shows as having 77 million 13F (institutional) owners in 2017, despite only 11 million shares outstanding…


**I argue that GameStop was the crux of Wall Street’s arrogance. I argue that existing data indicates naked short selling attempts to send GME into a death spiral by rolling** ***at least*** **double the number of outstanding shares in derivative short positions and FTDs, effectively diluting share price by inflating supply.**


This would’ve been high-risk/high-reward with GME, because it’s 70 million shares outstanding is so small compared to other targeted companies. Blockbuster had 220 million. AMC has 450 million.


With such limited supply, these “refurbished” (rehypothecated, rolling) FTDs can be more effective in driving price down. However, if the “bankruptcy death spiral” fails, covering **years worth** of these positions gets *very* violent.


*Why?* Well the supply is comparatively low to begin with, and the creation/redemption process *during the death spiral* actually syphons real shares from GMEs float (I’ll explain how that works below). So the arbitrage process has moved a portion of the (already small) float into ETFs, and each share covered simultaneously increases demand and reduces supply. At some point, GME’s liquidity becomes bone dry because so many of it’s actual shares were converted into ETF shares.


Demand for GME keeps rising, but supply is already zero. Demand drives the price up, lack of liquidity drives the price up, APs scramble to find ETF shares, further increasing demand and decreasing ETF supply. However, this time, providing the GME to cover shorts **adds no extra supply**, so the price for anything containing GME goes vertical. The whole process starts feeding on itself in reverse, and I argue that this has already begun.


Chapter 1: ETF ARBITRAGE
========================


The Game
--------


[Blackrock’s explanation](https://youtu.be/iX7fOx5G40A) [(wb)](https://youtu.be/iX7fOx5G40A)


I’m the context of ETFs, arbitrage is simply profiting from the price difference of a security and an ETF containing that security. ETF shares trade on the market at market price, like an equity stock, but an ETF share actually represents an aggregate total of many stocks in a set proportion. The aggregate value of these equities in that proportion is called the Net-Asset-Value (NAV).


ETF shares don’t always trade at their NAV. When this happens, there is a potential for profit because 50,000 shares of the ETF == 50,000 shares of the underlying securities in price, but Authorized Participants (APs) can exchange them nonetheless for a small fee. APs are usually big Banks and Market Makers (MMs): JP, Goldman, BoA, oh and Citadel.


This “exchange” is done through a process called creation and redemption. APs, *exclusively*, are allowed to do this, and APs are usually big Banks and Market Makers (MMs): JP, Goldman, BoA, oh and Citadel. For example:


Blackrock’s ETFs (iShares) are generally rebalanced 4 times per year: at the end of February, May, August, and November. So if GameStop goes to $350 in January after being balanced around $16 in November, the list I mentioned above (and more) can buy IWM, IJR, IWN, IJT, and all the other ETFs that GME is a portion of, break them open into their individual shares (this is done in 50,000 share baskets called Creation Units) and sell the GME inside. Because the ETFs proportioned GME at a $16 dollar price, the ETFs trading price didn’t go up as much it would if GME were proportioned in real time. NAV =/= ETF trading price, so while GME is rising, 50,000 ETF shares are cheaper than the 50,000 shares they’re redeemed for, because of the GME inside.


*Why* are they allowed to do this?? According to the SEC, the answer is… [Liquidity](https://www.sec.gov/rules/sro/nscc/2020/34-89088.pdf) [(wb)](https://web.archive.org/web/20210601044222/https://www.sec.gov/rules/sro/nscc/2020/34-89088.pdf) Oh, and somehow also [efficiency and transparency](https://www.sec.gov/investment/exchange-traded-funds-small-entity-compliance-guide) [(wb)](https://web.archive.org/web/20210601221622/http://www.sec.gov/investment/exchange-traded-funds-small-entity-compliance-guide).


//


Let’s take a step back for a second. So some portion of GME’s 70 million shares are purchased by ETF funds, like BlackRock’s iShares, in order to issue the first ETF shares. Then, APs come in and either 1) put some of those GME shares back or 2) take more out, based on the NAV of the ETF. Now, and this this important, **because APs PROFIT from volatility through arbitrage, they have an incentive to favor creation over redemption.**


If, as an AP, you buy the shares from the market (or just naked short them), and have them trade as ETF instead, you decrease supply of the security. This increases volatility, which creates more opportunity for arbitrage - i.e. more opportunity for profit. AND if you have more shares for creation/redemption, you have better control over the prices of both the ETF and it’s securities.


[Did I mention that Citadel is the world’s largest HFT firm](https://www.insidermonkey.com/blog/10-biggest-hft-firms-in-the-world-586528/?singlepage=1) [(wb)](https://web.archive.org/web/20210601044205/https://www.insidermonkey.com/blog/10-biggest-hft-firms-in-the-world-586528/?singlepage=1)?


Anyway, there is a very strong incentive to take shares from securities and have them trade as ETF instead. And I’d argue that at some point, the “providing liquidity” excuse becomes void, because the AP was the one who diminished the liquidity in the first place.


//


Well what happens when an 7% of an ETF contains shares of a company you intend to bankrupt?


[This 2019 Presentation at Wharton](https://youtu.be/ncq35zrFCAg) [(wb)](https://youtu.be/ncq35zrFCAg), as linked above, briefly talks about XRT. I’ve linked it a few times now, *please* watch or save that video.


The presenter notes that the example is extreme, and I’d say it’s borderline heinous. The SPDR fund had issued \~11 million shares of XRT in 2017, but the 13F filings added up to *77 million shares*. There had been 66 million shares created, but not redeemed. AP’s have the **exclusive** ability to create shares, and in 2017 the settlement period was 2 days instead of 6…


The presentation also discusses an AP’s exemption allowing them to sell ETF shares up to **6 days** before depositing the required securities into the ETF fund to create the basket. The presenter discusses certain cases where ETFs are more liquid than their underlying securities, like GME, and the ETF shares seem to be continually created without ever being redeemed. This led to XRT.


So of those 77 million XRT shares, say 6 % were GME (not sure exactly what it was at the time but it’s 6.75% now). That represents **4.62 million** shares of GME trading in XRT baskets. That represents almost 10% of GME’s reported float, from this one ETF alone.


And *where* are these shares reported, exactly? I’ll let BlackRock tell you:


** “any securities accepted for deposit and any securities used to satisfy redemption requests will be sold in transactions that would be exempt from registration under the Securities Act of 1933, as amended (the “1933 Act”).” **


As I’m sure you guessed, they’re off the books.


//


**To recap:**


When institutional investors and retail investors place bids for ETF shares, APs (banks and citadel) can sell ETF shares that they don’t have to “provide liquidity”. Then, within 6 days, the AP must deposit the sold securities into the ETF Fund.


BUT!


APs can (and have been known to) profit from expected decreases in the NAV of the ETF by waiting up to 6 days to deliver the shares. Until settled, this is a naked short position, and it’s not reported in the short interest. Oh and one more thing,


[GME is in over 60 ETFs.](https://fintel.io/soe/us/gme) [(wb)](https://web.archive.org/web/20210316134511/https://fintel.io/soe/us/gme) Go to “Top ETF” under “Ownership”. 68 listed ETFs right now. An AP can short XRT today, and settle by shorting IWM next week, then GAMR, then XRT again, then IJR…. you get the picture.


//


And it keeps getting worse.


How exactly do you think this creation/redemption process is carried out in, say, Citadel? Is there a creation/redemption department with a few dozen people monitoring all these ETFs, the underlying securities, the NAV, and the incoming orders - looking for price discrepancies? A few hundred people? Just Ken-bo? Is Kenny G the Michael Jordan of arbitrage?


Nope. Citadel is all about HFT. It’s algos.


From [Investopedia](https://www.investopedia.com/articles/active-trading/092114/strategies-and-secrets-high-frequency-trading-hft-firms.asp) [(wb)](https://web.archive.org/web/20210417224320/https://www.investopedia.com/articles/active-trading/092114/strategies-and-secrets-high-frequency-trading-hft-firms.asp) in 2020 -


“Another way these [HFT] firms make money is by looking for price discrepancies between securities on different exchanges or asset classes. This strategy is called statistical arbitrage, wherein a proprietary trader is on the lookout for temporary inconsistencies in prices across different exchanges. With the help of ultra fast transactions, they capitalize on these minor fluctuations which many don’t even get to notice.”


So, to be clear, Citadel, [the world’s largest HFT firm](https://www.insidermonkey.com/blog/10-biggest-hft-firms-in-the-world-586528/?singlepage=1) [(wb)](https://web.archive.org/web/20210601044205/https://www.insidermonkey.com/blog/10-biggest-hft-firms-in-the-world-586528/?singlepage=1) by \~20x the AUM of second place - the very same firm that [clears over 50% of RH’s trades](https://cdn.robinhood.com/assets/robinhood/legal/RHS%20SEC%20Rule%20606a%20and%20607%20Disclosure%20Report%20Q2%202020.pdf) [(wb)](https://web.archive.org/web/20201218115641/https://cdn.robinhood.com/assets/robinhood/legal/RHS%20SEC%20Rule%20606a%20and%20607%20Disclosure%20Report%20Q2%202020.pdf) and gets almost as much total trading volume as the entire NYSE, does the vast majority of that volume with lines of code, stuffed into thousands of black boxes in some fortress in the middle of nowhere… They buy *yachts* with this creation/redemption system. Do you think these lines of code secure a locate when they short shares to “provide liquidity”?


(( Side note on another gem from that link:


“HFT firms also make money by indulging in momentum ignition. The firm might aim to cause a spike in the price of a stock by using a series of trades with the motive of attracting other algorithm traders to also trade that stock. The instigator of the whole process knows that after the somewhat “artificially created” rapid price movement, the price reverts to normal and thus the trader profits by taking a position early on and eventually trading out before it fizzles out.”


So yeah, no wonder we’ve had dozens of days with insane swings that ended up within 2 percent of open. Those RH orders pile up on Ken’s computers and he can basically execute them however and whenever he’d like. I digress. ))


//


GameStop
--------


Back to GME in January. Ryan Cohen stepped in and at one point, GME did almost 200 million volume in a day. As buy orders come in, market makers like Citadel had to add liquidity from somewhere. After all, GME’s 70m shares outstanding pales in comparison to most other stocks in XRT, and just in general. AMC has 450m. NOK has 4.7 billion.


So in a perfect world, these HFT algos buy ETF shares from the market, redeem them (often from BlackRock, who owns iShares, or StateStreet who distributes SPDR ETFs), and sell the GME. Remember - the number of ETF shares outstanding can fluctuate, but not GME (without shorts or moves from GameStop), so this would reduce the total number of shares of the ETF and *restore* the shares of GME that the process had originally depleted.


So unless I’m mistaken here, keeping in mind Citadel itself clears almost the same volume as the entire NYSE - to provide liquidity and decrease volatility as buying pressure go up (aka delay the MOASS), should be buying ETF shares to put the GME back. So ETF ownership should **decrease** as they’re bought up and broken apart. If the ETF ownership stays the same, the extra liquidity is more likely to be short positions, naked or otherwise (to be covered the next day or who knows when).


Well, somehow, from January 15-March 31, ETF institutional ownership **went up**.


//


Here they are
-------------


I did some math.


I used FINRA numbers and the official ETF issuer’s websites (SEC requires them to provide this) to find 1) total shares outstanding today in May (from issuer), 2) institutional ownership from Jan and March (FINRA), 3) the percent GME (issued), and 4) who bought shares (and who did **NOT** buy shares).


I looked at about 30 of GME biggest ETFs are picked out the ETFs with the most shares floating around. These account for the majority of total volume. Here are some of the standouts, as of, May 31:


**IWM** - (0.44% GME) - **300m shares outstanding and 345m institutional ownership.**


345m IWM shares represents 1.5m GME shares.


**IJR** - (1.15% GME) - **629.7m shares outstanding and 444m institutional ownership.**


1.15% of 629.7m shares is 7.24 million shares of GME.


**FNDX** - (1.01% GME) - **128.55m shares outstanding and 100.4m institutional ownership.**


Another 1.3 million GME.


*last but not least*


[Wedbush back at it again with](https://www.stocklaw.com/securities-fraud-blog/2019/june/wedbushs-latest-penalty-is-an-8-1-million-sec-fi/) [(wb)](https://web.archive.org/web/20210601044224/https://www.stocklaw.com/securities-fraud-blog/2019/june/wedbushs-latest-penalty-is-an-8-1-million-sec-fi/) **GAMR** - (1.42% GME) - **70.77m shares outstanding and 190,000 institutional ownership.**


Another million.


Honorable mention goes to XRT, with 15 million institutional owners holding a total 1 million GameStop shares, though XRT has only 9m shares outstanding.


**Adding up just the ETFs I looked at, there are over 20 million claimed owners GME via ETF**


That 20m number doesn’t even include retail ownership in ETF, short interest, “family offices” (like Archegos) that don’t have to report their positions to the SEC, any shares from ivestco ETFs (they have many shares outstanding but no reported GME weight despite owning GME, per fintel), or any trades settled in ex-clearing.


It also excludes short positions extended by options and other derivative instruments, which I’ll talk about in the next post.


This is just the tip of the Glacier.


Even the at 20 million at face value means that, as of May, there is a **float sized chunk** of GME trading as ETF shares.


I’d estimate, just through the ways around regulation that an ape can find on the internet, the number is *at least* twice that. Byrne mentioned that it could be closer to 5x the reported numbers.


When Ryan Cohen simultaneously mapped GameStop’s future and gobbled up 9 million shares, I think shorts piled into ETFs, particularly BlackRock’s iShares. They got a glimpse. In light of this, I think it’s *very* telling that they hodled. Hodled Citadel, by the balls, that is.


Oh, and somehow, almost every ETF I looked at miraculously **increased** in shares outstanding and institutional ownership 2020-2021, even from Jan to March. Despite the fact that the NAV was consistently higher during those periods…


Among the buyers were Morgan Stanley, Bank of America, Goldman Sachs…


So who were the sellers?

