"""Exact symbolic and rational checks for the NB + Bernoulli moment region.

Run: python3 moment_region_check.py
The mathematical proof is in RESULT.md; finite checks alone do not prove it.
"""
from fractions import Fraction as F
import sympy as s

p,a,r,m,v = s.symbols('p a r m v', positive=True)
z=s.symbols('z')
k=s.log(1+p*z)-r*s.log(1-a*z)
expected = [p+r*a, -p**2+r*a**2, 2*(p**3+r*a**3)]
for j,c in enumerate(expected,1):
    assert s.simplify(s.diff(k,z,j).subs(z,0)-c)==0

A=m-p
B=v+p**2
inverse_a=B/A
inverse_r=A**2/B
assert s.simplify((inverse_r*inverse_a+p)-m)==0
assert s.simplify((inverse_r*inverse_a**2-p**2)-v)==0
t=B**2/A+p**3
assert s.simplify(inverse_r*inverse_a**3+p**3-t)==0
prime=s.diff(t,p)
assert s.simplify(prime - (B*(B+4*p*A)/A**2+3*p**2))==0

# Rational example: first two factorial cumulants agree with Binomial(2,1/4).
q=F(1,4); pm=F(2,5); shape=F(2,7); theta=F(7,27)
odds=theta/(1-theta)
assert pm+shape*odds==F(1,2)
assert shape*odds**2-pm**2==-F(1,8)
assert 2*(shape*odds**3+pm**3)==F(61,400)
assert 2*2*q**3==F(1,16)

# Reconstruct shape, odds and the third cumulant for a grid of exact rational values.
N=0
for P in (F(1,8),F(1,3),F(3,4),F(7,8)):
    for H in (F(1,20),F(2,5),F(3,2),F(5,1)):
        for R in (F(1,10),F(1),F(5,2),F(13)):
            M=P+R*H; V=R*H*H-P*P; T=R*H**3+P**3
            Hp=(V+P*P)/(M-P); Rp=(M-P)**2/(V+P*P)
            assert (Hp,Rp)==(H,R)
            assert (V+P*P)**2/(M-P)+P**3==T
            assert (V+P*P)>0 and M-P>0
            N+=3
print('PASSED:',3+3+1+4+1+N,'exact checks')
