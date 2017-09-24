global code_list #every letter in the code is an element in this
code_list = [a for a in input('please put the code')]

def indexes(lists,elements):
    indexs = []
    while 1:
        try:
            indexs.append(lists.index(elements))
            lists.pop(lists.index(elements))
        except ValueError:
            break
    return indexs

def bilgram(code_number):# input the digitalised code, return score
    score = 0
    count = 0
    while count <= len(code_number) - 2:
        #for 'th'
        if code_number[count] == 20 and code_number[count + 1] == 8:
            score += 1
        #for 'he'
        elif code_number[count] == 8 and code_number[count + 1] == 5:
            score += 1
        count += 1
    
    return score

def code_to_num(code):
    return [ord(a)-96 for a in code]

def num_to_code(num):
    return [chr(a + 96) for a in num]

def shift(code):
    count = 1
    scores = [0]
    while count <= 26:
        scores.append(bilgram([a+count - 26 if a + count >= 27 else a+ count for a in (code_to_num(code))]))
        count += 1
    count = scores.index(max(scores))
    return ''.join(num_to_code([a+count - 26 if a + count >= 27 else a+count for a in (code_to_num(code))]))

def check_repeat(code):
    items = []
    for a in code:
        if a in items == False:
            items.append(a)




def testbase():
    global a
    a = range(27)
    a.pop(0)
    a = [26 if (b*12)%26 == 0 else (b*12)%26 for b in a]
    
