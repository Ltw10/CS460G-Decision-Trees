import pandas as pd

# Discretizes data into k buckets and saves the discretized data as a seperate file
def discretize(file_name, column_names, ks):
    if file_name == "pokemon-data-clean.csv":
        df = pd.read_csv(file_name)
    else:
        df = pd.read_csv(file_name, names=["A", "B", "Label"])
    for index in range(len(column_names)):
        max = df[column_names[index]].max()
        min = df[column_names[index]].min()
        data_diff = max - min
        bucket_size = data_diff / ks[index]
        buckets = []
        for i in range(1, ks[index]+1):
            buckets.append(min + (bucket_size * i))
        buckets[len(buckets) - 1] = max
        for i in range(len(df.index)):
            for bucket_index in range(len(buckets)):
                if df.at[i, column_names[index]] <= buckets[bucket_index]:
                    df.at[i, column_names[index]] = bucket_index
                    break
    new_file_name = "discretized-" + file_name
    df.to_csv(new_file_name, index=False)