import math
import pandas as pd

# Node class is used to create the decision tree
class Node:
    # Each node may contain a feature to split on, children to navigate to, or a prediction value (for leaves)
    def __init__(self, feature=None, children=None, prediction=None):
        self.feature = feature
        self.children = children
        self.prediction = prediction

    # print function for tree - does not print cleanly
    def __str__(self) -> str:
        print = ""
        if (self.feature != None):
            print += "Feature: " + str(self.feature) + "\n"
        if (self.children != None):
            print += "Children:" + "\n"
            for child in self.children:
                print += "\t" + "Feature Value: " + str(child) + "\n\t" + str(self.children[child])
        if (self.prediction != None):
            print += "Prediction: " + str(self.prediction) + "\n"
        return print

# This function returns a map where the keys are all of the possible values in a column of data and
# the values are the frequency of those keys. Column value map is used in many places when creating the tree
def create_col_val_map(col):
    map = {}
    for val in col:
        if val in map:
            map[val] += 1
        else:
            map[val] = 1
    return map

# This function calculates the entropy of a column of data
def calculate_entropy(col):
    map = create_col_val_map(col)
    entropy = 0
    for label in map:
        ratio = map[label]/len(col)
        entropy -= ratio * math.log2(ratio)
    return entropy

# This function calculates the information gain of all columns in a dataframe and returns
# a map where the keys are the column names and the values are their information gain
def calculate_information_gain(df):
    information_gain_map = {}
    parentEntropy = calculate_entropy(df["Label"])
    for columnName, columnValue in df.items():
        childrenEntropy = 0
        if columnName != "Label":
            map = create_col_val_map(columnValue)
            for val in map:
                grouped_df = df.groupby(columnName)
                df_partitioned = grouped_df.get_group(val)
                childrenEntropy -= map[val]/len(df.index) * calculate_entropy(df_partitioned["Label"])
            information_gain_map[columnName] = parentEntropy + childrenEntropy
    return information_gain_map

# This recursive function is similar to the ID3 tree algorithm. It uses information gain to decide which features
# to partition the data on and keeps track of the tree using the node class above. The root of the tree is returned
def create_tree(df, depth):    
    if (calculate_entropy(df["Label"].tolist()) == 0):
        return Node(None, None, df["Label"].tolist()[0])
    # If tree is at depth 3 the most common class label is chosen as that leaves prediction value
    if (len(df.columns) == 1 or depth == 3):
        for columnName, columnValue in df.items():
            map = create_col_val_map(columnValue)
        return Node(None, None, max(map, key=map.get))
    information_gain = calculate_information_gain(df)
    root = Node(max(information_gain, key=information_gain.get), {})
    depth += 1
    feature_vals = create_col_val_map(df[root.feature])
    for value in feature_vals:
        grouped_df = df.groupby(root.feature)
        partitioned_df = grouped_df.get_group(value).drop(root.feature, axis=1)
        new_node = create_tree(partitioned_df, depth)
        root.children[value] = new_node

    return root

# This function traverses the tree (node) for a given dataframe row of data and returns a 1 if 
# the tree predicted correctly, and a 0 if not
def traverse_tree(row, node):
    if (node.prediction != None):
        if (row["Label"] == node.prediction):
            return 1
        else:
            return 0
    else:
        return traverse_tree(row, node.children[row[node.feature]])

# This function returns the class label value predicted from the decision tree (node) for a given dataframe row 
def traverse_tree_prediction(row, node):
    if (node.prediction != None):
        return node.prediction
    else:
        if row[node.feature] in node.children:
            return traverse_tree_prediction(row, node.children[row[node.feature]])
        else:
            return 0

        
# Main function reads in the data, creates the tree, and traverses the tree for all of the data
# to calculate the success rate
def main(name):
    df = pd.read_csv(name)
    tree = create_tree(df, 0)
    # print(tree)
    correct, incorrect = 0, 0
    for index, row in df.iterrows():
        if (traverse_tree(row,tree)):
            correct += 1
        else:
            incorrect += 1
    success = correct/(correct + incorrect)
    return(success)


