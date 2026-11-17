"""Exact symbolic and independent numerical checks for Hermite-window disk concentration."""
from fractions import Fraction
from math import exp, factorial
import sympy as s
from scipy.integrate import quad

A,t=s.symbols('A t', positive=True)
def q(n):
    if n==0:return s.Integer(1)+A
    return sum(A**j/s.factorial(j) for j in range(n)) + A**n*(A-n+1)/s.factorial(n)

for n in range(1,40):
    assert s.simplify(q(n)-q(n-1)-A**(n-1)*(A-n+1)*(A-n)/s.factorial(n)) == 0
for n in range(0,15):
    if n==0:
        v=t*s.exp(-t)
    else:
        v=t**(n-1)*(n-t)**2*s.exp(-t)/s.factorial(n)
    total=s.integrate(v,(t,0,A))
    assert s.simplify(total-(1-s.exp(-A)*q(n))) == 0
for x in [0.125,0.5,0.999,1.0,1.001,1.5,2,2.5,3,8.5]:
    vals=[]
    for n in range(60):
        f=lambda u: exp(-u)*u if n==0 else exp(-u)*u**(n-1)*(n-u)**2/factorial(n)
        vals.append(quad(f,0,x,epsabs=1e-13)[0])
    maxi=max(vals)
    if x<1: assert vals[1]==maxi
    if x>1: assert vals[0]==maxi
    if x==1: assert max(abs(vals[j]-maxi) for j in [0,1,2])<1e-12
    m=int(x)
    for n in range(1,30):
        d=vals[n]-vals[n-1]
        predicted=-(x**(n-1)*(x-n+1)*(x-n)/factorial(n))*exp(-x)
        assert abs(d-predicted)<1e-11
print('HERMITE_DISK_TRIPLE_CROSSING_PASS algebraic_differences=39 integrated_profiles=15 numeric_radii=10')
