n = int(input('Please enter an range end point: ')) 
FzBz_list = []  

for num in range(1,n+1): 
    if num % 3 == 0 and num % 5 == 0:
        FzBz_list.append('FizzBuzz')
    elif num % 5 == 0:
        FzBz_list.append('Buzz')
    elif num % 3 == 0:
        FzBz_list.append('Fizz')
    else:
         FzBz_list.append(num)  
print(FzBz_list)

