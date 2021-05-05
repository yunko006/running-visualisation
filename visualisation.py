from plotly.graph_objs import Bar, Layout
# import plotly.graph_objects as go
from plotly import offline
from json_parser import main
from collections import Counter


def graph_distance(km):
    """
    Graph qui montre : la distance parcouru de chaque jour
    """
    x_values = list(range(1, len(km) + 1))
    data = [Bar(x=x_values, y=km)]

    x_axis_config = {'title': 'Jour'}
    y_axis_config = {'title': 'Km'}
    my_layout = Layout(title='Mes kms parcourus',
                       xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': my_layout}, filename='distance.html')


def course_par_distance(km):
    """
    Graph qui montre : le nombre de fois que j'ai couru une certaines distances
    """
    # permet de créer un dictionnaire pour chaque valeur et de compter leur occurence

    round_km = [round(k) for k in km]
    x_values = list(set(round_km))  # les différentes distances
    count = Counter(round_km)  # le nombre de fois que j'ai couru ces distances
    y_values = list(count.values())

    data = [Bar(x=x_values, y=y_values)]

    x_axis_config = {'title': 'distance (en km)'}
    y_axis_config = {'title': 'count'}

    my_layout = Layout(title="nombres de fois que j'ai parcouru X km",
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout},
                 filename='nb_de_fois_par_distance.html')


def graph_km_accumuler(semaine, km_accumuler):
    """
    graph qui montre les kms accumulés depuis le début
    TODO : penser ou années
    """

    x_values = sorted(list(set(semaine)))  # les semaines
    # associer les valeurs de km en fonction de leurs semaines
    y_values = km_accumuler

    data = [Bar(x=x_values, y=y_values)]

    x_axis_config = {'title': 'Semaines'}
    y_axis_config = {'title': 'km accumulé'}

    my_layout = Layout(title="kilometres accumulé en fonction des semaines",
                       xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout},
                 filename='km_accumule.html')


def grah_km_by_week(semaine, link_km_weeks):
    semaine_demander = str(input("Semaine: "))

    # jour de la semaine (un peu caca pour le moment)
    x_values = list(range(1, len(link_km_weeks[semaine_demander]) + 1))
    # montrer les kms en fonction de la semaine souhaité par l'urtilisateur
    y_values = link_km_weeks[semaine_demander]

    data = [Bar(x=x_values, y=y_values)]

    x_axis_config = {'title': 'Jours'}
    y_axis_config = {'title': 'Kms parcourus'}

    my_layout = Layout(
        title=f"Kms parcouru lors de la semaine {semaine_demander}", xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='test4.html')


if __name__ == '__main__':
    km, semaine, date, duree, link_km_weeks, km_accumuler = main()
    graph_distance(km)
    course_par_distance(km)
    graph_km_accumuler(semaine, km_accumuler)
    grah_km_by_week(semaine, link_km_weeks)
