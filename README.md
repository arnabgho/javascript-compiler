# Practical JavaScript Compiler
- We'll be working on creating a JavaScript practical compiler.
    - The version we are targeting is ES5.
    - Constructs which are bad will be omitted.
        - with
    - Lesser used constructs will also be omitted.
        - eval
        - '==' and '===' mean the same thing
        - '!=' and '!==' mean the same thing
    - There is no forwards compatibility.
        - class
        - const
        - extends
        - field
        - final
        - import
        - package
        - private
        - protected
        - public
        - super
    - Library routines are not implemented.
        - OOP features are not implemented because it is a library feature.
    - RegEx are not supported.
    - Ternary operator is not supported.
    - comma at the end of arrays and objects are not allowed
    - Overloading of '+' is not allowed
    - Only one type of number is allowed (compliant with the specs)
- The target architecture is SPIM.
- The implementation language is python.

# Todo
- Symbol table
- String and number conversion
- unary minus
- typeof operator
- extension of expressions
- relational expressions

# Milestones

## Features Implemented till now
- Declaration of variables
    - Objects and arrays are supported
- Assignment of values to variables
- Addition, Subtratction, Multiplication, Division of numbers
- String concatenation

# Usage
- run python lexer.py <testFileName>

# Build Instruction
- lexer.py contains the token definitions
    - the variable **lexer** stores the lexer
    - to start lexing, we need to give **lexer** a string and call **lexer.token** for a token

## Dependencies
- Python 2.7 and higher
- [ply](https://github.com/dabeaz/ply)

## Compiling and Building
- The builds are only for a Linux compliant machine (preferably Ubuntu)
- Use the makefile provided (instructions will be added as and when new components will be added)

## Tests
- All the test files need to added under the tests folder

