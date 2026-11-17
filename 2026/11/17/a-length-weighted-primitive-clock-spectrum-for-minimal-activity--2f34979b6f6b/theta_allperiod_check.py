#!/usr/bin/env python3
"""Independent phase and microscopic checks for activity-one theta chip firing."""
from itertools import product

def graph(arms):
    n=sum(arms)-1
    N=[set() for _ in range(n)]
    k=2
    for L in arms:
        seq=[0]+list(range(k,k+L-1))+[1]
        k+=L-1
        for u,v in zip(seq,seq[1:]):N[u].add(v);N[v].add(u)
    assert k==n
    return [tuple(sorted(a)) for a in N]

def predicted(arms,p):
    return 2*sum(arms[i] for i in range(3) if (sum(arms)-arms[i])%p==0)

def phase_count(arms,p):
    N=graph(arms);n=len(N)
    total=0
    for phase in product(range(p),repeat=n):
        weight=1
        for v in range(n):
            a=sum(phase[w]==(phase[v]-1)%p for w in N[v])
            if not a:weight=0;break
            weight*=a
        total+=weight
    assert total%p==0
    return total//p

def direct_count(arms,p):
    N=graph(arms);n=len(N);d=[len(q) for q in N]
    count=0
    for x in product(*(range(2*v) for v in d)):
        y=x;activity=[0]*n
        for _ in range(p):
            fire=[int(y[v]>=d[v]) for v in range(n)]
            for v in range(n):activity[v]+=fire[v]
            y=tuple(y[v]-d[v]*fire[v]+sum(fire[w] for w in N[v]) for v in range(n))
        if y==x and all(z==1 for z in activity):count+=1
    assert count%p==0
    return count//p

if __name__=='__main__':
    phase_cases=0;direct_cases=0;microscopic_states=0
    for arms in ((1,2,2),(1,2,3),(1,2,4),(1,3,3),(2,2,2),(2,2,3),(2,3,3),(3,3,3)):
        for p in range(3,9):
            if p**(sum(arms)-1)>100000:continue
            found=phase_count(arms,p)
            want=predicted(arms,p)
            assert found==want,(arms,p,found,want)
            phase_cases+=1
        for p in range(3,7):
            found=direct_count(arms,p)
            want=predicted(arms,p)
            assert found==want,(arms,p,found,want)
            direct_cases+=1
            microscopic_states+=6*6*4**(sum(arms)-3)
    print('THETA_ALL_PERIODS_ACTIVITY_ONE_CHECK_PASSED',
          'phase_cases',phase_cases,'microscopic_cases',direct_cases,
          'microscopic_states',microscopic_states)
    for arms in ((1,2,3),(1,2,4),(1,3,3),(2,3,4),(3,3,3)):
        print('arms',arms,'p3_to_p10',[predicted(arms,p) for p in range(3,11)])
