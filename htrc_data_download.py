#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:19:56 2019

@author: kashish
"""
'''importing the library'''
import json

    # This code will execute when running `python -O script.py`
    # The -O argument turns on optimizations, setting __debug__ = False.
import htrc.volumes as volumes
'''loading volume id's in the form of list from json'''

with open('/home/dcuser/download_htrc/htrc/data.json') as f:
    data = json.load(f)
#convert all the volume id's into list

'''converting into list'''
volume_ids=list(data)
''' function for obtaining token'''
#tok=volumes.get_oauth2_token('kkothari442', 'K@shish99')
#print(token)

'''function for obtaining volume'''
#v=volumes.get_volumes(tok, [volume_ids[0]], concat=True)
#print(vol)
''' enter the name of directory to save downloaded volumes'''
output_directory=Input("please enter the name of your output directory")

if output_directory:
    volumes.download_volumes([volume_ids[0]],output_directory)

else:
    output_directory="downloaded volume"
    volumes.download_volumes([volume_ids[0]],output_directory)


print("%d of volumes download is completed", %(len(volume_ids)))
