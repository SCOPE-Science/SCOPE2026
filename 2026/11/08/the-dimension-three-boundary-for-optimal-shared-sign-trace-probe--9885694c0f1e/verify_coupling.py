"""Exact-rational checks for finite-dimensional sign-probe coupling formulas.

The analytical optimality proof uses rearrangement and Birkhoff's theorem;
finite enumeration here checks formulas and examples, not all dimensions.
"""
from fractions import Fraction as F
from itertools import permutations, product
import random

COUNTS = 0
def check(flag, description=''):
    global COUNTS
    COUNTS += 1
    assert flag, description

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def dot(x,y):
    return sum(xi*yi for xi,yi in zip(x,y))

def quadratic(a,z):
    return dot(z,[dot(row,z) for row in a])

def average(xs):
    return sum(xs,F(0))/len(xs)

def variance(xs):
    return average([x*x for x in xs])-average(xs)**2

def covariance(xs,ys):
    return average([x*y for x,y in zip(xs,ys)])-average(xs)*average(ys)

CLASSES=[(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]
def values(a,b,c):
    return (a+b+c,a-b-c,-a+b-c,-a-b+c)

def edge_cond(e,fp):
    return all((e[i]-e[j])*(fp[i]-fp[j])>=0 for i in range(4) for j in range(i))

def six_cond(x,y):
    a,b,c=x
    d,e,f=y
    return all(v*w>=0 for v,w in ((a+b,d+e),(a+c,d+f),(b+c,e+f),
                                   (a-b,d-e),(a-c,d-f),(b-c,e-f)))

def max_cov(x,y):
    return max(covariance(x,[y[j] for j in p]) for p in permutations(range(4)))

# Dimension-three classification, independently optimize all 24 couplings.
for x in product(range(-2,3),repeat=3):
    y=(x[0]+1,2*x[1]-1,2-x[2])
    vx,vy=values(*x),values(*y)
    is_opt=covariance(vx,vy)==max_cov(vx,vy)
    check(is_opt==edge_cond(vx,vy),'pairwise rearrangement classification')
    check(is_opt==six_cond(x,y),'six polynomial inequalities')

# Random integer triples with sign ties and generic strict orders.
rg=random.Random(20261104)
for _ in range(250):
    x=tuple(rg.randrange(-30,31) for _ in range(3))
    y=tuple(rg.randrange(-30,31) for _ in range(3))
    vx,vy=values(*x),values(*y)
    check((covariance(vx,vy)==max_cov(vx,vy))==six_cond(x,y))

# Distribution of a 3-dimensional Rademacher vector has four 2-to-1 classes.
for a,b,c in ((1,2,0),(-5,2,7),(0,0,0)):
    M=[[3,a,b],[a,4,c],[b,c,10]]
    full=[quadratic(M,z) for z in product((-1,1),repeat=3)]
    cv=[quadratic(M,z) for z in CLASSES]
    check(sorted(full)==sorted(cv*2))
    check(average(full)==sum(M[i][i] for i in range(3)))
    check(variance(full)==4*(a*a+b*b+c*c))

# Explicit SPD polynomial example. Strict diagonal dominance makes L SPD;
# x and x^2/12 are both strictly increasing on the positive spectrum.
L=[[4,1,2],[1,20,0],[2,0,3]]
L2=matmul(L,L)
check(L2==[[21,24,14],[24,401,2],[14,2,13]])
check(all(L[i][i]>sum(abs(L[i][j]) for j in range(3) if j!=i)
          for i in range(3)))
Fv=[quadratic(L,z) for z in CLASSES]
G12=[quadratic(L2,z) for z in CLASSES]
check(Fv==[33,25,29,21]);check(G12==[515,451,411,363])
Gv=[F(x,12) for x in G12]
P=(0,2,1,3)
Gp=[Gv[i] for i in P]
check(variance(Fv)==20)
check(variance(G12)==3104)
check(variance(Gv)==F(194,9))
check(covariance(Fv,Gv)==F(52,3))
check(covariance(Fv,Gp)==F(62,3))
check(variance([x-y for x,y in zip(Fv,Gv)])==F(62,9))
check(variance([x-y for x,y in zip(Fv,Gp)])==F(2,9))
check(variance([x-y for x,y in zip(Fv,Gv)])/
      variance([x-y for x,y in zip(Fv,Gp)])==31)
check(covariance(Fv,Gp)==max_cov(Fv,Gv))
check(not six_cond((1,2,0),(24,14,2)))
check(sorted(Fv)==sorted(Fv[i] for i in P))
check(sorted(Gv)==sorted(Gp))
# Verify actual probe coordinate permutation induces claimed class swap.
def swap23(z):return (z[0],z[2],z[1])
check([quadratic(L2,swap23(z)) for z in CLASSES]==[G12[i] for i in P])

# Exhaust all 2D Rademacher outcomes for positive monotone functions
# instantiated as f(x)=x, g(x)=x^2 (A diagonal dominant positive definite).
for a,b,c in product(range(1,6),range(-3,4),range(1,6)):
    M=[[a,b],[b,c]]
    if a*c<=b*b: continue
    M2=matmul(M,M)
    xx=[quadratic(M,z) for z in product((-1,1),repeat=2)]
    yy=[quadratic(M2,z) for z in product((-1,1),repeat=2)]
    check(covariance(xx,yy)>=0)
    # In 2D the common-probe copula is already comonotone.
    check((M[0][1]*M2[0][1])>=0)

print('PASS: %d exact-rational assertions' % COUNTS)
print('Example covariance/variance: shared=62/9; swapped=2/9; ratio=31.')
print('Scope: n=2 polynomial witnesses and n=3 finite coefficient grids; proof is analytic.')
