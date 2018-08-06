# def prime_num():
# 	num = x/1 
# 	if num 
# 		i==0
# 		print()
# prime_num()
# prime numbers are greater than 1
# num = input()
# num = 12
# if num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")


a = 90
b = 100
for num in range(a, b + 1):
	if num >1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:		
			print(num)			