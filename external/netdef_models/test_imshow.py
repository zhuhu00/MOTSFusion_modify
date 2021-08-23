'''
Description test to load the float3 data and show
LastEditTime 2021-08-20 19:22:07
'''
from netdef_slim.utils.io import read 
occ_file = '000000.png.disp.L.float3'
occ_data = read(occ_file) # returns a numpy array

# to visualize
import matplotlib.pyplot as plt
plt.imshow(occ_data[:,:,0])
plt.show()