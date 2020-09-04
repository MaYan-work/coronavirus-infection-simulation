# Name: Yan Ma
# Student ID: 31245773
# Major: Business Analytics
# Start date: 2020-05-24
# Last modified: 2020-06-08
# Description of the program: This program is to simulate the spread of a viral disease epidemics
#                             and understand how it happens by visualising the simulation result.

# Task 1: Representing social connections in your program


class Person:
    """
    purpose: Create a Person class with the given methods to represent a person
             who is linked to other people by social connections.
    argument: The first_name, last_name of a person.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.first_name + ' ' +  self.last_name
        self.person = [self.name]

    # Add the given methods
    def add_friend(self, friend_person):
        """
        purpose: Add the friends of each person
        argument: friend_person
        """
        self.person.append(friend_person)

    def get_name(self):
        """
        purpose: Get the name of each person
        return: Name of person
        """
        return self.person[0]
    
    def get_friends(self):
        """
        purpose: Get the friends' name of each person
        return: Names of friends
        """
        return self.person[1:]


def load_people():
    """
    purpose: Read in the sample set and create a list to store them. Creates a new Person object for each record (line)
             in the file, which contains the name of the person represented by that record.
    return: Return a people_list of all the person and their friends that have been created from the file records.
    """
    # Create a suitable data type for storing: here choose list
    people_list = []

    # Read the sample set and get the names
    with open('./a2_sample_set.txt', 'r') as f:        
        while True:            
            line = f.readline()
            if not line:
                break
            person = line.split(':')
            friend = person[1].split(',')

            # Get first name and last name of the person
            person_me = person[0].split(' ')
            name = Person(person_me[0], person_me[1])

            # Add the person's friends' name to the Person object
            for i in range(len(friend)):
                name.add_friend(friend[i])

            # Add names to the people_list we created
            people_list.append(name)

        # Close the a2_sample_set.txt file
        f.close()    

    #  Return a list of all the Person objects that have been created from the file records.
    return people_list


if __name__ == '__main__':
    people_list = load_people()






