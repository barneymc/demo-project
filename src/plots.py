import pandas as pd


def subtract(a, b):
    return a - b


def add(a, b):
    return a + b


data = {"Name": ["Alice", "Bob"], "Age": [24, 27], "City": ["New York", "London"]}

df = pd.DataFrame(data)

df.head(1)
