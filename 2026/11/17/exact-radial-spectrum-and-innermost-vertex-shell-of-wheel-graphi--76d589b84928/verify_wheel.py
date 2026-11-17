#!/usr/bin/env python3
"""Independent exhaustive and transfer-matrix verification for wheel zonotope vertex radii.
No external packages. Run: python3 verify_wheel.py
"""
from collections import defaultdict

STATES = [(0,0),(0,1),(1,0),(1,1)]

def transfer(m):
    result=defaultdict(int)
    for start in STATES:
        curr={(start,0,0):1}
        for _ in range(m):
            nxt=defaultdict(int)
            for (state,k,s),w in curr.items():
                a,b=state
                for c,d in STATES:
                    if a!=c and b!=a:
                        continue
                    extr=int((c==1 and b==0 and d==1) or
                             (c==0 and b==1 and d==0))
                    nxt[((c,d),k+c,s+extr)]+=w
            curr=nxt
        for (last,k,s),w in curr.items():
            if last==start:
                result[k,s]+=w
    result[0,0]-=2
    result[m,0]-=2
    return {key:val for key,val in result.items() if val}

def independently_enumerate(m):
    """Build all 2^(2m) graph orientations, reject directed cycles by Kahn's algorithm.
    Count hub indegree and rim extrema from the graph itself; no local cycle shortcut.
    """
    edges=[(i,i+1 if i+1<m else 0) for i in range(m)] + [(i,m) for i in range(m)]
    n=m+1
    count=defaultdict(int)
    radial=defaultdict(int)
    checks=0; valid=0
    for mask in range(1 << len(edges)):
        indeg=[0]*n
        outgoing=[[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            if (mask >> i)&1: u,v=v,u
            outgoing[u].append(v)
            indeg[v]+=1
        tmp=indeg[:]
        queue=[i for i in range(n) if tmp[i]==0]
        head=0
        while head<len(queue):
            u=queue[head];head+=1
            for v in outgoing[u]:
                tmp[v]-=1
                if tmp[v]==0:queue.append(v)
        checks+=1
        if head!=n:continue
        valid+=1
        k=indeg[m]
        s=sum(indeg[i] in (0,3) for i in range(m))
        cnt=(2*k-m)**2 + sum((2*indeg[i]-3)**2 for i in range(m))
        assert cnt==(2*k-m)**2+m+8*s
        count[k,s]+=1
        radial[cnt]+=1
    return count,radial,checks,valid

def main():
    comparisons=0; orient_total=0; acyclic_total=0
    for m in range(4,10):
        got,radial,attempts,acyclic=independently_enumerate(m)
        predicted=transfer(m)
        assert dict(got)==predicted,(m,got,predicted)
        assert sum(predicted.values())==3**m-3
        for k in range(1,m):
            assert predicted.get((k,2),0)==m*k*(m-k),(m,k)
            comparisons+=1
        for k,s in got:
            assert s >= (2 if 0<k<m else 1)
            comparisons+=1
        sq_min=(m+16 if m%2==0 else m+17)
        assert min(radial)==sq_min
        n_min=(m**3//4 if m%2==0 else m*(m*m-1)//2)
        assert radial[sq_min]==n_min
        comparisons+=4
        orient_total+=attempts;acyclic_total+=acyclic
        print(f'm={m}: oriented_edge_assignments={attempts}, vertices={acyclic}, first_squared_norm_times_4={sq_min}, first_shell_size={n_min}, radial_shells={len(radial)}')
    print(f'VERIFIED: {orient_total} directed-edge assignments, {acyclic_total} acyclic orientations, {comparisons} polynomial and boundary assertions')

if __name__=='__main__': main()
