import numpy as np

percentage=np.array([69,71,73,68,74])

n=len(percentage)

fav_outcome=np.count_nonzero(percentage>70)

probability=fav_outcome/n

print(probability)