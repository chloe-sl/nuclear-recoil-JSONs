#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json
import numpy as np
import pandas as pd
import itertools
import math
import string
import re

non_decimal = re.compile(r'[^\d.]+')


# In[16]:


def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# In[17]:


def csv_to_json(filename, yield_type):
    '''
    filename should be in the format 'placeholder.csv'
    yield_type should be 'charge' or 'light'
    This function automatically reads all datasets in the CSV and turns them into JSONs, then saves
    them as JSON files.
    
    Please check the README for proper units for all measurements, and make sure your data is formatted
    correctly before loading it!
    
    If your data's interaction type is anything other than NR, you can edit the 'interaction_type' variable
    to reflect the correct interaction type.
    '''

    all_data = pd.read_csv('placeholder.csv')
    all_data = all_data.set_index(['Field'])
    all_fields = all_data.index.values.tolist()
    all_fields = list(dict.fromkeys(all_fields))
    for field in all_fields:
        field_data = all_data.loc[field]
        name= str(field_data['Name'].tolist()[0])
    
        gdf = non_decimal.sub('',str((field_data['GasF [V/cm]']).tolist()[0]))
        if is_num(gdf) == True:
            gdf = float(gdf)
        ldf = non_decimal.sub('',str((field_data['LiqF [V/cm]'].tolist()[0])))
        if is_num(ldf) == True:
            ldf = float(ldf)
    
        if yield_type == 'charge':
            variables = {'name': name,
                         'identification': field_data['Name'].tolist()[1],
                         'interaction_type': 'NR',
                         'field': field,
                         'yield_type': 'charge',
                         'drift_field_error': field_data['df +/- [V/cm]'].tolist()[0],
                 
                         'gas_drift_field': gdf,
                         'liquid_drift_field': ldf,
                         'extraction_efficiency': non_decimal.sub('',str((field_data['Extr Assumed'].tolist()[0]))),
                         'pixey': non_decimal.sub('',str(field_data['Extr PIXeY'].tolist()[0])),
                         'recoil_energy': field_data['keVr'].tolist(),
                         'yield': field_data['Q_y (e-/keVr)'].tolist(),
                         'recoil_error': field_data['error'].tolist(),
                         'corrected_energy': field_data['EnergyCorr'].tolist()}
        
            
        elif yield_type == 'light':
            variables = {'name': name,
                         'identification': field_data['Name'].tolist()[1],
                         'interaction_type': 'NR',
                         'field': field,
                         'yield_type': 'light',
                         'drift_field_error': field_data['df +/- [V/cm]'].tolist()[0],
                         'recoil_energy': field_data['keVr'].tolist(),
                         'yield': field_data['Ly (ph/keVr)'].tolist(),
                         'recoil_error': field_data['error'].tolist(),
                         'corrected_energy': field_data['EnergyCorr'].tolist()}
        
        for val in field_data['Y+'].tolist():
            if math.isnan(val) != True:
                variables['max_recoil']= field_data['Y+'].tolist()
                variables['min_recoil']= field_data['Y-'].tolist()
        for val in field_data['x+'].tolist():
            if math.isnan(val) != True:
                variables['max_yield']= field_data['x+'].tolist()
                variables['min_yield']= field_data['x-'].tolist()
    
        newname = name.lower()
        newname = newname.replace(' ', '_')
        if yield_type == 'charge':
            filename = [newname, field, 'qy.json']
        elif yield_type == 'light':
            filename = [newname, field, 'ly.json']
        filename = '_'.join(str(v) for v in filename)    
    
        with open(filename, 'w') as z:
            json.dump(variables, z, indent=4)


# In[ ]:




