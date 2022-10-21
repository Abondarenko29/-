import pandas as pd

def float_ (widsotok):
    try:
        widsotok = str (widsotok)
        return float(widsotok.replace(',', '.'))
    except: pass

#дитяча смертність (на 1000 народжених), ВВП ($ на душу населення), Смертність, Промисловість

d = pd.read_csv ("countries of the world.csv")
for a in d:
    d[a] = d[a].fillna (0)
    d[a] = d[a].apply (float_)