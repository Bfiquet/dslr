from process_data import data
import matplotlib.pyplot as plt

def pair_plot():
    subjects = data.subjects
    n = len(subjects)
    fig, axes = plt.subplots(
        n,
        n,
        figsize=(15, 15)
    )
    houses = [
        (data.Gryffindor, "red"),
        (data.Slytherin, "green"),
        (data.Ravenclaw, "blue"),
        (data.Hufflepuff, "orange")
    ]
    values = {}
    for students, color in houses:
        points = []
        for student in students:
            row = []
            for subject in subjects:
                row.append(student[subject])
            points.append(row)
        values[color] = points
    for i in range(n):
        for j in range(n):
            ax = axes[i][j]
            if i != j:
                for color, points in values.items():
                    x = []
                    y = []
                    for student in points:
                        if (
                            student[j] is not None
                            and student[i] is not None
                        ):
                            x.append(student[j])
                            y.append(student[i])
                    ax.scatter(
                        x,
                        y,
                        c=color,
                        s=5,
                        alpha=0.5
                    )
            if i == j:
                ax.axis("off")
            ax.tick_params(
                labelsize=5
            )
            if i == n-1:
                ax.set_xlabel(subjects[j], fontsize=7)
            if j == 0:
                ax.set_ylabel(subjects[i], fontsize=7)
    plt.tight_layout()
    plt.show()
    
pair_plot()