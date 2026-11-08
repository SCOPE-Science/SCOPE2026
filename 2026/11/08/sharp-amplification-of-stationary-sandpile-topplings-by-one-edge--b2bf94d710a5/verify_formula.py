"""Exhaustive independent check of the exact rooted-subtree formula.
All trees on vertices 0,2,...,N+1 (0 sink), N<=5,
and all possible edges from the source leaf 1 to an old nonroot vertex.
Uses exact Fraction Gaussian elimination in a separate module.
"""
from fractions import Fraction
from itertools import product
from verify_extremal import tree_edges, solve_mean, predicted

def rooted_data(N,edges):
    adj=[[] for _ in range(N+2)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    parent={0:-1};order=[0]
    for u in order:
        for v in adj[u]:
            if v not in parent:
                parent[v]=u;order.append(v)
    size={v:1 for v in order}
    for v in order[:0:-1]:size[parent[v]]+=size[v]
    return parent,size

def main():
    tested=0
    for N in range(1,6):
        vs=[0]+list(range(2,N+2))
        for code in product(vs,repeat=N-1):
            edges=tree_edges(vs,code)
            parent,size=rooted_data(N,edges)
            for x in range(2,N+2):
                acc=0;path=[];q=x
                while q:
                    path.append(q);acc+=size[q];q=parent[q]
                d=len(path)
                candidate=edges+[(0,1),(1,x)]
                actual=solve_mean(N,candidate)
                expected=Fraction(1)+Fraction(acc-1,d+2)
                assert actual==expected,(N,edges,x,actual,expected)
                assert actual<=max(predicted(N,j) for j in range(1,N+1))
                tested+=1
    for N in range(1,500):
        ds=list(range(1,N+1))
        d0=next(d for d in ds if (d+2)*(d+3)>=4*(N+2))
        assert predicted(N,d0)==max(predicted(N,d) for d in ds)
    print(f'PASS exact rooted path formula over {tested} all tree-source-chord instances (N<=5); integer maximizer for N<=499')
if __name__=='__main__':main()
