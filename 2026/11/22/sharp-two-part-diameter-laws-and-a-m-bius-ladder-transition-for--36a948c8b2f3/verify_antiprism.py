#!/usr/bin/env python3
"""Independent finite checks of exact two-cluster antiprism formulas.
The quantified theorem is proved analytically in RESULT.md; these checks are corroboration.
"""
import math
from collections import deque


def pts(n, u):
    h=math.sqrt(u)
    r=math.sqrt(1-u)
    return [(r*math.cos(2*math.pi*j/n),r*math.sin(2*math.pi*j/n),h) for j in range(n)] + [
       (r*math.cos((2*j+1)*math.pi/n),r*math.sin((2*j+1)*math.pi/n),-h) for j in range(n)]

def pair_distances(n,u):
    p=pts(n,u)
    return [(i,j,sum((p[i][k]-p[j][k])**2 for k in range(3))) for i in range(2*n) for j in range(i+1,2*n)]

def bipartite(n,edges):
    adj=[[] for _ in range(n)]
    for i,j,_ in edges:
        adj[i].append(j);adj[j].append(i)
    color=[-1]*n
    for z in range(n):
        if color[z]>=0: continue
        color[z]=0;q=deque([z])
        while q:
            i=q.popleft()
            for j in adj[i]:
                if color[j]==-1: color[j]=1-color[i];q.append(j)
                elif color[j]==color[i]: return False
    return True

def test(n,u,critical=False):
    D=pair_distances(n,u)
    s=math.sin(math.pi/(2*n))
    if n%2:
        A=4*(1-u)*(1-s*s)
        B=4.0
        v=A;w=B
    else:
        A=4*(1-u)
        B=4*(u+(1-u)*(1-s*s))
        v=min(A,B);w=max(A,B)
    tol=1e-10
    assert abs(max(d for i,j,d in D)-w)<tol,(n,u,'diameter')
    # > v admits two colors; >= v does not; an exact two-clustering optimum is v.
    strict=[(i,j,d) for i,j,d in D if d>v+tol]
    inclusive=[(i,j,d) for i,j,d in D if d>=v-tol]
    assert bipartite(2*n, strict),(n,u,'upper bound bipartite')
    assert not bipartite(2*n,inclusive),(n,u,'lower bound odd cycle')
    top=[(i,j,d) for i,j,d in D if abs(d-w)<tol]
    if n%2:
        assert len(top)==n and bipartite(2*n,top)
    elif critical:
        assert len(top)==3*n and not bipartite(2*n,top)
    elif A>B: assert len(top)==n and bipartite(2*n,top)
    else: assert len(top)==2*n and bipartite(2*n,top)
    return len(D)


def main():
    tries=0;total=0
    for n in range(4,42,2):
        s=math.sin(math.pi/(2*n));qc=s*s/(1+s*s)
        vals=[qc*(1-0.001),qc*(1+0.001),qc*0.3,qc*1.8,0.5,0.9]
        for u in vals:
            total+=test(n,u);tries+=1
        # exact tie classified analytically; floating-point geometry checked within 1e-10
        total+=test(n,qc,critical=True); tries+=1
    for n in range(3,42,2):
        for u in [0.00003,0.01,0.1,0.5,0.93,0.999]:
            total+=test(n,u);tries+=1
    print('FINITE_METRIC_CHECK_OK', 'cases',tries,'pair_checks',total)

if __name__=='__main__':main()
