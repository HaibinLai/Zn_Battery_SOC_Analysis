# APAC

import NewareNDA

df = NewareNDA.read('LHB.ndax')
print(df)

# save df into csv:
import numpy as np

# Open the file in append mode
with open("output.csv", "a") as csv_file:
    # Create a NumPy array with the new data
    new_data = np.array(df)
    # Append the data to the file
    np.savetxt(csv_file, new_data, delimiter=",", fmt="%s")
