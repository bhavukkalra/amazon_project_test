# amazon_project_test
to use this code first you have to install requests and bs4(Beautifullsoup) using the pip command

1) change the link to the amazon page you want to track the prices of
URL("YOUR_LINK",'User-agent' "YOUR_USER AGENT")
(to get your user agent search what is my user agent on google and copy the text displayed)

2)change the converted price array ([2:7]  in example) have to program catch the actual digits of the price
(THIS IS A FUTURE UPDATE TO THE PROJECT THAT I AM WORKING ON AFTER WHICH YOU NO LONGER NEED THIS STEP)

3) set the desired price to which you want to receive a message about price going down
(IN IF STATEMENT)

4) server.sendmail('bhavukkalra1786@gmail.com','YOUR_EMAIL_ADDRESS',msg)  change this line to fill in your email address and thats it.

in upcoming update a global emailing service is incorporated(finished) (to be pushed)

