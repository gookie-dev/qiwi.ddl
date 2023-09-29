import requests

url = input("Enter download link: ")

response = requests.get(url).text
slug = response.split("\\\",\\\"slug\\\":\\\"")[1].split("\\\",\\\"fileName\\\"")[0]
ext = response.split("\\\",\\\"fileName\\\":\\\"")[1].split("\\\",\\\"owner\\\"")[0].split(".")[-1]
print(f"https://spyderrock.com/{slug}.{ext}")