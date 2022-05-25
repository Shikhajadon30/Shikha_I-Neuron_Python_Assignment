#!/usr/bin/env python
# coding: utf-8
Question:- 1. In the below elements which of them are values or an expression? 
    eg:- values can beinteger or string and expressions will be mathematical operators.
*
'hello'
-87.8
-
/
+
6

Answer:-
   *    --------------- Expression
'hello' --------------- Value
-87.8 ----------------- Value
-     ----------------- Expresion
/     ----------------- Expression
+     ----------------- Expression
6     ----------------- Value
Question 2:- What is the difference between string and variable?
    
Answer :- Strings is a data type for a a sequence of characters (e.g. ‘’zaldnQfYJSMfwp”). In addition to letters, they can also
    include numbers, spaces, punctuation, and even line breaks (using ‘\n’ for new line). 
   
Strings can not be used for calculation (even if your string is just a number like ‘5’), you would have to convert it to a 
number data type first to perform math operations on it.

You, the programmer, define a string by putting single quotes (‘ ’) or double quotes (“ “) around whatever you want to classify
as a string. The string data type is primarily used for reading and writing data.

Variables are references that you create to refer to other values in your program later. An example of a value you might 
reference using a variable could be:

“This is a really long string that no-one wants to have to re-type, ever, because it’s so laborious and frustrating to have
to type out, it would be great to have a quick reference for this big, long string.”

When writing a program, you can assign the value to a variable (e.g. my_string = “This is a really long string…”) so that 
you can refer to it later in your program just by typing my_string. Variables are also 

great for being able to refer values in that change in response to different events in your program.

Strings and variables are fundamental concepts that are common to most modern programming languages    3. Describe three different data types.
Answer:- 
    1).Integers
In Python 3, there is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount of 
memory your system has, as are all things, but beyond that an integer can be as long as you need it to be:

>>> print(123123123123123123123123123123123123123123123123 + 1)
123123123123123123123123123123123123123123123124

  2).Floating-Point Numbers
The float type in Python designates a floating-point number. float values are specified with a decimal point. Optionally, 

the character e or E followed by a positive or negative integer may be appended to specify scientific notation:

>>> 4.2
4.2
>>> type(4.2)
<class 'float'>
>>> 4.
4.0
>>> .2
0.2

>>> .4e7
4000000.0
>>> type(.4e7)
<class 'float'>
>>> 4.2e-4
0.00042

3). Complex Numbers
Complex numbers are specified as <real part>+<imaginary part>j. 
For example:

>>> 2+3j
(2+3j)
>>> type(2+3j)
<class 'complex'>
Strings
Strings are sequences of character data. The string type in Python is called str.

String literals may be delimited using either single or double quotes. All the characters between the opening delimiter 

and matching closing delimiter are part of the string:

>>> print("I am a string.")
I am a string.
>>> type("I am a string.")
<class 'str'>

>>> print('I am too.')
I am too.
>>> type('I am too.')
<class 'str'>
A string in Python can contain as many characters as you wish. The only limit is your machine’s memory resources. 

A string can also be emptyQuestion:- 4. What is an expression made up of? What do all expressions do?
   
