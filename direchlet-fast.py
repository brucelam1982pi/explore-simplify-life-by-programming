import math
from operator import itemgetter

# -*- coding: utf-8 -*-
# This code is freely use by anyone. 本代碼可自由使用。
# author: BruceLam
# bug report email: brucelam1982pi@gmail.com

def getFraction(real_number):
    '''
    int(real_number) is the integer part of real_number
    return: fraction part of real_number
    '''
    return real_number - int(real_number)

def make_list(r, n):
    '''
    make list of tuple (i, fraction-part-of(i * real-number r)),
    integer i: 0 <= i < (n+1), name the list fractions, sort it by fraction-part
    from small to large, return the sorted list.
    '''
    fractions = []
    for i in range(0, n+1):
        data = (i, getFraction(i * r))
        fractions.append(data)
        #print(fractions) #delete first # for testing

    #sort the list by fraction-part b(from small to large in tuble (a, b)
    #by using key=itemgetter(1)
    fractions = sorted(fractions, key=itemgetter(1))
    #print(fractions)
    return fractions

#binary search the target, fast than search all combinations
def getApproximations(fractions, r, n):
    '''
    fractions: sorted list by calling make_list
    r: real_number, n: integer >= 100 for meaningful result
    return: tuple (start index i, end index j) of list fractions such that
    absolute value of ( fraction part of (j*r) - fraction part of (i*r) ) is
    less than 1.0/n
    '''
    integers_to_approximate = set()
    for i in range(0, n):#i is the index of sorted list fractions
        fraction_i = fractions[i][1]
        fraction_i_plus_1 = fractions[i+1][1]
        #diff: absolute value of diffence
        diff = abs(fraction_i - fraction_i_plus_1)
        allowed_error = 1.0/n
        if diff < allowed_error:
            '''
            binary search the end index named middle in the next while loop.
            Use the index middle of list fractions to extract original index
            in the tuple (index, fraction_part_of(index * real number r))

            index i, low, middle, high help us to narrow the range including
            the target tuple, what we want is the original index in the
            target tuple
            '''
            low = i
            high = n
            while low < high:
                middle = int((low + high) / 2)
                if abs(fractions[middle][1] - fraction_i) < allowed_error and\
                   abs(fractions[middle+1][1] - fraction_i) > allowed_error:
                    j_in_formula = fractions[i][0]
                    i_in_formula = fractions[middle][0]
                    #print(j_in_formula, i_in_formula)
                    a = j_in_formula - i_in_formula
                    b = int(j_in_formula * r) - int(i_in_formula * r)
                    integers_to_approximate.add( (a, b) )
                if abs(fractions[middle][1] - fraction_i) >= allowed_error:
                    #end index of fractions in the lower half
                    high = middle - 1
                else:
                    #end index of fractions in the higher half
                    low = middle + 1
    
    #convert integers_to_approximate from set to list, then
    #sort the list by integer a in tuble (a, b) using key=itemgetter(0) 
    return sorted(list(integers_to_approximate), key=itemgetter(0))

def verify():
    '''Reader can try following more acurate pi value, please change %.15f 
    in for loop accordingly.
    3.141592653589793238462643383279502884197169399
    3.14159265358979323846264338327950288419716939937510582097494459230781640628620899
    '''
    #r: a real number
    r = 3.141592653589793
    #r = math.pi
    #r = math.e
    n = 10000
    fractions = make_list(r, n)
    pairs_of_integers = getApproximations(fractions, r, n)
    for a_pair in pairs_of_integers:
        a = a_pair[0]
        b = a_pair[1]
        approximate = b / a
 
        print("actual value: \n%.15f" % r)
        print("approximate value %d/%d:\n%.15f" % (b, a, approximate))
        
        actual_error = abs(r - approximate)
        print("actual_error: \n%.15f" % actual_error)

        #theoretically, |a*r-b| < (1/n) -> |r-b/a|< (1.0/(a*n))
        theoretical_error = 1.0 / (a * n)
        print("theoretical_error: \n%.15f\n" % theoretical_error)
        print('-'*35)
        
if __name__ == '__main__':
    verify()
