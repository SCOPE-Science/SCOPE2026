#!/usr/bin/env python3
"""Direct bitwise synchronous neighbor sums and exhaustive orbit decomposition."""
from collections import Counter

def analytic(m,n):
    d=m+n+m*n
    if m%2==0 and n%2==0:
        exps=[0,d-2*(m+n-1),d-(m+n),d-2,d]
        return {1:1},exps,4
    if m%2 and n%2:
        s=m+n-2; b=(m-1)*(n-1)
        return {1:2**s,2:(2**(2*s)-2**s)//2},[2*s,2*s+b+1,2*s+b+2,d],3
    e,o=(m,n) if not m%2 else (n,m)
    b=(e-2)*(o-1)+1
    return {1:2**(e-1),2:(2**(2*e-2)-2**(e-1))//2,4:(2**(2*e)-2**(2*e-2))//4}, [2*e,2*e+b+(o-1),2*e+b+2*(o-1),d],3

def main():
    cases=0;states=0
    for m,n in [(2,2),(2,3),(3,2),(2,4),(3,3),(2,5),(3,4),(4,3)]:
        d=m+n+m*n
        neighbors=[0]*d
        for i in range(m):
            for j in range(n):
                edge=m+n+i*n+j
                for v in (i,m+j):
                    neighbors[edge]|=1<<v
                    neighbors[v]|=1<<edge
        def evolve(x):
            out=0
            for u,mask in enumerate(neighbors):
                out |= ((x&mask).bit_count()&1)<<u
            return out
        # Exhaust every trajectory, independently of matrix-power logic.
        seen={}; orbit_types=Counter(); depths=Counter()
        for initial in range(1<<d):
            x=initial;path=[];pos={}
            while x not in seen and x not in pos:
                pos[x]=len(path);path.append(x);x=evolve(x)
            if x in seen:
                depth,period,orbit=seen[x]
                for y in reversed(path):
                    depth+=1;seen[y]=(depth,period,orbit)
            else:
                a=pos[x];cycle=tuple(path[a:]); period=len(cycle)
                for y in cycle:seen[y]=(0,period,min(cycle))
                for k in range(a-1,-1,-1):seen[path[k]]=(a-k,period,min(cycle))
        for x,(depth,period,orb) in seen.items():
            depths[depth]+=1
            if depth==0:orbit_types[period]+=1
        predicted,exps,maxdepth=analytic(m,n)
        predicted_counts={p:orbits*p for p,orbits in predicted.items()}
        assert dict(orbit_types)==predicted_counts,(m,n,orbit_types,predicted_counts)
        cum=0
        for t,exp in enumerate(exps):
            cum+=depths[t]
            assert cum==2**exp,(m,n,t,cum,2**exp)
        assert max(depths)==maxdepth,(m,n,max(depths),maxdepth)
        assert len(seen)==1<<d
        cases+=1;states+=1<<d
    print('STATE_CHECK_OK',cases,'graphs',states,'initial states, exact depth and primitive orbit counts')
if __name__=='__main__':main()
