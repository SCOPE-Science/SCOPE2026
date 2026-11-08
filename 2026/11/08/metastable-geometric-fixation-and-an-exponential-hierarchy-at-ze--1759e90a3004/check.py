"""Exact occupancy-chain checks for the survivor-only voting process.
Run: python3 check.py
Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial

checks = 0

def verify(condition, label):
    global checks
    assert condition, label
    checks += 1

def stirling2(n, k):
    arr = [[0]*(k+1) for _ in range(n+1)]
    arr[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            arr[i][j] = arr[i-1][j-1] + j*arr[i-1][j]
    return arr[n][k]

def row(n,k):
    return [Fraction(comb(k,j)*factorial(j)*stirling2(n,j),k**n)
            for j in range(k+1)]

def exact(n):
    H=[Fraction(0) for _ in range(n+1)]
    U=[Fraction(0) for _ in range(n+1)]
    E=[Fraction(0) for _ in range(n+1)]
    H[1] = Fraction(1)
    E[2] = Fraction(2**(n-1))
    for k in range(3,n+1):
        p=row(n,k)
        den=1-p[k]
        H[k]=(p[1]+sum((p[j]*H[j] for j in range(3,k)),Fraction(0)))/den
        U[k]=(1+sum((p[j]*U[j] for j in range(3,k)),Fraction(0)))/den
        E[k]=U[k]+(1-H[k])*E[2]
    return H,U,E

for n in range(3,11):
    H,U,E=exact(n)
    q=Fraction(1,2**(n-1))
    for k in range(2,n+1):
        p=row(n,k)
        verify(sum(p)==1,('stochastic',n,k))
        verify(p[0]==0,('no-empty',n,k))
        verify(p[1]==Fraction(k,k**n),('one',n,k))
        if k>=3:
            verify(p[2]==Fraction(comb(k,2)*(2**n-2),k**n),('two',n,k))
            verify(H[k] <= Fraction(1,2**n-1),('skip-bound',n,k))
            verify(U[k] <= sum((Fraction(j,j-1)**n for j in range(3,k+1)),Fraction(0)),('prebound',n,k))
            verify(E[k] == U[k]+(1-H[k])/q,('renewal',n,k))
            verify(abs(E[k]-1/q)<=U[k]+H[k]/q,('mean-bound',n,k))
        else:
            verify(E[k]==1/q,('geom',n,k))
    verify(H[n]>=0,('skip-nonnegative',n))
    verify(U[n] <= (n-2)*Fraction(3,2)**n,('uniform-mean',n))

# Independent combinatorial enumeration of n ordered ballot choices into k active candidates.
for n in range(3,7):
    for k in range(2,n+1):
        counts=[0]*(k+1)
        for votes in product(range(k),repeat=n):
            counts[len(set(votes))]+=1
        p=row(n,k)
        for j in range(1,k+1):
            verify(Fraction(counts[j],k**n)==p[j],('surjection-enumeration',n,k,j))

# Direct finite-horizon absorption distribution vs independent recursion of transition matrix.
for n in range(3,8):
    rows={k:[float(t) for t in row(n,k)] for k in range(2,n+1)}
    survival={k:1. for k in range(2,n+1)}
    # t=0 survival one; at each step use backward recurrence
    for t in range(1,201):
        new={k:sum(rows[k][j]*survival[j] for j in range(2,k+1)) for k in range(2,n+1)}
        survival=new
        verify(all(0<=v<=1+1e-12 for v in survival.values()),('survival-prob',n,t))
        verify(abs(survival[2]-(1-2**(1-n))**t)<2e-11,('two-support-tail',n,t))

# Independent visit-probability decomposition, using only support-chain transitions.
for n in range(3,16):
    H,U,E=exact(n)
    rows={k: row(n,k) for k in range(2,n+1)}
    total=Fraction(0)
    for target in range(2,n+1):
        hit={k:Fraction(0) for k in range(1,target)}
        hit[target]=Fraction(1)
        for k in range(target+1,n+1):
            pp=rows[k]
            hit[k]=sum((pp[j]*hit[j] for j in range(target,k)),Fraction(0))/(1-pp[k])
        hold=1/(1-rows[target][target])
        verify(0<=hit[n]<=1,('hitting-range',n,target))
        total+=hit[n]*hold
    verify(total==E[n],('occupation-decomposition',n))

print('PASS',checks,'exact and finite-horizon assertions')
for n in (3,4,6,8,10):
    H,U,E=exact(n)
    print('n=',n,'E_n=',float(E[n]),'E_n / 2^(n-1)=',float(E[n])/2**(n-1),
          'skip2=',float(H[n]))
