"""Independent finite checks for spectral-order conductance design on triangular books.

Run: python verify_book_moments.py
Requires numpy and scipy. The mathematical proof, not these finite checks,
covers arbitrary real positive prices and spectral orders.
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar, brentq

rng = np.random.default_rng(1729)
checks = 0

def tick(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def laplacian(m, spoke_edges, spine):
    n = m + 2
    L = np.zeros((n, n), dtype=float)
    edges = [(0, 1, spine)]
    for j in range(m):
        edges += [(0, j + 2, spoke_edges[2 * j]),
                  (1, j + 2, spoke_edges[2 * j + 1])]
    for u, v, w in edges:
        L[u, u] += w
        L[v, v] += w
        L[u, v] -= w
        L[v, u] -= w
    return L

def objective(eigs, p):
    vals = np.sort(eigs)[1:]
    if vals[0] <= 1e-11:
        return math.inf
    if p == 0:
        return -np.log(vals).sum()
    return np.exp(-p * np.log(vals)).sum()

def critical(m, p):
    D = 1 + (m - 1) * (m / 2) ** p + (m / (m + 2)) ** p
    return 4 / D

def optimum(m, p, c):
    A = (m - 1) * 2 ** (-p) + (m + 2) ** (-p)
    if c >= critical(m, p):
        t = 0.0
    else:
        t = .5 * (math.exp(math.log(m * (4 - c) / (c * A)) / (p + 1)) - m)
    x = 1 / (2 * m + c * t)
    y = t * x
    return x, y, t

def scalar_objective(m, p, c, t):
    x = 1/(2*m+c*t)
    eig = np.array([2*x]*(m-1) + [(m+2)*x, (m+2*t)*x])
    if p == 0:
        return -np.log(eig).sum()
    return np.sum(eig ** (-p))

# Eigenvalues from a full, independently assembled Laplacian.
for m in range(2, 16):
    for _ in range(30):
        x = 10 ** rng.uniform(-2,1)
        y = 10 ** rng.uniform(-2,1)
        direct = np.linalg.eigvalsh(laplacian(m,[x]*(2*m),y))
        expected = np.sort([0] + [2*x]*(m-1) + [(m+2)*x, m*x+2*y])
        tick(np.allclose(direct, expected, atol=1e-10, rtol=1e-10), ('spectrum',m))

# Exact allocation formula vs generic scalar minimization, including p=0.
for m in range(2, 15):
    for p in (0, .12, .4, 1, 1.9, 3.7, 8):
        for c in (.02, .5, 1.05, 1.6, 2.1, 4.4):
            x,y,t=optimum(m,p,c)
            tick(abs(2*m*x+c*y-1)<3e-12, ('budget',m,p,c))
            tick(t>=0 and x>0 and y>=0, ('domain',m,p,c))
            calc=objective(np.linalg.eigvalsh(laplacian(m,[x]*(2*m),y)),p)
            exact=scalar_objective(m,p,c,t)
            tick(abs(calc-exact)<1e-8*max(1,abs(exact)), ('value',m,p,c))
            t_upper=max(5, t*2+10)
            sol=minimize_scalar(lambda z: scalar_objective(m,p,c,z),bounds=(0,t_upper),method='bounded',options={'xatol':1e-9})
            tick(calc <= sol.fun + 3e-7*max(1,abs(sol.fun)),('scalar optimum',m,p,c,t,sol.x,calc,sol.fun))

# Unrestricted feasible competitors with individually random edge weights.
for m in range(2, 11):
    for p in (0, .5, 1, 2, 4):
        for c in (.2, 1.1, 1.8, 3):
            x,y,t=optimum(m,p,c)
            val=objective(np.linalg.eigvalsh(laplacian(m,[x]*(2*m),y)),p)
            for _ in range(60):
                costs=np.r_[c, np.ones(2*m)]
                budget_share=rng.dirichlet(np.ones(2*m+1)*rng.choice([.3,1,3]))
                w=budget_share/costs
                competing=objective(np.linalg.eigvalsh(laplacian(m,w[1:],w[0])),p)
                tick(competing >= val-1e-8*max(1,abs(val)),('asymmetric competitor',m,p,c,val,competing))

# Strict support frontier monotonicity and closed asymptotics.
ps=np.r_[np.linspace(0,3,60), np.linspace(3.1,16,30)]
for m in range(2,35):
    vals=np.array([critical(m,p) for p in ps])
    if m==2:
        tick(np.all(np.diff(vals)>0), ('m2 rising',m))
        tick(abs(vals[0]-4/3)<1e-14, 'm2 zero')
    else:
        tick(np.all(np.diff(vals)<0), ('multipage falling',m))
        tick(abs(vals[0]-4/(m+1))<1e-14, 'multipage zero')
for p in (0,.3,1,2,4):
    for m in (50,100,200,600):
        ratio=critical(m,p)*m**(p+1)/2**(p+2)
        tick(abs(ratio-1)<.13, ('large-m',p,m,ratio))

# Two-page unique peak and activation order, including p=0 endpoint.
c0=4/(1+2**1.5)
for c in np.linspace(c0+.005,1.98,35):
    a=math.log((4-c)/c)
    def N(p):
        return (p+1)*math.log(2)/(1+2**p)-a+math.log1p(2**(-p))
    hi=500
    peak=brentq(N,0,hi)
    def t_at(p): return optimum(2,p,c)[2]
    delta=1e-3
    tick(t_at(peak)>t_at(max(0,peak-delta)),('peak left',c,peak))
    tick(t_at(peak)>t_at(peak+delta),('peak right',c,peak))
    if c>4/3:
        pc=-math.log2(4/c-2)
        tick(t_at(max(0,pc-1e-5))==0,('off',c,pc))
        tick(t_at(pc+1e-5)>0,('on',c,pc))
        tick(peak>pc,('peak after activation',c,peak,pc))
for c in (.1,.4,.9,c0):
    a=math.log((4-c)/c)
    for p in (0, .2,.7,1,3,6,10,30):
        t=optimum(2,p,c)[2]
        t_next=optimum(2,p+.001,c)[2]
        tick(t_next <=t+2e-9,('monotone two page',c,p))
for c in (.4,.9,1.2,1.7,1.95):
    for p in (100,300,800):
        actual=optimum(2,p,c)[2]
        pred=math.log((4-c)/c)/(p+1)
        tick(abs(actual/pred-1)<.03, ('m2 high order',c,p,actual,pred))

print(f'PASS: {checks} independent finite assertions')
