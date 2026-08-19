import matplotlib.pyplot as plt
from utils import lowest_variance

def histogram():
    results = lowest_variance()
    subjects = [result[0] for result in results]
    variances = [result[1] for result in results]
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.barh(subjects, variances)
    ax.set_xlabel("Variance")
    ax.set_title("Two most homogeneous subjects")
    for bar, var in zip(bars, variances):
        ax.text(
            bar.get_width(),
            bar.get_y() + bar.get_height() / 2,
            f"  {var:.2f}",
            va="center"
        )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    plt.show()

histogram()