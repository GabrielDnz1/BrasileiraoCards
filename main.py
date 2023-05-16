#Pandas
import pandas as pd

# Variables read from Seasons/Variables.py
from Variables import season2007, season2008, season2009, season2010, season2011, season2012, season2013, season2014, season2015, season2016, season2017, season2018, season2019, season2020, season2021, season2022

# Running Dataframes for each specific season

# Season 2007 #
print("All data obtained by TransferMarkt Fairness, more info: github.com/GabrielDnz1")
print("                                    /Season 2007-08/")
print(season2007)
season2007 = pd.read_csv("Seasons/BRSeason2007.csv")

# 2007 Yellow Cards #
season2007['Yellow Cards'] = pd.to_numeric(season2007['Yellow Cards'], errors='coerce')
TotalYC2007 = season2007['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2007}")

# 2007 Red Cards & Total Cards #
season2007['Red Cards'] = pd.to_numeric(season2007['Red Cards'], errors='coerce')
TotalRC2007 = season2007['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2007}")
print(f"Total Cards: {TotalRC2007 + TotalYC2007}")

# Season 2008 #
print("                                 /Season 2008-09/")
print(season2008)
season2008 = pd.read_csv("Seasons/BRSeason2008.csv")

# 2008 Yellow Cards #
season2008['Yellow Cards'] = pd.to_numeric(season2008['Yellow Cards'], errors='coerce')
TotalYC2008 = season2008['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2008}")

# 2008 Red Cards & Total Cards #
season2008['Red Cards'] = pd.to_numeric(season2008['Red Cards'], errors='coerce')
TotalRC2008 = season2008['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2008}")
print(f"Total Cards: {TotalRC2008 + TotalYC2008}")

# Season 2009 #
print("                                 /Season 2009-10/")
print(season2009)
season2009 = pd.read_csv("Seasons/BRSeason2009.csv")

# 2009 Yellow Cards #
season2009['Yellow Cards'] = pd.to_numeric(season2009['Yellow Cards'], errors='coerce')
TotalYC2009 = season2009['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2009}")

# 2009 Red Cards & Total Cards #
season2009['Red Cards'] = pd.to_numeric(season2009['Red Cards'], errors='coerce')
TotalRC2009 = season2009['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2009}")
print(f"Total Cards: {TotalRC2009 + TotalYC2009}")

# Season 2010 #
print("                                 /Season 2010-11/")
print(season2010)
season2010 = pd.read_csv("Seasons/BRSeason2010.csv")

# 2010 Yellow Cards #
season2010['Yellow Cards'] = pd.to_numeric(season2010['Yellow Cards'], errors='coerce')
TotalYC2010 = season2010['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2010}")

# 2010 Red Cards & Total Cards #

season2010['Red Cards'] = pd.to_numeric(season2010['Red Cards'], errors='coerce')
TotalRC2010 = season2010['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2010}")
print(f"Total Cards: {TotalRC2010 + TotalYC2010}")

# Season 2011 #
print("                                 /Season 2011-12/")
print(season2011)
season2011 = pd.read_csv("Seasons/BRSeason2011.csv")

# 2011 Yellow Cards #
season2011['Yellow Cards'] = pd.to_numeric(season2011['Yellow Cards'], errors='coerce')
TotalYC2011 = season2011['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2011}")

# 2011 Red Cards & Total Cards #
season2011['Red Cards'] = pd.to_numeric(season2011['Red Cards'], errors='coerce')
TotalRC2011 = season2011['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2011}")
print(f"Total Cards: {TotalRC2011 + TotalYC2011}")


# Season 2012 #
print("                                 /Season 2012-13/")
print(season2012)
season2012 = pd.read_csv("Seasons/BRSeason2012.csv")

# 2012 Yellow Cards #
season2012['Yellow Cards'] = pd.to_numeric(season2012['Yellow Cards'], errors='coerce')
TotalYC2012 = season2012['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2012}")

# 2012 Red Cards & Total Cards #
season2012['Red Cards'] = pd.to_numeric(season2012['Red Cards'], errors='coerce')
TotalRC2012 = season2012['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2012}")
print(f"Total Cards: {TotalRC2012 + TotalYC2012}")


# Season 2013 #
print("                                 /Season 2013-14/")
print(season2013)
season2013 = pd.read_csv("Seasons/BRSeason2013.csv")

# 2013 Yellow Cards #
season2013['Yellow Cards'] = pd.to_numeric(season2013['Yellow Cards'], errors='coerce')
TotalYC2013 = season2013['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2013}")

# 2013 Red Cards & Total Cards #
season2013['Red Cards'] = pd.to_numeric(season2013['Red Cards'], errors='coerce')
TotalRC2013 = season2013['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2013}")
print(f"Total Cards: {TotalRC2013 + TotalYC2013}")

# Season 2014 #
print("                                 /Season 2014-15/")
print(season2014)
season2014 = pd.read_csv("Seasons/BRSeason2014.csv")

# 2014 Yellow Cards #
season2014['Yellow Cards'] = pd.to_numeric(season2014['Yellow Cards'], errors='coerce')
TotalYC2014 = season2014['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2014}")

# 2014 Red Cards & Total Cards #
season2014['Red Cards'] = pd.to_numeric(season2014['Red Cards'], errors='coerce')
TotalRC2014 = season2014['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2014}")
print(f"Total Cards: {TotalRC2014 + TotalYC2014}")

# Season 2015 #
print("                                 /Season 2015-16/")
print(season2015)
season2015 = pd.read_csv("Seasons/BRSeason2015.csv")

# 2015 Yellow Cards #
season2015['Yellow Cards'] = pd.to_numeric(season2015['Yellow Cards'], errors='coerce')
TotalYC2015 = season2015['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2015}")

# 2015 Red Cards & Total Cards #
season2015['Red Cards'] = pd.to_numeric(season2015['Red Cards'], errors='coerce')
TotalRC2015 = season2015['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2015}")
print(f"Total Cards: {TotalRC2015 + TotalYC2015}")


# Season 2016 #
print("                                 /Season 2016-17/")
print(season2016)
season2016 = pd.read_csv("Seasons/BRSeason2016.csv")

# 2016 Yellow Cards #
season2016['Yellow Cards'] = pd.to_numeric(season2016['Yellow Cards'], errors='coerce')
TotalYC2016 = season2016['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2016}")

# 2016 Red Cards & Total Cards #
season2016['Red Cards'] = pd.to_numeric(season2016['Red Cards'], errors='coerce')
TotalRC2016 = season2016['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2016}")
print(f"Total Cards: {TotalRC2016 + TotalYC2016}")

# Season 2017 #
print("                                 /Season 2017-18/")
print(season2017)
season2017 = pd.read_csv("Seasons/BRSeason2017.csv")

# 2017 Yellow Cards #
season2017['Yellow Cards'] = pd.to_numeric(season2017['Yellow Cards'], errors='coerce')
TotalYC2017 = season2017['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2017}")

# 2017 Red Cards & Total Cards #
season2017['Red Cards'] = pd.to_numeric(season2017['Red Cards'], errors='coerce')
TotalRC2017 = season2017['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2017}")
print(f"Total Cards: {TotalRC2017 + TotalYC2017}")

# Season 2018 #
print("                                 /Season 2018-19/")
print(season2018)
season2018 = pd.read_csv("Seasons/BRSeason2018.csv")

# 2018 Yellow Cards #
season2018['Yellow Cards'] = pd.to_numeric(season2018['Yellow Cards'], errors='coerce')
TotalYC2018 = season2018['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2018}")

# 2018 Red Cards & Total Cards #
season2018['Red Cards'] = pd.to_numeric(season2018['Red Cards'], errors='coerce')
TotalRC2018 = season2018['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2018}")
print(f"Total Cards: {TotalRC2018 + TotalYC2018}")


# Season 2019
print("                                 /Season 2019-20/")
print(season2019)
season2019 = pd.read_csv("Seasons/BRSeason2019.csv")

# 2019 Yellow Cards #
season2019['Yellow Cards'] = pd.to_numeric(season2019['Yellow Cards'], errors='coerce')
TotalYC2019 = season2019['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2019}")

# 2019 Red Cards & Total Cards #
season2019['Red Cards'] = pd.to_numeric(season2019['Red Cards'], errors='coerce')
TotalRC2019 = season2019['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2019}")
print(f"Total Cards: {TotalRC2019 + TotalYC2019}")


# Season 2020 #
print("                                 /Season 2020-21/")
print(season2020)
season2020 = pd.read_csv("Seasons/BRSeason2020.csv")

# 2020 Yellow Cards #
season2020['Yellow Cards'] = pd.to_numeric(season2020['Yellow Cards'], errors='coerce')
TotalYC2020 = season2020['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2020}")

# 2020 Red Cards & Total Cards #
season2020['Red Cards'] = pd.to_numeric(season2020['Red Cards'], errors='coerce')
TotalRC2020 = season2020['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2020}")
print(f"Total Cards: {TotalRC2020 + TotalYC2020}")

# Season 2021 #
print("                                 /Season 2021-22/")
print(season2021)
season2021 = pd.read_csv("Seasons/BRSeason2021.csv")

#  2021 Yellow Cards #
season2021['Yellow Cards'] = pd.to_numeric(season2021['Yellow Cards'], errors='coerce')
TotalYC2021 = season2021['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2021}")

# 2021 Red Cards & Total Cards #
season2021['Red Cards'] = pd.to_numeric(season2021['Red Cards'], errors='coerce')
TotalRC2021 = season2021['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2021}")
print(f"Total Cards: {TotalRC2021 + TotalYC2021}")

# Season 2022
print("                                 /Season 2022-23/")
print(season2022)
season2022 = pd.read_csv("Seasons/BRSeason2022.csv")

# 2022 Yellow Cards #
season2022['Yellow Cards'] = pd.to_numeric(season2022['Yellow Cards'], errors='coerce')
TotalYC2022 = season2022['Yellow Cards'].sum()
print(f"Total Yellow Cards: {TotalYC2022}")

# 2022 Red Cards & Total Cards #
season2022['Red Cards'] = pd.to_numeric(season2022['Red Cards'], errors='coerce')
TotalRC2022 = season2022['Red Cards'].sum()
print(f"Total Red Cards: {TotalRC2022}")
print(f"Total Cards: {TotalRC2022 + TotalYC2022}")

#----------------------------------------------------------------------------------------------------------------------#
import matplotlib.pyplot as plt

cards = [
    TotalYC2007 + TotalRC2007,
    TotalYC2008 + TotalRC2008,
    TotalYC2009 + TotalRC2009,
    TotalYC2010 + TotalRC2010,
    TotalYC2011 + TotalRC2011,
    TotalYC2012 + TotalRC2012,
    TotalYC2013 + TotalRC2013,
    TotalYC2014 + TotalRC2014,
    TotalYC2015 + TotalRC2015,
    TotalYC2016 + TotalRC2016,
    TotalYC2017 + TotalRC2017,
    TotalYC2018 + TotalRC2018,
    TotalYC2019 + TotalRC2019,
    TotalYC2020 + TotalRC2020,
    TotalYC2021 + TotalRC2021,
    TotalYC2022 + TotalRC2022
]
season = [
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022"
]
plt.plot(season, cards)
plt.xlabel("Season")
plt.ylabel("Total Cards")
plt.title("Total Cards per Season // All data by TransferMarkt")
plt.show()
