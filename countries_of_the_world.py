import pandas as pd
import matplotlib.pyplot as show
def standard_or_living (temp):
#def standard_or_living (temp, temp2, temp3, temp4):
    print (temp)
    return temp

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

#d["Standard of living"] = d[["GDP ($ per capita)", "Industry", "Infant mortality (per 1000 births)", "Deathrate"]].apply (standard_or_living)

d.plot (kind = "hist", x = "Area (sq. mi.)", y = "GDP ($ per capita)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Net migration", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Population", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Pop. Density (per sq. mi.)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Coastline (coast/area ratio)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Infant mortality (per 1000 births)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Literacy (%)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Phones (per 1000)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Arable (%)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Crops (%)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Other (%)", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Climate", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Birthrate", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Deathrate", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Agriculture", bins = 80)
show.show ()

d.plot (kind = "hist", x = "GDP ($ per capita)", y = "Industry", bins = 80)
show.show ()

d.plot (kind = "barh", x = "GDP ($ per capita)", y = "Service")
show.show ()