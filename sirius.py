import requests


def request(url):
    if "https" not in url:
    	url = "https://" + url
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


url = input("Website url: \n")

with open("wordlist.list", "r") as wordlist_file:
    counter = 0
    for line in wordlist_file:
        word = line.strip()
        target_url = url + "/" + word

        counter += 1
        print("\r[+] Keywords tried: " + str(counter), end="")

        response = request(target_url)
        if response:
            print("\n[+] File/directory Discovered: " + target_url)
