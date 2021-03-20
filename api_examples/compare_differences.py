import wapi
import pandas as pd
from matplotlib import pyplot as plt

# authentification
session = wapi.Session(client_id='9-k2UK_O.nj6dzxl1gpSfhwJUbxI7mv8', client_secret='eSv3Xk3W-M.A.NrP.i1onr0k-Pf5UMhNxm4.CU7aOFPVUSZI0IYeLF4dpBl5_-HUr7Sws.iUSwHf7bcSxUOfPCm032W_Q8PwZRPQ')

# set the dates
start_date = pd.Timestamp.now().floor('D')

############################

### Get daily average price
curve = session.get_curve(name='pri de spot €/mwh cet min15 a') # which curve to get
ts = curve.get_data(data_from=start_date) # date of the curve
da_price = ts.to_pandas() # convert TS object to pandas.Series object (for plotting)

### Get predicted price
curve = session.get_curve(name='pri de spot ec00 €/mwh cet h f')
ts = curve.get_latest()
#ts = curve.get_instance(issue_date=yesterday)
predicted_da_price = ts.to_pandas() 


### WIND 
# PREDICRION
curve = session.get_curve(name='pro de wnd ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=start_date)
wind_pred = ts.to_pandas()
# ACTUAL
curve = session.get_curve(name='pro de wnd mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date)
wind_actual = ts.to_pandas() 

### SOLAR
# PREDICITION
curve = session.get_curve(name='pro de spv ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=start_date)
solar_pred = ts.to_pandas()
# ACTUAL
curve = session.get_curve(name='pro de spv mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date)
solar_actual = ts.to_pandas()
print(wind_actual)

combined_renewables = wind_actual + solar_actual
predicted_renewables = wind_pred[0:96] + solar_pred[0:96]


### PLOTTING
fig, ax = plt.subplots(2,1)

ax[0].plot(combined_renewables, label="actual renewable energy")
ax[0].plot(predicted_renewables, label="predicted renewable energy")
ax[0].legend(loc='upper right')
ax[0].set_ylabel("MWH")

ax[1].plot(da_price, label="actual price")
#ax[1].plot(predicted_da_price, label="predicted price")
ax[1].legend(loc='upper right')
ax[1].set_ylabel("€/MWH")

plt.show()