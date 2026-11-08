"""Exact coefficient-by-coefficient verification for cubic spherical harmonic moments.

Requires Python 3 and SymPy. No floating-point or sampled-point computations.
Run: python check_cubic_moments.py
"""
from itertools import product
import sympy as s

x,y,z = s.symbols('x y z')
c = s.symbols('c0:7')
r2 = x*x+y*y+z*z
basis = [
    5*z**3-3*z*r2,
    x*(5*z*z-r2), y*(5*z*z-r2),
    z*(x*x-y*y), 2*x*y*z,
    x*(x*x-3*y*y), y*(3*x*x-y*y),
]
assert all(s.expand(sum(s.diff(p,t,2) for t in (x,y,z)))==0 for p in basis)
monoms=[x**i*y**j*z**k for i in range(4) for j in range(4-i) for k in [3-i-j]]
assert s.Matrix([[s.expand(p).coeff(x,i).coeff(y,j).coeff(z,3-i-j)
                  for p in basis] for i in range(4) for j in range(4-i)]).rank()==7
h = s.expand(sum(c[i]*basis[i] for i in range(7)))
coords=(x,y,z)
T=[[[s.diff(h,coords[i],coords[j],coords[k])/6 for k in range(3)]
    for j in range(3)] for i in range(3)]
E=s.expand(sum(T[i][j][k]**2 for i,j,k in product(range(3),repeat=3)))
B=[[s.expand(sum(T[i][p][q]*T[j][p][q] for p,q in product(range(3),repeat=2)))
    for j in range(3)] for i in range(3)]
trB2=s.expand(sum(B[i][j]**2 for i,j in product(range(3),repeat=2)))

def df(n):
    ans=1
    for k in range(n,0,-2):ans*=k
    return ans

def average(p):
    # Normalized surface probability measure on S^2; all integration exact.
    poly=s.Poly(s.expand(p),x,y,z)
    return s.expand(sum(coeff*s.Rational(df(i-1)*df(j-1)*df(k-1),df(i+j+k+1))
        for (i,j,k),coeff in poly.terms() if i%2==j%2==k%2==0))

m2=average(h*h)
m4=average(h**4)
assert s.Poly(m2-s.Rational(2,35)*E,*c).is_zero
assert s.Poly(m4-s.Rational(4,715)*E**2-s.Rational(24,5005)*trB2,*c).is_zero
assert s.Poly(m4,*c).total_degree()==4
assert len(s.Poly(m4,*c).terms())==45

# A particular nonzero harmonic cubic, z(x^2-y^2), has isotropic B.
values={c[i]:(1 if i==3 else 0) for i in range(7)}
e0=E.subs(values);b0=s.Matrix(B).subs(values)
assert e0>0 and b0==s.eye(3)*e0/3
assert s.cancel(m4.subs(values)/m2.subs(values)**2)==s.Rational(315,143)

# A nonflat comparison: the real highest-weight cubic x(x^2-3y^2).
values2={c[i]:(1 if i==5 else 0) for i in range(7)}
assert s.cancel(m4.subs(values2)/m2.subs(values2)**2)==s.Rational(350,143)
print('SEVEN_DIMENSIONAL_HARMONIC_BASIS_AND_LAPLACIAN_OK')
print('EXACT_SECOND_AND_FOURTH_MOMENT_POLYNOMIAL_IDENTITIES_OK')
print('ALL_210_POSSIBLE_DEGREE_FOUR_COEFFICIENTS_CHECKED 45_nonzero')
print('SHARP_ISOTROPY_EQUALITY_AND_NONTRIVIAL_COMPARISON_OK 315/143 350/143')
print('ALL_CUBIC_HARMONIC_MOMENT_CHECKS_OK')
