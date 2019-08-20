thistuple = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z')

thistuple1=('a' , 'b', 'c', 'd', 'e', 'f','g', 'h','i','j','k', 'l', 'm', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z')

thistuple2= ('0123456789')



#now run the commands********

print (" Enter any capital letter !", '\n')

x = input()

if x in thistuple :
	print("yes ! your input is accessible.")
	
elif x in thistuple1:
	print("Opps ! You have entered a lower-case letter !", '\n')
	print(" strike the ENTER key, to get data !")
	input()
	mytuple = thistuple1.count(x)
	myindex = thistuple1.index(x)
	print('\n', thistuple1)
	print('\n')
	print('Identity :', x , '\n')
	print('No. of letters : ' ,mytuple, '\n',  'Position   No.  : ' ,myindex)
	exit()
	
elif x in thistuple2:
	print('\n', " Opps ! You have entered a digit !", "\n")
	print("strike the ENTER key, to get data !")
	input()
	mytuple = thistuple2.count(x)
	myindex = thistuple2.index(x)
	print('\n', thistuple2)
	print('\n')
	print('Identity :', x , '\n')
	print('No. of digits : ' ,mytuple, '\n',  'Position   No.  : ' ,myindex)
	exit()

elif x

mytuple = thistuple.count(x)
myindex = thistuple.index(x)
print('\n', thistuple)
print('\n')
print('Identity :', x , '\n')
print('No. of letters : ' ,mytuple, '\n',  'Position   No.  : ' ,myindex)
