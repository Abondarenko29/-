import pandas as pd
import matplotlib.pyplot as show

def group (temp):
    return temp.split (" ")[1]

d = pd.read_csv ("StudentsPerformance.csv")

d["race/ethnicity"] = d["race/ethnicity"].apply (group)

print (d["race/ethnicity"])

d.plot (kind = "line", x = "lunch", y = "math score")
show.show ()