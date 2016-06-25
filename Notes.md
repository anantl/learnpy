# 08.04.2016 @ 0316

- When we need to make a certain line end with a character other than new line '\n' then use ",end("character")" after the print command
- To print a string as it is we can prefix an r to the string to show that it is a raw string
- For python every single physical line is a logical line unless you put a ';' at the end of a line which would mean that you can have multiple logical lines on a single physical line.
- '//' is used to divde and round the number down
- In Python we can have an 'else' clause for a while statement
- We should always add a ':' at the end of every control statement
- There is no limit for the size of ints in Python
- When the curly brances are used in the print statement then it is necessary to use the format function to get the output properly
- The global keyword can be used during a variable definition so that its value in the outermost block is used within the function also
- When passing default values to parameters in a function, we cannot have a parameter without a default value after a paramter with a default value in the function declaration statement
- The 'dir()' function can be used to list out all the variables and functions that are available for use from a certain module that has been imported
- We can use the ':' operator within the index of any sequence to fetch a sub-sequence from within. Sequences include: lists, strings, tuples etc. When specifying values before and after the ':' operator, the index from *before* to *after*-1 is fetched. A third argument can be given like so `a[x:y:z]` in which we will fetch items from x to y-1 with an increment of z between the indices.
- If we want to make a copy of a sequence then we need to assign a full slice of the sequence to another sequence. Using the '=' creates a reference to a sequence which is mutually bound.
- Using the 'os.sep' operator from the os module will enable us to use a seperator that is uniform throughout all operating systems
- In python a constructor is defined using the '__init__' function that is usually implicitly defined
- If we prefix a variable with a double underscore then the variable becomes a private variable
