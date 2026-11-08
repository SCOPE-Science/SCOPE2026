#!/usr/bin/env python3
"""Exact modular checks for classical Lucas numbers at the prime seven."""
from collections import Counter

def lucas_residues(mod, length):
    a,b=2 % mod,1 % mod
    ans=[]
    for _ in range(length):
        ans.append(a)
        a,b=b,(a+b)%mod
    assert (a,b)==(2%mod,1%mod)
    return Counter(ans)

def square_root_counts(k):
    m=7**k
    return Counter((t*t)%m for t in range(m))

def expected_frequencies(k):
    mod=7**k
    if k==1:
        return Counter([2,1,3,4,0,4,4,1,5,6,4,3,0,3,3,6])
    out=Counter()
    ordinary={0:2,1:2,3:4,4:4,6:2}
    for y in range(mod):
        v=ordinary.get(y%7,0)
        if k>=2 and y%7 in (2,5):
            base=2 if y%7==2 else -2
            factor=2205 if y%7==2 else -2205
            if (y-base)%49 == 0:
                m=7**(k-2)
                inv=pow(factor//49,-1,m) if m>1 else 0
                u=((y-base)//49*inv)%m if m>1 else 0
                count=square_counts[u] if m>1 else 1
                v=7*count
        if v:
            out[y]=v
    return out

for k in range(1,6):
    p=7**k
    T=16*7**(k-1)
    got=lucas_residues(p,T)
    square_counts=square_root_counts(k-2) if k>=2 else Counter()
    exp=expected_frequencies(k)
    assert got==exp,(k, list((got-exp).items())[:3],list((exp-got).items())[:3])
    assert sum(got.values())==T
    # A proper period divisor would have a smaller period; check each prime divisor of T.
    divisors=[2,7]
    vals=[]
    a,b=2%p,1%p
    for _ in range(T):
        vals.append(a)
        a,b=b,(a+b)%p
    for q in divisors:
        if T%q==0:
            s=T//q
            assert any(vals[i]!=vals[(i+s)%T] for i in range(T))
    print('level',k,'modulus',p,'period',T,'residues',len(got),'hist',dict(sorted(Counter(got.values()).items())))
# exact Pell/Lucas Binet checks on the matrix (no floating point)
# (alpha^16+beta^16)=2207 and (alpha^16-beta^16)/sqrt5=987
def integer_recurrence(a,b,n):
    for _ in range(n):
        a,b=b,a+b
    return a
assert integer_recurrence(2,1,16)==2207
assert integer_recurrence(0,1,16)==987
assert integer_recurrence(2,1,8)==47
assert 2207-2==2205==45*49
assert 987%7==0 and 987%49!=0
assert 21%7==0 and 21%49!=0
print('VERIFY_OK levels=1..5 exact_individual_residues=19607 least_periods=PASS')
