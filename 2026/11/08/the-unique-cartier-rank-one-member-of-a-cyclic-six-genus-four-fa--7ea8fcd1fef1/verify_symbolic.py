#!/usr/bin/env python3
"""Exact polynomial identity checks over F_11; Python 3 standard library only."""
P = 11

def add(*polys):
    z = {}
    for poly in polys:
        for mon, coef in poly.items():
            z[mon] = (z.get(mon, 0) + coef) % P
    return {k:v for k,v in z.items() if v}

def scalar(poly, c):
    return {k:v*c%P for k,v in poly.items() if (v*c)%P}

def mul(u,v):
    z={}
    for x,c in u.items():
        for y,d in v.items():
            k=tuple(i+j for i,j in zip(x,y))
            z[k]=(z.get(k,0)+c*d)%P
    return {k:v for k,v in z.items() if v}

def power(u,n):
    z={tuple(0 for _ in next(iter(u))):1}
    for i in range(n):z=mul(z,u)
    return z

one={(0,0,0):1}; aa={(1,0,0):1}; bb={(0,1,0):1}; tt={(0,0,1):1}
q=add(power(tt,3),power(tt,2),mul(aa,tt),bb)
r=power(q,5)
def coeff(k):return {(i,j):v for (i,j,t),v in r.items() if t==k}
a={(1,0):1}; b={(0,1):1}; one2={(0,0):1}

def term(i,j,c):return {(i,j):c%P}

u1=term(1,4,5)
p5=add(term(5,0,1),term(3,1,-2),term(2,2,-3),term(1,2,-3),term(0,3,-2))
v1=add(term(3,0,-1),term(2,0,-3),term(1,1,5),term(1,0,5),term(0,2,-1),term(0,1,-2))
v2=add(term(3,0,-2),term(2,1,-3),term(2,0,-1),term(1,1,5),term(0,2,-3),term(0,1,5))
u2=add(term(1,0,-2),term(0,1,5),term(0,0,-1))
for k, formula in [(1,u1),(5,p5),(9,v1),(8,v2),(12,u2)]:
    assert coeff(k)==formula,(k,coeff(k),formula)

L=add(term(2,0,1),term(1,0,-3),term(1,1,-3),term(0,1,1),term(0,0,-4))
assert not add(v2,scalar(v1,-3),scalar(mul(a,L),-1))

den=add(one2,term(1,0,-3)); bnum=add(term(2,0,-1),term(1,0,3),term(0,0,4))
def subs_and_clear(which):
    # all monomials in v1, v2 have b-exponent <=2
    t={}
    for (i,j),v in which.items():
        t=add(t,scalar(mul(mul(power(a,i),power(bnum,j)),power(den,2-j)),v))
    return t
rhs1=scalar(power(add(a,term(0,0,-4)),5),2)
rhs2=scalar(power(add(a,term(0,0,-4)),5),-5)
assert subs_and_clear(v1)==rhs1
assert subs_and_clear(v2)==rhs2

# At a=4 the second block can vanish only for b=-2; that point is singular.
def ev(f,A,B):return sum(v*pow(A,i,P)*pow(B,j,P) for (i,j),v in f.items())%P
delta=add(term(2,0,1),term(3,0,-4),term(1,1,18),term(0,2,-27),term(0,1,-4))
assert ev(delta,0,9)!=0 and ev(p5,0,9)==5
assert ev(delta,4,9)==0
for B in range(P):
    assert ev(v1,4,B)==-(B+2)**2 % P
    assert ev(v2,4,B)==-3*(B+2)**2 % P
print('VERIFY_SYMBOLIC_OK; characteristic=11; coefficients=5; elimination=3')
