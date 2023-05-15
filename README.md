# Inputbetter
An easier way to input data into python lists
install via: https://pypi.org/project/Inputbetter/
or use pip install Inputbetter

![logo](https://github.com/Sankie005/Betterinput/blob/3e1eabc95e6922444b7746da9b0946d869db781d/betterinputlogo.png)




***
## A quick example on how to use it: 
### Here type represents str, int and mixed is the variable type you'd like to enter into your list (str) 
### Display is the text that's shown to the user when entering data, it will be appended with the number of the current entry and ":" (str)
### Number is the number of elements you'd like to enter in a list (int)
~~~ 
import Inputbetter
mylistnames=[] #creating an emptylist 
mylistnames=mylistnames+(Inputbetter.btrinpt("type","Display",Number)) #joining our newly created list with values from inputbetter 
print(mylistnames)
~~~
