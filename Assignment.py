# -*- coding: utf-8 -*-
"""
@author: Sainavya
"""
#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

#Create a pandas data frame from the Pound_to_Dollar.csv file.

Pound_to_Dollar = pd.read_csv("Pound_to_Dollar.csv")

#Define Line Chart Function

def line_graph(Pound_to_Dollar):
    
    """
      Read the Pound to Dollar pands dataframe and select the required data columns 
      such as date, price, open, high, and low from the 2023 year 
      before plotting a line graph.
    """
    
    #select the required data columns from the Pound_to_Dollar dataframe
    Date = Pound_to_Dollar["Date"]
    Price = Pound_to_Dollar["Price"]
    Open = Pound_to_Dollar["Open"]
    High = Pound_to_Dollar["High"]
    Low = Pound_to_Dollar["Low"]
    
    #assign the labels for line graph. 
    line_graph = plt.xlabel("Date", fontsize = 25)
    line_graph = plt.ylabel("Price", fontsize = 25)
    line_graph = plt.title('Currency Coversion Rate of Pounds to Dollar in 2023 Year',fontsize = 25)
    
    #Plot the data
    line_graph = plt.plot(Date, Price, label = "Price") 
    line_graph = plt.plot(Date, Open, label = "Open") 
    line_graph = plt.plot(Date, High, label = "High") 
    line_graph = plt.plot(Date, Low, label = "Low") 
    line_graph = plt.legend()
    line_graph = plt.show() 

    return line_graph

line_graph = line_graph(Pound_to_Dollar)

#Create a pandas data frame from the Crime Statistics 2000-2020.csv file.

Crime_Statistics = pd.read_csv("Crime_Statistics_2000-2020.csv")

#Define Bar Chart Function

def bar_graph(Crime_Statistics):
    
    """
        Read the Crime Statistics pands dataframe and select the required data columns 
        such as Type of Crime and Number of Crimes from the 2000 year 
        before plotting a bar graph.
    """
    
    #select the required data columns from the Crime_Statistics dataframe
    TypeofCrime = Crime_Statistics["Type of Crime"]
    NumberofCrimes = Crime_Statistics["Number of Crimes"]
    
    #Plot the data
    bar_graph = plt.figure(figsize = (20, 10))
    bar_graph = plt.bar(TypeofCrime, NumberofCrimes, label = "NumberofCrimes")
    bar_graph = plt.xlabel('Type of Crime',fontsize = 25)
    bar_graph = plt.ylabel('Number of Crimes',fontsize = 25)
    bar_graph = plt.title('Types of Crime Statistics in 2000 Year',fontsize = 25)
    bar_graph = plt.legend()
    bar_graph = plt.show() 

    return bar_graph

bar_graph = bar_graph(Crime_Statistics)

#Define Pie Chart Function

def pie_graph(Crime_Statistics):
    
    """
        Read the Crime Statistics pands dataframe and select the required data columns 
        such as Type of Crime and Number of Crimes from the 2000 year 
        before plotting a pie graph.
    """
    
    #select the required data columns from the Crime_Statistics dataframe
    TypeofCrime = Crime_Statistics["Type of Crime"]
    NumberofCrimes = Crime_Statistics["Number of Crimes"]
    
    #Plot the data
    pie_graph = plt.subplots(figsize = (12, 10))
    pie_graph = plt.pie(NumberofCrimes, labels = TypeofCrime, autopct='%1.1f%%')
    pie_graph = plt.axis('equal')
    pie_graph = plt.title('Percentage of Crimes in 2000 Year',fontsize = 25)
    pie_graph = plt.legend(title='Type of Crimes',loc="best", bbox_to_anchor=(1, 0, 0.5, 1))
    pie_graph = plt.tight_layout()
    pie_graph = plt.show()

    return pie_graph

pie_graph = pie_graph(Crime_Statistics)
 


