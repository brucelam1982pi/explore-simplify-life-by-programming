import math
from operator import itemgetter

# -*- coding: utf-8 -*-
# This code is freely use by anyone.
# author: BruceLam
# bug report email: brucelam1982pi@gmail.com
# last modify: 2021-09-19

def getFraction(real_number):
    '''
    int(real_number) is the integer part of real_number
    return: fraction part of real_number
    '''
    return real_number - int(real_number)

#go through all combinations
def getApproximations(r, n = 100):
    '''
    r: a real number, n: integer >= 100 for effective approximation
    return: sorted list of tuple (a, b) such that |a*r-b| < (1/n)
    '''
    integers_to_approximate = set()
    for i in range(0, n+1):
        for j in range(i+1, n+1):
            #diff: absolute value of diffence
            diff = abs(getFraction(i * r) - getFraction(j * r))
            if (diff) < 1.0/n:
                #print("i=%d, j=%d" % (i, j))
                a = j - i
                b = int(j * r) - int(i * r)
                integers_to_approximate.add( (a, b) )
                
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
    
    pairs_of_integers = getApproximations(r, n)
    for a_pair in pairs_of_integers:
        a = a_pair[0]
        b = a_pair[1]
        approximate = b / a
        print("actual value: \n%.15f" % r)
        print("approximate value %d/%d:\n%.15f" % (b, a, approximate))
        
        actual_error = abs(r - approximate)
        print("actual_error: \n%.15f" % actual_error)

        theoretical_error = 1.0 / (a * n)
        print("theoretical_error: \n%.15f\n" % theoretical_error)
        print('-'*35)
        
if __name__ == '__main__':
    verify()
