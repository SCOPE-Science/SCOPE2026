"""Exact polynomial-integral checks for low-order volume moments of a regular 24-cell.

Run with: python3 verify.py
Uses only the Python standard library. Polynomials are sparse Fraction maps.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product

N=4
Z=(0,)*N

def c(q):
    q=F(q)
    return {Z:q} if q else {}

def v(i):
    p=[0]*N;p[i]=1
    return {tuple(p):F(1)}

def add(*args):
    d={}
    for a in args:
        for p,q in a.items():
            d[p]=d.get(p,F(0))+q
            if not d[p]:del d[p]
    return d

def mul(a,b):
    d={}
    for p,q in a.items():
        for r,s in b.items():
            k=tuple(x+y for x,y in zip(p,r))
            d[k]=d.get(k,F(0))+q*s
            if not d[k]:del d[k]
    return d

def scale(a,q):
    q=F(q)
    return {p:k*q for p,k in a.items() if k*q}

def power(a,n):
    s=c(1)
    for _ in range(n):s=mul(s,a)
    return s

def int_simplex(a):
    # Integral over {t_i>=0, sum t_i<=1}, unnormalized.
    return sum((q*F(factorial(p[0])*factorial(p[1])*factorial(p[2])*factorial(p[3]),factorial(sum(p)+4)) for p,q in a.items()),F(0))

def int_cube(a):
    return sum((q*F(1,(p[0]+1)*(p[1]+1)*(p[2]+1)*(p[3]+1)) for p,q in a.items()),F(0))

def eval_poly(expr,x):
    total={}
    for ex,coeff in expr.items():
        z=c(coeff)
        for i,m in enumerate(ex):z=mul(z,power(x[i],m))
        total=add(total,z)
    return total

def polys(x):
    squares=[power(t,2) for t in x]
    r2=add(*squares)
    return {
        'one':c(1),
        'r2':r2,
        'r4':power(r2,2),
        'r6':power(r2,3),
        'sum4':add(*(power(t,4) for t in x)),
        'sum22':add(*(mul(squares[i],squares[j]) for i in range(4) for j in range(i+1,4))),
        'sum6':add(*(power(t,6) for t in x)),
        'sum42':add(*(mul(power(x[i],4),squares[j]) for i in range(4) for j in range(4) if i!=j)),
        'sum222':add(*(mul(mul(squares[i],squares[j]),squares[k]) for i in range(4) for j in range(i+1,4) for k in range(j+1,4)))
    }

a,b,cvar,d=map(v,range(4))
# Affine map from the unit four-simplex onto a single signed-and-sorted chamber.
y=add(b,cvar,d)
xs=[add(a,scale(y,F(1,2))),scale(y,F(1,2)),scale(add(cvar,d),F(1,2)),scale(d,F(1,2))]
# The map has Jacobian 1/8; the 384 congruent chambers / cell volume 2
# yield normalized expectation 24 times the unit-simplex integral.
P=polys(xs)
out_s={name:24*int_simplex(expr) for name,expr in P.items()}

# Completely different parametrization of that chamber via a unit cube:
# x2=a/2, x1=a/2+(1-a)b, x3=ac/2, x4=acd/2.
xx=[add(scale(a,F(1,2)),mul(add(c(1),scale(a,-1)),b)),scale(a,F(1,2)),scale(mul(a,cvar),F(1,2)),scale(mul(mul(a,cvar),d),F(1,2))]
J=scale(mul(mul(power(a,2),cvar),add(c(1),scale(a,-1))),F(1,8))
out_c={name:192*int_cube(mul(expr,J)) for name,expr in polys(xx).items()}
assert out_s==out_c,(out_s,out_c)
expect={
 'one':F(1),'r2':F(13,30),'r4':F(3,14),'r6':F(289,2520),
 'sum4':4*F(3,112),'sum22':6*F(1,112),
 'sum6':4*F(251,26880),'sum42':12*F(403,241920),
 'sum222':4*F(5,6912)
}
assert out_s==expect,(out_s,expect)
A=out_s['sum4']/4;B=out_s['sum22']/6
assert A==3*B==F(3,112)
A6=out_s['sum6']/4;B6=out_s['sum42']/12;C6=out_s['sum222']/4
assert (A6,B6,C6)==(F(251,26880),F(403,241920),F(5,6912))
assert A6-5*B6==F(61,60480)
assert (A6+15*B6)/4==F(173,20160)
assert A6-(A6+15*B6)/4==F(61,80640)
assert out_s['r4']-out_s['r2']**2==F(167,6300)
assert 4*A6+36*B6+24*C6==out_s['r6']
# The 24 vertices of the Voronoi 24-cell and the Hadamard symmetry.
from itertools import permutations
verts=set()
for i in range(4):
 for sg in [-1,1]:
  u=[F(0)]*4;u[i]=F(sg);verts.add(tuple(u))
for sign in product([-1,1],repeat=4):verts.add(tuple(F(v,2) for v in sign))
assert len(verts)==24
H=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
assert all(tuple(sum(F(H[i][j],2)*u[j] for j in range(4)) for i in range(4)) in verts for u in verts)
assert all(sum(u[i]**2 for i in range(4))==1 for u in verts)
assert all(abs(u[i])+abs(u[j])<=1 for u in verts for i in range(4) for j in range(i+1,4))
print('VERIFY_OK exact_D4_Voronoi_cell_384_chambers simplex_cube_independent_integrals second_fourth_sixth_moments fourth_isotropy_sixth_anisotropy')
for k in ('r2','r4','r6','sum4','sum22','sum6','sum42','sum222'):
 print(k,out_s[k])
