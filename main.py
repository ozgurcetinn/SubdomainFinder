import requests

target = "google.com"  # Enter a target website

with open("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "http://" + word + "." + target
        try:
            response = requests.get(url)
            if response:
                print("Subdomain Found: " + url)
        except:
            pass
