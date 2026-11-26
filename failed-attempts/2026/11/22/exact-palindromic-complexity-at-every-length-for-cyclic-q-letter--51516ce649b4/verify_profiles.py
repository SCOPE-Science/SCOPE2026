#!/usr/bin/env python3
"""Finite, independent enumeration of palindromic factors of cyclic valuation words."""

def val(n):
    assert n>0
    return (n & -n).bit_length()-1

def prediction(q,n):
    if n==1: return q
    if n%2==0: return int(n==2)
    h=(n-1)//2
    k=h.bit_length()-1
    return q+1+int(k>=1 and h<3*(1<<(k-1)))

def pal_occurrences(q,limit=32768,H=42):
    # Return all palindromic words of odd radii, constructed from each actual center.
    out=[set() for _ in range(H+1)]
    for c in range(H+2, limit-H):
        center=str(val(c)%q)
        out[0].add(center)
        acc=center
        for h in range(1,H+1):
            left=val(c-h)%q
            right=val(c+h)%q
            if left!=right: break
            acc=str(left)+acc+str(right)
            out[h].add(acc)
    return out

if __name__=='__main__':
    checked=0
    for q in range(3,9):
        H=31 # for this range, all required center witnesses lie within 32768
        out=pal_occurrences(q,32768,H)
        for h in range(H+1):
            n=2*h+1
            got=len(out[h]); want=prediction(q,n)
            assert got==want,(q,n,got,want)
            checked+=1
        # Separate even-palindrome check on an actual finite prefix.
        s=''.join(str(val(j)%q) for j in range(1,32769))
        for n in range(2,66,2):
            found=set()
            for j in range(len(s)-n+1):
                w=s[j:j+n]
                if w==w[::-1]: found.add(w)
            assert len(found)==prediction(q,n),(q,n,found)
            checked+=1
    print('PASS',checked,'length-alphabet checks, actual centers and even factors')
