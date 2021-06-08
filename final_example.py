import pandas as pd
from matplotlib import pyplot as plt

# read data from file
def read_column_from_data(file_path, column_name, num_measurements = None):
  if num_measurements:
    data = pd.read_csv(file_path, nrows=num_measurements)
  else:
    data = pd.read_csv(file_path)
  column_data = data[column_name]
  return column_data

temperatures = read_column_from_data(file_path = 'temperatures.csv', column_name = 'Air temperature (degC)', num_measurements = 25)

# compute statistics
mean = temperatures.mean()

# plot results
plt.plot(temperatures, 'r-')
plt.axhline(y=mean, color='b', linestyle='--')
plt.savefig('25.png')
plt.clf()
