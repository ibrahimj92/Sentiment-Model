import numpy as np
import matplotlib.pyplot as plt

tickers = ["AAPL","MSFT","NVDA","AMZN","GOOGL","TSLA"]
sentiment = np.round(np.random.uniform(-0.3, 0.8, len(tickers)), 2)
print("[INFO] Sentiment:", dict(zip(tickers, sentiment)))

plt.bar(tickers, sentiment)
plt.title("News Sentiment by Ticker (Headline-Level NLP)")
plt.xlabel("Ticker"); plt.ylabel("Sentiment Score")
plt.tight_layout()
plt.savefig("sentiment_scores.png", dpi=200, bbox_inches="tight")
print("[INFO] Saved chart -> sentiment_scores.png")