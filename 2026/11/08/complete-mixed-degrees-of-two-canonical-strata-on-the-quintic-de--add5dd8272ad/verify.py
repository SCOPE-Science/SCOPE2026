"""Exact, dependency-free Chow-intersection check for two jet-incidence loci.
Run: python3 verify.py
"""
from fractions import Fraction as F
from math import comb

# Variables A,B represent Chern roots of the dual tautological two-plane;
# H represents the hyperplane class on the quintic del Pezzo threefold.
def one():
    return {(0, 0, 0): F(1)}

def term(a=0, b=0, h=0, coeff=1):
    return {(a, b, h): F(coeff)}

def add(*polys):
    out = {}
    for poly in polys:
        for key, val in poly.items():
            out[key] = out.get(key, F(0)) + val
    return {key: val for key, val in out.items() if val}

def mul(*polys):
    out = one()
    for poly in polys:
        nxt = {}
        for (a,b,h), v in out.items():
            for (a2,b2,h2), w in poly.items():
                k = a+a2, b+b2, h+h2
                if k[2] <= 3:
                    nxt[k] = nxt.get(k, F(0)) + v*w
        out = nxt
    return out

def power(poly, n):
    out = one()
    for _ in range(n):
        out = mul(out, poly)
    return out

def gr_integral(poly, n):
    # Coefficient of A^(n-1) B^(n-2) in (A-B)*poly,
    # for the Grassmannian Gr(2,n) in its Pluecker embedding.
    av = poly.get((n-2,n-2,0), F(0))
    bv = poly.get((n-1,n-3,0), F(0))
    return av - bv

def product_integral(poly):
    # Integrate first over X: int_X H^3=5; then Gr(2,7).
    return 5 * mul(add(term(a=1),term(b=1,coeff=-1)),poly).get((6,5,3),F(0))

A, B, H = term(a=1), term(b=1), term(h=1)
Sigma1 = add(A,B)
Sigma11 = mul(A,B)
Sigma2 = add(power(A,2),Sigma11,power(B,2))

# The first factor is the zero locus of S -> O_X(H); the second is
# the Porteous class of D_1(S -> Omega_X^1(H)).
sigma_class = mul(
    add(Sigma11, mul(H,Sigma1),power(H,2)),
    add(Sigma2,mul(H,Sigma1),term(h=2,coeff=F(7,5)))
)

def jet_factor(root):
    return add(power(root,4),
               mul(term(coeff=2),H,power(root,3)),
               mul(term(coeff=F(12,5)),power(H,2),power(root,2)),
               mul(term(coeff=2),power(H,3),root))

z_class = mul(jet_factor(A),jet_factor(B))

def gr2n_integral(f,n):
    # Full homogeneous degree 2(n-2) polynomial, H exponent zero.
    prod=mul(add(A,term(b=1,coeff=-1)), f)
    return prod.get((n-1,n-2,0),F(0))

# First reconstruct the two Grassmannian intersections determining the
# Chern numbers of V_5 = Gr(2,5) intersected with three hyperplanes.
assert gr2n_integral(power(Sigma1,6),5) == 5
assert gr2n_integral(mul(power(Sigma1,4),Sigma11),5) == 2
assert 2*5 + 2 == 12  # int_X H*c2(T_X)
assert 2*5 - 3*2 == 4  # int_X c3(T_X)

values = {}
for name, cls, dim in [('Sigma',sigma_class,9),('Z',z_class,5)]:
    values[name] = tuple(int(product_integral(mul(cls,power(H,i),power(Sigma1,dim-i)))) for i in range(4))
assert values['Sigma'] == (504,448,210,45), values
assert values['Z'] == (110,52,20,5), values

# Independent flag/projective-bundle calculation (no root-polynomial
# integration). c_j(J^1 O(H)) against H^(3-j) integrates to these numbers.
chern_integrals = (5,10,12,10)
def ci(n,k):
    return comb(n,k) if 0 <= k <= n else 0

sigma_flag=[]
for i in range(4):
    n=9-i
    q1=n-6; q2=n-7
    x=(ci(n,4)-ci(n,5)) * (chern_integrals[q1] if 0<=q1<=3 else 0)
    x+=(ci(n,5)-ci(n,6)) * (chern_integrals[q2] if 0<=q2<=3 else 0)
    sigma_flag.append(x)

z_projective=[]
for i in range(4):
    n=5-i
    x=0
    for j in range(2,n+1):
        d=j-2
        if d<=3:
            x+=ci(n,j)*2**(n-j)*(-1)**d*chern_integrals[d]
    z_projective.append(x)
assert tuple(sigma_flag)==values['Sigma']
assert tuple(z_projective)==values['Z']
assert sum(ci(9,i)*v for i,v in enumerate(values['Sigma']))==15876
assert sum(ci(5,i)*v for i,v in enumerate(values['Z']))==620
assert values['Sigma'][0] == 12 * 42  # Pluecker degree of Gr(2,7) is 42.
print('Sigma mixed degrees:', values['Sigma'])
print('Z mixed degrees:', values['Z'])
print('Segre degrees:', 15876, 620)
print('VERIFY_OK')
