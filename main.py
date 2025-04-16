from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

API_KEY = '55e53818f217464abc0c84f8a6677527'  # 🔑 Вставь свой API-ключ сюда

def get_random_news():
    url = f"https://newsapi.org/v2/everything?q=news&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if articles:
            article = random.choice(articles)
            return {
                "title": article.get("title", "Без заголовка"),
                "description": article.get("description", ""),
                "url": article.get("url", "#"),
                "source": article.get("source", {}).get("name", "Неизвестно")
            }
    return {
        "title": "Не удалось загрузить новости",
        "description": "",
        "url": "#",
        "source": ""
    }

@app.route('/')
def index():
    news = get_random_news()
    return render_template("index.html", news=news)

if __name__ == '__main__':
    app.run(debug=True)
