import wapi
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# authentification
session = wapi.Session(client_id='9-k2UK_O.nj6dzxl1gpSfhwJUbxI7mv8', client_secret='eSv3Xk3W-M.A.NrP.i1onr0k-Pf5UMhNxm4.CU7aOFPVUSZI0IYeLF4dpBl5_-HUr7Sws.iUSwHf7bcSxUOfPCm032W_Q8PwZRPQ')

# set the date to start from 0:00 this day
#start_date = pd.Timestamp.now().floor('D')
start_date = pd.Timestamp(year=2021, month=3, day=1, hour=0, minute=00, tz='CET')
end_date = pd.Timestamp(year=2021, month=3, day=11, hour=0, minute=00, tz='CET')

############################

# create a dataframe for all variables
df = pd.DataFrame(columns = ["wind_pred", "wind_actual", "solar_pred", "solar_actual", "price_intraday"])

### WIND 
# PREDICRION
curve = session.get_curve(name='pro de wnd ec00 mwh/h cet min15 f')
ts = curve.search_instances(issue_date_from=start_date, issue_date_to=end_date, with_data=True)
wind_pred = ts[0].to_pandas()
print(wind_pred.shape)
df["wind_pred"] = wind_pred


# ACTUAL
curve = session.get_curve(name='pro de wnd mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
wind_actual = ts.to_pandas() 
print(wind_actual.shape)
df["wind_actual"] = wind_actual

### SOLAR
# PREDICITION
curve = session.get_curve(name='pro de spv ec00 mwh/h cet min15 f')
ts = curve.search_instances(issue_date_from=start_date, issue_date_to=end_date, with_data=True)
solar_pred = ts[0].to_pandas()
print(solar_pred.shape)
df["solar_pred"] = solar_pred

# ACTUAL
curve = session.get_curve(name='pro de spv mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
solar_actual = ts.to_pandas()
print(solar_actual.shape)
df["solar_actual"] = solar_actual

### Get intraday prices
curve = session.get_curve(name='pri de intraday vwap id1 €/mwh cet h a') # which curve to get
ts = curve.get_data(data_from=start_date, data_to=end_date) # date of the curve
intraday_price = ts.to_pandas() # convert TS object to pandas.Series object (for plotting)

print(intraday_price.shape)
df["price_intraday"] = intraday_price
upsampled = df["price_intraday"].resample('15min')
interpolated = upsampled.interpolate(method='linear')
df["price_intraday"] = interpolated
print(interpolated.shape)

print(df)
df.to_csv('data/volue_data.csv')  

"""
### PLOTTING
fig, ax = plt.subplots(2,1)

ax[0].plot(solar_actual, label="difference (produced - predicted)")
ax[0].legend(loc='lower left')
ax[0].axhline(0, color="black")
ax[0].set_ylabel("MWH")

ax[1].plot(intraday_price, label="intraday price")
ax[1].legend(loc='lower left')
ax[1].set_ylabel("€/MWH")
plt.show() """
