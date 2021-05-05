import datetime
from collections import defaultdict


def duration_en_min(duration):
    # convertir la duration en nb decimal
    decimal = duration / 60
    # prendre que la virgule du float
    virgule = decimal % 1
    # partie pleine du chiffre
    plein = int(decimal // 1)
    # assemble les deux partie sous forme d'un str
    strr = f"{plein}.{int(virgule * 60)}"
    # convertit le str en float
    return float(strr)


def convert_time(date):
    """
    convertit le temps epoch en temps humain
    return a  list
    """
    time_list = []

    converted_time = datetime.datetime.fromtimestamp(date)
    conv_time_str = str(converted_time)
    time = conv_time_str.split()[0]

    time_list.append(int(time[0:4]))

    if time[5] == "0":
        time_list.append(int(time[6:7]))
    else:
        time_list.append(int(time[5:7]))

    if time[8] == "0":
        time_list.append(int(time[9:10]))
    else:
        time_list.append(int(time[8:10]))

    return time_list


def date_to_week(converted_time):
    """
    return a str
    """
    week = datetime.date(
        converted_time[0], converted_time[1], converted_time[2]).strftime("%V")
    return week


def link_km_and_semaine(semaine, km):
    """
    take two list and merge them with zip to iterate over and create a dictionnary
    take two list
    return a dict
    """
    zip_list = zip(semaine, km)
    link = defaultdict(list)

    for k, v in zip_list:
        link[k].append(v)

    return link


def accumulatedKm(defaultdict):
    """
    sum all the km in the database
    take a dictionnary
    return a list
    """
    accumule = 0
    acc_list = []
    for key in defaultdict:
        for i in defaultdict[key]:
            accumule += i
        acc_list.append(accumule)
    return acc_list


def duration_per_km(duration):
    """
    convertit le temps décimal en temps normal
    return a float
    """
    x = str(duration).split(".")
    dec = str(int(x[1]) * 60)
    # remplace la valeur de x[1]
    x[1] = dec[:2]
    # join les deux valeurs pour former le nouveau chiffre
    return float(".".join(x))
