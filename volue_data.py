import wapi
import pandas as pd
from matplotlib import pyplot as plt

# authentification
session = wapi.Session(client_id='9-k2UK_O.nj6dzxl1gpSfhwJUbxI7mv8', client_secret='eSv3Xk3W-M.A.NrP.i1onr0k-Pf5UMhNxm4.CU7aOFPVUSZI0IYeLF4dpBl5_-HUr7Sws.iUSwHf7bcSxUOfPCm032W_Q8PwZRPQ')

# set the dates
start_date = pd.Timestamp(year=2021, month=3, day=13)
end_date = pd.Timestamp(year=2021, month=3, day=14)
issue_date = pd.Timestamp(year=2021, month=3, day=13, hour=0, minute=00, tz='CET')


# create a dataframe for all variables
df = pd.DataFrame(columns = ["da_price", "vwap", "imbalance_price", "grid_imbalance", "nuclear_prod", "coal_prod", "lignite_prod", "gas_prod", "wind_pred", "wind_actual", "solar_pred", "solar_actual"])

### DA PRICE
curve = session.get_curve(name='pri de spot €/mwh cet min15 a') # which curve to get
ts = curve.get_data(data_from=start_date, data_to=end_date) # date of the curve
da_price = ts.to_pandas() # convert TS object to pandas.Series object (for plotting)
df["da_price"] = da_price # append to the dataframe


### INTRADAY VWAP
curve = session.get_curve(name='pri de intraday vwap €/mwh cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
vwap = ts.to_pandas()
df["vwap"] = vwap

### IMBALANCE PRICE
#curve = session.get_curve(name='pri de imb stlmt €/mwh cet min15 s')
#ts = curve.get_data(data_from=start_date, data_to=end_date)
#imbalance_price = ts.to_pandas()
#df["imbalance_price"] = imbalance_price

### GRID IMBALANCE
curve = session.get_curve(name='pri cwe imb stlmt igcc €/mwh cet min15 s')
ts = curve.get_data(data_from=start_date, data_to=end_date)
grid_imbalance = ts.to_pandas()
df["grid_imbalance"] = grid_imbalance


### NUCLEAR
curve = session.get_curve(name='pro de nuc mwh/h cet h af')
ts = curve.get_data(data_from=start_date, data_to=end_date)
nuclear_prod = ts.to_pandas()
df["nuclear_prod"] = nuclear_prod

### COAL
curve = session.get_curve(name='pro de thermal coal mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
coal_prod = ts.to_pandas()
df["coal_prod"] = coal_prod

### LIGNITE
curve = session.get_curve(name='pro de thermal lignite mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
lignite_prod = ts.to_pandas()
df["lignite_prod"] = lignite_prod

### GAS
curve = session.get_curve(name='pro de thermal gas mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
gas_prod = ts.to_pandas()
df["gas_prod"] = gas_prod

### WIND 
# PREDICRION
curve = session.get_curve(name='pro de wnd ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=issue_date)
wind_pred = ts.to_pandas()
df["wind_pred"] = wind_pred
# ACTUAL
curve = session.get_curve(name='pro de wnd mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
wind_actual = ts.to_pandas() 
df["wind_actual"] = wind_actual

### SOLAR
# PREDICITION
curve = session.get_curve(name='pro de spv ec00 mwh/h cet min15 f')
ts = curve.get_instance(issue_date=issue_date)
solar_pred = ts.to_pandas()
df["solar_pred"] = solar_pred
# ACTUAL
curve = session.get_curve(name='pro de spv mwh/h cet min15 a')
ts = curve.get_data(data_from=start_date, data_to=end_date)
solar_actual = ts.to_pandas()
df["solar_actual"] = solar_actual

print("Dataframe shape: ", df.shape)


### PLOTTING
fig, ax = plt.subplots(4,1)

ax[0].plot(da_price, label="average price")
ax[0].plot(vwap, label="intraday vwap")
#ax[0].plot(imbalance_price, label="imbalance_price")
ax[0].plot(grid_imbalance, label="grid imbalance")
ax[0].legend(loc='upper right')
ax[0].set_ylabel("€/MWH")

ax[1].plot(nuclear_prod, label="nuclear production")
ax[1].plot(coal_prod, label="coal production")
ax[1].plot(lignite_prod, label="lignite production")
ax[1].plot(gas_prod, label="gas production")
ax[1].legend(loc='upper right')
ax[0].set_ylabel("MWH")

ax[2].plot(wind_actual, label="wind actual")
ax[2].plot(wind_pred[0:96], label="wind predicted")
ax[2].legend(loc='upper right')
ax[0].set_ylabel("MWH")

ax[3].plot(solar_actual, label="solar actual")
ax[3].plot(solar_pred[0:96], label="solar predicted")
ax[3].legend(loc='upper right')
ax[0].set_ylabel("MWH")

plt.show()