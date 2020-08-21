import random as rnd
import pandas as pd
import numpy as np


def group_data(group):
    df = pd.DataFrame(columns=['Nature', 'Max Health',
                               'Speed', 'Sex', 'Current Health'])
    for creature in group:
        row = {
            'Nature': creature.nature,
            'Max Health': creature.full_health,
            'Speed': creature.speed,
            'Sex': str(creature.sex),
            'Current Health': creature.health
        }
        df = df.append(row, ignore_index=True)

    return df


def print_creatures(group):
    for creature in group:
        creature.describe()


def analyse_group(creatures_df):
    df = {
        'Selfish': creatures_df[creatures_df['Nature'] == 'selfish'].shape[0],
        'Sharing': creatures_df[creatures_df['Nature'] == 'sharing'].shape[0],
        'Males': creatures_df[creatures_df['Sex'] == '1'].shape[0],
        'Females': creatures_df[creatures_df['Sex'] == '0'].shape[0],
        'Survivors': creatures_df['Current Health'].astype(bool).sum(axis=0),
        'Avg Max Health': creatures_df['Max Health'].mean(),
        'Avg Health': creatures_df['Current Health'].mean(),
        'Avg Speed': creatures_df['Speed'].mean(),
    }
    df = pd.DataFrame(df, index=[0])
    return df
