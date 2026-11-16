#!/usr/bin/env python3
"""Exact and numerical checks for spin-2, degree-3 symmetric polar-cap localization.

Only Python standard library is required. All polynomials have rational coefficients;
finite sampling is not used as a substitute for the global gap-sign proof.
"""
from fractions import Fraction as F
from math import factorial, cos, pi, isclose


def poly(v):
    return [F(t) for t in v]

def add(a,b):
    return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]

def scale(a,s):
    return [F(s)*t for t in a]

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def power(a,k):
    r=poly([1])
    for _ in range(k):r=mul(r,a)
    return r

def equal(a,b):
    n=max(len(a),len(b))
    return all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0) for i in range(n))

def at(a,x):
    return sum(v*x**i for i,v in enumerate(a))

def primitive_even_cap_density(v):
    # K(c)=(7/2)*[ int_c^1 v(x)dx + int_-1^-c v(x) dx ]
    z=poly([1])
    for i,x in enumerate(v):
        if i%2==0:z=add(z,poly([0]*(i+1)+[-7*x/F(i+1)]))
    return z

x=poly([0,1]); p=scale(add(poly([1]),x),F(1,2)); q=scale(add(poly([1]),scale(x,-1)),F(1,2))
# Squared Wigner small-d entries |d^3_{m,-2}|^2, in p=(1+x)/2 and q=(1-x)/2.
# Their spin-harmonic normalization is 7/(4*pi) and dx-integral is 2/7.
dens={
 0:scale(mul(power(add(x,poly([-1])),2),mul(power(add(x,poly([1])),2),power(x,2))),F(15,8)),
 1:scale(mul(power(add(scale(p,2),scale(q,-1)),2),mul(power(q,3),p)),10),
 2:mul(power(add(scale(p,5),scale(q,-1)),2),power(q,4)),
 3:scale(mul(power(q,5),p),6),
 -1:scale(mul(power(add(p,scale(q,-2)),2),mul(q,power(p,3))),10),
 -2:mul(power(add(p,scale(q,-5)),2),power(p,4)),
 -3:scale(mul(q,power(p,5)),6)
}
for m,v in dens.items():
    assert at(v,1) >= 0
    assert equal(scale([sum(v[i]/F(i+1) for i in range(0,len(v),2))],2),poly([F(2,7)])),m

L={m:primitive_even_cap_density(dens[m]) for m in dens}
for m in range(1,4):assert equal(L[m],L[-m]),m
expected={
 0: poly([1,0,0,F(-35,8),0,F(21,4),0,F(-15,8)]),
 1: poly([1,F(-35,32),0,F(35,32),0,F(-77,32),0,F(45,32)]),
 2: poly([1,F(-7,4),0,F(35,16),0,F(-7,8),0,F(-9,16)]),
 3: poly([1,F(-21,32),0,F(-35,32),0,F(21,32),0,F(3,32)])
}
for m in range(4):assert equal(L[m],expected[m]),m
assert equal(add(add(L[0],scale(L[1],2)),add(scale(L[2],2),scale(L[3],2))),poly([7,-7]))
assert all(at(L[m],F(0))==1 and at(L[m],F(1))==0 for m in range(4))

r=add(poly([1]),scale(power(x,2),-1))
gap_expected={
 (0,1):scale(mul(mul(x,power(r,2)),add(poly([1]),scale(power(x,2),-3))),F(35,32)),
 (0,3):scale(mul(mul(x,power(r,2)),add(poly([1]),scale(power(x,2),-3))),F(21,32)),
 (1,3):scale(mul(mul(x,power(r,2)),add(poly([1]),scale(power(x,2),-3))),F(-7,16)),
 (0,2):scale(mul(mul(x,r),add(add(poly([4]),scale(power(x,2),-11)),scale(power(x,4),3))),F(7,16)),
 (1,2):scale(mul(mul(x,r),add(add(poly([-3]),scale(power(x,2),2)),scale(power(x,4),9))),F(-7,32)),
 (2,3):scale(mul(mul(x,r),add(add(poly([-5]),scale(power(x,2),10)),scale(power(x,4),3))),F(7,32))
}
for (i,j),e in gap_expected.items():assert equal(add(L[i],scale(L[j],-1)),e),(i,j)

# Independently reconstruct a Wigner d entry via the finite factorial sum
# (j=3, m'=-2); signs depend on convention but squared entries do not.
def d_wigner(j,m,mp,theta):
    import math
    u=math.cos(theta/2);v=math.sin(theta/2)
    z=0.
    pref=math.sqrt(factorial(j+m)*factorial(j-m)*factorial(j+mp)*factorial(j-mp))
    for k in range(max(0,m-mp),min(j+m,j-mp)+1):
        den=factorial(j+m-k)*factorial(k)*factorial(mp-m+k)*factorial(j-mp-k)
        z+=((-1)**(k-m+mp))*pref/den*u**(2*j+m-mp-2*k)*v**(mp-m+2*k)
    return z

for m in range(-3,4):
    for xx in [-.91,-.5,-.12,.0,.14,.73,.92]:
        # Orthogonal Wigner d columns: choose same m,m' convention.
        z=d_wigner(3,m,-2,__import__('math').acos(xx))**2
        assert isclose(z,float(at(dens[m],xx)),rel_tol=3e-11,abs_tol=5e-12),(m,xx,z,float(at(dens[m],xx)))

# Exact sign checks at rational cutoffs in each of the three sharp top phases.
for c,top,bottom in [(F(1,4),0,2),(F(3,5),1,2),(F(2,3),1,0),(F(3,4),2,0),(F(9,10),2,0)]:
    vals={m:at(L[m],c) for m in range(4)}
    assert vals[top]==max(vals.values()),(c,vals)
    assert vals[bottom]==min(vals.values()),(c,vals)

# Endpoint sharp stability scaling: leading coefficients in delta=1-c.
# Taylor at c=1: lambda0 has order 3; lambda2 has order 1.
assert sum(F(i*(i-1))*L[0][i] for i in range(2,len(L[0])))==0
assert sum(F(i)*L[0][i] for i in range(1,len(L[0])))==0
assert sum(F(i*(i-1)*(i-2))*L[0][i] for i in range(3,len(L[0])))==F(-105)
assert sum(F(i)*L[2][i] for i in range(1,len(L[2])))==F(-7,2)
print('SPIN2_DEGREE3_EXACT_CAP_SPECTRUM_AND_GAPS_PASS')
