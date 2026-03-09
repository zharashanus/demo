import requests
l = input("ведите язык на которую нужно перевести('введите по языковому коду'): ")
w = input("введите текст: ")



url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

payload = {
 "from": "auto",
 "to": l,
 "text": w
}
headers = {
 "x-rapidapi-key": "2688537f06msha893320bbef5c97p17b443jsn78e51307cfb2",
 "x-rapidapi-host": "google-translate113.p.rapidapi.com",
 "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

t = response.json()["trans"]

if l is not l[1]:
    print(f"Переведенный текст: {t}")

else:
    print(f"Введите язык правильно.")

def new_profile(code):
 return "fixing profile"