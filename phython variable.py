first=input('enter the first number?')
second=input('enter the second number?')
first=int(first)
second=int(second)
print("----press keys for operator(+,-.*,/,%)------------")
operator=input('enter operator:')
if operator=="+":
     print( int(first + second))
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="/":
    print(first/second)
elif operator=="%":
    print(first%second)
else:
    print("invalid operation")