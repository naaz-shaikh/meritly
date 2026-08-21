import pandas as pd

def load_colleges():
    """
    Reads colleges.csv into a Pandas DataFrame.
    This is the ONLY place in the whole app that touches the CSV file directly.
    If we later switch to a database, we only change this one function —
    nothing else in the app needs to know or care.
    """
    df = pd.read_csv("data/colleges.csv")
    return df