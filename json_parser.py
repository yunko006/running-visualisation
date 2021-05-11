import json
import pathlib
from utils import *


def main():
    km = []
    date = []
    duree = []
    semaine = []

    # ouvre tous les fichiers json dans le repertoire puis
    for path in pathlib.Path(r"C:\Users\Thomas\Downloads\export-20210406-000\Sport-sessions").iterdir():
        if path.is_file():
            with open(path, 'r') as read_file:
                data = json.load(read_file)
                distance = data["distance"] / 1000
                duration = data["duration"] / 60000
                duration_convertit = duration_en_min(duration)
                epoch_time = int(str(data["start_time"])[:-3])
                converted_time = convert_time(epoch_time)
                weeks = date_to_week(converted_time)
                # append les kms round a 2 digits tel que 4.56
                km.append(round(distance, 2))
                # append les durées en minutes tel que 30 mins = 0.30
                duree.append(duration_convertit)
                # append une valeur tel que Y-M-D
                date.append("-".join(str(i) for i in converted_time))
                # append les semaines en str tel que "13"
                semaine.append(weeks)
                # close the current file
                read_file.close()

    link_km_weeks = link_two_list(semaine, km)
    link_weeks_day = link_two_list(semaine, date)
    km_accumuler = accumulatedKm(link_km_weeks)
    # print(km_accumuler)
    return km, semaine, date, duree, link_km_weeks, link_weeks_day, km_accumuler


if __name__ == '__main__':
    main()
