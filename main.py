import requests

api_key = "ba57fde11d5849a7a31c0eca63e743f4"

url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2026-05-23&sortBy=publishedAt&apiKey=" \
      "ba57fde11d5849a7a31c0eca63e743f4"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print (article["description"])

