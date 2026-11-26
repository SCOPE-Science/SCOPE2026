"""Exact rational proof-certificate replay for Erlang renewal purity ordering."""
from fractions import Fraction as F
from math import comb

def coefficients(n):
    c=[comb(n,k) for k in range(n+1)]
    c[0]+=1
    for k in range(0,n+1,2):
        c[k//2]-=2*(-1)**(k//2)*comb(n,k)
    for k in range(1,n+1,2):
        c[(k+1)//2]-=n*(-1)**((k-1)//2)*comb(n,k)
    assert c[0]==c[1]==0, (n,c[:2])
    return c[2:]

def shifted(co,a,b):
    # Coefficients of q(a+(b-a)t) in increasing powers of t.
    d=len(co)-1
    return [sum(F(co[j])*comb(j,k)*a**(j-k)*(b-a)**k for j in range(k,d+1)) for k in range(d+1)]

def bernstein(co,a,b):
    d=len(co)-1
    u=shifted(co,a,b)
    return [sum(u[j]*F(comb(k,j),comb(d,j)) for j in range(k+1)) for k in range(d+1)]

def tail(co,a):
    d=len(co)-1
    return [sum(F(co[j])*comb(j,k)*a**(j-k) for j in range(k,d+1)) for k in range(d+1)]

checks=0
assert coefficients(1)==[]
for n in range(2,14):
    c=coefficients(n)
    cutoff=F(1,2) if n<=6 or n>=12 else F(1)
    quarters=int(4*cutoff)
    for i in range(quarters):
        b=bernstein(c,F(i,4),F(i+1,4))
        assert len(b)==n-1
        assert all(x>0 for x in b), ('bernstein',n,i,b)
        checks+=len(b)
    shifted_tail=tail(c,cutoff)
    assert all(x>0 for x in shifted_tail), ('tail',n,shifted_tail)
    checks+=len(shifted_tail)
    assert c[-1]==1

# The sharp onset n=14 has an exact negative test frequency squared y=1/3.
y=F(1,3)
co14=coefficients(14)
assert co14==[3185,-21658,43043,-24024,7917,3238,3003,2002,1001,364,91,14,1]
q=sum(F(c)*y**i for i,c in enumerate(co14))
assert q==F(-13436039,531441)
D=y*q/(14*14*(1+y)**14)
assert D==F(-40308117,52613349376)
# For the symmetric 2-level pure reset vector, the P-O difference is D/2.
assert D/2==F(-40308117,105226698752)
# Exact positive witnesses at small/large frequencies indicate a sign reversal,
# rather than universally reversed ordering at n=14.
assert co14[0]>0 and co14[-1]>0

# Independent check of polynomial numerator via Gaussian integer arithmetic.
# For rational z=1/2, exact complex arithmetic avoids floating-point polynomial assembly.
def cmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cdiv(a,b):
    den=b[0]*b[0]+b[1]*b[1]
    return ((a[0]*b[0]+a[1]*b[1])/den,(a[1]*b[0]-a[0]*b[1])/den)
for n in range(1,15):
    for z in [F(1,2),F(3,4),F(1)]:
        q=(F(1),F(0))
        for _ in range(n):q=cmul(q,(F(1),-z))
        q=cdiv((F(1),F(0)),q) # (1+i*z)^(-n)
        amp=cdiv((q[0]-1,q[1]),(F(0),n*z))
        direct=amp[0]**2+amp[1]**2-amp[0]
        expected=F(0) if n==1 else z*z*sum(F(c)*(z*z)**i for i,c in enumerate(coefficients(n)))/(n*n*(1+z*z)**n)
        assert direct==expected, ('complex comparison',n,z,direct,expected)
        checks+=1
print('PASS exact Bernstein-positive intervals, positive shifted tails, onset witness, and complex-transform checks:',checks)
