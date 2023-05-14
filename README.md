# Betterinput
An easier way to input data into python lists
***
### A quick example on how to use it: 
~~~ 
  from Betterinput import btrinpt as bti 
  ## Here type represents either str or int and is the variable type you'd like to enter into your list (str) 
  ## Display is the text that's shown to the user when entering data, it will be appended with the number of the current entry and ":" (str)
  ## Number is the number of elements you'd like to enter in a list (int)
  
  bti.("type","display",number)
  ## By default the created list will be declared as "mylist" in the global scope 
  print(mylist)
~~~
