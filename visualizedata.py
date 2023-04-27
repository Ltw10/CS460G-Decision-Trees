import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from decisiontrees import create_tree, traverse_tree_prediction

def create_tree_img(name):
    df = pd.read_csv(name, names = ["A", "B", "Label"])
    dfdiscrete = pd.read_csv("discretized-" + name)
    root = create_tree(dfdiscrete, 0)

    xx, yy = np.meshgrid(np.unique(dfdiscrete["A"]), np.unique(dfdiscrete["B"]))
    predictions = np.zeros(xx.shape)

    for i in range(xx.shape[0]):
        for j in range(xx.shape[1]):
            predictions[i, j] = traverse_tree_prediction(pd.Series({"A": xx[i, j], "B": yy[i, j]}), root)

    levels = np.linspace(np.min(predictions), np.max(predictions), 3)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.contourf(xx, yy, predictions, levels=levels, cmap=plt.cm.RdBu)
    ax2.scatter(df["A"], df["B"], c=df["Label"], cmap=plt.cm.RdBu, edgecolors="k")
    plt.xlabel("A")
    plt.ylabel("B")
    plt.title(name)
    plt.show()
    
    

create_tree_img("synthetic-1.csv")
create_tree_img("synthetic-2.csv")
create_tree_img("synthetic-3.csv")
create_tree_img("synthetic-4.csv")

