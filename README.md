# (Ke)yboard (G)olfed (+)

## Three Main Structures

If statements: `[stmt_true | stmt_false]`
While loops: `{cond | test_type | body}`
For loops: `(count | variable | body)`

### Optional/Default values
#### If
* stmt_false: ``

#### While
* cond: `1`
* test_type: `P` (pre-test... "p" is post-test)

#### For
* count: `!`
* variable: `£x` (where x is the loop level)

## Functions
### Defining

`@name params | body@`

The name is optional and, if left out, makes the function a sort of inline type of function.

Params is also optional, as when it is not given, nothing is used as params.

A `*` can be used to select all items in the main stack.

<!-- That could actually lead to a whole entire system of selective parameters... -->

### Calling

`@name;`

Takes the name of the function and calls it

# Variables

Defining: `£name`
Accessing: `¥name`

Valid names can only include `A-Z a-z 0-9`

# Ranges
## Inclusive

Usage: `x…y`

`x` is any valid number as is `y`

Examples:

`0…9` > `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
`1…10` > `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
`20…15` > `[20, 19, 18, 17, 16, 15]`

## Exclusive

Usage: `x»y`

Examples:

`0»9` > `[0, 1, 2, 3, 4, 5, 6, 7, 8]`
`1»10` > `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
`20»15` > `[20, 19, 18, 17, 16]`

## Steps

Usage: `x∆y|z` (where ∆ is any range symbol)

Examples:

`0…10|2` > `[0, 2, 4, 6, 8, 10]`
`21»0|3` > `[21, 18, 15, 12, 9, 6, 3]`
`0»1|1` > `[0]`

## Strings, Compression and Object Strings

Strings are marked with \`s and can contain string compression codes (SCCs) or objects (it's a bit of a messy part...)

Examples:

    `This is a string`
    `So is this`
    `This string has ssc;` #just pretend ssc is the row for Compression
    `n[ ];` #object String

### Potential Idea: Formatting

Like in other languages (such as Python), Keg+ could allow for strings to have variables inserted into them (kind of like f-strings in python: f"{name}")

The symbol for this would simply be the `¥` character, and would be used as so:

    [s| ]£s
    `Bottle¥s`  #Kind of conditional formatting in a way.

### String Compression codes

It is clear from looking at languages such as 05AB1E that strings, as they are, can oftentimes be inefficient. Consequently, a new feature in Keg+ is string compression. Here's how it works:

Included within the repo for Keg+ is a ~1 million word 'dictionary', where each line corresponds with a certain word or phrase. For example, the word "Whomst'd've'ly'yaint'nt'ed'ies" might be at row "xA2" (probably won't tho.)

Note that to make a word start with an uppercase letter, use a `^`

These row codes (or **S**tring **C**ompression **C**odes - SCCs) are made up of, at most, 3 symbols (excluding `;`, `^` and `\`). To use these SCCs, simply create a string as usual, and put the SCC followed by a semi-colon. SCCs will be grouped in threes where possible (if not, in twos or singularly). To avoid having a letter be a part of a SCC, simply escape it using `\`.

Some examples:

    `3[?;`  #gets word at row 3[?
    `\3[?;` #gets word at row [?
    `mEME;` #gets word at row EME
    `Da\nk;`    #gets word at row Dak and inserts the character "n" halfway
    `D\ank;`    #gets word at row Dnk and inserts the character "a" halfway
    `Dan\k;`    #gets word at row Dan and inserts the character "k" at the end
    `Dank\;`    #Nothing special
    `f;`    #gets word at row f

Let it be noted that there are only ~470k words in the english dictionary, much less than 1 million, so some rows might have phrases and even other languages

### Object Strings
<!-- Or, the easiest way to fully implement the standard library 100% in Keg+ -->

Object strings are normal strings that start with either a 'n' or a 'c' and contain the desired effect

For example:

    `n[ ]@` #new stack
    `n" "@` #new empty string
    `n[1, 2, 3, 4, 5]@` #new stack with objects 1, 2, 3, 4 and 5 inside it

and

    `cS>I@` #treat top item as a string and convert it to an integer
    `cS>A@` #'                        ' and convert it to a stack object
    `cC>S@` #treat top item as a character and convert it to a string

(Types: _I_nteger, _F_loat, _S_tring, _A_rray, _s_tack)

Essentially, `n` is for objects, and `c` is for type casting

## Indexing and stacks

Indexing is done with the repurposed `.` command. It pops the last item of the stack at pushes the object at the popped index of the new last item.

Examples:

(Assuming the stack is `[[1, 2, 3, 4, 5, 6, 7, 8]]`)

    3.  #[[1, 2, 3, 4, 5, 6, 7, 8], 4]
    22*. #[[1, 2, 3, 4, 5, 6, 7, 8], 5]

(Assuming the stack is `["Hello"]`)

    2. #["Hello", ("l", 108)]
    43- #["Hello", ("e", 101)]


### Assignment through Indexing

Use the `√` command

Pops `x` and `y` off the stack and sets `z[x]` to `y` (`z` is the last item on the stack after popping `x` and `y`)

Example:

(Assuming the stack is `[[0, 0, 0, 0, 0]]`)

    2.1+    #[[0, 0, 0, 0, 0], 1]
    2   #[[0, 0, 0, 0, 0], 1, 2]
    √   #[[0, 0, 0, 1, 0]]

## Printing

`,` pretty prints, `§` prints object "as is" (i.e. raw)
