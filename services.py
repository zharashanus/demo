import requests
l = input("ведите язык на которую нужно перевести('введите по языковому коду'): ")
w = input("введите текст: ")



url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

payload = {
 "from": "auto",
 "to": l,
 "text": w
}