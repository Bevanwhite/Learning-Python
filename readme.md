
1. what is python
    - object-oriented, interpreted language that's easy to use and runs on many operating systems.
    - named after the cult comedy show **Monty Python's Flying Circus**
    - supports basic data types such as 
      - numbers and strings, 
      - complex types like lists and dictionaries, 
      - that can greatly simplify data processing.
    - supports several programming paradigms
      - Procedural Programming
      - Functional Programming
      - Object Oriented Programming
    - Data in python are strongly typed
      - so attempting to add a number and string will give an error
    - Dynamically typed,
      - you are free to from worrying about variable declarations
    - Very powerful language
    - one of the official languages at Google
    - creator of python is _**Guido van Rossum**_
    - python team decided to break backward compatibility when creating python 3
    - python 2 last stable version is 2.7 is no longer supported after 2019.

2. what is programming paradigm
   - A style or way of programming - a set of principles and concepts that define how programs are structured and how computations are performed. It influences how you think about and write code.
   - major programming Paradigms
     - Imperative Programming - How to perform step-by-step
     - Object-Oriented Programming - Modeling software as collections of interacting objects
     - Functional Programming - Computation as the evaluation of pure functions.
     - Procedural Programming - Breaking programs into procedures or routines
     - Logic Programming - Defines  rules and facts, and letting the computer infer results
     - Declarative Programming - 

| Jargon             | Meaning                                                                                                                                                                                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| literal            | A value of some type<br/> Examples of numeric literals are 1, 42, 98.04<br/> Examples od string literals are: "Hello, World!", "Guido van Rossum", "Python"                                                                                                                         |
| function           | A named block of code that we can call, by using it's name.<br/> We can write our own functions, or we can use functions that are built into python (such as **print**)<br/> In Python, all functions **return** a value.                                                           |
| arguments          | A value passed to a **function**, in order to give it values to work with.<br/> There may be no **arguments**, or there mat be 1 or more.<br/> Arguments appear in parentheses after the **function** name.<br/> If there are no arguments, you still have to types the parentheses |
| calling a function | Using the **function** name to execute the function's code. <br/> when you **call** a function, you have to provide the **arguments** that the function expects. <br/> if it doesn't expect any arguments, don't put anything between the parentheses.                              |
| return value       | The value that a **function** returns. <br/> we haven't talked about that yet, but it belongs in this slide, to make the slide complete.                                                                                                                                            |
| parameters         | Also called **formal parameter**.<br/> This is something else we haven't discussed yet, and we'll learn about **parameters** when we write our own functions.                                                                                                                       |

3. Variables and types
   - when a program's running everything the program needs ends up stored in the computer's memory.
   - The program code itself will be stored in one area of memory
   - the data it works on will also be stored somewhere in memory.
   - variable is
     - is basically just way to give a (meaningful) name to an area of memory, 
     - into which we can place certain value.
   - few rules for variable names
     - begins with  a letter or an underscore (_) character
     - can contain letters, numbers or underscore character
     - can't start with numbers
     - variables are case-sensitive greeting and Greeting are two different variables
     - variables are created first they attach the value using = sign.
   - python built-in data types
     - numeric
     - iterator
     - sequence(which are also iterators)
     - mapping 
     - file
     - class
     - exception
   - numeric Data types
     - int 
     - float
     - complex
     - python 2 had another type called long, 
     - because it's int type couldn't store very large values.
     - in python 3, the int replaces long.
   
4. int data type
   - python integer data type called int
   - integers are just whole numbers
   - float is numbers having a fractional par after the decimal point.
   - int effectively has no maximum size
   - you'll run out of memory before you exceed the size limit.
   - 