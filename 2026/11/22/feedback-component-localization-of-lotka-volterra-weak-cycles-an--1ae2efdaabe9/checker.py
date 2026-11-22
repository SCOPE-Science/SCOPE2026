"""Exact finite checks for a feed-forward Lotka--Volterra weak-graph result.
Finite tests supplement, but do not replace, the proof for all parameters.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def solve(a,b):
    n=len(b)
    x=[[F(a[i][j]) for j in range(n)]+[F(b[i])] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if x[i][j]!=0),None)
        if p is None:return None
        x[j],x[p]=x[p],x[j]
        c=x[j][j]
        x[j]=[t/c for t in x[j]]
        for i in range(n):
            if i!=j:
                c=x[i][j]
                x[i]=[t-c*s for t,s in zip(x[i],x[j])]
    return [row[-1] for row in x]

def equilibria(a,b):
    n=len(b)
    out=[]
    for mask in range(1<<n):
        inds=[j for j in range(n) if mask>>j&1]
        c=solve([[a[i][j] for j in inds] for i in inds],[-b[i] for i in inds]) if inds else []
        if c is None or any(t<=0 for t in c):continue
        point=[F(0)]*n
        for i,t in zip(inds,c):point[i]=t
        out.append(tuple(point))
    return out

def weak_edges(a,b,eq):
    n=len(b)
    edges=[]
    for i,x in enumerate(eq):
        for j,y in enumerate(eq):
            if i==j:continue
            entering=[k for k in range(n) if x[k]==0 and y[k]>0]
            leaving=[k for k in range(n) if x[k]>0 and y[k]==0]
            rx=lambda k:b[k]+sum(a[k][t]*x[t] for t in range(n))
            ry=lambda k:b[k]+sum(a[k][t]*y[t] for t in range(n))
            if all(rx(k)>=0 for k in entering) and all(ry(k)<=0 for k in leaving):
                edges.append((i,j))
    return edges

def cyclic(size,edges):
    nbr=[[] for _ in range(size)]
    for i,j in edges:nbr[i].append(j)
    color=[0]*size
    def dfs(v):
        color[v]=1
        for w in nbr[v]:
            if color[w]==1:return True
            if color[w]==0 and dfs(w):return True
        color[v]=2
        return False
    return any(color[v]==0 and dfs(v) for v in range(size))

def sample(blocks,rng):
    n=sum(blocks)
    a=[[F(0) for j in range(n)] for i in range(n)]
    offset=0
    for s in blocks:
        if s==1:
            a[offset][offset]=F(-rng.randint(1,4))
        elif s==2:
            a[offset][offset]=-F(rng.randint(1,4))
            a[offset+1][offset+1]=-F(rng.randint(1,4))
            # Include both reciprocal (when determinant stays positive)
            # and antagonistic two-species interactions.
            p=rng.randint(-8,8)
            q=rng.randint(-8,8)
            if p*q>=int(a[offset][offset]*a[offset+1][offset+1]):
                q=-q if q else -1
            assert a[offset][offset]*a[offset+1][offset+1]-p*q>0
            a[offset][offset+1]=F(p)
            a[offset+1][offset]=F(q)
        else:raise ValueError('only blocks of size <=2')
        offset+=s
    p=0
    for k,s in enumerate(blocks):
        q=0
        for l,t in enumerate(blocks):
            if k>l:
                for i in range(p,p+s):
                    for j in range(q,q+t):
                        a[i][j]=F(rng.choice([-50,-10,-1,0,1,10,50]))
            q+=t
        p+=s
    b=[F(rng.randint(-4,4)) for _ in range(n)]
    return a,b

def main():
    rng=Random(283710)
    sample_counts={}
    for blocks in [(1,1,1),(2,1),(1,2),(2,2),(1,1,2),(2,2,1)]:
        for sample_index in range(110):
            a,b=sample(blocks,rng)
            eq=equilibria(a,b)
            edges=weak_edges(a,b,eq)
            assert not cyclic(len(eq),edges),('UNEXPECTED_CYCLE',blocks,a,b,eq,edges)
        sample_counts[tuple(blocks)]=110
    # Explicit 2+2 example: arbitrary feed-forward coupling is compatible with diagonal Lyapunov stability.
    a=[[-1,2,0,0],[-2,-1,0,0],[100,0,-1,2],[0,100,-2,-1]]
    b=[1,1,1,1]
    eq=equilibria(a,b)
    assert not cyclic(len(eq),weak_edges(a,b,eq))
    h=[10000,10000,1,1]
    g=[[-h[i]*a[i][j]-h[j]*a[j][i] for j in range(4)] for i in range(4)]
    for j in range(4):
        assert g[j][j]>0
    assert g[0][2]==-100 and g[1][3]==-100
    assert g[0][0]*g[2][2]-g[0][2]**2==30000
    assert g[1][1]*g[3][3]-g[1][3]**2==30000
    # Feedback SCC of size 3: known rock-paper-scissors admits a weak 3-cycle.
    a3=[[-1,-2,2],[2,-1,-2],[-2,2,-1]]
    b3=[1,1,1]
    eq3=equilibria(a3,b3)
    e3=weak_edges(a3,b3,eq3)
    assert cyclic(len(eq3),e3)
    loc={p:i for i,p in enumerate(eq3)}
    one=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
    assert all((loc[one[i]],loc[one[(i+1)%3]]) in e3 for i in range(3))
    print('PASS: 660 nondegenerate block-triangular samples (exact rational equilibria/weak graphs)')
    print('PASS: exact four-dimensional strong-coupling and diagonal Lyapunov checks')
    print('PASS: three-dimensional sharpness example with a directed singleton 3-cycle')
    print('FINITE CHECKS DO NOT PROVE THE GENERAL THEOREM')

if __name__=='__main__':main()
