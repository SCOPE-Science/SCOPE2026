#!/usr/bin/env python3
"""Exact projector checks for a one-bond-weighted bipartite quantum walk."""
from fractions import Fraction as F

def rank(a):
    if not a: return 0
    a=[list(map(F,row)) for row in a]
    rows,cols=len(a),len(a[0]); r=0
    for c in range(cols):
        p=next((i for i in range(r,rows) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]; d=a[r][c]
        for j in range(c,cols):a[r][j]/=d
        for i in range(r+1,rows):
            t=a[i][c]
            if t:
                for j in range(c,cols):a[i][j]-=t*a[r][j]
        r+=1
        if r==rows:break
    return r

def inv(a):
    n=len(a); q=[list(map(F,a[i]))+[F(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if q[i][c]);q[c],q[p]=q[p],q[c]
        d=q[c][c]
        for j in range(2*n):q[c][j]/=d
        for i in range(n):
            if i==c:continue
            t=q[i][c]
            if t:
                for j in range(2*n):q[i][j]-=t*q[c][j]
    return [row[n:] for row in q]

def expected(m,n,w):
    N=m+n; p=[[F(0) for j in range(N)] for i in range(N)]
    blocks=([[1],list(range(m))[:1]+list(range(2,m)),list(range(m,m+n))]
            if w==1 else [[0],[1],list(range(2,m)),[m],list(range(m+1,m+n))])
    # For the uniform graph, trap at a1: exclude a1 from the A-other block.
    for block in blocks:
        for i in block:
            for j in block:p[i][j]=F(1,len(block))
    return p

def run(m,n,w):
    N=m+n
    h=[[F(0) for _ in range(N)] for _ in range(N)]
    for a in range(m):
        for b in range(n):
            h[a][m+b]=h[m+b][a]=w if (a,b)==(0,0) else F(1)
    v=[F(int(i==1)) for i in range(N)];basis=[]
    for _ in range(N+1):
        trial=basis+[v]
        if rank([[z[i] for z in trial] for i in range(N)])==len(trial):basis.append(v)
        else:break
        v=[sum(h[i][j]*v[j] for j in range(N)) for i in range(N)]
    r=len(basis)
    gram=[[sum(basis[i][k]*basis[j][k] for k in range(N)) for j in range(r)] for i in range(r)]
    ginv=inv(gram)
    p=[[sum(basis[s][i]*ginv[s][t]*basis[t][j] for s in range(r) for t in range(r)) for j in range(N)] for i in range(N)]
    assert r==(3 if w==1 else 5),(m,n,w,r)
    assert p==expected(m,n,w),(m,n,w)
    return r

if __name__=='__main__':
    count=0
    for m in range(3,7):
        for n in range(3,7):
            for w in [F(1),F(1,2),F(2),F(3,2)]:
                run(m,n,w);count+=1
    print('EXACT_BRIGHT_PROJECTOR_CHECKS_PASSED',count)
