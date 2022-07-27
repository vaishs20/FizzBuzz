import re                                                                           #re package to reverse output for final query
def FizzBuzz_():                                                                    #function and list loop 
    _ = []
    for i in range(1,101):                                                          # expand range to 301 to check 
        if (i % 3 == 0) and (i % 5 == 0):                                           #if num % 15 == 0 #most complex piece of code #first come order 
            _.append("FizzBuzz")
        elif i % 5 == 0:
            _.append("Buzz")
        elif i % 3 == 0:
            _.append("Fizz")
        else:
            _.append(i)
    return _
test_FizzBuzz_ = FizzBuzz_()
print("firststep")
print(test_FizzBuzz_)

def Bang_(test_FizzBuzz_):
    for i in range(len(test_FizzBuzz_)):
        if ((i+1) % 21 == 0) or ((i+1) % 35 == 0):                                  # to include both %3 and %5  
            test_FizzBuzz_[i] = test_FizzBuzz_[i] + "Bang"
        elif  ((i+1) % 7 == 0):
            test_FizzBuzz_[i] = "Bang"
    return(test_FizzBuzz_)
test1_= Bang_(test_FizzBuzz_)
print("step2firstquery")
print(test1_)   

def Bong_(test1_):
    for i in range(len(test1_)):
        if ( (i+1) % 11 == 0):
          test1_[i] = "Bong"
    return(test1_)
test2_= Bong_(test1_)
print("secondquery")
print(test2_)

def Fezz_(test2_):
    for i in range(len(test2_)):
        if ((i+1) % 13 == 0):
            start_b =  str(test2_[i]).startswith('B')                                  #startswith to ensure output intials of B come at the end
            if start_b:                                                                #condition and if else to get the above outcome
                test2_[i] =  "Fezz" + test2_[i]                                        #imporvement require to split list and reorder to esnure 'Fuzz' can be in middle
            else :
                test2_[i] = "Fezz"
    return(test2_)
test3_ = Fezz_(test2_)
print("thirdquery")
print(test3_)

def reversed_list_(test3_):
    for i in range(len(test3_)):
        if ((i+1) % 17 == 0):
            order_ =  filter(None, re.split("([A-Z][^A-Z]*)",str(test3_[i]) ))      #turned list into string to oragnaised it 
            reversed_ = list(order_)[::-1]                                          #used indice to sort output in reverse
            test3_[i] = "".join(reversed_)                                          #used join to turn string into list again
    return(test3_)
finaltest_= reversed_list_(test3_)
print("finalquery")
print(finaltest_)

