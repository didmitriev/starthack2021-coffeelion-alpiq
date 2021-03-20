import wapi
import pandas as pd
from matplotlib import pyplot as plt

# authentification
session = wapi.Session(client_id='9-k2UK_O.nj6dzxl1gpSfhwJUbxI7mv8', client_secret='eSv3Xk3W-M.A.NrP.i1onr0k-Pf5UMhNxm4.CU7aOFPVUSZI0IYeLF4dpBl5_-HUr7Sws.iUSwHf7bcSxUOfPCm032W_Q8PwZRPQ')

# set the date to start from 0:00 this day
start_date = pd.Timestamp.now().floor('D')

############################

### Get intraday prices
curve = session.get_curve(name='pri de intraday vwap id1 €/mwh cet h a') # which curve to get
ts = curve.get_data(data_from=start_date) # date of the curve
intraday_price = ts.to_pandas()[0:24] # convert TS object to pandas.Series object (for plotting)

### Get day ago price
curve = session.get_curve(name='pri de spot €/mwh cet h a') # which curve to get
ts = curve.get_data(data_from=start_date) # date of the curve
da_price = ts.to_pandas()[0:24] # convert TS object to pandas.Series object (for plotting)


### WIND 
# PREDICRION
curve = session.get_curve(name='pro de wnd ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=start_date)
wind_pred = ts.to_pandas()[0:96]
# ACTUAL
curve = session.get_curve(name='pro de wnd mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date)
wind_actual = ts.to_pandas() 

### SOLAR
# PREDICITION
curve = session.get_curve(name='pro de spv ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=start_date)
solar_pred = ts.to_pandas()[0:96]
# ACTUAL
curve = session.get_curve(name='pro de spv mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date)
solar_actual = ts.to_pandas()
print(wind_actual)

combined_renewables = wind_actual + solar_actual
predicted_renewables = wind_pred + solar_pred


### PLOTTING
fig, ax = plt.subplots(2,1)

ax[0].plot(combined_renewables, label="actual renewable energy")
ax[0].plot(predicted_renewables, label="predicted renewable energy")
ax[0].legend(loc='lower right')
ax[0].set_ylabel("MWH")

ax[1].plot(intraday_price, label="intraday price")
ax[1].plot(da_price, label="day ago price")
ax[1].legend(loc='lower right')
ax[1].set_ylabel("€/MWH")

plt.show()