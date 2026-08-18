import matplotlib.pyplot as plt
from process_data import data
from utils import lowest_variance
 
def histogram():
	subject, var = lowest_variance()
	plt.bar(subject, var, color="red")
	plt.ylabel("Variance")
	plt.title("Lowest variance")
	plt.show()
	
histogram()