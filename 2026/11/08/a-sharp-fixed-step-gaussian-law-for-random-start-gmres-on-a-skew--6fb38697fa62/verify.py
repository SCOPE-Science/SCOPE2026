"""Reproducibility checks for fixed-step GMRES on a skew Toeplitz stencil.
Run: python3 verify.py. Only the Python standard library is needed.
These finite checks supplement, not replace, the analytic limit proof.
"""
from fractions import Fraction as F
from math import comb, cos, pi, sqrt
from random import Random

checks = 0

def require(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for k, v in enumerate(a): c[k] += v
    for k, v in enumerate(b): c[k] += v
    return c

def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c

def scale(a, c): return [c*x for x in a]

def cheby(n):
    if n == 0: return [F(1)]
    a, b = [F(1)], [F(0), F(1,2)]
    for _ in range(1, n):
        a, b = b, add([F(0)]+b, scale(a,F(-1)))
    return b

def moment(p):
    return sum((v*comb(i,i//2) for i,v in enumerate(p) if i%2==0), F(0))

def kernel(q):
    d = F(2*q+1)
    p = [F(1)]
    for j in range(1,q+1):
        p = add(p,scale(cheby(2*j),F(2*(-1)**j)))
    return scale(p,1/d)

for q in range(1,9):
    L = 2*q+1
    p = kernel(q)
    require(p[0] == 1, 'value at spectral origin')
    for j in range(1,q+1):
        require(moment([F(0)]*(2*j)+p) == 0, 'normal equations')
    p2 = mul(p,p)
    p4 = mul(p2,p2)
    require(moment(p2) == F(1,L), 'limiting squared residual')
    require(moment(p4) == F(2*L*L+1, 3*L**3), 'fourth Dirichlet moment')
    v_sq = 2*(moment(p4)-moment(p2)**2)
    v_norm = v_sq*F(L,4)
    require(v_sq == F(2*(2*L-1)*(L-1),3*L**3), 'squared norm CLT variance')
    require(v_norm == F((2*L-1)*(L-1),6*L*L), 'norm CLT variance')
    for theta_ind in range(81):
        x = 2*cos(pi*theta_ind/80)
        lhs = sum(float(v)*x**j for j,v in enumerate(p))
        rhs = (1+2*sum((-1)**j*cos(2*j*pi*theta_ind/80) for j in range(1,q+1)))/L
        require(abs(lhs-rhs)<2e-7, 'Chebyshev/Dirichlet profile')

def S(v):
    n = len(v)
    return [ (v[i-1] if i else 0.) - (v[i+1] if i+1<n else 0.) for i in range(n) ]

def dot(u,v): return sum(a*b for a,b in zip(u,v))

def solve(G,h):
    n = len(h)
    a = [list(row)+[h[i]] for i,row in enumerate(G)]
    for j in range(n):
        k=max(range(j,n),key=lambda i:abs(a[i][j]))
        require(abs(a[k][j])>1e-12, 'positive Gram')
        a[j],a[k]=a[k],a[j]
        d=a[j][j]
        for z in range(j,n+1):a[j][z]/=d
        for i in range(n):
            if i!=j:
                c=a[i][j]
                for z in range(j,n+1):a[i][z]-=c*a[j][z]
    return [a[i][-1] for i in range(n)]

def residual_squared(b,k):
    v=[]; x=b
    for _ in range(k):
        x=S(x);v.append(x)
    h=[dot(t,b) for t in v]
    G=[[dot(t,u) for u in v] for t in v]
    c=solve(G,h)
    return max(0.,1-sum(t*u for t,u in zip(h,c))/dot(b,b))

rng=Random(4105)
for n in (12,16,20,32):
    for q in (1,2,3):
        for _ in range(15):
            b=[rng.gauss(0,1) for i in range(n)]
            e=residual_squared(b,2*q)
            f=residual_squared(b,2*q+1)
            require(abs(e-f)<1e-10, 'exact odd-step stagnation')

# Direct trace sampling from the known skew-Toeplitz eigenvalues.
for n in (64,128,256,512):
    for q in (1,2,3):
        p=kernel(q)
        z=sum(sum(float(v)*(2*cos(j*pi/(n+1)))**i for i,v in enumerate(p))**2 for j in range(1,n+1))/n
        require(abs(z-1/(2*q+1)) < 12/n, 'Toeplitz spectral arcsine quadrature')

# Finite-sample check only, not a proof of the CLT.
for q in (1,2):
    n=96; observations=[]
    for _ in range(500):
        b=[rng.gauss(0,1) for j in range(n)]
        observations.append(sqrt(n)*(sqrt(residual_squared(b,2*q)) - 1/sqrt(2*q+1)))
    avg=sum(observations)/len(observations)
    var=sum((x-avg)**2 for x in observations)/len(observations)
    target=(4*q+1)*(2*q)/(6*(2*q+1)**2)
    require(abs(avg) < 0.17, 'finite-sample centered residual')
    require(abs(var-target) < 0.09, 'finite-sample fluctuation scale')
print('VERIFY_OK',checks)
