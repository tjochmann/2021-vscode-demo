# %% Import

import pandas as pd


# %% Generate some dummy data

df_qsm = pd.DataFrame({"rois": ['gm', 'wm', 'csf'], "chi":[3.2, 2.7, 7.1]})
df_dq = pd.DataFrame({"rois": ['gm', 'wm', 'csf'], "chi":[3.1, 2.2, 5.2]})


# %% Show data

df_dq


# %% Export data

df_qsm.to_excel("qsm.xls")
df_qsm.to_csv("qsm.csv")

df_dq.to_excel("dq.xls")
df_dq.to_csv("dq.csv")
