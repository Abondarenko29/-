import pandas as pd
d = pd.read_csv ("acquisitions.csv")

def id (temp):
    temp = temp.replace ("c:", "")
    return int(temp)

d["acquiring_object_id"] = d["acquiring_object_id"].apply (id)
d["acquired_object_id"] = d["acquired_object_id"].fillna ("-1")
d["acquired_object_id"] = d["acquired_object_id"].apply (id)

d["term_code"] = d["term_code"].fillna ("doesn't say")

d["acquired_at"] = d["acquired_at"].fillna ("999-999-999")

d["source_url"] = d["source_url"].fillna ("https://pastebin.com/bLRBrjGh")

d["source_description"] = d["source_description"].fillna ("NoneDescription")

d.info ()