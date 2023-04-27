from decisiontrees import main
from discretizedata import discretize
from pokemondata import clean_pokemon_data

def synthetic_run():
    discretize("synthetic-1.csv", ["A","B"], [2,2])
    success = main("discretized-synthetic-1.csv")
    print("Success rate for synthetic-1.csv with k=[2, 2] bins for discretizing continuous data in columns: " + str(success * 100) + "%")
    discretize("synthetic-2.csv", ["A", "B"], [10, 7]) # 10, 7
    success = main("discretized-synthetic-2.csv")
    print("Success rate for synthetic-2.csv with k=[10, 7] bins for discretizing continuous data in columns: " + str(success * 100) + "%")
    discretize("synthetic-3.csv", ["A", "B"], [9, 9])
    success = main("discretized-synthetic-3.csv")
    print("Success rate for synthetic-3.csv with k=[9, 9] bins for discretizing continuous data in columns: " + str(success * 100) + "%")
    discretize("synthetic-4.csv", ["A", "B"], [9, 10])
    success = main("discretized-synthetic-4.csv")
    print("Success rate for synthetic-4.csv with k=[9, 10] bins for discretizing continuous data in columns: " + str(success * 100) + "%")


def pokemon_run():
    clean_pokemon_data()
    discretize("pokemon-data-clean.csv", ["Total","HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"], [2, 2, 2, 2, 2, 2, 2])
    success = main("discretized-pokemon-data-clean.csv")
    print("Success rate for pokemon data with k=[2] bins for discretizing continuous data in columns: " + str(success * 100) + "%")

synthetic_run()
pokemon_run()
