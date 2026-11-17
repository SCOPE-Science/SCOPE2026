#!/usr/bin/env python3
"""Exhaustive finite-state validation of reversible vs transient prisms, Python stdlib."""
from collections import Counter
from verify_power_two import fixed as polynomial_fixed

def step(x,n):
    y=0
    for rail in (0,1):
        for j in range(n):
            k=rail*n+j
            bit=((x>>(rail*n+(j-1)%n))^(x>>(rail*n+(j+1)%n))^(x>>((1-rail)*n+j)))&1
            y|=bit<<k
    return y

def predicted_hist(n):
    total=1<<(2*n)
    if n%3:return {0:total}
    v=n&-n;D=2 if v==1 else v;periodic_dim=2*n-4*v
    def nullity(t):return (0 if t==0 else 2 if t==1 else 4) if v==1 else 4*min(t,v)
    cumulative=[1<<(periodic_dim+nullity(t)) for t in range(D+1)]
    return {t:cumulative[t]-(cumulative[t-1] if t else 0) for t in range(D+1)}

def main():
    allcount=0
    for n in range(3,9):
        N=1<<(2*n)
        succ=[step(x,n) for x in range(N)]
        # Follow paths using cached smallest step to cycle; no matrix methods.
        distance={};cycles={}
        for x in range(N):
            if x in distance:continue
            path=[];at={};y=x
            while y not in at and y not in distance:
                at[y]=len(path);path.append(y);y=succ[y]
            if y in at:
                st=at[y];cycle=path[st:];period=len(cycle)
                for node in cycle:distance[node]=0;cycles[node]=period
                path=path[:st]
            for node in reversed(path):
                distance[node]=distance[y]+1
                cycles[node]=cycles[y]
                y=node
        hist=dict(sorted(Counter(distance.values()).items()))
        want=predicted_hist(n)
        assert hist==want,(n,hist,want)
        assert all(cycles[x]>=1 for x in range(N))
        fixed_at={t:sum(1 for x in range(N) if distance[x]==0 and t%cycles[x]==0) for t in range(1,13)}
        for t in range(1,13):
            assert fixed_at[t] == polynomial_fixed(n,t),(n,t,fixed_at[t],polynomial_fixed(n,t))
        # Independent exact polynomial GCD counts cover every tested temporal period.
        if n==3: assert fixed_at[1]==2 and fixed_at[2]==4
        if n==6: assert fixed_at[1]==4 and fixed_at[2]==16
        print('n',n,'states',N,'first_periodic_hist',hist,'periodic_points',sum(distance[x]==0 for x in distance),'fixed_first_six',tuple(fixed_at[t] for t in range(1,7)))
        allcount+=N
    print('state_exhaustion_passed',allcount)
if __name__=='__main__':main()
