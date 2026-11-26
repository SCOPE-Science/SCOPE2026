#!/usr/bin/env python3
"""Finite exact certificate and independent small tests for the three-bit quotient obstruction.
Run with Python 3.9 or newer; no external dependencies.
"""
from fractions import Fraction

def reverse3(x):
    assert 4 <= x <= 7
    return (x & 1)*4 + (x & 2) + (x & 4)//4

def witnesses(prefix, residue):
    ans=[]
    for scale in (4, 8):
        for bottom in range(4, 8):
            for top in range(4, 8):
                if (residue*reverse3(bottom)-reverse3(top)) % 8: continue
                # Strict overlap of (prefix,prefix+1) with
                # (scale*top/(bottom+1), scale*(top+1)/bottom).
                if scale*top < (prefix+1)*(bottom+1) and prefix*bottom < scale*(top+1):
                    assert max(Fraction(prefix),Fraction(scale*top,bottom+1)) < min(Fraction(prefix+1),Fraction(scale*(top+1),bottom))
                    ans.append((scale,bottom,top))
    return ans

empty={(5,1),(7,3)}
for p in range(4,8):
    for r in (1,3,5,7):
        cand=witnesses(p,r)
        assert (not cand)==((p,r) in empty),(p,r,cand)
        print('PREFIX',p,'RESIDUE',r,'WITNESS',cand[0] if cand else 'NONE','TOTAL',len(cand))

# Explicit exhaustive integer checks for both forbidden syndromes.
for p,r in empty:
    assert not witnesses(p,r)

# A separate literal palindrome implementation, for finite counterexample checks.
def ispal(n):
    s=bin(n)[2:]
    return s == s[::-1]

def forbidden(n):
    bits=bin(n)[2:]
    return (len(bits)>=6 and ((bits[:3]=='101' and bits[-3:]=='001') or
                                (bits[:3]=='111' and bits[-3:]=='011')))

allp=[n for n in range(1,1<<15,2) if ispal(n)]
checks=0
for n in range(1,1<<10,2):
    if not forbidden(n): continue
    for b in allp:
        assert not ispal(n*b),(n,b)
        checks+=1
assert checks>0
print('FINITE_PALINDROME_TESTS',checks)

# Independently count every cylinder in 6..16-bit dyadic shells.
for k in range(3,14):
    t=1<<k
    shell=sum(forbidden(n) for n in range(4*t,8*t))
    assert shell==t//4,(k,shell)
    first=sum(forbidden(n) for n in range(4*t,5*t))
    second=sum(forbidden(n) for n in range(5*t,6*t))
    third=sum(forbidden(n) for n in range(6*t,7*t))
    fourth=sum(forbidden(n) for n in range(7*t,8*t))
    assert (first,second,third,fourth)==(0,t//8,0,t//8)
print('SHELL_COUNTS',11)
print('VERIFIED')
