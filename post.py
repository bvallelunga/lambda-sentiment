import requests

url = 'https://oysf0nmwfh.execute-api.us-west-1.amazonaws.com/api/'
#url = 'http://127.0.0.1:8000'
payload = {
        'texts': [
            "The book was good.",
            "Today SUX!"
        ]
}
response = requests.post(url, json=payload)
print(response.content)
