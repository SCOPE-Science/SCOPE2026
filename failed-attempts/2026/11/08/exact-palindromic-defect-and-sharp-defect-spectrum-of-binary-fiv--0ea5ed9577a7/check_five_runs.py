#!/usr/bin/env python3
"""Independent exhaustive checks for the five-run palindromic-defect theorem."""
from itertools import product

def palindromes(w):
    ans=set()
    for center in range(2*len(w)-1):
        left=center//2
        right=(center+1)//2
        while left>=0 and right<len(w) and w[left]==w[right]:
            ans.add(w[left:right+1])
            left-=1
            right+=1
    return ans

def predicted(a,b,c,d,e):
    return (max(0,min(a,e)-c) if b!=d else 0)

def predicted_palindromes(a,b,c,d,e):
    result={'0'*t for t in range(1,max(a,c,e)+1)}
    result.update({'1'*t for t in range(1,max(b,d)+1)})
    for size in range(1,min(a,c)+1):
        result.add('0'*size+'1'*b+'0'*size)
    for size in range(1,min(c,e)+1):
        result.add('0'*size+'1'*d+'0'*size)
    for size in range(1,min(b,d)+1):
        result.add('1'*size+'0'*c+'1'*size)
    if b==d:
        for size in range(1,min(a,e)+1):
            result.add('0'*size+'1'*b+'0'*c+'1'*d+'0'*size)
    return result

def check():
    count=0
    for a,b,c,d,e in product(range(1,7),repeat=5):
        w='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
        got=palindromes(w)
        assert got==predicted_palindromes(a,b,c,d,e), (a,b,c,d,e,'factor set')
        assert len(w)-len(got)==predicted(a,b,c,d,e), (a,b,c,d,e,'defect')
        count+=1
    spectrum_count=0
    for n in range(5,31):
        got=set()
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e=n-a-b-c-d
                        got.add(predicted(a,b,c,d,e))
        assert got==set(range(max(0,(n-6)//2)+1)),(n,got)
        spectrum_count+=1
    print(f'PASS: {count} independent palindrome-set comparisons, {count} defect comparisons, {spectrum_count} lengthwise spectra (n=5..30).')
if __name__=='__main__':check()
