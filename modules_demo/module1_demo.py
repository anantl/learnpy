# module1 can be imported freely since it is there in the same folder
import module1

# Calling a function from module1
module1.demo_format("Jumbo jack")

# printing a variable that is from the module that was imported
print(module1.ananth)

#Passing a variable from the imported module to a function in the module itself
module1.demo_format(module1.ananth)
