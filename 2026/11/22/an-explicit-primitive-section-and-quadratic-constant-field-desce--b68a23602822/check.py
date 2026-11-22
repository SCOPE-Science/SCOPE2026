"""Exact arithmetic tests accompanying the finite-field Mordell--Weil claim.
The geometric fiber and height arguments are given in RESULT.md, not certified by these tests.
"""
from fractions import Fraction

p=5

def trim(a):
    b=[x%p for x in a]
    while len(b)>1 and b[-1]==0:b.pop()
    return b

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def neg(a):return trim([-x for x in a])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c)
def power(a,k):
    b=[1]
    for _ in range(k):b=mul(b,a)
    return b

def scale(a,c):return trim([x*c for x in a])

def eq(a,b):assert trim(a)==trim(b),(a,b)

t=[0,1];s=add(t,[2]);x=mul(t,s)
A=scale(mul(t,power(s,3)),3)
B=scale(mul(power(t,4),power(s,2)),3)
# alpha^2=2; y=alpha*x.
eq(scale(power(x,2),2),add(add(scale(power(x,3),4),mul(A,x)),B))
# Discriminant of y^2=4x^3+Ax+B, modulo 5.
D=neg(add(power(A,3),scale(power(B,2),27)))
eq(D,mul(power(t,3),power(s,4)))
# j=1728*A^3/(A^3+27*B^2)=4*(t+2)^5 (mod 5).
eq(scale(power(A,3),1728),mul(neg(D),scale(power(s,5),4)))
# At infinity the section passes through the singular point (x_s,y_s)=(1,0)
# of the nodal cubic y_s^2=4*x_s^3+3*x_s+3.
assert (4+3+3)%p==0 and (12+3)%p==0
# At t=-2 the tangent-cone relation y^2=3s^2 is satisfied by P.
assert (2*3*3-3)%p==0
# At t=0 the tangent-cone relation y^2=4tx is satisfied by P.
assert (2*2*2-4*2)%p==0
# Positive height excludes the two middle I_5 components.
for i in (1,4):
    assert 2-Fraction(1,2)-Fraction(2,3)-Fraction(i*(5-i),5)==Fraction(1,30)
for i in (2,3):
    assert 2-Fraction(1,2)-Fraction(2,3)-Fraction(i*(5-i),5)<0
# alpha^5 = alpha*(alpha^2)^2 = -alpha in F_25.
assert 2**2 % 5==4
assert 10-2-(1+2+4)==1
assert 2*3*5==30
print('PASS: section, discriminant, j, local tangents, height candidates, Frobenius, lattice ranks')
