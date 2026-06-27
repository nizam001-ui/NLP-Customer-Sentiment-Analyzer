import pandas as pd

data = {
    "Review_Date": pd.date_range(start="2026-05-01", periods=20, freq="D"),
    "Customer_Name": ["User" + str(i) for i in range(1, 21)],
    "Rating": [5, 1, 4, 2, 5, 5, 3, 1, 4, 5, 2, 1, 5, 4, 3, 5, 2, 1, 5, 4],
    "Review_Text": [
        "Absolutely love this machine! The coffee is hot and brews perfectly.",
        "Terrible. It arrived broken and leaks water everywhere.",
        "Good value for the money, but a bit loud.",
        "Stopped working after a week. Customer service ignored me.",
        "Best espresso maker I have ever owned. Highly recommend!",
        "Fast shipping, great taste, very easy to clean.",
        "It is okay. Nothing special, just a standard coffee pot.",
        "Complete garbage. The plastic tastes like chemicals.",
        "Solid machine, makes a great morning cup.",
        "Five stars! Beautiful design and great functionality.",
        "The frother is weak and barely works.",
        "Do not buy this. It burned my counter.",
        "Perfection. I use it every single morning.",
        "Nice features, but the water tank is a bit small.",
        "Average brew time, slightly difficult to program.",
        "A lifesaver for early mornings. So fast!",
        "Too expensive for the quality you get.",
        "Horrible experience, returning it tomorrow.",
        "Incredible flavor extraction. Worth every penny.",
        "Very good, just wish it came with a reusable filter."
    ]
}

df = pd.DataFrame(data)
df.to_csv("raw_reviews.csv", index=False)
print("Success: raw_reviews.csv created!")