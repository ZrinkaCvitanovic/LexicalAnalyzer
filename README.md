# LexicalAnalyzer
This is a Python program that simulates the first phase of compiling a code - lexical analysis. The analyzer accepts a simple programming laguage that contains the followng lexical units: <br>
1. keywords <br>
for - start of a for loop (KW_FOR) <br>
rof - closing a for loop (KW_ROF) <br>
from  - start of a range (KW_FROM) <br>
to - end of a range (KW_TO) <br>
<br>
2. variables/identifiers (IDN) <br> <br>
3. operators + (OP_ADD), - (OP_SUB), * (OP_MUPLTIPLY), / (OP_DIVIDE), ( (LEFT_P), ) (RIGHT_P), = (OP_ASSIGN) <br> <br>
4. constants (only integers for simplicity) (NUM) <br>
<br>
The keywords that are written in the output of a program for each unit are written in parenthesis. <br>
The program reads each line of users input and parses each lexical unit. For each unit it prints out the name of a unit, line number and the unit itself. For example:  <br>
<i>a = 3  <br>
b = 4  <br> </i> <br>
will result in   <br> <br>
<i> ID 1 a  <br>
OP_ASSIGN 1 =  <br>
num 1 3  <br>
ID 2 b  <br>
OP_ASSIGN 2 = <br>
NUM 2 4  <br> </i
<br> <br>
The program splits user input by lines and each line by space since it is the most common way of writing code. However, since compilers usually ignore whitespaces, this analyzer is also 
adjusted for inputs that don't contain whitespaces. That's why input such as "1abc" will not raise an error, even though variable names cannot begin with a numbers,
but it will be interpreted as a number "1" and a variable "abc" written without a space in between. <br>
Newlines are not ignored becuase in case of an error in later phases of analysis it is important to let the user know exactly which line caused an error. <br>
I hope this code servers for better understanding of how lexical analysis works.
