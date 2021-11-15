#1.
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

#2.
def c_to_f(c):
	return (c*9/5)+32
def f_to_c(f):
	return (f-32)*5/9

print(c_to_f(60))
print(f_to_c(45))

#3.
def start_guess():
	from random import randint as rt
	g= rt(1,9)

	while True:
	    ug = int(input("Guess a number: "))
	    if g==ug:
	        print("Well guessed!")
	        break
	    else:
       		print("Incorrect!\n")
#start_guess()
#input does not work in sublime so i have this commented 

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
#decrements
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#word = input("Input a word to reverse: ")
word = "hello"
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


l = [2,4,6,10, 21, 4, 45, 66, 93, 1,11,31] 

even, odd= 0, 0

for i in l: 

    if i % 2 == 0: 

        even += 1

    else: 

        odd+= 1          

print("Even : ", even) 

print("Odd : ", odd)
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")