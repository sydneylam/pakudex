from pakuri import Pakuri

class Pakudex:
    def __init__(self):
        self.__pakudex = []

    def get_species_list(self):
        list_of_species = [] #Creates a list within the function to eventually return back

        if self.__pakudex == []: #If the list is empty,the function will return none
            return None
        else:
            for i in range(len(self.__pakudex)):
                current_paku = self.__pakudex[i].get_species()
                list_of_species.append(current_paku) #adds all the species into a list to return to the user
            return list_of_species

    def get_stats(self, species):
        list_of_stats = []
        if self.__pakudex == []: #If the list is empty,the function will return none
            return None
        else:
            for i in range(len(self.__pakudex)): #Adding all added species to the created list_of_stats
                if self.__pakudex[i].get_species() == species:
                    list_of_stats.append(self.__pakudex[i].level)
                    list_of_stats.append(self.__pakudex[i].cp)
                    list_of_stats.append(self.__pakudex[i].hp)

            if list_of_stats == []: #If the list of stats later becomes empty, function will return none
                return None

            return list_of_stats

    def sort_pakuri(self):

        sorted_pakudex = sorted(self.__pakudex, key=lambda i: i.get_species()) #Sorts the species by alphabetical order
        self.__pakudex = sorted_pakudex

    def add_pakuri(self, species, level):
        for i in range(len(self.__pakudex)):
            if self.__pakudex[i].get_species() == species:
                return False #returns false if the list already contains the pakuri the user wants to add
        new_pakuri = Pakuri(species, level)
        self.__pakudex.append(new_pakuri)
        return True #successfully adds the user inputted pakuri and returns true

    def remove_pakuri(self, species):
        for i in range(len(self.__pakudex)):
            if self.__pakudex[i].get_species() == species:
                self.__pakudex.remove(self.__pakudex[i])
                return True #removes the pakuri and then ends the for loop
        return False #no pakuri is removed

    def evolve_species(self, species):
        for i in range(len(self.__pakudex)):
            if(self.__pakudex[i].get_species() == species):
                self.__pakudex[i].level *= 2
                self.__pakudex[i].set_attack((self.__pakudex[i].get_attack())+1)
                return True #returns true and the pakuri is successfully evolved
        return False

def main():

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    print_menu()

    pak = Pakudex() #creating a pakudex object called pak

    selection = valid_input() #prompts the user for input and ensures that it is of int type

    while selection != 7: #repeats as long as the user does not input 7 (exit)
        if selection == 1:
            species_list = pak.get_species_list()

            if species_list == None:
                print("\nNo Pakuri currently in the Pakudex!") #if the list is empty
            else:
                print("\nPakuri in Pakudex:")
                for i in range(len(species_list)):
                    print(f'{i+1}. {species_list[i]}') #displays a list of all the pakuri in the pakudex

            print_menu()
            selection = valid_input()

        elif selection == 2:
            species_name = input("\nEnter the name of the species to display: ")
            species_list = pak.get_species_list()

            if species_list == None:
                print("Error: No such Pakuri!") #if the list is empty
            else:
                if species_name in species_list: #checks if the species inputted by user is in the pakudex
                    stats_list = pak.get_stats(species_name)
                    print("\nSpecies: ", species_name)
                    print("Level: ", stats_list[0])
                    print("CP: ", stats_list[1])
                    print("HP: ", stats_list[2]) #displaying all stats
                else:
                    print("Error: No such Pakuri!") #error message displayed if user's input is not in the pakudex

            print_menu()
            selection = valid_input()

        elif selection == 3:
            valid_species = True

            added_name = input("\nSpecies: ")
            species_list = pak.get_species_list()
            if species_list != None: #ensuring that the list is not empty
                for i in range(len(species_list)): #checking to see if pakudex already contains the species
                    if species_list[i] == added_name:
                        print("Error: Pakudex already contains this species!")
                        valid_species = False
                        break

            #Program asks user for the pakuri's level only if the Pakudex does not already contain that species
            while(valid_species):
                #Checking to see if user inputs a valid level (a non-negative number)
                while True:
                    level_input = input("Level: ")
                    try:
                        added_level = int(level_input)
                        if added_level < 0:
                            print("Level cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Invalid level!")

                #Error handling complete, adding pakuri to pakudex
                pak.add_pakuri(added_name, added_level)
                print(f'Pakuri species {added_name} (level {added_level}) added!')
                break

            print_menu()
            selection = valid_input()

        elif selection == 4:
            removed_pakuri = input("\nEnter the name of the Pakuri to remove: ")
            species_list = pak.get_species_list()
            pakuri_present = 0 #a flag which checks if the pakuri to remove is even in the pakudex

            if species_list == None: #if the list is empty, display an error
                print("Error: No such Pakuri! ")
            else:
                for i in range(len(species_list)):
                    if species_list[i] == removed_pakuri:
                        pakuri_present += 1 #signals that the pakuri is in the pakudex

                if pakuri_present == 1: #pakuri is in the pakudex so it is removed
                    pak.remove_pakuri(removed_pakuri)
                    print(f'Pakuri {removed_pakuri} removed.')

                else: #pakuri is not in the pakudex so nothing is removed and error message is shown
                    print("Error: No such Pakuri! ")


            print_menu()
            selection = valid_input()

        elif selection == 5:
            evolved_species = input("\nEnter the name of the species to evolve: ")
            species_list = pak.get_species_list()
            pakuri_present = 0 #signals that the pakuri is in the pakudex

            if species_list == None: #if the list is empty, display an error
                print("Error: No such Pakuri! ")
            else:
                for i in range(len(species_list)):
                    if species_list[i] == evolved_species:
                        pakuri_present += 1 #signals that the pakuri is in the pakudex

                if pakuri_present == 1:
                    pakuri_present = 0
                    pak.evolve_species(evolved_species) #pakuri is in the pakudex so it is evolved
                    print(f'{evolved_species} has evolved!')
                else: #pakuri is not in the pakudex so nothing is evolved and error message is shown
                    print("Error: No such Pakuri! ")

            print_menu()
            selection = valid_input()

        elif selection == 6:

            pak.sort_pakuri() #sorts the pakuri and informs the user
            print("\nPakuri have been sorted!")
            print_menu()
            selection = valid_input()

        else:
            print("\nUnrecognized menu selection!") #displayed if the user inputs an integer that is not on menu list
            print_menu()
            selection = valid_input()

    print("\nThanks for using Pakudex! Bye!") #farewell message

def print_menu(): #function to display menu
    print(""" 
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Remove Pakuri
5. Evolve Pakuri
6. Sort Pakuri
7. Exit
    """)

# Validating user menu input
def valid_input():
    userInput = input("What would you like to do? ")
    while True:
        try:
            selection = int(userInput)
            break
        except:
            print("\nUnrecognized menu selection!")
            print_menu()
            userInput = input("What would you like to do? ")
    return selection

if __name__ == "__main__":
    main()