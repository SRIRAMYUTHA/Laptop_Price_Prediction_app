import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import os
import pickle
#import xgboost as xgb
#from xgboost.sklearn import XGBRegressor
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
#import matplotlib

#matplotlib.use(‘TkAgg’)


# absolute path to this file
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# # absolute path to this file's root directory
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# # absolute path of directory_of_interest
# dir_of_interest = os.path.join(PARENT_DIR, "resources")

# data_path = os.path.join(dir_of_interest, "data", "df.pkl")
# # ml_data = os.path.join(dir_of_interest, "data", "rf.pkl")
# model = os.path.join(dir_of_interest, "data", "model.pkl")

df = pickle.load(open('df.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Laptop Price Predictor')
df = pd.DataFrame(df)
# st.dataframe(df1)
cm = st.selectbox(' Select Laptop Screen cm',df['cm'].unique())
if cm == '29.46 ':
      cm_inp = 1
elif cm == '35.81 ':
      cm_inp = 2
elif cm == '38.1 ':
      cm_inp = 3
elif cm == '38.0 ':
      cm_inp = 4
elif cm == '88.9 ':
      cm_inp = 5
elif cm== '35.56 ':
      cm_inp=6
elif cm=='33.02 ':
      cm_inp=7
elif cm=='39.62 ':
      cm_inp=8
elif cm=='40.89 ':
      cm_inp=9
elif cm =='42.16 ':
      cm_inp=10
elif cm=='33.78 ':
      cm_inp=11
elif cm=='34.29 ':
      cm_inp=12
elif cm=='34.54 ':
      cm_inp=13
elif cm=='34.04 ':
      cm_inp=14
elif cm=='40.64 ':
      cm_inp=15
elif cm=='43.94 ':
      cm_inp=16
elif cm=='36.07 ':
      cm_inp=17
else: cm_inp=18
      

warranty =st.selectbox("Select the years of waranty:- ", df["Warranty"].unique())
if warranty == '0':
      w_inp = 1
elif warranty=='1':
      w_inp=2
elif warranty=='2':
      w_inp=3
else: w_inp=4
      

ram =st.selectbox("Select RAM Size:- ", df["RAM"].unique())
if ram=='4':
    r_inp=1
elif ram=='8':
      r_inp=2
elif ram=='12':
      r_inp=3
elif ram=='16':
      r_inp=4
else: r_inp=5
      

processor =st.selectbox("Select the Processor:- ", df["Processor"].unique())
if processor=='Intel_Celeron_Quad_Core':
      p_inp=1
elif processor=='Intel_Celeron_Dual_Core':
      p_inp=2
elif processor=='AMD_Dual_Core':
      p_inp=3
elif processor=='AMD_Athlon_Dual_Core':
      p_inp=4
elif processor=='Intel_Pentium_Silver':
      p_inp=5
elif processor=='Qualcomm_Snapdragon_7c_Gen_2':
      p_inp=6
elif processor=='Intel_Pentium_Quad_Core':
      p_inp=7
elif processor=='AMD_Ryzen_3_Dual_Core':
      p_inp=8
elif processor=='Intel_Core_i3':
      p_inp=9
elif processor=='AMD_Ryzen_5_Quad_Core':
      p_inp=10
elif processor=='AMD_Ryzen_3_Quad_Core':
      p_inp=11
elif processor=='Intel_OptaneIntel_Core_i3':
      p_inp=12
elif processor=='AMD_Ryzen_7_Quad_Core':
      p_inp=13
elif processor=='AMD_Ryzen_5_Dual_Core':
      p_inp=14
elif processor=='AMD_Ryzen_5_Hexa_Core':
      p_inp=15
elif processor=='Intel_Core_i5':
      p_inp=16
elif processor=='Intel_Evo_Core_i5':
      p_inp=17
elif processor=='AMD_Ryzen_3_Hexa_Core':
      p_inp=18
elif processor=='AMD_Ryzen_7_Octa_Core':
      p_inp=19
elif processor=='Apple_M1':
      p_inp=20
elif processor=='Intel_Core_i7':
      p_inp=21
elif processor=='Apple_M2':
      p_inp=22
elif processor=='AMD_Ryzen_9_Octa_Core':
      p_inp=23
elif processor=='Apple_M1_Pro':
      p_inp=24
elif processor=='Intel_Core_i9':
      p_inp=25
else: p_inp=26
      
      
storage =st.selectbox("Select the Storage:- ", df["Storage"].unique())
if storage=='256 GB HDD256 GB SSD':
      st_inp=1
elif storage=='128 GB SSD':
      st_inp=2
elif storage=='256 GB SSD':
      st_inp=3
elif storage=='1 TB HDD':
      st_inp=4
elif storage=='512 GB SSD':
      st_inp=5
elif storage=='1 TB HDD256 GB SSD':
      st_inp=6
elif storage=='128 GB SSD1 TB HDD128 GB SSD':
      st_inp=7
elif storage=='1 TB HDD512 GB SSD':
      st_inp=8
elif storage=='1 TB SSD':
      st_inp=9
else: st_inp=10
      

ram_type =st.selectbox("Select the RAM Type:- ", df["RAM_Type"].unique())
if ram_type=='LPDDR4':
      r_t_inp=1
elif ram_type=='DDR4DDR4':
      r_t_inp=2
elif ram_type=='DDR4DDR5DDR4':
      r_t_inp=3
elif ram_type=='DDR4':
      r_t_inp=4
elif ram_type=='LPDDR5':
      r_t_inp=5
elif ram_type=='DDR5':
      r_t_inp=6
elif ram_type=='Unified Memory':
      r_t_inp=7
else: r_t_inp=8
      
operating_system =st.selectbox("Select the Operating System:- ", df["os"].unique())
if operating_system=='Chrome Operating System':
      os_inp=1
elif operating_system=='DOS Operating System':
      os_inp=2
elif operating_system=='Windows 11 when availableAMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64 bit Windows 11 Operating System':
      os_inp=3
elif operating_system=='Windows 11 when availableAMD Ryzen 5 Hexa Core Processor8 GB DDR4 RAM64 bit Windows 10 Operating System':
      os_inp=4
elif operating_system=='Windows 10 Operating System':
      os_inp=5
elif operating_system=='Windows 11 Operating System':
      os_inp=6
elif operating_system=='Windows 10 Operating SystemWindows 10 Operating System':
      os_inp=5
elif operating_system=='Mac OS Operating System':
      os_inp=7



butt = st.button("Predict")



query = np.array([[cm_inp,w_inp, r_inp, p_inp, st_inp, r_t_inp,os_inp]])
query = query.reshape(1, 7)
p = model.predict(query)[0]
# result = np.exp(p)
st.subheader("Your Predicted Prize is: ")
st.subheader("₹{}".format(p.round(2)))

