"""Exact coefficient and sign checks for RK4 on positive weighted trees.

Uses only the Python standard library. Finite tests supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def mul(A, B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def tree_test(n, edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    neigh=[[] for _ in range(n)]
    for i,j,w in edges:
        L[i][i]+=w;L[j][j]+=w
        L[i][j]-=w;L[j][i]-=w
        neigh[i].append((j,w));neigh[j].append((i,w))
    d=[L[i][i] for i in range(n)]
    A=[[(-L[i][j] if i!=j else d[i]) for j in range(n)] for i in range(n)]
    powers={1:A}
    for k in range(2,5):powers[k]=mul(powers[k-1],A)
    def dist(i,j):
        frontier=[i]; seen={i}; depth=0
        while frontier:
            if j in frontier:return depth
            seen.update(frontier)
            frontier=[z for v in frontier for z,w in neigh[v] if z not in seen]
            depth+=1
        return None
    checks=0
    for i in range(n):
        for j in range(i+1,n):
            ell=dist(i,j)
            if ell==1:
                w=-L[i][j]
                S=d[i]+d[j]
                C=powers[3][i][j]/w
                D=powers[4][i][j]/w
                U=sum(v*v for z,v in neigh[i] if z!=j)
                V=sum(v*v for z,v in neigh[j] if z!=i)
                assert powers[2][i][j]/w==S
                assert C==d[i]**2+d[i]*d[j]+d[j]**2+w*w+U+V
                predicted=S*(d[i]**2+d[j]**2+2*w*w+U+V)
                predicted+=sum(v*v*(d[i]+d[z]) for z,v in neigh[i] if z!=j)
                predicted+=sum(v*v*(d[j]+d[z]) for z,v in neigh[j] if z!=i)
                assert D==predicted
                assert C*C < 2*S*D
                assert 4*C*C < 9*S*D
            elif ell==2:
                path=[v for v,w in neigh[i] if any(z==j for z,_ in neigh[v])]
                assert len(path)==1
                k=path[0];u=-L[i][k];v=-L[k][j]
                S=d[i]+d[k]+d[j]
                P=powers[4][i][j]/(u*v)
                assert powers[2][i][j]==u*v
                assert powers[3][i][j]==u*v*S
                assert 3*P>S*S
            elif ell==3:
                # Unique 3-edge path
                paths=[]
                for x,_ in neigh[i]:
                    for y,_ in neigh[x]:
                        if y!=i and any(z==j for z,_ in neigh[y]):paths.append((i,x,y,j))
                assert len(paths)==1
                vs=paths[0]
                u=F(1)
                for a,b in zip(vs,vs[1:]):u*=(-L[a][b])
                assert powers[3][i][j]==u
                assert powers[4][i][j]==u*sum(d[k] for k in vs)
            elif ell==4:
                assert powers[4][i][j]>0
                assert powers[3][i][j]==0
            else:
                assert powers[4][i][j]==0
            checks+=1
    return checks

rng=Random(20261119)
trees=0;pairs=0
for n in range(2,13):
    for _ in range(55):
        edges=[(j,rng.randrange(j),F(rng.randrange(1,50),rng.randrange(1,35))) for j in range(1,n)]
        pairs+=tree_test(n,edges);trees+=1
for n in range(2,10):
    for a in (F(1,100),F(1),F(100)):
        edges=[(j,j-1, a if j%2==1 else F(1,a)) for j in range(1,n)]
        pairs+=tree_test(n,edges);trees+=1
print(f'VERIFY_OK trees={trees} exact_vertex_pairs={pairs}')
