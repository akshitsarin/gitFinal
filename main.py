from add import add
from diff import subtract
from multiply import multi
from division import div
from modulus import mod

input1 = int(input("enter number 1: "))
input2 = int(input("enter number 2: "))

op = input("enter operator: ")

if op == '+':
	print ("sum:", add(input1, input2))
elif op == '-':
	print ("difference:", subtract(input1, input2))
elif op == '*':
	print ("product:", multi(input1, input2))
elif op == '/':
	print ("quotient:", div(input1, input2))
elif op == '%':
	print ("modulus:", mod(input1, input2))