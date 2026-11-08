#!/usr/bin/env python3
"""Enumerate minimum graph-burning schedules on near-square cycles via cyclic center gaps."""
from itertools import permutations, combinations, product
from math import factorial

def gap_vectors(k,d):
    if d==0:
        yield (0,)*k
    if d==1:
        for a in range(k):
            x=[0]*k; x[a]=1; yield tuple(x)
    if d==2:
        for a,b in combinations(range(k),2):
            x=[0]*k; x[a]=x[b]=1;yield tuple(x)
        for a in range(k):
            x=[0]*k; x[a]=2; yield tuple(x)

def cyclic_center_schedules(k,d):
    n=k*k-d
    # In cyclic order start at the unique radius-zero center.
    for v in range(n):
        for perm in permutations(range(1,k)):
            labels=(0,)+perm
            for gaps in gap_vectors(k,d):
                # t=2 is forbidden on either boundary adjacent to radius zero.
                if gaps[0]==2 or gaps[-1]==2:continue
                pos=[v]
                for j in range(k-1):
                    a,b=labels[j:j+2]
                    pos.append((pos[-1]+a+b+1-gaps[j])%n)
                close_dist=(pos[0]-pos[-1])%n
                assert close_dist ==labels[-1]+labels[0]+1-gaps[-1]
                sched=[0]*k
                for label,c in zip(labels,pos):
                    sched[k-1-label]=c
                yield tuple(sched)

def valid(k,d,sched):
    n=k*k-d
    if len(set(sched))!=k:return False
    for i in range(k):
        for j in range(i+1,k):
            dd=abs(sched[i]-sched[j]);dd=min(dd,n-dd)
            if dd<j-i:return False
    union=set()
    for i,c in enumerate(sched):
        r=k-1-i
        union.update((c+u)%n for u in range(-r,r+1))
    return len(union)==n

def brute(k,d):
    n=k*k-d;sol=set()
    for sched in product(range(n), repeat=k):
        if valid(k,d,sched):sol.add(sched)
    return sol

def predicted(k,d):
    n=k*k-d
    a={0:1,1:k,2:(k*k+k-4)//2}[d]
    return n*factorial(k-1)*a

def main():
    for k in range(3,8):
        for d in range(3):
            sols=set(cyclic_center_schedules(k,d))
            expect=predicted(k,d)
            assert len(sols)==expect,(k,d,len(sols),expect)
            assert all(valid(k,d,s) for s in sols),(k,d,'invalid generated')
            if k<=4:
                true=brute(k,d)
                assert sols==true,(k,d,'mismatch',len(sols),len(true))
            print(f'k={k} deficit={d} n={k*k-d} count={len(sols)} expected={expect} valid=YES direct_exhaustive={k<=4}',flush=True)
    print('CONSTRUCT_CHECK_OK')
if __name__=='__main__':main()
