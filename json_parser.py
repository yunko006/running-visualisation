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
                # pour le moment je round les donnes a l'entier pour simplifier les choses
                km.append(round(distance, 2))
                duree.append(duration_convertit)
                date.append(converted_time)
                semaine.append(weeks)
                read_file.close()

    acc = accumulate_km(semaine, km)
    return km, semaine, date, duree, acc


if __name__ == '__main__':
    main()
