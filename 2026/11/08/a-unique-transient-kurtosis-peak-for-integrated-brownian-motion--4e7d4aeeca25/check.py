"""Standalone algebraic and numerical diagnostics for the kurtosis peak theorem.

Requires Python 3, sympy, mpmath. Run: python check.py
"""
import math
import sympy as sp
import mpmath as mp

z, s, t, r = sp.symbols('z s t r', positive=True)
f = z - 2 + (z + 2)*sp.exp(-z)
g = 12*z**2 + 120*z - 840 + (9*z**4 + 68*z**3 + 288*z**2 + 720*z + 840)*sp.exp(-z)
H = (1440 - 168*z)*sp.exp(2*z) -(9*z**5 + 32*z**4 + 132*z**3 + 264*z**2 + 2544*z + 2880)*sp.exp(z) + (9*z**5 + 104*z**4 + 564*z**3 + 1704*z**2 + 2712*z + 1440)
assert sp.simplify(sp.expand((sp.diff(g,z)*f - 2*g*sp.diff(f,z))*sp.exp(2*z) - H)) == 0

# Symbolic verification of the independently derived renewal Laplace transforms.
M = 6 / (s**2*(s+r)**2)
Q = 720/(s**2*(s+r)**5)+72*r/(s**3*(s+r)**5)
assert sp.simplify(sp.inverse_laplace_transform(M, s, t) - 6*f.subs(z,r*t)/r**3) == 0
assert sp.simplify(sp.inverse_laplace_transform(Q, s, t) - 3*g.subs(z,r*t)/r**6) == 0

fall = lambda n,j: math.prod(range(n-j+1,n+1))
def coeff_factorial(n):
    return 2**n*(1440 - 84*n) - (9*fall(n,5)+32*fall(n,4)+132*fall(n,3)+264*fall(n,2)+2544*n+2880)
assert sp.series(H,z,0,9).removeO() == 0
assert [coeff_factorial(n) for n in (6,7,8)] == [0,0,0]
assert [coeff_factorial(n) for n in range(9,18)] == [6048,33840,113784,291456,608088,1019616,1149840,-374208,-7594512]
# For n >=18 the first summand is strictly negative and every bracket summand positive.
assert 1440-84*18 < 0
for n in range(18,101):
    assert coeff_factorial(n) < 0

K = sp.factor(g/(4*f**2)-3)
assert sp.simplify(sp.diff(K,z) - sp.exp(-2*z)*H/(4*f**3)) == 0
assert sp.limit(K/z,z,0) == sp.Rational(9,10)
assert sp.limit(K*z,z,sp.oo) == 42

mp.mp.dps = 70
def F(w):return w-2+(w+2)*mp.exp(-w)
def G(w):return 12*w**2+120*w-840+(9*w**4+68*w**3+288*w**2+720*w+840)*mp.exp(-w)
def HH(w):return (1440-168*w)*mp.exp(2*w)-(9*w**5+32*w**4+132*w**3+264*w**2+2544*w+2880)*mp.exp(w)+(9*w**5+104*w**4+564*w**3+1704*w**2+2712*w+1440)
def KK(w):return G(w)/(4*F(w)**2)-3
assert HH(6)>0 and HH(7)<0
root=mp.findroot(HH,(mp.mpf('6.6'),mp.mpf('6.7')))
peak=KK(root)
assert abs(root-mp.mpf('6.6595993253935155704510738061348761410')) < mp.mpf('1e-33')
assert abs(peak-mp.mpf('3.456181435553493726441881210077962176')) < mp.mpf('1e-32')
# Independent moment evaluation at a few times against the renewal-interval variance.
for w in (mp.mpf('0.4'),mp.mpf('2'),mp.mpf('7'),mp.mpf('15')):
    m=6*F(w); q=3*G(w)
    assert m>0 and q>m*m
    assert abs((3*(q/m**2-1))-KK(w)) < mp.mpf('1e-55')
print('PASS: symbolic renewal identities, all-order coefficient argument, endpoint laws and high-precision root')
print('dimensionless peak time:',mp.nstr(root,45))
print('excess kurtosis peak:',mp.nstr(peak,45))
