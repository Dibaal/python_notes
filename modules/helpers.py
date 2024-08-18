def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)


#(1)import module as namespace, (note helpers.py is the name of the module)
    import helpers #This pulls in the entire helpers module and creates a namespace called helpers.To access any function or variable from the helpers module, we need to prefix we need to prefix it with the namespace(helpers)
    helpers.display('Not a Warning') #Anytime we need to use a function in the namespace(helpers) we type the namespace(which is helpers in this case).the name of the function we want. This method encapsulates all the module's content within the helpers namespace, reducing risk of name conflicts and improves code readability.

 #(2)import all into current namespace. when we use this method. We are importing all functions, classes. and variables from the helpers module directly into the current namespace i.e we are not creating a new namespace here, we just import the contents of the module into the existing global namespace. Hence, accessing any function,classes, variables is directly without the helpers prefix.
from helpers import * # This method does not create a namespace, it just makes all the module's content available directly in the current namespace, which can lead to name conflicts and reduce readability.
display('Not a Warning')

#PACKAGES: They are published collection of modules.The best code in the world is the code that's already written.
#pip: the command line installer for installing packages

#Install an individual package
pip install colorama

#Install from a list of packages
pip install -r requirements.txt

#requirements.txt # Has a list of packages.
colarama 