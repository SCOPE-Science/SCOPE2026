"""Exact finite parity checks and numeric diagnostics for two Rademacher local branches."""
from itertools import product
from fractions import Fraction as F
from math import sqrt, log

def moment(a,k):
    signs=list(product((-1,1),repeat=4))
    return sum((sum(a[i,j]*s[i]*s[j] for i in range(4) for j in range(i+1,4)))**k for s in signs)/16

# Unnormalized square coefficients: four edges of a four-cycle all 1.
square={(i,j):F(1) if (i,j) in {(0,1),(1,2),(2,3),(0,3)} else F(0)
        for i in range(4) for j in range(i+1,4)}
full={(i,j):F(1) for i in range(4) for j in range(i+1,4)}
assert moment(square,2)==4 and moment(square,4)==64 and moment(square,6)==1024
assert moment(full,2)==6 and moment(full,4)==168 and moment(full,6)==5856
# The normalized fourth moments are 64/16=4 and 168/36=14/3.
assert moment(square,4)/moment(square,2)**2==4
assert moment(full,4)/moment(full,2)**2==F(14,3)

# Orthogonal parity-block identity for rational coefficients, verified by enumeration.
for q in range(1,45):
    a={(i,j):F(((i+2)*(j+3)+q)%13-6, q+4)
       for i in range(4) for j in range(i+1,4)}
    up=((a[0,1]+a[2,3]),(a[0,2]+a[1,3]),(a[0,3]+a[1,2]))
    um=((a[0,1]-a[2,3]),(a[0,2]-a[1,3]),(a[0,3]-a[1,2]))
    def av(u,k):
        return sum((u[0]*x+u[1]*y+u[2]*z)**k for x,y,z in product((-1,1),repeat=3))/8
    assert moment(a,4) == (av(up,4)+av(um,4))/2

def g(p): return 3**(p-1)-4*p+5
def h(t): return 3*(1.5)**t+6**(-t)-4

def root(f,a,b):
    assert f(a)*f(b)<0
    for _ in range(90):
        c=(a+b)/2
        if f(a)*f(c)<=0: b=c
        else: a=c
    return (a+b)/2
ploc=root(g,2.2,2.6)
pcross=2+2*root(h,.25,.5)
assert 2.34182245<ploc<2.34182246
assert 2.73627732<pcross<2.73627733
assert ploc<2.5<pcross
for p in (2.2,2.3,2.5,2.7,2.8,2.99):
    cflat=p*(4*p-5-3**(p-1))/(3**p+3)
    csquare=p*(p-3)/8
    assert csquare<0
    assert (cflat<0)==(p>ploc)
    m1=2**(p-2)
    m2=(3**p+3)/8*(2/3)**(p/2)
    assert (m1>m2)==(p<pcross)
print('EXACT_16_SIGN_MOMENTS_AND_PARITY_BLOCKS_OK 44')
print('LOCAL_AND_CROSSING_ROOTS_OK %.12f %.12f'%(ploc,pcross))
print('ALL_TWO_LOCAL_BRANCH_CHECKS_OK')
