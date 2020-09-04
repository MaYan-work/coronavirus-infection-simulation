# Name: Yan Ma
# Student ID: 31245773
# Major: Business Analytics
# Start date: 2020-05-24
# Last modified: 2020-06-08
# Description of the program: This program is to simulate the spread of a viral disease epidemics
#                             and understand how it happens by visualising the simulation result.

# Task 2: Simulate disease spread

# Import all the things from task1
from a2_31245773_task1 import *
# Import libraries
import math
import random
import numpy
import scipy
import matplotlib
import pandas

class Patient(Person):
    def __init__(self, first_name, last_name, health):
        """
        purpose: Define a Patient class which inherits the methods of the Person class through inheritance.
        argument: first_name, last_name and health of a person
        """
        super(Patient, self).__init__(first_name, last_name)
        self.health = health


    def get_health(self):
        """
        purpose: Get the current health of each patient.
        return: The get_health method will return the patient’s current health points.
        """
        if self.health < 0:
            self.health = 0
        if self.health > 100:
            self.health = 100
        self.health = round(self.health)
        return self.health

    def set_health(self, new_health):
        """
        purpose: The set_health method will change the patient's current health points.
        argument: new_health
        """
        self.health = new_health

    def is_contagious(self):
        """
        purpose: Figure out whether a person is contagious.
        return: The is_contagious method will return whether the person is currently contagious.
        """
        if self.health < 50:
            return True
        else:
            return False

    def infect(self, viral_load):
        """
        purpose: The infect method infects the Patient object with a viral load.
                 And calculate the health point after receiving the viral load.
        return: The health point after receiving the viral load.
        """
        if self.health >= 50:
            self.health = self.health - 2.0 * viral_load        
        elif 29 < self.health < 50:
            self.health = self.health - 1.0 * viral_load       
        elif self.health <= 29:
            self.health = self.health - 0.1 * viral_load            
        if self.health < 0:
            self.health = 0 

    def sleep(self):
        """
        purpose: Calculate the health point after sleep.
        return: The health point after sleep.
        """
        self.health = self.health + 5   # The sleep method causes the person to recover 5 hps with one night's sleep.

    # Given methods defined in task1
    def add_friend(self, friend_person):
        super().add_friend(friend_person)
        
    def get_name(self):  
        super().get_name()
        return self.person[0]
    
    def get_friends(self):
        super().get_friends()
        return self.person[1:]

def random_choice(meeting_probability):
    """
    purpose: Define a random choice of whether a person go out to see friends by getting a random value between 0 and 1.
    argument: meeting_probability
    return: Whether they will meet each other
    """
    val = random.random()
    # If random value < meeting_probability means they will meet, else will not.
    if val < meeting_probability:
        return True
    else:
        return False

def load_patients(health):    # The same steps with task1
    """
    purpose: Create Patient objects, the same steps with task1.
    argument: health
    return: Return a patient_list of all the Patient objects created from the file records.
    """
    patient_list = []
    # Read from the a2_sample_set.txt
    # Creates a new Patient object for each record (line) in the file, which contains the name of the person
    # represented by that record.
    with open('./a2_sample_set.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            person = line.split(':')
            friend = person[1].split(',')

            person_me = person[0].split(' ')

            name = Patient(person_me[0], person_me[1], health)

            for i in range(len(friend)):
                name.add_friend(friend[i])

            patient_list.append(name)

        f.close()

    # Return a list of all the Patient objects created from the file records
    return patient_list


def run_simulation(days, meeting_probability, patient_zero_health):
    """
    purpose: Define how to run the simulation.
    argument: days of simulation, meeting_probability, patient_zero_health(the health point of patient zero)
    return: A ill_list contains the counts of sick people each day.
    """
    # Set the initial_health for all person
    initial_health = 75
    patient_list = load_patients(initial_health)

    # Set the patient_zero_health for the first person in the patient_list
    patient_list[0].set_health(patient_zero_health)

    # Make a list to store the information of amount of each day's sick people
    ill_list = []

    # Run through each day of the simulation
    for i in range(days):

        # Store the count of sick people each day in ill_count
        ill_count = 0

        # Run through each patient
        for j in range(len(patient_list)):
            # Get the patient's name by patient_list
            person = patient_list[j].get_name()
            # Get the patient's friends list
            friend_list = patient_list[j].get_friends()

            # Run through each friend of the patient
            for k in range(len(friend_list)):
                # Get the name of friend
                HPb_name = friend_list[k]
                HPb_name = HPb_name[1:]
                HPb_name = HPb_name.replace("\n", "")

                # Calculate the results of people meeting each other
                for n in range(len(patient_list)):
                    if patient_list[n].get_name() == HPb_name: # Get each friend's index position of patient_list

                        # When they meet each other
                        if random_choice(meeting_probability) == True:

                            # If both of them are sick, they will infect each other.
                            if patient_list[j].is_contagious() == True and patient_list[n].is_contagious() == True:
                                HPa = patient_list[j].get_health()  # the patient
                                HPb = patient_list[n].get_health()  # the friend
                                viral_load_j = 5 + ((HPa - 25)**2) / 62
                                viral_load_n = 5 + ((HPb - 25)**2) / 62
                                patient_list[n].infect(viral_load_j) 
                                patient_list[j].infect(viral_load_n)

                            # If the patient's friend is sick and he/she is not, he/she will infected by the friend.
                            elif patient_list[j].is_contagious() == False and patient_list[n].is_contagious() == True:
                                HPb = patient_list[n].get_health() 
                                viral_load_n = 5 + ((HPb - 25)**2) / 62
                                patient_list[j].infect(viral_load_n) 

                            # If the patient is sick and the friend is not, he/she will infect the friend.
                            elif patient_list[j].is_contagious() == True and patient_list[n].is_contagious() == False:
                                HPa = patient_list[j].get_health()
                                viral_load_j = 5 + ((HPa - 25)**2) / 62
                                patient_list[n].infect(viral_load_j)

                            # If both of them are not sick
                            else:
                                pass

        # Count the amount of each day's sick person
        for m in range(len(patient_list)):     
            if patient_list[m].is_contagious() == True:
                ill_count += 1

            # Sleep after one day pass and recover 5 points of health
            patient_list[m].sleep()

        # Add the count of sick people to ill_list
        ill_list.append(ill_count)

    # Return a list with the daily number of contagious cases through the duration of the simulation
    return ill_list


    



if __name__ == '__main__':
    test_result = run_simulation(15, 0.8, 49)   
    print(test_result)
    
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.


    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    
    #sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]