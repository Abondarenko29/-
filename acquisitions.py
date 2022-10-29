import pandas as pd
import matplotlib.pyplot as show
d = pd.read_csv ("acquisitions.csv")

def date (temp):
    temp = temp.replace ("-", "")
    return int(temp)

def id (temp):
    temp = temp.replace ("c:", "")
    return int(temp)

d["acquiring_object_id"] = d["acquiring_object_id"].apply (id)
d["acquired_object_id"] = d["acquired_object_id"].fillna ("-1")
d["acquired_object_id"] = d["acquired_object_id"].apply (id)

d["term_code"] = d["term_code"].fillna ("doesn't say")

d["acquired_at"] = d["acquired_at"].fillna ("999-999-999")
d["acquired_at"] = d["acquired_at"].apply (date)

d["source_url"] = d["source_url"].fillna ("https://pastebin.com/bLRBrjGh")

d["source_description"] = d["source_description"].fillna ("NoneDescription")

d.plot (kind = "line", x = "acquired_at", y = "source_url")
show.show ()