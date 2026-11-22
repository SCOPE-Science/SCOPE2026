"""Independent exact-rational checks for a BCC Voronoi radial-tail identity.
Scientific statement and proof are in RESULT.md; this script checks finite algebraic certificates.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, comb, sqrt

# Polytope V: |x_i| <= 1/2, |x_1|+|x_2|+|x_3| <= 3/4.
facets = []
for i in range(3):
    for z in (-1,1):
        normal = tuple(z if i==j else 0 for j in range(3))
        facets.append((normal,F(1,2)))
for signs in product((-1,1),repeat=3):
    facets.append((signs,F(3,4)))

def determinant(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def intersect(planes):
    A = [list(map(F,p[0])) for p in planes]
    b = [p[1] for p in planes]
    d=determinant(A)
    if not d: return None
    return tuple(determinant([[b[i] if j==k else A[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))

vertices=set()
for triplet in combinations(facets,3):
    x=intersect(triplet)
    if x is not None and all(sum(F(a)*z for a,z in zip(n,x))<=q for n,q in facets):
        vertices.add(x)
expected=set()
for k in range(3):
    for j in range(3):
        if k==j:continue
        other=({0,1,2}-{k,j}).pop()
        for a,b in product((-1,1),repeat=2):
            x=[F(0)]*3;x[k]=F(a,2);x[j]=F(b,4)
            expected.add(tuple(x))
assert vertices==expected and len(vertices)==24
assert all(sum(c*c for c in v)==F(5,16) for v in vertices)
assert all(sum(sum(n[i]*v[i] for i in range(3))==q for n,q in facets)==3 for v in vertices)
min_d2=min(sum((a-b)**2 for a,b in zip(v,w)) for v,w in combinations(vertices,2))
assert min_d2==F(1,8)

# Jacobian and squared deficit for v=(1/2,1/4,0) using
# x=(1/2-2p,1/4+2p-2q-2r,2r-2q), p,q,r>=0.
def x_from_pqr(p,q,r):
    return (F(1,2)-2*p,F(1,4)+2*p-2*q-2*r,2*r-2*q)
def h(a,b,c): return a*a-a*(b+c)+b*b+c*c
for p,q,r in product((F(0),F(1,40),F(1,30)),repeat=3):
    x=x_from_pqr(p,q,r)
    deficit=F(5,16)-sum(z*z for z in x)
    assert deficit==p+q+r-8*h(p,q,r)
    if p+q+r<=F(1,40):
        assert all(sum(F(a)*z for a,z in zip(n,x))<=t for n,t in facets)

# Multivariate polynomial in (a,b,c), h=a^2-ab-ac+b^2+c^2.
terms={(2,0,0):F(1),(1,1,0):F(-1),(1,0,1):F(-1),(0,2,0):F(1),(0,0,2):F(1)}
def multiply(a,b):
    out={}
    for (i,j,k),u in a.items():
        for (x,y,z),v in b.items():
            key=(i+x,j+y,k+z);out[key]=out.get(key,F(0))+u*v
    return out

def simplex_integral(poly):
    return sum(v*F(factorial(i)*factorial(j)*factorial(k),factorial(i+j+k+2))
               for (i,j,k),v in poly.items())

moments=[];power={(0,0,0):F(1)}
coeffs=[]
for m in range(7):
    integral=simplex_integral(power)
    moments.append(integral)
    coeff=F(256*3,m+3)*comb(2*m+2,m)*8**m*integral
    coeffs.append(coeff)
    power=multiply(power,terms)
assert moments[:3]==[F(1,2),F(1,6),F(13,180)]
assert coeffs[:3]==[F(128),F(1024),F(53248,5)]
assert all(c>0 for c in coeffs)

# The local vertex cone has coordinate Jacobian exactly 16.
assert determinant([[-2,0,0],[2,-2,-2],[0,-2,2]])==16
# Volume of V: eight positive octants in a half-size cube. Irwin-Hall at 3/2.
volume=8*F(1,8)*F(F(3,2)**3-3*F(1,2)**3,6)
assert volume==F(1,2)
# Lower-case exact h range on the 2-simplex, verified analytically in RESULT:
assert h(F(2,5),F(3,10),F(3,10))==F(1,10)

print('vertices',len(vertices),'minimum squared vertex separation',min_d2)
print('Voronoi volume',volume,'squared covering radius',F(5,16))
for m,(moment,coefficient) in enumerate(zip(moments,coeffs)):
    print('m',m,'simplex integral',moment,'tail coefficient for epsilon^'+str(m+3),coefficient)
