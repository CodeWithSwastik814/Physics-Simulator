import numpy as np
import pandas as pd

# Loading Dimension Dataset
df = pd.read_csv('physics_dimensions.csv')

# Enter the Foumla Name
value = str(input('enter formula name : '))

def findingDim(value):
    print('M : Mass, L : Length, T : Time, I : Current, Theta : Temp, N : Amount, J : Luminosity')
    # this Calculates row of the formula 
    index_num = df[df['Formula Name'] == value].index

    # this outputs the Dimension of given Formula
    print(df.iloc[index_num, 10])

findingDim(value)