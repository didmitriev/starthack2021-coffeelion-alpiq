import wapi
import pandas

from matplotlib import pyplot as plt
session = wapi.Session(client_id='9-k2UK_O.nj6dzxl1gpSfhwJUbxI7mv8',
client_secret='eSv3Xk3W-M.A.NrP.i1onr0k-Pf5UMhNxm4.CU7aOFPVUSZI0IYeLF4dpBl5_-HUr7Sws.iUSwHf7bcSxUOfPCm032W_Q8PwZRPQ')
## TIME_SERIES curve
curve = session.get_curve(name='tt de con °c cet min15 s')
ts = curve.get_data(data_from="2018-06-01", data_to="2018-06-08")
pds = ts.to_pandas() # convert TS object to pandas.Series object
print(pds.shape)
plt.plot(pds)
plt.show()
