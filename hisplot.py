import pandas
from collections import Counter

def plot_histogram(res):
    state_counts = Counter(res)
    df = pandas.DataFrame.from_dict(state_counts, orient = 'index')
    df = df/df.sum()
    # df = pandas.DataFrame(state_counts,orient = 'index)
    # df.plot(kind='bar',legend=False, rot = 'horizontal', x='States', y = 'Probability')
    ax = df.plot.bar(legend=False, rot = 'horizontal')
    ax.set_xlabel("States")
    ax.set_ylabel("Probability")
    ax.set_title("Histogram")