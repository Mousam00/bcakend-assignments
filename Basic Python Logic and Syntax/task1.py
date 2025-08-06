def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0: # multiples of both three and five print "FizzBuzz"
            print(i,"FizzBuzz")
        elif i % 3 == 0 : # for multiples of three print "Fizz"
            print(i,'Fizz')
        elif i % 5 == 0:
            print(i,"Buzz") #for the multiples of five print "Buzz"
        else:
            print(i)

fizz_buzz(15)