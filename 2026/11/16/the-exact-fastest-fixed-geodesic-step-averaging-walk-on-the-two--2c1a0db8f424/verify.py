"""Exact algebra and supplemental finite-degree checks for spherical circle means.

Run: python verify.py. Only Python's standard library is required.
An analytical bound in RESULT.md, not a finite loop, handles all degrees >= 6.
"""
from fractions import Fraction as F
import math

# Store elements u+v*sqrt(6) as rational pairs.
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]+6*z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def sub(z,w): return add(z,(-w[0],-w[1]))
def sc(z,r): return (r*z[0],r*z[1])
def power(z,n):
    t=(F(1),F(0))
    for _ in range(n):t=mul(t,z)
    return t

def calc_legendre(n,z):
    u,v=(F(1),F(0)),z
    if n==0:return u
    if n==1:return v
    for k in range(1,n):
        w=sc(sub(sc(mul(z,v),F(2*k+1)),sc(u,F(k))),F(1,k+1))
        u,v=v,w
    return v

a=(F(-1,5),F(1,5))
rho=(F(2,25),F(3,25))
one=(F(1),F(0))
b=sub(one,power(a,2))
assert calc_legendre(2,a)==sc(rho,F(-1))
assert calc_legendre(3,a)==sc(rho,F(-1))
assert calc_legendre(4,a)==(F(-41,250),F(13,125))
assert calc_legendre(5,a)==(F(2173,6250),F(-3,6250))
B6=add(add(power(a,6),sc(mul(power(a,4),b),F(3,2))),
       add(sc(mul(power(a,2),power(b,2)),F(9,8)),sc(power(b,3),F(5,16))))
assert B6==(F(1262,3125),F(-189,6250))
assert sub(rho,B6)==(F(-2024,6250),F(939,6250))

# Rigorous rational comparison for Q(sqrt6): 2449/1000 < sqrt(6) < 49/20.
lo,hi=F(2449,1000),F(49,20)
assert lo*lo<F(6)<hi*hi
def interval(z):
    return (z[0]+z[1]*(lo if z[1]>=0 else hi),
            z[0]+z[1]*(hi if z[1]>=0 else lo))
def lt(z,w):return interval(sub(w,z))[0]>0
assert lt((F(0),F(0)),a) and lt(a,rho) and lt(rho,(F(1),F(0)))
assert lt(rho,(F(2,5),F(0)))  # stronger than rho < 1/sqrt(5)
assert lt((F(0),F(0)),calc_legendre(4,a)) and lt(calc_legendre(4,a),rho)
assert lt((F(0),F(0)),calc_legendre(5,a)) and lt(calc_legendre(5,a),rho)
assert lt(B6,rho)

# Supplemental numerical recurrence check at 1<=degree<=512, not proof of infinity.
ax=(math.sqrt(6)-1)/5
r=(2+3*math.sqrt(6))/25
v0,v1=1.,ax
n_checks=0
for ell in range(2,513):
    v2=((2*ell-1)*ax*v1-(ell-1)*v0)/ell
    if ell>=4:
        assert abs(v2)<r-1e-10,(ell,v2,r)
        n_checks+=1
    v0,v1=v1,v2
# Sampling checks across theta on both sides of optimal x.
for i in range(1001):
    x=i/1000
    p1=x;p2=(3*x*x-1)/2;p3=x*(5*x*x-3)/2
    if abs(x-ax)>0.002:
        assert max(abs(p1),abs(p2),abs(p3))>r-1e-10
    n_checks+=1
print(f'PASS: exact algebra and rational interval inequalities; {n_checks} finite-degree/grid comparisons;'
      f' a={ax:.15f}, rho={r:.15f}, theta_degrees={math.degrees(math.acos(ax)):.12f}')
