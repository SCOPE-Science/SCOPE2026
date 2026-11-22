"""Finite, exact checks for bounded-block equivalence tuple orbits.
Run with Python 3, standard library only. This verifies samples, not the infinite theorem.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

def trunc_mul(a,b,d):
    out=[F(0)]*(d+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b[:d+1-i]): out[i+j]+=x*y
    return out

def exponential_kernel(q,d):
    # exp(sum_{j=1}^q z^j/j!) via F'=F*G'
    a=[F(0)]*(d+1); a[0]=F(1)
    for n in range(1,d+1):
        a[n]=sum(F(1,factorial(j-1))*a[n-j] for j in range(1,min(q,n)+1))/n
    return a

def series(q,caps,d):
    a=exponential_kernel(q,d)
    for cap in caps:
        e=[F(1,factorial(k)) if k<=cap else F(0) for k in range(d+1)]
        a=trunc_mul(a,e,d)
    return [factorial(r)*a[r] for r in range(d+1)]

def independent_type_count(q,caps,r):
    # Each named old class is fixed. New unnamed classes are first-appearance-indexed.
    nold=len(caps); total=0
    def rec(i,old_counts,new_counts):
        nonlocal total
        if i==r:
            total+=1
            return
        for j in range(nold):
            if old_counts[j]<caps[j]:
                old_counts[j]+=1; rec(i+1,old_counts,new_counts); old_counts[j]-=1
        for j in range(len(new_counts)):
            if new_counts[j]<q:
                new_counts[j]+=1; rec(i+1,old_counts,new_counts); new_counts[j]-=1
        new_counts.append(1); rec(i+1,old_counts,new_counts); new_counts.pop()
    rec(0,[0]*nold,[])
    return total

def log_coeff(a,d):
    out=[F(0)]*(d+1)
    for n in range(1,d+1):
        out[n]=a[n]-sum(F(k,n)*out[k]*a[n-k] for k in range(1,n))
    return out

def recover(q,T):
    d=q-1
    a=[F(T[r],factorial(r)) for r in range(d+1)]
    h=log_coeff(a,d)
    for k in range(1,d+1):h[k]-=F(1,factorial(k))
    N=h[1]
    recovered={}
    for k in range(2,q):
        known=F(0)
        for cap in range(1,k-1):
            e=[F(1,factorial(j)) if j<=cap else F(0) for j in range(k+1)]
            known+=recovered[cap]*log_coeff(e,k)[k]
        recovered[k-1]=(h[k]-known)*(-factorial(k))
    if q>=2:recovered[q-1]=N-sum(recovered.values())
    assert all(z.denominator==1 for z in recovered.values())
    return [int(recovered[c]) for c in range(1,q)]

checks=0; inversion_checks=0
for q in range(2,7):
    caps_profiles=[[]]
    for n in range(1,4):caps_profiles.extend(product(range(1,q),repeat=n))
    for caps in caps_profiles:
        d=min(6,q+1)
        T=series(q,caps,d)
        for r in range(d+1):
            B=independent_type_count(q,caps,r)
            assert T[r]==B,(q,caps,r,T[r],B)
            checks+=1
        inv=recover(q,series(q,caps,q-1))
        assert inv==[caps.count(c) for c in range(1,q)],(q,caps,inv)
        inversion_checks+=1
    a=[q-1]*q # q singly represented classes
    b=[q-2]*q # q doubly represented classes; cap 0 means a full class
    assert series(q,a,q-2)==series(q,b,q-2)
    assert series(q,a,q-1)[-1]-series(q,b,q-1)[-1]==q
print('DIRECT_ORBIT_CHECKS_PASS',checks)
print('INVERSE_RECOVERY_CHECKS_PASS',inversion_checks)
print('SHARP_SAME_BASE_SIZE_WITNESSES_PASS q=2,3,4,5,6')
