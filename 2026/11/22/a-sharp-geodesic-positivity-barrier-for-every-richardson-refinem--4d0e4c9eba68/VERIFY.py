"""Exact checks for a Richardson–Euler graph-diffusion distance barrier."""
from fractions import Fraction
from math import comb, factorial
import sympy as sp

def b(r,k):
    return Fraction(comb(r+k-1,k),r**k)
def a(r,k):
    return (r*b(r,k)-1)/Fraction(r-1)
def d(r):
    k=2
    while a(r,k)>=0:
        k+=1
    return k

for r, expected in [(2,4),(3,4),(17,4),(18,5),(109,5),(110,6),(704,6),(705,7)]:
    actual=d(r)
    assert actual==expected,(r,actual,expected)
    assert a(r,actual)<0
    assert all(a(r,j)>=0 for j in range(2,actual))

# Exact coefficient identities and the absence of first-order error.
R=sp.symbols('r',positive=True,integer=True)
for k,expected in [
    (1,1),
    (2,sp.Rational(1,2)),
    (3,(R-2)/(6*R)),
    (4,(R**2-17*R-6)/(24*R**2)),
    (5,(R**3-109*R**2-74*R-24)/(120*R**3)),
]:
    product=sp.prod((R+j)/R for j in range(k))/sp.factorial(k)
    ak=(R*product-1)/(R-1)
    assert sp.cancel(ak-expected)==0,(k,sp.factor(ak-expected))

# Exact five-vertex diffusion and a distance-four witness.
L=sp.zeros(5)
for u in range(4):
    L[u,u]+=1;L[u+1,u+1]+=1
    L[u,u+1]-=1;L[u+1,u]-=1
I=sp.eye(5)
h=sp.Rational(1,100)
H=2*(I+h*L/2).inv()**2-(I+h*L).inv()
assert H[0,4]<0 and all(H[i,j]==H[j,i] for i in range(5) for j in range(5))
assert H*sp.ones(5,1)==sp.ones(5,1)
assert all(H[i,i]>0 for i in range(5))
assert ((2*(I+L/2).inv()**2-(I+L).inv())[0,4])>0
print('Coefficient and boundary checks passed: r=2,3,17,18,109,110,704,705')
print('P5 endpoint, r=2, h=1/100:',H[0,4],float(H[0,4]))
print('P5 endpoint, r=2, h=1:',(2*(I+L/2).inv()**2-(I+L).inv())[0,4])
print('a_3(r=2)=',a(2,3),'a_4(r=2)=',a(2,4))
print('All tests passed.')