Answer :- An expression is a combination of operators and operands that is interpreted to produce some other value. In any 
    programming language, an expression is evaluated as per the precedence of its operators. So that if there is more than 
    one operator in an expression, their precedence decides which operation will be performed first. We have many different 
    types of expressions in Python. Let’s discuss all types along with some exemplar codes :

    1. Constant Expressions: These are the expressions that have constant values only.
    
    2. Arithmetic Expressions: An arithmetic expression is a combination of numeric values, operators, and sometimes parenthesis. 
    
    The result of this type of expression is also a numeric value. The operators used in these expressions are arithmetic operators
    like addition, subtraction, etc. Here are some arithmetic operators in Python:

    Operators	Syntax	Functioning
    +	x + y	Addition
    –	x – y	Subtraction
    *	x * y	Multiplication
    /	x / y	Division
    //	x // y	Quotient
    %	x % y	Remainder
    **	x ** y	Exponentiation
    3. Integral Expressions: These are the kind of expressions that produce only integer results after all computations and 
        type conversions.
        
    4. Floating Expressions: These are the kind of expressions which produce floating point numbers as result after all 
        computations and type conversions.
             
    5. Relational Expressions: In these types of expressions, arithmetic expressions are written on both sides of relational 
        operator (> , < , >= , <=). Those arithmetic expressions are evaluated first, and then compared as per relational 
        operatorand produce a boolean output in the end. These expressions are also called Boolean expressions.
                
    6. Logical Expressions: These are kinds of expressions that result in either True or False. It basically specifies one 
        or moreconditions. For example, (10 == 9) is a condition if 10 is equal to 9. As we know it is not correct, so it 
        will return False.Studying logical expressions, we also come across some logical operators which can be seen in 
        logical expressions most often. Here are some logical operators in Python:

Operator	Syntax	Functioning
and	P and Q	It returns true if both P and Q are true otherwise returns false
or	P or Q	It returns true if at least one of P and Q is true
not	not P	It returns true if condition P is false

    7. Bitwise Expressions: These are the kind of expressions in which computations are performed at bit level.
        
    8. Combinational Expressions: We can also use different types of expressions in a single expression, and that will be termed 
        as combinational expressions.
            
            Multiple operators in expression (Operator Precedence)
            
It’s a quite simple process to get the result of an expression if there is only one operator in an expression. But if there is 
more than one operator in an expression, it may give different results on basis of the order of operators executed. To sort out
these confusions, the operator precedence is defined. Operator Precedence simply defines the priority of operators that which 
operator is to be executed first. Here we see the operator precedence in Python, where the operator higher in the list has more
precedence or priority:

Precedence	Name	Operator
1	Parenthesis   	( ) [ ] { }
2	Exponentiation	 **
3	Unary plus or minus, complement 	-a , +a , ~a
4	Multiply, Divide, Modulo  	/  *  //  %
5	Addition & Subtraction 	+  –
6	Shift Operators	>>  <<
7	Bitwise AND	&
8	Bitwise XOR	^
9	Bitwise OR	|
10	Comparison Operators	>=  <=  >  <
11	Equality Operators	==  !=
12	Assignment Operators 	=  +=  -=  /=  *=
13	Identity and membership operators	is, is not, in, not in
14	Logical Operators   	and, or, not
So, if we have more than one operator in an expression, it is evaluated as per operator precedence. For example, 
if we have the expression “10 + 3 * 4”. Going without precedence it could have given two different outputs 22 or 52. 
But now looking at operator precedence, it must yield 22. Let’s discuss this with the help of a Python program:

Hence, operator precedence plays an important role in the evaluation of a Python expression.Question:- 5. This assignment statements, like spam = 10. What is the difference between an
            expression and a statement?
        
Answer:- Difference between Expressions and Statements in Python:
                       Expression               	                          Statement
An expression evaluates to a value              	                    A statement executes something
The evaluation of a statement does not changes state            	    The execution of a statement changes state
Evaluation of an expression always Produces or returns a result value.	Execution of a statement may or may not produces or                                                                  displays a result value, it only does whatever the statement says.
Every expression can’t be a statement.           	                    Every statement can be an expression.
Example: >>> a + 16
>>> 20                                          	                     Example: >>> x = 3
                                                                        >>> print(x)

                                                                         Output: 3        
# In[ ]:


get_ipython().set_next_input('Question:- 6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1

Answer :- 23


# Question:- 7. What should the values of the following two terms be?
# 'spam'+'spamspam'
# 'spam'*3
# 
# Answer:- 'spamspamspam'

# In[ ]:


get_ipython().set_next_input('Question:- 8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')
    
Answer:- Because variable names cannot begin with a number.

