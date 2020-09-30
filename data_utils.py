#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
import glob

def load_all():
    '''
    This creates a list of dataframes that are equivalent to the JSONs created with jsons.py
    ''' 
    files = glob.glob('*.json')
    dfs = []
    for file in files:
        df = pd.read_json(file)
        dfs.append(df)

def field_filter(lower_field, upper_field, dataframes):
    '''
    Input numeric vales for the field values, and a list of pandas dataframes. 
    This filters out all data whose fields are not equal to or within the limits
    '''
    return_dfs = []
    for df in dataframes:
        field = df['field'][0]
        if lower_field <= field <= upper_field:
            return_dfs.append(df)
    return return_dfs

def energy_filter(lower_energy, upper_energy, dataframes):
    '''
    Input numeric vales for the field values, and a list of pandas dataframes.
    This filters out all data with recoil_energy values that are not equal to or within the limits
    '''
    return_dfs = []
    for df in dataframes:
        energies = df['recoil_energy']
        flag = True
        for e in energies:
            if lower_energy <= e <= upper_energy:
                pass
            else:
                flag = False
        if flag == True:
            return_dfs.append(df)
    return return_dfs

def interaction_type_filter(interaction, dataframes):
    '''
    Input a string for the interaction type, and a list of pandas dataframes.
    The function filters data based on interaction type.
    '''
    return_dfs = []
    for df in dataframes:
        if df['interaction_type'][0] == interaction:
            return_dfs.append(df)
    return return_dfs
