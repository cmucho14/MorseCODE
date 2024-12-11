# MorseCODE
Old Signals, New Possibilities

## About
A Programming Language where you can code in secrecy. Editing the TextX file of commands allows you to fully customize your language to you desires

## HelloWorld.morse

Start message { 
   *--* "Hello World" 
} End message

command should be '*--*' not '*'

## Overview of keywords for my preferences

These commands are how I originally created the language, but you are more than welcome to change it up to however you like.

## Program File Format

Program Start:

Start message {
  commands go here
} End message

## Syntax For Block Structures

This includes: Conditionals, For and While Loops
Block Syntax:

'-*--' / Y {
commands here
} '--**' / Z

##Commands

'*-' / A --> Assign //Assigns values to variables

'-***' / B --> Increment //Increment a variable by one or your specified amount 

'-*-*' / C --> Conditional //Block used to check the boolean value of a condition and run code inside the declared block

'-**' / D --> Division //Takes two numbers, divides them, and then stores the results

'**-*' / F --> For Loop // Fors a set number of times 

'****' / H --> ElseClause //Is ran in addition to the Conditional, if you want an else statement

'**' / I --> Index //retrieves the index of an element of a list if contained, otherwise returns -1

'*---' / J --> Length //returns the length of a list

'-*-' / K --> List //Creates a list

'--' / M --> Modulo //Finds the remainder of a number being divided with another 

'---' / O --> Open List //Opens a specific, valid index of a list

'*--*' / P --> Print //Prints what ever is after the statement
NOTE: for some reason the README does not like the print command. The correct syntax is a '*' before and after the '--'

'--*- / Q --> Insert List// Inserts a value at a speicifc, valid index into a list

'*-*' / R --> Add List// Adds an element to the end of a list

'***' / S --> Subtraction// Subtracts a value from another and stores the results

'-' / T --> Addition// Finds the sum of two values and stores the results

'*--' / W --> While Loop// runs a loop of commands until the condition is false

## Condition Operators

'*' / E --> ==

'--*' / G --> >

'*-**' / L --> <

'***-' / V --> >=

'-*' / N --> !=

'*--' / Q --> <=

## To Run

To run programs create a file with the end being .morse

Create your program using the syntax, then run your python file
