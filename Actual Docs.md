
# Keg+ documentation

Keg+ is a stack-based esolang that focuses on improving the compactness of its predecessor Keg. What makes this different from other esolangs is:

* Alphanumerical characters are still auto pushed

* The community can contribute to a list of standard sequences (explained later)

* The included word dictionary has over 1 million words and phrases

* And much more.

<!-- yes, I did steal the intro from Keg. It's my esolang for goodness sakes -->

## A few conventions of this document

* `∆...∆` in a code snippet still means that the code is optional

* `>` in a code snippet means an input prompt

* `>>>` in a code snippet means a command prompt

## Design Principles

The main inspiration for Keg+ comes from comparing Keg's program sizes with other popular golfing languages such as 05AB1E, Japt, Pyth and even Teg - it was clear that more compact language features were needed. To do this, more structures needed to be introduced (such as functions, compressed strings and variables).

## The Basics

Most tutorials show how to print the string `Hello, World!` , so that’s what this tutorial will do as well. Here is a simple 21 byte program to achieve the goal.

    Hello\, World\!^(!|,)

Too much like the old tutorial for you? Okay then, here's a different version:

    Hello\, World\!


Still too unoriginal?!? Okay then, here's something new:

    `Hello, World!`

### Explanation

The new \` keyword delimits a string - a series of letters one after another - and pushes it as a string object.

-----------

Indeed, with Keg+ comes a new set of data types:

* Integers
* Characters
* Strings
* Stacks

These new data types will be talked about later.

### The Stack

Just like Keg, Keg+ has a main stack, which works just like its predecessor:

    3 # [3]
    4 # [3, 4]
    + # [7]

In the above example, the numbers 3 and 4 are pushed onto the stack, and are then added using the + operator. The way it works is that the + pops what will be called x and y off the stack (the first and second last item) and pushes y + x back onto the stack. Note that the order of x and y are important when using the - and \ operators, as x - y doesn’t equal y - x most of the time (as is the same with x / y and y / x). This can be seen in the following example:

    34-, #Outputs -1
    43-, #Outputs 1
    34/, #Outputs 0.75
    43/, #Outputs 1.333333333333

### Input/Output

Keg+ has a kind of different IO system to Keg, as the `. ` function has been changed. Rather than having two different functions
that print the top of the stack as either an integer or a character, Keg+ prints items off the stack as they are, either pretty-printed (achieved using `,`) or raw (achieved using `§`).

Input is done via the `?` function, and pushes the given input as an integer if the string is int-like, a character if it is a single character that isn't numeric and a string otherwise. For example, given input `123`, it will be pushed as the integer 123. While if the input is `a`, the character "a" will be pushed. And with input `abc123`, the string "abc123" will be pushed.

## Program Flow

### If Statements

If statements are still the same in Keg+, so the section from the Keg tutorial will be quoted:

As mentioned in the introduction, Keg has a readable and intuitive way of expressing if statements, for and while loops. The form of an if statement is:

    [...1 ∆| ...2∆]

When an if statement is run, the last item on the stack is popped, and if it is non-zero, ...1 is executed. If there is a |...2, it is executed if the popped value is 0.

### For loops

The form of a for loop has been updated and is now:

    (...1 ∆| ...2 | ..3∆)

When a for loop is run:
* If all three branches are present, then `...1` is the count of the loop, `...2` is the variable used to keep count of the loop and `...3` is the code executed in each loop.
* If only two branches are present, then `...1` is still the count of the loop, `¥L_` is the loop variable (where `L` is the level of the loop) and `...2` is the code executed in each loop.
* If only one branch is present, then `!` is the count of the loop (the length of the stack), `¥L_` is the loop variable (as explained above) and `...1` is the code to be executed each loop.

#### Evaluation of the count of the loop

Just like Keg, Keg+ evaluates the count of the loop (whether it be `...1` or `!`) in a similar way to its predecessor. In evaluating the expression, a temporary stack is created of which the top item is returned as the actual count. In this stack:

* `:` takes the top item from the main stack and duplicates it onto the temp stack
* `!` pushes the length of the main stack onto the temp stack
* `_` takes the top item from the main stack and pushes it onto the temp stack
* Core structures, comments, variable declarations and `|`s cannot be used _unescaped_ in the expression, and will raise an error
* Variables can still be accessed however.
* Operators all effect the temp stack

An example of a valid expression to evaluate would be:

    :91++

Which works by:

* Pushes the top item of the main stack onto the temp
* Pushes the number 9 onto the temp
* Pushes the number 1 onto the temp
* Adds 9 and 1 to get 10
* Adds 10 and whatever was duplicated at the start, and uses this value as the count.


An invalid expression might be

    ~9=[8]

Although maybe in future versions of the Keg family (perhaps Keg++), this may be valid.
<!-- Actually, conditional ranges might be a good idea and something to explore at a later date -->

### While loops

While loops have also had the form updated, and now look like:

    {...1 ∆|...2 | ...3∆}

When a while loop is executed:
* If all three branches are present, then `...1` is the condition of the loop, `...2` is used to determine whether the loop is pre-test or post-test (either `P` for pre-test and `p` for post-test) and `...3` is the body to be executed
* If only two branches are present, then `...1` is the condition of the loop, `P` is used as the test type and `...2` is the body of the while loop
* If only one branch is present, `1` is the condition of the loop (an infinite loop), `P` is still used as the test type and `...1` is the loop of the body

### Functions

Unlike Keg, functions are actually implemented in Keg+. The form is the same as original Keg:

    @name ∆n∆ | ...@

Where:

* `name` is the name of the function (can only contain a-z A-Z 0-9)
* `n` is the number of parameters to pop from the stack
* `...` is the body of the function

#### Example Functions

    @triple 1 | ::++@

This function, named "triple" takes 1 item from the main stack, duplicates it twice, adds it together twice and returns the result.

    @sum * | (+)@

This function, named "sum" takes all of the items on the main stack, and sums them all up, and returns the result

    @x _[3] | (§)@

This function, named "x", pops the last item on the stack, and, if it is an integer, pops that many items from the main stack (otherwise, the value in the brackets is used). It then prints everything in the parameter stack in its raw form and exits.

## Variables
A major new feature in Keg+ is the introduction of variables -- an improvement of the single register of Keg. Variables are assigned with the new `£` keyword and their values are retrieved with the new `¥` keyword.

When assigning the value of a variable, the top item is popped from the stack and used as the value. Also, variable names can only contain letters in the range of `a-z,A-Z,0-9`.

 For example:

	25*£abc

Will:

* Push `2` and `5` onto the main stack
* Multiply them to get `10`
* Store the value `10` in variable `abc`

And

	¥abc 5/

Will:

* Push the value of the variable `abc` (10) onto the stack
* Push `5` onto the stack
* Divide the two values to get a value of `2`

Note that when setting/getting the value of a variable, either a non-variable character or a space must be present after the name.

## Data Types

Unlike Keg, Keg+ has a whole new system of datatypes, including integers, strings, arrays and characters. These data types work in different ways, and will be explored below:

### Data Co-ercion
Unlike most traditional languages, Keg+ will automatically cast data types to other data types if needed; for example, when adding a string and an integer, there is no need to explicitly cast the integer to a string. However, this may lead to some unexpected situations, so a table of results can be found for each operator below.

#### Addition (+)



|   \<lhs\> + \<rhs\>   | Integer | Character | String (int-like) | String |   Stack   |
|:-----------------:|:-------:|:---------:|:-----------------:|:------:|:---------:|
|      Integer      | Integer |  Integer* |      Integer      | String | Integer** |
|     Character     |  String |   String  |       String      | String |   Stack   |
| String (int-like) |  String |   String  |       String      | String |   Stack   |
|       String      |  String |   String  |       String      | String |   Stack   |
|       Stack       |  Stack  |   Stack   |       Stack       |  Stack |   Stack   |

  

*The result would be the integer plus the ascii code of the character
**If the items in the stack are all integers, chars and int-like strings, then the stack is all added together and then added to the original integer. Otherwise, the result is a stack

#### Subtraction (-)

|   \<lhs\> - \<rhs\>   |  Integer |  Character | String (int-like) |   String  |   Stack   |
|:-----------------:|:--------:|:----------:|:-----------------:|:---------:|:---------:|
|      Integer      |  Integer |  Integer*  |      Integer      |   Error   | Integer** |
|     Character     |   Error  | Character? |       Error       |   Error   |  Stack*** |
| String (int-like) |   Error  |    Error   |     Stack****     | Stack**** |  Stack*** |
|       String      |   Error  |    Error   |     Stack****     | Stack**** |  Stack*** |
|       Stack       | Stack*** |  Stack***  |      Stack***     |  Stack*** |  Stack*** |

  

*The result would be the integer minus the ascii code of the character
**If the items in the stack are all integers, chars and int-like strings, then the stack is all added together and then subtracted from the original integer. Otherwise, the result is a stack
***Removes all occurances of the item in the stack
****A stack with the chars that are unique to both strings

#### Multiplication (*)

|   \<lhs\> * \<rhs\>   |        Integer       | Character | String (int-like) |        String        |        Stack        |
|:-----------------:|:--------------------:|:---------:|:-----------------:|:--------------------:|:-------------------:|
|      Integer      |        Integer       |  Integer* |      Integer      | String (python-like) | Stack (python-like) |
|     Character     |         Error        |  String** |       Error       |         Error        |        Error        |
| String (int-like) | String (python-like) |   Error   |       Error       |         Error        |        Error        |
|       String      | String (python-like) |   Error   |       Error       |         Error        |        Error        |
|       Stack       |  Stack (python-like) |   Error   |       Error       |         Error        |        Error        |

  

*The result would be the integer times the ascii code of the character
**The result would be the lhs multipled by the ascii code of the rhs and turned into a string in a python like fashion

#### Division (/)
|     \<lhs\> / \<rhs\>     | Integer | Character | String (integer-like) | String |  Stack  |
|:---------------------:|:-------:|:---------:|:---------------------:|:------:|:-------:|
|        Integer        | Integer |  Integer* |        Integer        |  Error | Stack** |
|       Character       |  Error  |   Error   |         Error         |  Error |  Error  |
| String (integer-like) |  Error  |   Error   |         Error         |  Error |  Error  |
|         String        |  Error  |   Error   |         Error         |  Error |  Error  |
|         Stack         | Stack** |   Error   |         Error         |  Error |  Error  |

  

*The result would be the integer divided the ascii code of the character
**Goes through and devides each item in the stack by the integer
_NB: Modulus would be the same as this table_

### Creation of data types

Now that it is known how different data types interact with each other, it is time to look at just how they are created; this section will try to explain how an instance of each data type can be made, show some examples and explain some of the inner workings of the storage of these data types.

#### Integers
An integer, simply put, is any whole number (either positive or negative) -- like a counting number -- and can be used to create other integers, or even decimal numbers.

Integers are created by pushing characters in the range of `0-9` onto the stack:

	0	#Pushes the integer 0 onto the stack
	7	#Pushes the integer 7 onto the stack
	25*	#Pushes 2 and 5 and multiplies them to get 10
	99+	#Pushes 9 and 9 and adds them to get 18
	12-	#Pushes 1 and 2 and subtracts them to get -1
	12/	#Pushes 1 and 2 and divides them to get 0.5

Within the main stack, integers are simply stored as is -- no special treatement is needed internally, as these are the simplest data types.

#### Characters
A character (char) is any single ascii/unicode character (unlike a string, which is a concatenated series of characters), and can be used either as an integer (through its ordinal value) or as an actual letter.

Characters are created by pushing characters (funny about that) that are either not binded to any built-in functions or escaped using a `\`:

	a	#Pushes the character "a" onto the stack
	G	#Pushes the character "G" onto the stack
	¬	#Pushes the character "¬" onto the stack
	\!	#Pushes the character "!" onto the stack
	\\	#Pushes the character "\" onto the stack

Within the main stack, characters are stored as a two-item dictionary (or associative-array for you non-pythoners) in the following structure:

	{
		"char" : ...,
		"code" : ...
	}

_Note that integers can be pushed as characters by escaping them with_ `\`

#### Strings
A string can be seen in these purposes as a series of concatenated characters, consequently making a singular object that can be easily manipulated.

##### Creation of Strings
You may be wondering about the reason why there is a whole entire subsection dedicated to the creation of strings... well, that's because there are just too many ways to create strings to put in one simple code block. But before the syntax for string creation is discussed, it is first important to define a few terms: the word "spaceful" refers to the act of placing spaces after String Compression Codes (you'll see what I mean later) and variables, while "spaceless" means that String Compression Codes are left "as-is".

Anyhow, here are the six types of strings in Keg+

|         Type        |   Form  |
|:-------------------:|:-------:|
| Spaceless, Standard |  `...`  |
|  Spaceful, Standard | `¶...¶` |
| Spaceless, SCC Only | `“...”` |
|  Spaceful, SCC Only | `‘...’` |
|  Spaceless, Special | `„...„` |
|  Spaceful, Special  | `«...«` |
