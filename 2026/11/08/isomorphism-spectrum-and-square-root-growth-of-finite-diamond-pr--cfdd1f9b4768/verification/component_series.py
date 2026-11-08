"""Unlabelled functional-component Euler-transform verifier (stdlib)."""
from fractions import Fraction
from math import comb, gcd

N=12

def conv(a,b):
    z=[Fraction(0)]*(N+1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b[:N+1-i]):
            if y:z[i+j]+=x*y
    return z

def power(a,n):
    z=[Fraction(1)]+[Fraction(0)]*N
    for _ in range(n):z=conv(z,a)
    return z

def tot(n):return sum(1 for k in range(1,n+1) if gcd(k,n)==1)

# The standard rooted-unlabeled-tree recurrence from T=z exp(sum_{r>=1}T(z^r)/r).
t=[0]*(N+1);t[1]=1
for n in range(2,N+1):
    t[n]=sum(t[n-j]*sum(d*t[d] for d in range(1,j+1) if j%d==0) for j in range(1,n))//(n-1)
T=list(map(Fraction,t))
cycle=[Fraction(0)]*(N+1)
for ell in range(2,N+1):
    for d in range(1,ell+1):
        if ell%d:continue
        Td=[Fraction(0)]*(N+1)
        for k in range(1,N//d+1): Td[k*d]=T[k]
        P=power(Td,ell//d)
        for j,v in enumerate(P):cycle[j]+=Fraction(tot(d),ell)*v
assert all(v.denominator==1 for v in cycle)
components=[int(4*T[n]+cycle[n]) for n in range(N+1)]
# Euler transform: each of components[n] unlabeled connected types can be used any number of times.
A=[1]+[0]*N
for n in range(1,N+1):
    if components[n]==0:continue
    term=[0]*(N+1)
    for k in range(N//n+1):term[k*n]=comb(components[n]+k-1,k)
    A=[int(v) for v in conv(list(map(Fraction,A)),list(map(Fraction,term)))]
assert A[:11]==[1,4,15,50,161,497,1513,4528,13451,39678,116603],A
print('rooted_tree',t[1:11]);print('cycle_components',cycle[2:11]);print('A_top',A[:11]);
print('unlabeled_total',[(m,A[m]+(m+1)**2) for m in range(2,11)])
print('VERIFY_OK')
