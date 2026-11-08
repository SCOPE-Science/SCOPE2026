#!/usr/bin/env python3
"""Exact arithmetic checks for the fixed-index Narayana-square classification.
Run: python3 verify.py
Requires only Python 3 standard library; this is corroboration, not an infinite proof.
"""
from math import comb, isqrt


def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return sorted(out)


def square_index_family(c):
    assert c >= 2
    b=c*c
    if b%2==0:
        h=b-1
        vals={ (u+h*h//u+2*h)//4 for u in divisors(h*h) if u<h }
        maximum=b*b//4
    else:
        h=(b-1)//4
        vals={ u+h*h//u+2*h for u in divisors(h*h) if u<h }
        maximum=((b+3)//4)**2
    return b,h,vals,maximum


square_classes=0
square_values=0
for c in range(2,151):
    b,h,values,maximum=square_index_family(c)
    assert len(values)==(len(divisors(h*h))-1)//2
    assert max(values)==maximum
    assert b in values
    assert all(a>=b and isqrt(a*(a-b+1))**2==a*(a-b+1) for a in values)
    if c<=20:
        cap=min(maximum+80,35000)
        found={a for a in range(b,cap+1)
               if isqrt(a*(a-b+1))**2 == a*(a-b+1)}
        assert found=={a for a in values if a<=cap}
    if c<=6:
        for a in values:
            N=comb(a,b)*comb(a,b-1)//a
            assert N*a==comb(a,b)*comb(a,b-1)
            assert isqrt(N)**2==N
    square_classes+=1
    square_values+=len(values)

assert square_index_family(2)[2] == {4}
assert square_index_family(3)[2] == {9}
assert square_index_family(4)[2] == {16,20,27,64}
assert square_index_family(5)[2] == {25,27,32,49}

# Pell construction for nonsquare indices: directly check three successive even powers.
pell_checks=0
for d in (2,3,5,6,7,10,11,13,17,19,21,29):
    assert isqrt(d)**2!=d
    Y=1
    while True:
        X=isqrt(1+d*Y*Y)
        if X*X-d*Y*Y==1:break
        Y+=1
        assert Y<=200000
    # Square the fundamental unit to make the Y-coordinate even.
    X,Y=X*X+d*Y*Y,2*X*Y
    assert X%2==1 and Y%2==0 and X*X-d*Y*Y==1
    for s in (1,2,3):
        b=d*s*s
        XX,YY=1,0
        previous=0
        for _ in range(3):
            XX,YY=XX*X+d*YY*Y,XX*Y+YY*X
            a=(b-1)*(XX+1)//2
            assert a>b and a>previous
            assert (b-1)*(XX+1)%2==0
            z=a*b*(a-b+1)
            assert isqrt(z)**2==z
            previous=a
            pell_checks+=1

print(f'VERIFY_OK square_indices={square_classes} exact_divisor_families={square_values} ' 
      f'direct_scans_c=2..20 exact_binomial_c=2..6 nonsquare_Pell_witnesses={pell_checks} ' 
      'square_b4_b9_only_trivial=PASS all_comparisons_integer=PASS')
