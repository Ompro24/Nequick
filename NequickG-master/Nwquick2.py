# Import necessary modules (assuming they are imported correctly)
from NequickG import GalileoBroadcast, NEQTime, NequickG, NequickG_parameters, Position
from NequickG_global import NequickG_global
from aux import *
import CCIR_MoDIP.ccir_fm3
import CCIR_MoDIP.ccir_f2
import CCIR_MoDIP.modip
import numpy as np

# Defining the  example values for latitude, longitude, month, universal time, and broadcast parameters
latitude_value = 40 # 18.5541
longitude_value = 0 # 73.9063
month_value = 4 # 7
universal_time_value = 12 # 14.5  # Example value for universal time
ai0_value = 236.831 # 0.123
ai1_value = 0 #  0.456
ai2_value = 0 # 0.789


position = Position(latitude_value, longitude_value)# Define the parameter for Position
time = NEQTime(month_value, universal_time_value) # Define the parameters for NEQTime
broadcast = GalileoBroadcast(ai0_value, ai1_value, ai2_value) # Define the parameters for NequickG_parameters
nGlobal = NequickG_global(time, broadcast)
nLocal, para = nGlobal.get_Nequick_local(position)

params = NequickG_parameters(position, broadcast, time)# Create NequickG_parameters instance


nequick = NequickG(params)# Create NequickG instance

# Example integration endpoints
h1 = 100
h2 = 2000  # Adjust based on your specific needs

# Calculate TEC using the vTEC method from NequickG instance
vtec_value = nLocal.vTEC(h1, h2)
print("Vertical TEC:", vtec_value)

