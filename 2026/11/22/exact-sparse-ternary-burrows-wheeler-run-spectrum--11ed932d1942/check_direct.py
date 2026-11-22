from collections import Counter
from itertools import product
from math import comb

def run_count(s):
    return 1+sum(a!=b for a,b in zip(s,s[1:]))

def bwt_runs(w):
    rotations=[w[i:]+w[:i] for i in range(len(w))]
    rotations.sort()
    return run_count(''.join(t[-1] for t in rotations))

def count(n):
    result=Counter()
    for a in range(n-2):
        for b in range(n-2-a):
            c=n-3-a-b
            w='1'+'0'*a+'2'+'0'*b+'2'+'0'*c
            result[bwt_runs(w)]+=1
    return result

def expected(n):
    if n==3:return {2:1}
    if n==4:return {3:2,4:1}
    if n==5:return {3:2,4:2,5:2}
    k,j=divmod(n,6)
    three=(1,3,1,2,2,2)[j]
    four=(6*k-2,6*k-3,6*k,6*k,6*k+1,6*k+2)[j]
    five=(11*k-7,11*k-6,11*k-3,11*k-2,11*k,11*k+2)[j]
    six=comb(n-1,2)-three-four-five
    return {r:c for r,c in [(3,three),(4,four),(5,five),(6,six)] if c}

if __name__=='__main__':
    for n in range(3,55):
        actual=count(n)
        assert actual==expected(n),(n,actual,expected(n))
    print('Verified complete direct BWT spectrum for every length 3 through 54 (all compositions).')
    for n in range(3,13):print(n,dict(sorted(count(n).items())))
