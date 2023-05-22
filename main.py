import os
import subprocess
import re
import requests
from bs4 import BeautifulSoup
#Part 1

print("===========================AUTO FUZZER===========================")
ip = str(input("What IP should the script target? "))
print("=================================================================")

#Runs the nmap and gobuster scans
print("\nScanning with nmap to find open ports....")
nmap = subprocess.run("nmap -A " + ip, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print("Nmap scan done! \n")

print("Scanning gobuster to find directories....")
gobust = subprocess.run("gobuster -e -u http://" + ip + " -w /usr/share/wordlists/dirbuster-ng/wordlists/common.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print("Gobuster scan done! \n")
print("=================================================================\n")

urls = []
filteredurls = []

#returns only http ports
def nmapscan():
    filterpattern = r"\d+\/tcp\s+open\s+http"
    http_ports = re.findall(filterpattern, str(nmap))

    sanitized_output = "\n".join(http_ports)

    if "http" in sanitized_output:
        return True
    
#returns all ports
def allPorts():
    filterpattern = r"\d+\/tcp"
    http_ports = re.findall(filterpattern, str(nmap))

    sanitized_output = "\n".join(http_ports)

    return sanitized_output


#Part 2 
def gobusterScan():
    #makes sure the url list includes the base url as well
    urls.append('http://' + ip + '/index.html')

    filterpattern = r'(http://\S+)\s\(Status: (\d+)\)'
    matches = re.findall(filterpattern, str(gobust))
    
    for match in matches:
        
        url, status = match

        urls.append(str(url))
    
    
    print("Urls found: ")
    for i in urls:
        print(i + "\n")

print("TCP ports found: \n" + allPorts() + "\n")

#runs tests and filters outputs
if nmapscan() == True:
    gobusterScan()

else:
    allPorts()

#Part 3 - Web Scraping



for i in urls:
    response = requests.get(i)

    soup = BeautifulSoup(response.content, 'html.parser')
    #searches for any and all input fields
    inputs = soup.find_all('input')
    
    totalinputs = 0
    fileinputs = 0
    for input in inputs:
        field_name = input.get('name')
        field_value = input.get('value')
        field_type = input.get('type')
        
        totalinputs += 1

        if field_type == "file":
            fileinputs += 1
    #prints out results per ip
    print("=================================================================\n")

    print("Scrape results for " + i)
    print("\nTotal inputs found = " + str(totalinputs))
    print("\nFile upload inputs found: " + str(fileinputs) + "\n")

        
    