#This is a developing breaking cipher program
#It is the restructured edition from the 'classic cipher.py'
#
#
#
#
#
#
#Functions:

##indexes(list,element) returns every index number of that element

##bigram(code in digits<=26) returns the score on how english it is

##code_to_num(code in string) returns code in digit

##num_to_code(code in digit) returns code in string

##shift(code_list) returns the answer for ceaser shift

##check_repeat(code in string) print out the repeats and position, returns gcd

##gcd(two numbers) to work out the greatest common devisor\

##caesar() do caecar straight away

global code_list #every letter in the code is an element in this
code_list = [a for a in input('please put the code')]
#
#
#The function gcd(a,b) returns the greatest common factor of two integer input
#Using the famous Euclid's Algorithms.
def gcd(a,b):
    c = 1
    if a > b:
        c = b
        b = a
        a = c
    while c != 0:
        c = a%b
        a = b
        b = c
    return a
#indexes(list,element) returns a list that contains the index number of such element in the list
def indexes(in_list,elements):
    indexs = []
    lists = in_list[:]
    while 1:
        try:
            indexs.append(lists.index(elements))
            lists.pop(lists.index(elements))
        except ValueError:
            break
    return indexs
# input the digitalised code, return score
# Such score is determined by appearance of common bigrams in the text
##bigram intakes a list code_number
###code_number is a list that consist integers in range(1,26)
###each element in code_number represent an English Letter, in alphabetic order, 
###such as a == 1, b == 2 etc.
###functions num_to_code() and code_to_num() converts code into code_number and vise versa
def bigram(code_number):
    #example elif code_number[count] ==  and code_number[count + 1] == :
    score = 0
    count = 0
    while count <= len(code_number) - 2:
        #for 'th'
        if code_number[count] == 20 and code_number[count + 1] == 8:
            score += 1
        #for 'he'
        elif code_number[count] == 8 and code_number[count + 1] == 5:
            score += 1
        #for 'in'
        elif code_number[count] == 9 and code_number[count + 1] == 14:
            score += 1
        #for 'er'
        elif code_number[count] == 5 and code_number[count + 1] == 18:
            score += 1
        #for 'an'
        elif code_number[count] == 1 and code_number[count + 1] == 14:
            score += 1
        #for 'nd'
        elif code_number[count] == 14 and code_number[count + 1] == 4:
            score += 1
        count += 1
    
    return score

def code_to_num(code):
    return [ord(a)-96 for a in code]

def num_to_code(num):
    return [chr(a + 96) for a in num]

#shift(code_list) returns the answer for ceaser shift
def shift(code_cache):
    code = code_cache[:]
    count = 1
    scores = [0]
    
    while count <= 26:
        scores.append(bigram([a+count - 26 if a + count >= 27 else a+ count for a in (code_to_num(code))]))
        count += 1
    
    count = 1
    code.reverse()
    while count <= 26:
        scores.append(bigram([a+count - 26 if a + count >= 27 else a+ count for a in (code_to_num(code))]))
        count += 1

    count = scores.index(max(scores))
    print(count)
    if count <= 26:
        code.reverse()
    else:
        count -= 26
    print(code)
    return ''.join(num_to_code([a+count - 26 if a + count >= 27 else a+count for a in (code_to_num(code))]))

def check_frequency(code):
    items = []
    location = []
    mode_freq = 0
    for a in code:
        if a not in items:
            items.append(a)
    for a in items:
        location.append([a,indexes(code,a)])
        
        print(a,len(indexes(code,a)))
        if len(indexes(code,a)) >= mode_freq:
            mode_freq = len(indexes(code,a))
            mode = a
    print(mode)
    return 0
        

def caesar():
    return shift(code_list)
    
def trans(key_):
    length = (len(code_list)/key_)
    dev = [[],[],[],[],[],[],[],[],[],[]]
    while len(dev) >= key_ +1:
        dev.pop()
    print(len(dev))
    count = range(0,key_)
    index_ = 0
    for a in count:
        while len(dev[a]) <= length - 1:
            dev[a].append(code_list[index_])
            index_ += 1
    index_ = 0
    code = []
    print(dev)
    while index_ <= len(code_list)/key_ -1:
        code.append([a[index_] for a in dev])
        index_ += 1
    return (''.join(''.join(a) for a in code))
##testbase() is a temporary function to test output
def testbase():
    global asd
    asd = range(27)
    asd.pop(0)
    asd = [26 if (b*12)%26 == 0 else (b*12)%26 for b in asd]
    check_repeat(asd)

