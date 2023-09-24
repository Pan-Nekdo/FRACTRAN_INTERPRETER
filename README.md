# FRACTRAN_INTERPRETER

FRACTRAN INTERPRETER is a interpreter for the esoteric programming language FRACTRAN written in Python.

## Instalation

Download and run the FRACTRAN_INTERPRETER.py. Requires Python 3.

## Usage

FRACTRAN is an esoteric programming language invented by J. Conway. A program in FRACTRAN is an ordered list of fractions greater than zero together with initial positive integer input *n*. The program is run by updating the integer *n* as follows:
1. for the first fraction *f* in the list for which *nf* is an integer, replace *n* by *nf*
2. repeat this rule until no fraction in the list produces an integer when multiplied by *n*, then halt.

[This page](http://lomont.org/posts/2017/fractran/) demonstrates that even FRACTRAN can be run in FRACTRAN and while explaining it it describes how to write in FRACTRAN.

To enter your program here simply type the initial value n followed by the program (the fractions) separated by spaces. Note that the denominators of the fractions must be always present (even when the fraction is whole number - write it as *a/1*).

Because very often interesting are not only the final values but even the values during the execution this interpreter prints them. The number of these numbers during the process is often very high (and sometimes the programs are intentionally designed to be infinite - for example the PRIMEGAME by the author J. Conway that produces prime numbers) so it would be hard to go through them when all would be printed (almost) at the same time, this interpreter prints only limited number of them and then asks whether it should continue. You can change this limit in SETTINGS or even choose not to have it at all. You can turn off the printing of the numbers during the process as well.

This interpreter furthermore has the following commands:
* HELP - to open this help.
* SETTINGS - to change settings of this interpreter
* EXIT - to leave this interpreter


Finally this interpreter allows you to save programs and quickly access them using their name. To use them simply type the initial value followed by the name of the program. The following commands are used to save new ones, delete old ones and see which ones are currently saved (and can be used):
* SAVE - saves a new program (syntax: SAVE _NAME_ _FRACTIONS_)
* DEL - deletes a prorgam (syntax: DEL _NAME_)
* PROGRAMS - shows all currently saved programs

Upon start the following programs are saved (both invented by J. Conway):
* PRIMEGAME - together with initial *n = 2* it never halts, however, the sequence generated contains only the powers of 2 that are 2 to a prime
* FIBONACCIGAME - starting with *78\*5^(n-1)*, it halts on *2^F<sub>n</sub>* where *F<sub>n</sub>* is the *n*th Fibonacci number.
