# APAC
import NewareNDA
import numpy as np

df = NewareNDA.read('SDM`101_127.0.0.1-BTS83-46-7-5-655.ndax')
print(df)

# save df into csv:

# Open the file in append mode
with open("SingleCell.csv", "a") as csv_file:
    # Create a NumPy array with the new data
    new_data = np.array(df)
    # Append the data to the file
    np.savetxt(csv_file, new_data, delimiter=",", fmt="%s")
