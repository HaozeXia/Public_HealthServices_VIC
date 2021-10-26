import pandas as pd
from functools import reduce


# All functions are used to preprocessing the data.
# Extract the useful data from the csv downloaded from web scraping and sort it out.


# Labour( numbers of employment whose age >= 15 for each state)
# 2001-2019
def Labour():
    df = pd.read_csv('Before/x/labour.csv')
    Indicator = df['Indicator'].str.strip()  # remove whitespaces
    REG_ID = df['REG_ID']  # get region ID
    TIME = df['TIME']
    Value = df['Value']
    Region = df['Region']
    Gender = df['Gender']
    newdf = pd.DataFrame(
        {'Region': Region, 'Indicator': Indicator, 'REG_ID': REG_ID, 'TIME': TIME, 'Gender': Gender, 'Value': Value})

    # NSW
    newdf1 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU1" & Gender == "Total"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})

    # VIC
    newdf2 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU2" & Gender == "Total"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU3" & Gender == "Total"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU4" & Gender == "Total"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU5" & Gender == "Total"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU6" & Gender == "Total"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU7" & Gender == "Total"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT
    newdf8 = newdf.query('Indicator == "Employment (15 years old and over)" & REG_ID == "AU8" & Gender == "Total"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    labour = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    labour.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']  # combined all dataframe
    labour.to_csv("After/labour.csv")  # save as csv file
    return


