from decisiontrees import main
from discretizedata import discretize

def synthetic_test(name):
    max = 0
    a, b = 0, 0
    stop = False
    for i in range(1,26):
        for j in range(1,26):
            discretize(name, ["A","B"], [i,j])
            success = main("discretized-" + name)
            if success > max:
                max = success
                a = i
                b = j
            if max == 1:
                stop = True
                break
        if stop:
            break
    discretize(name, ["A","B"], [a,b])
    print("Success rate for " + name + " with k=[\"" + str(a) + "\", \"" + str(b) + "\"] bins for discretizing continuous data in columns: " + str(main("discretized-" + name)))