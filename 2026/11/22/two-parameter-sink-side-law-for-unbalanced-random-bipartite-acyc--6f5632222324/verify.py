"""Exact small-instance checks for sink laws of uniform bipartite DAG orientations.
Run: python3 verify.py. Python standard library only.
The finite checks do not certify the asymptotic result.
"""
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def stirling(n,k):
    if n == k == 0: return 1
    if n < 0 or k < 0 or k > n or n == 0 or k == 0: return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)

def count_by_last_block(a,b):
    """Returns arrays for sink side A and B indexed by sink multiplicity."""
    na=[0]*(a+b+1); nb=[0]*(a+b+1)
    for k in range(1,a+1):
        base=0
        for j in range(1,a+b+1):
            base += factorial(j-1)**2*stirling(a-k,j-1)*stirling(b,j-1)
            base += factorial(j-1)*factorial(j)*stirling(a-k,j-1)*stirling(b,j)
        na[k]=comb(a,k)*base
    for k in range(1,b+1):
        base=0
        for j in range(1,a+b+1):
            base += factorial(j-1)**2*stirling(b-k,j-1)*stirling(a,j-1)
            base += factorial(j-1)*factorial(j)*stirling(b-k,j-1)*stirling(a,j)
        nb[k]=comb(b,k)*base
    return na,nb

def count_all(a,b):
    return sum(factorial(j)**2*stirling(a+1,j+1)*stirling(b+1,j+1)
               for j in range(0,min(a,b)+1))

def brute(a,b):
    """Independently enumerate all directed orientations and test DAG by Kahn."""
    N=a+b; edges=[(i,a+j) for i in range(a) for j in range(b)]
    ca=[0]*(N+1);cb=[0]*(N+1)
    for mask in range(1<<len(edges)):
        outgoing=[[] for _ in range(N)]; indegree=[0]*N
        for idx,(i,j) in enumerate(edges):
            u,v=((i,j) if (mask>>idx)&1 else (j,i))
            outgoing[u].append(v);indegree[v]+=1
        ready=[i for i in range(N) if indegree[i]==0];seen=0
        while ready:
            u=ready.pop();seen+=1
            for v in outgoing[u]:
                indegree[v]-=1
                if indegree[v]==0:ready.append(v)
        if seen!=N:continue
        sinks=[i for i in range(N) if not outgoing[i]]
        assert sinks and all(i<a for i in sinks) or sinks and all(i>=a for i in sinks)
        if sinks[0]<a: ca[len(sinks)]+=1
        else:cb[len(sinks)]+=1
    return ca,cb

def main():
    cases=0
    for a in range(1,10):
        for b in range(1,10):
            ca,cb=count_by_last_block(a,b)
            assert sum(ca)+sum(cb)==count_all(a,b),(a,b)
            cases+=1
    exhaustive=0
    for a in range(1,5):
        for b in range(1,5):
            if a*b>12:continue
            exact=count_by_last_block(a,b);independent=brute(a,b)
            assert exact==independent,(a,b,exact,independent)
            exhaustive+=1
    print(f"PASS: {cases} Stirling-count identities; {exhaustive} independent exhaustive DAG enumerations")

if __name__=='__main__':main()
