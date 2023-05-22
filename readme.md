The project is going to automate the process of fuzzing servers for the purpose of CTF's. 

The general function can be broken down into 3 parts.

1 Initial Scan for ports:

This will run an nmap on the target website and spit out any open ports.
the output needs to be sanitized with none of the other usual bullshit 
that it spits out like "starting nmap scan" If there are any web servers 
running, then it will go to step 2, otherwise it will just spit out the 
ports on the machine.

2 Gobuster Time:

This is going to run a gobuster with the common wordlist (might change 
wordlist later) and sanitize the ouput to just give the directories that 
it kicks back and the status codes on them. From here it will pass the 
directories to some kind of web scraper. It will also check for subdomains

3 Web Scraping:

This is the complicated part. This part of the script is going to scraped
every webpage on the site for things like form input fields and file 
upload fields. Once this is ran it will spit everything out either to 
the terminal or a text file and will list the following:
    - Open ports on the machine
    - Directories/subdomains and the status codes on them
    - Each webpage scraped with the form inputs found.
    - Anything else that was scanned just in case it had a weird name 
        and didnt get detected and scraped. 


note: this script requires that gobuster and nmap are installed on your system. Also i put my own path for the wordlist for now, I will change this later.

