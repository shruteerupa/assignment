def sum_prod(a,b):
    product=a*b
    if (product>1000):
        return (a+b)
    else:
        return product
first_numb= int(input("enter first number"))
second_numb= int(input("enter second number"))
result=sum_prod(first_numb,second_numb)
print('the result is ', result)

