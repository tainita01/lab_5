n=0
numset=[int ( raw_input('Enter your test number : ') )]
answer=0

while n <= 0.5*max(numset):
    n+=1
    if n*n in numset:
        answer=n

if answer > 0:
    print "The square root is " + str(answer) +"."
else:
    print "Number not a perfect square!"

        
