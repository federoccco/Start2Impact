# Daily Crypto report

This is a report system that fetches information from coinmarket.com  

The script use the request module sending an HTTP request to an API Endpoint through an auth key, saving the data in a JSON file

Every day, at a given time, it fetches, elaborate and save data about:  
<ol>
  <li>Most volume ($) crypto in the last 24 hours</li>  
  <li>Top and flop 10 crypto (percentage increase in the last 24 hours)</li>  
<li>The amount of money necessary to buy a single unit of each in the top 20 crypto* leaderboard</li>  
<li>The amount of money necessary to buy a single unit of all those crypto which volume is above 76'000'000$ in the last 24 hours</li>  
<li>The percentage loss (earnings) if you would have bought a single unit of each in the top 20 crypto* leaderboard the day before running the script (assuming the leaderboard has not changed)</li>  
</ol>

*When i say top (or flop) 20 crypto, i am referring to the coinmarket.com default leaderboard, thus ordered by capitalization. 

You can view the code <a href="https://github.com/federoccco/Start2Impact/blob/main/Blockchain/daily-crypto-report/main.py"> Here </a>
