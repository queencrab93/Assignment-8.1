import os

chosendir=input("Please type the name of your chosen directory.")
if os.path.exists('chosendirec'):
    print
    os.chdir('chosendirec')
else:
    print("We will need to make this.") 
    os.mkdir('chosendirec')

uifil = ""
while not uifil:
    uifil = input("Please type the name of the file you'd like to save.")
print (f"you want to use {uifil} right?")    
if "yes":
    print ('ok')
else:
    print ('ok.')
