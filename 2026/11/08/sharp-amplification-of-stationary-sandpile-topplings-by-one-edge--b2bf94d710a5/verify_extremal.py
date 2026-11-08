"""Independent exhaustive rational check of sharp edge-addition bound.
Enumerates all labeled trees on vertices {sink,2,...,N+1}, adds a
source leaf 1 at the sink, then tests every available single edge.
No third-party packages.
"""
from fractions import Fraction
from itertools import combinations,product
from collections import defaultdict

def tree_edges(vertices,code):
    n=len(vertices)
    deg={v:1 for v in vertices}
    for v in code: deg[v]+=1
    edges=[]
    for v in code:
        leaf=min(v for v in vertices if deg[v]==1)
        edges.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    a,b=[v for v in vertices if deg[v]==1]
    return edges+[(a,b)]

def solve_mean(N,edges):
    size=N+1
    A=[[0]*size for _ in range(size)]
    for a,b in edges:
        if a:A[a-1][a-1]+=1
        if b:A[b-1][b-1]+=1
        if a and b:
            A[a-1][b-1]-=1;A[b-1][a-1]-=1
    M=[[Fraction(z) for z in row]+[Fraction(i==0)] for i,row in enumerate(A)]
    for col in range(size):
        pivot=next(j for j in range(col,size) if M[j][col])
        M[col],M[pivot]=M[pivot],M[col]
        scale=M[col][col]
        for k in range(col,size+1):M[col][k]/=scale
        for j in range(size):
            if j==col:continue
            scale=M[j][col]
            if scale:
                for k in range(col,size+1):M[j][k]-=scale*M[col][k]
    return sum(row[-1] for row in M)

def predicted(N,d):
    return Fraction(1)+Fraction(d*N-d*(d-1)//2-1,d+2)

def main():
    calls=0
    for N in range(1,6):
        v=[0]+list(range(2,N+2))
        theoretical=max(predicted(N,d) for d in range(1,N+1))
        global_max=Fraction(0)
        for code in product(v,repeat=N-1):
            base=tree_edges(v,code)+[(0,1)]
            base_set={tuple(sorted(e)) for e in base}
            assert solve_mean(N,base)==1
            for a,b in combinations(range(N+2),2):
                if (a,b) in base_set:continue
                m=solve_mean(N,base+[(a,b)])
                assert m>=0
                global_max=max(global_max,m)
                calls+=1
        assert global_max==theoretical,(N,theoretical,global_max)
        print('N=',N,'max=',theoretical,'edge tests to date=',calls)
    print('PASS exhaustive all rooted source-leaf labeled trees N<=5, all missing edges, with independent rational Green solve; tests=',calls)
if __name__=='__main__':main()
