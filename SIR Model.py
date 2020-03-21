# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:24:24 2020

@author: antob
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
import pandas as pd

# CovidData = pd.read_csv("COVID-19-geographic-disbtribution-worldwide-2020-03-18.csv", index_col = 0)
# CovidData.set_index("GeoId", inplace = True)
# CN_Covid = CovidData.loc["CN"]
# CN_Covid["T"] = np.arange(len(CN_Covid))
# CN_Covid = np.array(CN_Covid)


Flu_Data = pd.read_csv ("C:/Users/antob/OneDrive - Broward College/_FSU_/5 - SPRING 2020/UROP/Project/BoardingSchool.csv" , index_col = 0)
Flu_Data["T"] = np.arange(len(Flu_Data))
Flu_Data = np.array(Flu_Data)


#total population 
N = 738
#Initial number of infected: 
I0 = 3
#Number of initial recovered: 
R0 = 0
#The number of susceptible: 
S0 = N - I0 - R0

#Perameters that will eventually turn into dynamic vars 
beta = .002342
gamma = 0.476
#Number of days
t = np.linspace(0,13,14)

#To play around with the perameters and make sure they are correct
# R0 = gamma/beta
# print (R0)
Imax = -(gamma/beta) + (gamma/beta * np.log(gamma/beta)) + S0+ I0 - (gamma/beta*np.log(S0))
print (Imax)


#SIR model
def SIR (y, t, N, beta, gamma):
    S, I, R = y
    dSdt = (-beta * S * I)
    dIdt = (beta * S * I) - gamma * I
    dRdt = (gamma*I)
    return dSdt, dIdt, dRdt

#Initial condition vector: 
Y0 = S0, I0, R0

sol = odeint(SIR, Y0, t, args = (N, beta, gamma))
S, I, R = sol.T

#print(sol)
plt.plot (Flu_Data[:,2], S, c= "b", label = 'Susceptible')
plt.plot (Flu_Data[:,2], I, c="r", label = 'Infected')
plt.plot (Flu_Data[:,2], R, c="g",label = 'Recovered')


plt.plot (Flu_Data[:,2], Flu_Data[:,0], label = "Actual Infected")

plt.ylabel("Population(in 1000s)") 
plt.xlabel ('Days')
plt.legend(prop={"size":20})
plt.show()  

                        


