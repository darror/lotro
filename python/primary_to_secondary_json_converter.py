# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:54:54 2022

@author: Pari
"""


import pandas as pd
import json
mapper = {
    'Physical Mastery Rating': "Physical Mastery",
    'Tactical Mastery Rating': "Tactical Mastery",
    'Critical Rating': "Critical Rating",
    'Block Rating': "Block",
    'Parry Rating': "Parry",
    'Evade Rating': "Evade",
    'Maximum Morale': "Morale",
    'Resistance Rating': "Resistance",
    'Finesse Rating': "Finesse",
}

df = pd.read_csv("../data/primary_to_secondary.csv").dropna(how="all", axis=0)
processed = df.ffill().set_index(["1 point in", "grants X points in"])
intermediate_dict = processed.to_dict()
final_dict = {}
for k, d in intermediate_dict.items():
    final_dict[k] = {}
    for (primary_stat, secondary_stat), value in d.items():
        stat_name = mapper.get(secondary_stat, secondary_stat)
        final_dict[k].setdefault(primary_stat, {})[stat_name] = value



with open("../data/primary_to_secondary.json", "w") as f:
    json.dump(final_dict, f, indent=2)

