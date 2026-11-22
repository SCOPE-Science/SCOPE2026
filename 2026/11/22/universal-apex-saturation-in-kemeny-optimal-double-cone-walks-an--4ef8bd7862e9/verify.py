"""Independent finite diagnostics for symmetric Kemeny optimization on double cones.

These checks are finite diagnostics, not a proof of the all-graph theorem.
Requires Python 3, NumPy and SciPy.
"""
import math
import numpy as np
from scipy.optimize import minimize

CHECKS = 0

def check(condition, detail=''):
    global CHECKS
    assert bool(condition), detail
    CHECKS += 1

def cycle(n):
    h = np.zeros((n,n))
    for i in range(n):
        h[i,(i+1)%n] = h[(i+1)%n,i] = 1.
    return h

def clique(n):
    return np.ones((n,n))-np.eye(n)

def cube(k):
    n=2**k
    h=np.zeros((n,n))
    for i in range(n):
        for t in range(k):
            h[i,i^(1<<t)]=1.
    return h

def petersen():
    h=np.zeros((10,10))
    for i in range(5):
        for a,b in ((i,(i+1)%5),(5+i,5+(i+2)%5),(i,5+i)):
            h[a,b]=h[b,a]=1.
    return h

def double_cone_matrix(h,a,b):
    n=len(h); d=float(h[0].sum()); N=n+2
    p=np.zeros((N,N))
    p[:2,2:]=a; p[2:,:2]=a; p[2:,2:]=b*h
    np.fill_diagonal(p,1-p.sum(axis=1))
    return p

def kemeny(p):
    lam=np.linalg.eigvalsh(np.eye(len(p))-p)
    if lam[1]<=1e-10:
        return float('inf')
    return float(np.sum(1/lam[1:]))

def formula(h):
    n=len(h); d=float(h[0].sum()); a=1/n; b=(n-2)/(n*d)
    lap=np.diag(h.sum(axis=1))-h
    ls=np.linalg.eigvalsh(lap)
    return 1+ n/(n+2)+sum(1/(2*a+b*l) for l in ls[1:])

def all_edges(h):
    n=len(h); out=[]
    for i in range(2):
        for j in range(n):out.append((i,j+2))
    for i in range(n):
        for j in range(i+1,n):
            if h[i,j]: out.append((i+2,j+2))
    return out

def unrestricted_laplacian(n,edges,w):
    p=np.zeros((n,n))
    for (u,v),x in zip(edges,w):p[u,v]=p[v,u]=x
    np.fill_diagonal(p,1-p.sum(axis=1))
    return p

def check_unrestricted(h):
    n=len(h); d=float(h[0].sum()); N=n+2
    edges=all_edges(h); row_edges=[[k for k,(i,j) in enumerate(edges) if v in (i,j)] for v in range(N)]
    a=1/n; b=(n-2)/(n*d)
    reference=np.array([a if (i<2 or j<2) else b for i,j in edges])
    target=kemeny(unrestricted_laplacian(N,edges,reference))
    def constraint_fun(w):return np.array([1-sum(w[k] for k in row) for row in row_edges])
    def objective(w):
        if np.any(w<0):return 1e8
        val=kemeny(unrestricted_laplacian(N,edges,w));return val if np.isfinite(val) else 1e8
    rng=np.random.default_rng(N*377)
    for rep in range(2):
        v=reference*(0.4+0.2*rng.random(len(edges)))
        result=minimize(objective,v,method='SLSQP',bounds=[(0,1)]*len(edges),constraints=[{'type':'ineq','fun':constraint_fun}],options={'ftol':1e-10,'maxiter':200})
        check(result.success or abs(result.fun-target)<1e-6,'optimization termination')
        check(result.fun>=target-1e-6,'numeric lower bound')
        check(abs(result.fun-target)<1e-6,'numeric global match')
        check(max(abs(result.x-reference))<5e-4,'unrestricted numerical optimizer')

cases=[('cycle',cycle(n)) for n in range(3,25)]+ [('clique',clique(n)) for n in range(3,14)]+ [('cube',cube(k)) for k in range(2,6)]+[('petersen',petersen())]
for name,h in cases:
    n=len(h); d=float(h[0].sum()); check(np.allclose(h,h.T),'symmetric H')
    check(np.allclose(h.sum(axis=1),d),'regular H')
    a=1/n; b=(n-2)/(n*d)
    p=double_cone_matrix(h,a,b)
    check(np.min(p)>-1e-12,'nonneg P')
    check(np.max(abs(p.sum(axis=1)-1))<1e-12,'stochastic P')
    check(abs(kemeny(p)-formula(h))<1e-8,'spectrum formula')
    for factor in (0.4,0.65,0.92):
        anew=a*factor; bnew=(1-2*anew)/d
        check(kemeny(double_cone_matrix(h,anew,bnew))>kemeny(p)+1e-9,'strict a preference')
    if n<=8:check_unrestricted(h)

for n in range(3,80):
    r=1-2/n
    q=(1-math.sqrt(1-r*r))/r
    sumf=1+n/(n+2)-n/2+n*n/(2*math.sqrt(n-1))*(1+q**n)/(1-q**n)
    check(abs(sumf-formula(cycle(n)))<1e-7,'cycle resolvent')
for n in (100,400,1600,6400):
    r=1-2/n
    q=(1-math.sqrt(1-r*r))/r
    ko=1+n/(n+2)-n/2+n*n/(2*math.sqrt(n-1))*(1+q**n)/(1-q**n)
    s=2-math.sqrt(3)
    km=1+n/(n+2)-n/2+n*n/(2*math.sqrt(3))*(1+s**n)/(1-s**n)
    check(abs(ko/(n**1.5)-0.5)<0.1,'optimal asymptotic finite window')
    check(abs(km/n**2-1/(2*math.sqrt(3)))<0.01,'max degree asymptotic')
    check(km>ko,'unbounded advantage direction')
print('PASS:',CHECKS,'finite diagnostic assertions, across',len(cases),'graph instances')
