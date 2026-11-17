"""Exhaustive finite checks of a full-clock inverse law for three-state excitation.
Standard library only. These are finite tests, not a substitute for the all-size proof.
"""
from itertools import product

def cycle_power(n,p):
    return [tuple(sorted({(i+j)%n for j in range(-p,p+1) if j and (i+j)%n !=i})) for i in range(n)]

def complete(n):
    return [tuple(j for j in range(n) if j != i) for i in range(n)]

def complete_tripartite(a,b,c):
    sizes=[a,b,c]
    part=sum(([k]*s for k,s in enumerate(sizes)),[])
    return [tuple(j for j in range(sum(sizes)) if part[i]!=part[j]) for i in range(sum(sizes))]

def step(x,N,theta):
    return tuple((a+1)%3 if a else int(sum(x[j]==1 for j in N[i]) >= theta) for i,a in enumerate(x))

def full_clock(x,N,theta):
    return all(sum(x[j]==(v+1)%3 for j in N[i]) >= theta for i,v in enumerate(x))

def pred_count_clock(y,N,theta):
    return 1<<sum(v==0 and sum(y[j]==2 for j in N[i])<theta for i,v in enumerate(y))

def check(label,N,theta):
    n=len(N)
    indegrees={}
    full=[]
    for x in product(range(3),repeat=n):
        y=step(x,N,theta)
        indegrees[y]=indegrees.get(y,0)+1
        if full_clock(x,N,theta):
            full.append(x)
            assert step(x,N,theta)==tuple((v+1)%3 for v in x)
    for y in full:
        assert indegrees.get(y,0)==pred_count_clock(y,N,theta)
        if len(set(map(len,N)))==1 and len(N[0])==2*theta:
            for i,v in enumerate(y):
                assert sum(y[j]==(v+1)%3 for j in N[i])==theta
                assert sum(y[j]==(v-1)%3 for j in N[i])==theta
            assert indegrees[y]==1
    return (label,n,theta,len(full),sum(indegrees[y] for y in full),max((indegrees[y] for y in full),default=0))

if __name__=='__main__':
    cases=[('C6 critical',cycle_power(6,1),1),('C9 critical',cycle_power(9,1),1),
           ('C6 squared critical',cycle_power(6,2),2),
           ('C9 squared critical',cycle_power(9,2),2),
           ('K5 critical',complete(5),2),('K7 critical',complete(7),3),
           ('K222 critical',complete_tripartite(2,2,2),2),
           ('C6 squared subcritical',cycle_power(6,2),1)]
    for label,N,theta in cases:
        print(*check(label,N,theta))
    N=cycle_power(6,2)
    y=(0,0,0,1,1,2)
    p=tuple((v-1)%3 for v in y)
    q=list(p);q[2]=0;q=tuple(q)
    assert full_clock(y,N,1) and p!=q and step(p,N,1)==step(q,N,1)==y
    assert step(y,N,1)==tuple((v+1)%3 for v in y)
    print('subcritical witness y,p,q:',y,p,q)
    print('ALL CHECKS PASSED')
