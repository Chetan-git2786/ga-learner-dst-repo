# --------------
# Code starts here

# Create the lists 

class_1=['Geoffrey','Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry', 'Corinna Cortes']
# Concatenate both the strings
new_class= class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')


# Print the list
print(new_class)
#Geoffrey Hinton 
#sum('Math'+'English'+'History'+'French'+'Science')
# Create the Dictionary
#courses = {{Geoffrey Hinton:{'Math': 65, 'English' : 70,'History':80,'French': 70,'Science': 60}}}
courses = {'Math': 65, 'English' : 70,'History':80,'French': 70,'Science': 60}

# Slice the dict and stores  the all subjects marks in variable

sub=['Math','English','History','French','Science']

# Store the all the subject in one variable `Total`

total=0
for i in sub:
    total=courses[i]+total
# Print the total

print(total)  
# Insert percentage formula
percentage=(total)/(len((courses)))

# Print the percentage
print(percentage)

# Create the Dictionary
mathematics={'Geoffrey Hinton':78, 'Andrew Ng' : 95,'Sebastian Raschka':80,'Yoshua Benjio': 50,'Hilary Mason': 70,'Corinna Cortes': 66,'Peter Warden':75}

topper=max(mathematics,key=mathematics.get)
print(topper)
# Given string
topper= 'Andrew Ng'

# Create variable first_name 
first_name, last_name=topper.split()
print(first_name)
# Create variable Last_name and store last two element in the list
first_name, last_name=topper.split()
print(last_name)
# Concatenate the string
full_name=(last_name+' '+first_name)
# print the full_name
print(full_name)
# print the name in upper case
full_name= 'Ng Andrew'
certificate_name=full_name.upper()
print(certificate_name)
# Code ends here


