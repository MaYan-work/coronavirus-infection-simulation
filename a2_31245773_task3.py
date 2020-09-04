# Name: Yan Ma
# Student ID: 31245773
# Major: Business Analytics
# Start date: 2020-05-24
# Last modified: 2020-06-08
# Description of the program: This program is to simulate the spread of a viral disease epidemics
#                             and understand how it happens by visualising the simulation result.

# Task 3: Visualise the curve

# Answer:
# When the meeting_probability is close to 1, the results match the predictions well,
# and when meeting_probability is close to 0, the results are very random.

# Import from task2
from a2_31245773_task2 import *
import math
import random
import numpy
import scipy
import matplotlib.pyplot as plt
import pandas


def visual_curve(days, meeting_probability, patient_zero_health):
    """
    purpose: Run the simulation by calling the run_simulation function from task2 and plot the result.
    argument: days to simulate, meeting_probability, patient_zero_health
    return: The plot of simulation result.
    """
    ill_list = run_simulation(days, meeting_probability, patient_zero_health)
    print(ill_list)

    # Create a list x to store days information
    x = [ ]
    # Run through each day of simulation days
    for i in range(1, days+1):
        x.append(i)

    # Create a list y to store the information of amount of sick people
    y = ill_list

    # Create a new drawing background
    plt.figure()

    # Plot everyday's amount of sick people
    plt.plot(x, y)

    # Add the title of the X axis
    plt.xlabel('Days')

    # Add the title of the Y axis
    plt.ylabel('Count')

    # The range of X is:
    plt.xlim(0, len(ill_list))

    # The range of Y is:
    plt.ylim(0, max(ill_list))

    # Return the plot
    return plt    
    
    
if __name__ == '__main__':

    # User input 1
    days_text = input("Please enter how many days to simulate:")
    days = int(days_text)
    meeting_probability_text = input("Please enter a meeting probability(from 0 to 1):")
    meeting_probability = float(meeting_probability_text)
    patient_zero_health_text = input("Please enter health point of patient zero(from 0 to 49):")
    patient_zero_health = int(patient_zero_health_text)
    # Run simulation by user input 1 and plot the result
    plt_1 = visual_curve(days, meeting_probability, patient_zero_health)
    # Save the plot as scenario_A
    plt_1.savefig( './scenario_A.png')

    # User input 2
    days_text = input("Please enter how many days to simulate:")
    days = int(days_text)
    meeting_probability_text = input("Please enter a meeting probability(from 0 to 1):")
    meeting_probability = float(meeting_probability_text)
    patient_zero_health_text = input("Please enter health point of patient zero(from 0 to 49):")
    patient_zero_health = int(patient_zero_health_text)
    # Run simulation by user input 2 and plot the result
    plt_2 = visual_curve(days, meeting_probability, patient_zero_health)
    # Save the plot as scenario_B
    plt_2.savefig('./scenario_B.png')

    # User input 3
    days_text = input("Please enter how many days to simulate:")
    days = int(days_text)
    meeting_probability_text = input("Please enter a meeting probability(from 0 to 1):")
    meeting_probability = float(meeting_probability_text)
    patient_zero_health_text = input("Please enter health point of patient zero(from 0 to 49):")
    patient_zero_health = float(patient_zero_health_text)
    # Run simulation by user input 3 and plot the result
    plt_3 = visual_curve(days, meeting_probability, patient_zero_health)
    # Save the plot as scenario_C
    plt_3.savefig('./scenario_C.png')


