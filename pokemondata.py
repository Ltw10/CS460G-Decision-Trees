import pandas as pd

def clean_pokemon_data():
    df = pd.read_csv("pokemonStats.csv")
    type = []
    special_columns = ["Type 1_Bug", "Type 1_Dark", "Type 1_Dragon", "Type 1_Electric", "Type 1_Fairy", "Type 1_Fighting", "Type 1_Fire", 
    "Type 1_Flying", "Type 1_Ghost", "Type 1_Grass", "Type 1_Ground", "Type 1_Ice", "Type 1_Normal", "Type 1_Poison", "Type 1_Psychic", 
    "Type 1_Rock", "Type 1_Steel", "Type 1_Water", "Type 2_Bug", "Type 2_Dark", "Type 2_Dragon", "Type 2_Electric", "Type 2_Fairy", 
    "Type 2_Fighting", "Type 2_Fire", "Type 2_Flying", "Type 2_Ghost", "Type 2_Grass", "Type 2_Ground", "Type 2_Ice", "Type 2_Normal", 
    "Type 2_Poison", "Type 2_Psychic", "Type 2_Rock", "Type 2_Steel", "Type 2_Water"]
    for i in range(len(df.index)):
        for column in special_columns:
            if (df.at[i, column] == 1):
                type.append(column)
                break
            if (column == "Type 2_Water"):
                type.append("No Type")
    df.drop(axis=1, inplace=True, columns=special_columns)
    df_label = pd.read_csv("pokemonLegendary.csv")
    df_label = df_label.rename(columns={"Legendary": "Label"})
    label = df_label["Label"]
    df["Type"] = type
    df["Label"] = label
    df.to_csv("pokemon-data-clean.csv", index=False)