# -*- coding: utf-8 -*-
"""

@author: Aniket
"""
## Function for Data Manipulation of Biopic Dataset

def process_data():
    import pandas as pd
    biopics = pd.read_csv("biopics.csv", encoding = 'latin-1')
    # Filter out duplicated rows
    biopics.drop_duplicates(inplace=True)
    # Rename column
    biopics.rename(columns={"box_office": "earnings"},inplace = True)
    # Filter out missing values
    biopics.dropna(inplace=True)
    # Keep movies after 1990
    biopics = biopics[biopics['year_release'] >= 1990]
    # Convert columns to categorical
    biopics['type_of_subject'] = biopics['type_of_subject'].astype('category')
    biopics['country'] = biopics['country'].astype('category')
    # Create new variable
    biopics['lead_actor_actress_known'] = ~biopics['lead_actor_actress'].isnull()
    # update to million dollars
    biopics['earnings'] = biopics['earnings'] / 1000000
    # Sort by earning
    biopics.sort_values(by='earnings', ascending=False, inplace=True)
    
    return biopics