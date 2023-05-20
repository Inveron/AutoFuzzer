import os
import subprocess
import re

#Part 1

print("===========================AUTO FUZZER===========================")
ip = str(input("What IP should the script target? "))
print("=================================================================")
#Runs the nmap and gobuster scans
print("\nScanning with nmap to find open ports....")
nmap = subprocess.run("nmap -A " + ip, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print("Nmap scan done! \n")

print("Scanning gobuster to find directories....")
gobust = subprocess.run("gobuster -e -u http://" + ip + "/ -w /usr/share/wordlists/dirbuster-ng/wordlists/common.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print("Gobuster scan done! \n")
print("=================================================================\n\n")
urls = []
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
    filterpattern = r'(http://\S+)\s\(Status: (\d+)\)'
    matches = re.findall(filterpattern, str(gobust))
    
    for match in matches:
        
        url, status = match

        urls.append(str(url))
        
    print (urls)

#runs tests and filters outputs
if nmapscan() == True:
    gobusterScan()

else:
    allPorts()

#Part 3



# for /f %i in (urls.txt) do curl %i | grep -i -E "input .*?(email|name)" >> filtered_urls.txt