# GVA (gross value added for each state)
# 2004-2017
def GVA():
    newdf = pd.read_csv('Before/x/GVA in industry, including energy (ISIC rev4).csv')  # read raw data

    # NSW
    newdf1 = newdf.query('REG_ID == "AU1"')  # find region ID 1's data
    newdf1 = newdf1.sort_values(by=['TIME'])  # sorted by time
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})  # save as DataFrame

    # VIC
    newdf2 = newdf.query('REG_ID == "AU2"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('REG_ID == "AU3"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('REG_ID == "AU4"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('REG_ID == "AU5"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('REG_ID == "AU6"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('REG_ID == "AU7"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT Canberra
    newdf8 = newdf.query('REG_ID == "AU8"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    GVA = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    # combined all Dataframe
    GVA.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'Canberra(ACT)']
    GVA.to_csv("After/GVA.csv")
    return


# Unemployment Rate (% unemployed over labour force 15-64)
# 2001-2020
def Unemployment():
    newdf = pd.read_csv('Before/x/Unemployment Rate (% unemployed over labour force 15-64).csv')  # read csv

    # NSW
    newdf1 = newdf.query('REG_ID == "AU1" & Gender == "Total"')  # region ID 1 and sum up gender
    newdf1 = newdf1.sort_values(by=['TIME'])  # sort order by time
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})

    # VIC
    newdf2 = newdf.query('REG_ID == "AU2" & Gender == "Total"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('REG_ID == "AU3" & Gender == "Total"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('REG_ID == "AU4" & Gender == "Total"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('REG_ID == "AU5" & Gender == "Total"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('REG_ID == "AU6" & Gender == "Total"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('REG_ID == "AU7" & Gender == "Total"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT Canberra
    newdf8 = newdf.query('REG_ID == "AU8" & Gender == "Total"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    # combined all dataframe
    Unemployment = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    Unemployment.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']
    Unemployment.to_csv("After/Unemployment.csv")  # save as csv file
    return


# Life Expectancy at Birth
# 2001-2019
def Life():
    df = pd.read_csv('Before/x/life expectancy and mortality.csv')  # read csv

    # NSW
    newdf1 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU1" & Gender == "Total"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])

    # VIC
    newdf2 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU2" & Gender == "Total"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])

    # QLD
    newdf3 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU3" & Gender == "Total"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])

    # SA
    newdf4 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU4" & Gender == "Total"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])

    # WA
    newdf5 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU5" & Gender == "Total"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])

    # TAS
    newdf6 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU6" & Gender == "Total"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])

    # NT
    newdf7 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU7" & Gender == "Total"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])

    # ACT
    newdf8 = df.query('Indicator == "      Life Expectancy at Birth"& REG_ID == "AU8" & Gender == "Total"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])

    # combined all dataframe to 1
    Life = pd.DataFrame(
        {'YEAR': YEAR, 'NSW': NSW, 'VIC': VIC, 'QLD': QLD, 'SA': SA, 'WA': WA, 'TAS': TAS, 'NT': NT, 'ACT': ACT})
    Life.to_csv('After/Life expectancy.csv')
    return


# Population of each state
# 2001-2019
def Population():
    newdf = pd.read_csv('Before/x/REGION_DEMOGR_09102021070529748.csv')  # read csv

    # NSW
    newdf1 = newdf.query('REG_ID == "AU1" & Gender == "Total"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})

    # VIC
    newdf2 = newdf.query('REG_ID == "AU2" & Gender == "Total"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('REG_ID == "AU3" & Gender == "Total"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('REG_ID == "AU4" & Gender == "Total"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('REG_ID == "AU5" & Gender == "Total"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('REG_ID == "AU6" & Gender == "Total"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('REG_ID == "AU7" & Gender == "Total"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT Canberra
    newdf8 = newdf.query('REG_ID == "AU8" & Gender == "Total"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    population = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    population.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'Canberra(ACT)']
    population.to_csv("After/population.csv")
    return


# Population density (pop. per km2)
# 2001-2020
def Population_Density():
    newdf = pd.read_csv('Before/x/population density and area.csv')  # read csv

    # NSW
    newdf1 = newdf.query('REG_ID == "AU1" & Gender == "Total"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})

    # VIC
    newdf2 = newdf.query('REG_ID == "AU2" & Gender == "Total"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('REG_ID == "AU3" & Gender == "Total"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('REG_ID == "AU4" & Gender == "Total"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('REG_ID == "AU5" & Gender == "Total"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('REG_ID == "AU6" & Gender == "Total"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('REG_ID == "AU7" & Gender == "Total"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT Canberra
    newdf8 = newdf.query('REG_ID == "AU8" & Gender == "Total"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    population = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    population.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'Canberra(ACT)']
    population.to_csv("After/population_density.csv")
    return


# Disposable Household Income
# 2000-2019
def income():
    df = pd.read_csv('Before/x/regional income per capita.csv')

    Indicator = df['Indicator'].str.strip()
    REG_ID = df['REG_ID']
    TIME = df['TIME']
    Value = df['Value']
    Region = df['Region']
    newdf = pd.DataFrame({'Region': Region, 'Indicator': Indicator, 'REG_ID': REG_ID, 'TIME': TIME, 'Value': Value})

    # NSW
    newdf1 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU1"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])
    NSW = pd.DataFrame({'YEAR': YEAR, 'NSW': NSW})
    # print(NSW)

    # VIC
    newdf2 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU2"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])
    VIC_YEAR = list(newdf2['TIME'])
    VIC = pd.DataFrame({'YEAR': VIC_YEAR, 'ACT': VIC})

    # QLD
    newdf3 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU3"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])
    QLD_YEAR = list(newdf3['TIME'])
    QLD = pd.DataFrame({'YEAR': QLD_YEAR, 'ACT': QLD})

    # SA
    newdf4 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU4"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])
    SA_YEAR = list(newdf4['TIME'])
    SA = pd.DataFrame({'YEAR': SA_YEAR, 'ACT': SA})

    # WA
    newdf5 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU5"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])
    WA_YEAR = list(newdf5['TIME'])
    WA = pd.DataFrame({'YEAR': WA_YEAR, 'ACT': WA})

    # TAS
    newdf6 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU6"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])
    TAS_YEAR = list(newdf6['TIME'])
    TAS = pd.DataFrame({'YEAR': TAS_YEAR, 'ACT': TAS})

    # NT
    newdf7 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU7"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])
    NT_YEAR = list(newdf7['TIME'])
    NT = pd.DataFrame({'YEAR': NT_YEAR, 'NT': NT})

    # ACT
    newdf8 = newdf.query('Indicator == "Disposable Household Income" & REG_ID == "AU8"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])
    ACT_YEAR = list(newdf8['TIME'])
    ACT = pd.DataFrame({'YEAR': ACT_YEAR, 'ACT': ACT})

    income = reduce(lambda x, y: pd.merge(x, y, on='YEAR', how='outer'), [NSW, VIC, QLD, SA, WA, TAS, NT, ACT])
    income.columns = ['YEAR', 'NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']
    income.to_csv("After/income.csv")
    return


# Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)
# 2000-2019
def Air():
    df = pd.read_csv('Before/x/environment PM2.5 and co2.csv')

    # NSW
    newdf1 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU1"')
    newdf1 = newdf1.sort_values(by=['TIME'])
    YEAR = list(newdf1['TIME'])
    NSW = list(newdf1['Value'])

    # VIC
    newdf2 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU2"')
    newdf2 = newdf2.sort_values(by=['TIME'])
    VIC = list(newdf2['Value'])

    # QLD
    newdf3 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU3"')
    newdf3 = newdf3.sort_values(by=['TIME'])
    QLD = list(newdf3['Value'])

    # SA
    newdf4 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU4"')
    newdf4 = newdf4.sort_values(by=['TIME'])
    SA = list(newdf4['Value'])

    # WA
    newdf5 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU5"')
    newdf5 = newdf5.sort_values(by=['TIME'])
    WA = list(newdf5['Value'])

    # TAS
    newdf6 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU6"')
    newdf6 = newdf6.sort_values(by=['TIME'])
    TAS = list(newdf6['Value'])

    # NT
    newdf7 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU7"')
    newdf7 = newdf7.sort_values(by=['TIME'])
    NT = list(newdf7['Value'])

    # ACT
    newdf8 = df.query(
        'Indicator == "Air Pollution in PM2.5 (average level in µg/m³ experienced by the population)"& REG_ID == "AU8"')
    newdf8 = newdf8.sort_values(by=['TIME'])
    ACT = list(newdf8['Value'])

    air = pd.DataFrame(
        {'YEAR': YEAR, 'NSW': NSW, 'VIC': VIC, 'QLD': QLD, 'SA': SA, 'WA': WA, 'TAS': TAS, 'NT': NT, 'ACT': ACT})
    year = pd.DataFrame({'YEAR': list(range(2000, 2020))})  # add the missing year
    air = air.merge(year, how='outer', on='YEAR')  # merge dataframes
    air = air.sort_values(by=['YEAR'])  # sort by year
    air.reset_index(drop=True, inplace=True)  # reset the index
    air.to_csv('After/Air.csv')
    return

# Run functions
Labour()
GVA()
Unemployment()
Life()
Population()
Population_Density()
income()
Air()
