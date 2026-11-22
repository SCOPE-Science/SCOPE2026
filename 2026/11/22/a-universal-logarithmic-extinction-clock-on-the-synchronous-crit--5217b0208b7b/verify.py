"""Exact jet identities and finite diagnostics for a critical rational delay recurrence.

No third-party dependencies. Finite diagnostics supplement, rather than prove,
the infinite-orbit asymptotic proved in the accompanying mathematical note.
"""
from fractions import Fraction as F
from math import log, sqrt

N=12

def add(a,b): return [x+y for x,y in zip(a,b)]
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0) for _ in range(N)]
    for i,x in enumerate(a):
        for j,y in enumerate(b[:N-i]): c[i+j]+=x*y
    return c

def inv(a):
    assert a[0]
    z=[F(0) for _ in range(N)]
    z[0]=1/a[0]
    for k in range(1,N): z[k]=-sum(a[j]*z[k-j] for j in range(1,k+1))/a[0]
    return z

def pow_p(a,n):
    o=[F(1)]+[F(0)]*(N-1)
    for _ in range(n):o=mul(o,a)
    return o

def poly(m):
    out=[F(0)]*N
    for k,v in m.items():out[k]=F(v)
    return out

x=poly({1:1});one=poly({0:1})
f=poly({1:1,3:F(-1,3),5:F(1,9)})
f_of_f=add(sub(f,[F(c,3) for c in pow_p(f,3)]),[F(c,9) for c in pow_p(f,5)])
R=mul(add(f,x),inv(add(poly({0:2}),mul(x,f))))
jet=sub(R,f_of_f)
assert all(jet[j]==0 for j in range(7))
assert jet[7]==F(-1,27) and jet[8]==0 and jet[9]==F(13,162)

# Inverse-square increment for an exact odd polynomial step.
v=poly({1:1})
g=poly({0:1,1:F(-1,3),2:F(1,9)})
inverse_square=sub(pow_p(inv(g),2),one)
assert inverse_square[1]==F(2,3)
assert inverse_square[2]==F(1,9)
print('EXACT: R(f(t),t)-f(f(t)) = -t^7/27 + 13t^9/162 + O(t^11)')
print('EXACT: (1-t/3+t^2/9)^(-2)-1 = 2t/3+t^2/9+O(t^3)')

for a,b in [(1.,1.),(1.5,.5),(.01,.025),(3.,7.)]:
    prior,current=a,b
    saved={}
    for n in range(1,1000001):
        prior,current=current,(current+prior)/(2+current*prior)
        if n in (100000,1000000):
            saved[n]=(1/current**2-F(2,3)*n-log(n)/6, current*sqrt(n), (current-prior)*n**1.5)
    C100k,_,_=saved[100000]
    C1m,amplitude,lag=saved[1000000]
    assert abs(amplitude-sqrt(1.5))<.005
    assert abs(lag+sqrt(3/8))<.005
    assert abs(C1m-C100k)<.05
    print('DIAGNOSTIC start=',a,b,'C(1e5)=',float(C100k), 'C(1e6)=',float(C1m),'sqrt(n)u=',amplitude,'n^(3/2)gap=',lag)
print('All exact jet checks and finite diagnostics passed.')
