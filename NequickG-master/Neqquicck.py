from NequickG import GalileoBroadcast, NEQTime, NequickG, NequickG_parameters, Position
from aux import *  # Importing necessary modules (adjust as needed)
import CCIR_MoDIP.ccir_fm3
import CCIR_MoDIP.ccir_f2
import CCIR_MoDIP.modip
import numpy as np

# Define example values for latitude, longitude, month, universal time, and broadcast parameters
latitude_value = 18.0
longitude_value = 73.0
month_value = 7
universal_time_value = 14  # Example value for universal time
"""ai0_value = 0.123
ai1_value = 0.456
ai2_value = 0"""

# Define the parameters for NequickG_parameters, NEQTime, and Position
position = Position(latitude_value, longitude_value)
time = NEQTime(month_value, universal_time_value)
broadcast = GalileoBroadcast(236.831,0,0)

# Create NequickG_parameters instance
params = NequickG_parameters(position, broadcast, time)

# Create NequickG instance
nequick = NequickG(params)

# Calculate TEC
vtec_ratio = nequick.vTEC_ratio()
print("Vertical TEC Ratio:", vtec_ratio)
