### what is Python
- Python is an object-oriented, interpreted language that's easy to use, and runs on many operating systems
- it's named after the cult comedy show **Monty Python's Flying Circus** (not after the snake) and you'll find various references to **Monty Python** sketches in the official documentation
- Python supports basic data type such as numbers and strings as well as more complex types like list and dictionaries, that can greatly simplify data processing
- Python also supports several programming paradigms, and can be used for Procedural Programming, Functional Programming and Object-Oriented Programming
- Data in Python is strongly typed (so attempting to add number and a string will give an error)
  - it is also dynamically typed, so you are freed from worrying about variable declarations
- creator of python is ***Guido Van Rossum*** 



| Jargon             | Meaning                                                                                                                                                                                                                                                                      |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| literal            | A value of some type <br> Examples of numeric literals are: 1, 42, 98.04 <br> Examples of sting literals are "Hello, world", "Guido van Rossum","Python"                                                                                                                     |
| function           | A named block  of code that we can call, by using its name. <br> we can write our own functions, or we can use functions that are built into python (such as **print**)<br> in Python, all functions **return** a value                                                      |
| arguments          | A value passed to a **function**, in order to give it values to work with. <br> There may be no **arguments**, or there may be 1 or more. Arguments appear in parentheses after the **function** name <br> if there are no arguments, you still have to type the parentheses |
| calling a function | Using the **function** name to execute the function's code. <br> when you **call** a function you have to provide the **arguments** that the function expects. <br> if it doesn't expect any arguments,don't put anything between the parentheses.                           |
| return value       | The value that a **function** returns.<br> we haven't talked about that yet, but it belongs in this slide, to make the slide complete                                                                                                                                        |            
| parameter          | Also called **formal parameter** <br> This is something else we haven't discussed yet, and we'll learn about **parameters** when we write out own functions.                                                                                                                 |

- use backslash escape character rather than the raw in the print 
  - use `print("C://")` not `print(r""")`

#### Variables and Types
##### Variables
- a variable is basically just a way to give a meaningful name to an area of memory, into which we can place certain values.
- There are few rules for naming variables 
  - python variable names must begin with a letter(either upper or lower case) or an underscore _ character.
  - They can contain letters, numbers or underscore characters(but cannot begin with a number).
  - Python variables are case-sensitive, so **greeting** and **Greeting** would refer to 2 different variables
  - Variables are create d when they are first attached to a value, using =

##### Data Types
- numeric
- iterator
- sequence (which are also iterators)
- mapping
- file
- class
- exception

###### Numeric Data Types
- python3 has three numeric data types:
  - int
  - float
  - complex