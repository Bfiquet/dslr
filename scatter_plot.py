from process_data import data
import matplotlib.pyplot as plt

def scatter_plot():
    n = len(data.subjects)
    k = 1
    plt.figure(figsize=(25, 15))
    for i in range(n):
        for j in range(i + 1, n):
            x = []
            y = []
            for student in data.Students:
                if (student[data.subjects[i]] is not None and
                    student[data.subjects[j]] is not None):
                    x.append(student[data.subjects[i]])
                    y.append(student[data.subjects[j]])
            plt.subplot(n - 1, n - 1, k)
            plt.scatter(x, y, s=5)
            plt.title(data.subjects[i] + " / " + data.subjects[j], fontsize=6)
            plt.xticks([])
            plt.yticks([])
            k += 1
    plt.tight_layout()
    plt.show()
    
scatter_plot()