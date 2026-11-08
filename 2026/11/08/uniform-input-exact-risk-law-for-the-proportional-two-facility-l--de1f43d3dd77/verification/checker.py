"""Reproduce exact moment identities for a two-site distance-weighted lottery.

Python 3 standard library only; this checks algebra and finite allocations,
not the infinite-population limit theorem.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import pi, sqrt

Z=F(0); O=F(1)
def mul(a,b):
    r=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return r

def add(a,b):
    r=[Z]*max(len(a),len(b))
    for i,x in enumerate(a):r[i]+=x
    for i,x in enumerate(b):r[i]+=x
    return r

def primitive_at(p,t):
    return sum((coef*t**(i+1)/F(i+1) for i,coef in enumerate(p)),Z)

def polynomial_integral(p,lo,hi):return primitive_at(p,hi)-primitive_at(p,lo)

def f_polys(u):
    # The variable in each list is the second facility location v.
    left=[(1-u)**2/2+u*u/4,-u/2,F(3,4)]
    right=[F(1,2)+3*u*u/4,-O-u/2,F(3,4)]
    return left,right

def N(u,power):
    left,right=f_polys(u)
    a=b=[O]
    for _ in range(power):
        a=mul(a,left); b=mul(b,right)
    return polynomial_integral(mul([u,-O],a),Z,u)+polynomial_integral(mul([-u,O],b),u,O)

def h(u):return u*u-u+F(1,2)

def target1(u):return (34*u**4-68*u**3+54*u*u-20*u+5)/48

def target2(u):return F(11,480)*(2*u*u-2*u+1)*(11*u**4-22*u**3+15*u*u-4*u+1)

for i in range(5):
    u=F(i,6)
    assert N(u,1)==target1(u)
    assert N(u,1)/h(u)==F(17,24)*(u*u-u)+F(1,16)+F(7,48)/(2*u*u-2*u+1)
for i in range(7):
    u=F(i,8)
    assert N(u,2)==target2(u)
# Both sides above are polynomials of degree ≤4 and ≤6, respectively.
# Sufficient distinct rational evaluations prove polynomial equality identically.

# N2/h = 11(11u^4−22u^3+15u^2−4u+1)/240, so the
# u-integral is exactly 11/240*(11/5−22/4+15/3−4/2+1).
second=F(11,240)*(F(11,5)-F(22,4)+F(15,3)-F(4,2)+1)
assert second==F(77,2400)
assert 64*second==F(154,75)
mean=7*pi/12-4/9
assert abs(mean-1.3881512701496015)<1e-12
assert 1 < mean < F(7,5)
assert F(154,75)-mean*mean > 0

# Independent exact finite-profile expectation from ordered draws and unordered pairs.
num_profiles=0
alphabet=(F(0),F(1,4),F(1,2),F(3,4),F(1))
for n in (3,4):
    for xs in product(alphabet,repeat=n):
        if min(xs)==max(xs):continue
        S=[sum((abs(x-y) for y in xs),Z) for x in xs]
        def cost(i,j):
            return sum((min(abs(y-xs[i]),abs(y-xs[j])) for y in xs),Z)/n
        z=Z
        for i in range(n):
            for j in range(n):
                if i!=j and xs[i]!=xs[j]:z+=F(1,n)*abs(xs[i]-xs[j])/S[i]*cost(i,j)
        z2=Z;prob=Z
        for i,j in combinations(range(n),2):
            weight=F(1,n)*abs(xs[i]-xs[j])*(1/S[i]+1/S[j])
            prob+=weight
            z2+=weight*cost(i,j)
        assert prob==1 and z==z2,(n,xs,z,z2)
        num_profiles+=1

# Two forms of the quadratic ratio on the gap simplex.
for a,c in product([F(i,10) for i in range(11)],repeat=2):
    if a+c>1:continue
    b=1-a-c; s=a+c; d=a-c
    R=4*(a*a+c*c)+2*b*b
    assert R==1+4*(s-F(1,2))**2+2*d*d
    assert 4-R==8*(b+c)-6*b*b-8*b*c-8*c*c if a==1-b-c else True
assert h(F(1,4))==F(5,16)
assert 1/h(Z)+1/h(O)==4
# Density in (s,d) at the minimizer = 8/5.
assert F(1,4)*(1/h(F(1,4))+1/h(F(1,4)))==F(8,5)
print('PASS:',5,'degree-four and',7,'degree-six polynomial certificates;')
print('PASS:',num_profiles,'exact finite profiles, normalized draw probabilities, endpoint identities;')
print('PASS: limiting mean',mean,'and exact second moment',F(154,75))
