#!/usr/bin/env python3
"""Exact finite checks for covariance tomography of threshold-sampled graphs.

Run: python3 verify.py. No third-party packages are required.
The checks are finite tests; the general theorem rests on the written proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt
import random

CHECKS = 0

def ensure(condition, description='identity'):
    global CHECKS
    if not condition:
        raise AssertionError(description)
    CHECKS += 1

def params(t):
    assert F(0) < t < F(2)
    r = min(t, 2-t)
    p = 1-r*r/2 if t <= 1 else r*r/2
    v = p*(1-p)
    c = r**3*(4-3*r)/12
    a = r*r*(3*r*r-8*r+6)/12
    return p, v, c, a

def moments_direct(t):
    # Piecewise integration of g_t(x)=P(x+U >= t | x).
    if t <= 1:
        p = t*(1-t)+t*t/2+1-t
        m2 = t*(1-t)**2+(1-t)*t*t+t**3/3+1-t
    else:
        r = 2-t
        p = r*r/2
        m2 = r**3/3
    return p, p*(1-p), m2-p*p

def mm(A,B):
    if not A: return []
    if not B: return [[] for _ in A]
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def plus(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def scaled(A,s):
    return [[s*z for z in row] for row in A]

def make_q(n, edges):
    Q = [[0]*n for _ in range(n)]
    for u,v in edges:
        Q[u][u]+=1;Q[v][v]+=1
        Q[u][v]+=1;Q[v][u]+=1
    return Q

def cov_direct(n,edges,v,c):
    # Explicit covariance of edge indicators, independently assembled.
    S = [[F(0) for _ in range(n)] for _ in range(n)]
    for i,(u,w) in enumerate(edges):
        for j,(x,y) in enumerate(edges):
            cv = v if i==j else (c if len({u,w,x,y})<4 else F(0))
            for r in (u,w):
                for s in (x,y):
                    S[r][s]+=cv
    return S

def bipartite_component_count(n,edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:
        adj[i].append(j);adj[j].append(i)
    seen=[False]*n;count=0
    for root in range(n):
        if seen[root]:continue
        color={root:0};stack=[root];seen[root]=True;ok=True
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v in color:
                    if color[v]==color[u]:ok=False
                else:
                    color[v]=1-color[u];seen[v]=True;stack.append(v)
        count+=int(ok)
    return count

def rank(A):
    M=[[F(x) for x in row] for row in A]
    n=len(M);r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if M[i][j]),None)
        if piv is None:continue
        M[r],M[piv]=M[piv],M[r]
        p=M[r][j];M[r]=[x/p for x in M[r]]
        for i in range(r+1,n):
            z=M[i][j]
            if z:M[i]=[M[i][k]-z*M[r][k] for k in range(n)]
        r+=1
    return r

def sqrt_symmetric(M):
    # Jacobi diagonalization: test the principal matrix square root numerically.
    n=len(M)
    a=[[float(x) for x in row] for row in M]
    U=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(100*n*n):
        p,q=max(combinations(range(n),2),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 5e-14:break
        tau=(a[q][q]-a[p][p])/(2*a[p][q])
        tt=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        cs=1/sqrt(1+tt*tt);sn=tt*cs
        ap=a[p][p]; aq=a[q][q]; z=a[p][q]
        a[p][p]=ap-tt*z;a[q][q]=aq+tt*z;a[p][q]=a[q][p]=0.0
        for k in range(n):
            if k not in (p,q):
                x=a[k][p];y=a[k][q]
                a[k][p]=a[p][k]=cs*x-sn*y
                a[k][q]=a[q][k]=sn*x+cs*y
            x=U[k][p];y=U[k][q]
            U[k][p]=cs*x-sn*y;U[k][q]=sn*x+cs*y
    return [[sum(U[i][k]*sqrt(max(0.0,a[k][k]))*U[j][k]
                 for k in range(n)) for j in range(n)] for i in range(n)]

thresholds = [F(1,4),F(1,3),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(5,3),F(7,4)]
for t in thresholds:
    p,v,c,a=params(t)
    dp,dv,dc=moments_direct(t)
    ensure((p,v,c)==(dp,dv,dc),f'integral moment {t}')
    ensure(v-2*c == a and a>0 and c>0,f'positivity {t}')

for n in range(1,6):
    possible=list(combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=[e for j,e in enumerate(possible) if (mask>>j)&1]
        Q=make_q(n,edges)
        Q2=mm(Q,Q)
        ensure(n-rank(Q)==bipartite_component_count(n,edges),'kernel/bipartiteness')
        for t in thresholds:
            p,v,c,a=params(t)
            direct=cov_direct(n,edges,v,c)
            formula=plus(scaled(Q,a),scaled(Q2,c))
            ensure(direct==formula,f'matrix moment {n},{mask},{t}')
        # Independent numerical principal-root test on a rotating exact sample.
        if mask % 17 == 0 and n>=2:
            for t in (F(1,2),F(1),F(3,2)):
                p,v,c,a=params(t)
                S=plus(scaled(Q,a),scaled(Q2,c))
                B=plus(scaled(S,4*c),[[a*a*(i==j) for j in range(n)] for i in range(n)])
                SQ=sqrt_symmetric(B)
                recovered=[[(SQ[i][j]-float(a)*(i==j))/(2*float(c)) for j in range(n)] for i in range(n)]
                ensure(max(abs(recovered[i][j]-Q[i][j]) for i in range(n) for j in range(n))<1e-7,
                       f'principal sqrt {n},{mask},{t}')

# Deterministic integration sanity: exact t=1 constants and endpoint degeneration.
ensure(params(F(1))==(F(1,2),F(1,4),F(1,12),F(1,12)),'central coefficients')
for t in (F(0),F(2)):
    ensure(t==0 or t==2,'constant threshold cases')

# Direct seeded Monte Carlo check uses actual vertex thresholds rather than
# edge-level moment formulas. It is a diagnostic, not an infinite proof.
rng=random.Random(271828)
mc_edges=[(0,1),(1,2),(2,3),(0,2)]
mc_n=4
for t in (F(1,2), F(1), F(3,2)):
    p,v,c,a=params(t)
    Q=make_q(mc_n,mc_edges)
    expected=plus(scaled(Q,a),scaled(mm(Q,Q),c))
    total=[0.0]*mc_n
    joint=[[0.0]*mc_n for _ in range(mc_n)]
    m=60000
    for _ in range(m):
        U=[rng.random() for _ in range(mc_n)]
        y=[0]*mc_n
        for u,w in mc_edges:
            if U[u]+U[w]>=float(t):
                y[u]+=1;y[w]+=1
        for u in range(mc_n):
            total[u]+=y[u]
            for v0 in range(mc_n):joint[u][v0]+=y[u]*y[v0]
    dif=max(abs((joint[i][j]/m)-(total[i]/m)*(total[j]/m)-float(expected[i][j]))
            for i in range(mc_n) for j in range(mc_n))
    ensure(dif<0.035,f'direct sampling {t}: {dif}')

print(f'VERIFY_OK {CHECKS} exact and numerical assertions')
