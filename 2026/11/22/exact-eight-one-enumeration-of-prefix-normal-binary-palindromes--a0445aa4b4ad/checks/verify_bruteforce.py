#!/usr/bin/env python3
"""Independent exhaustive test of the eight-one palindrome enumeration."""
from itertools import combinations

def is_prefix_normal(word):
    n = len(word)
    pref = [0]
    for v in word:
        pref.append(pref[-1] + v)
    for length in range(1,n+1):
        bound = pref[length]
        for start in range(1,n-length+1):
            if pref[start+length]-pref[start] > bound:
                return False
    return True

def formula_coeffs(max_n):
    def denom(parts):
        a=[0]*(max_n+1);a[0]=1
        for p in parts:
            for n in range(p,max_n+1):a[n]+=a[n-p]
        return a
    aa=denom([7,2,2,1]);bb=denom([7,2,3,4])
    return [((aa[n-8] if n>=8 else 0) - (bb[n-10] if n>=10 else 0)) for n in range(max_n+1)]

if __name__ == '__main__':
    N=24
    formula=formula_coeffs(N)
    for n in range(8,N+1):
        h=n//2
        ct=0
        for one_positions in combinations(range(h),4):
            half=[int(i in one_positions) for i in range(h)]
            w=half + ([0] if n%2 else []) + half[::-1]
            ct += is_prefix_normal(w)
        assert ct==formula[n], (n,ct,formula[n])
        print(n,ct)
    print('PASS: exhaustive independent palindrome enumeration, n=8..24')
