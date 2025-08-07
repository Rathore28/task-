import requests
from bs4 import BeautifulSoup

# NPR News Page (Static content)
url = "https://www.npr.org/sections/news/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <h2> tags with class "title"
    headlines = soup.select("h2.title")

    headline_texts = [h.get_text(strip=True) for h in headlines]

    if headline_texts:
        with open("headlines.txt", "w", encoding="utf-8") as f:
            for idx, headline in enumerate(headline_texts, 1):
                f.write(f"{idx}. {headline}\n")
        print(f"{len(headline_texts)} headlines saved to 'headlines.txt'.")
    else:
        print("No headlines found on the page.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
