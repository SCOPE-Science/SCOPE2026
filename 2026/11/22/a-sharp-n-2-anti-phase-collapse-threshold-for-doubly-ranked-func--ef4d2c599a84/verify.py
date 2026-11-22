"""Reproducibility checks for antiphasic two-time rank summaries.

Standard library only. Numerical experiments illustrate but do not prove
any limiting distribution.
"""
import itertools
import math
import random


def rank_vector(values):
    out=[0]*len(values)
    for r,i in enumerate(sorted(range(len(values)),key=lambda j:values[j]),1):out[i]=r
    return out


def score(r,n):
    return math.log((r-.5)/(n-r+.5))


def collapsed(r,s):
    n=len(r)
    a=[(i+j)/2 for i,j in zip(r,s)]
    b=[(score(i,n)+score(j,n))/2 for i,j in zip(r,s)]
    return (all(abs(v-(n+1)/2)<1e-13 for v in a),
            all(abs(v)<1e-12 for v in b))


checks=0
for n in range(2,6):
    r=tuple(range(1,n+1))
    for s in itertools.permutations(r):
        eq=all(i+j==n+1 for i,j in zip(r,s))
        one,two=collapsed(r,s)
        assert one==two==eq
        checks+=1

rng=random.Random(17012026)
for n in (6,12,21):
    for it in range(100):
        x=[rng.gauss(0,1) for _ in range(n)]
        noise=[rng.gauss(0,.2) for _ in range(n)]
        r=rank_vector(x);s=rank_vector([-u+z for u,z in zip(x,noise)])
        crossings=sum((x[i]-x[j])*((-x[i]+noise[i])-(-x[j]+noise[j]))>0
                      for i in range(n) for j in range(i+1,n))
        a,b=collapsed(r,s)
        assert a==b==(crossings==0)
        checks+=1

c=4*math.pi
a=3.0
lam=c*(1+math.exp(-a*a))/(4*math.pi)
target=math.exp(-lam)
for n,reps in ((60,3500),(140,3500),(300,2500),(500,1800)):
    survived=0
    for _ in range(reps):
        x=[rng.gauss(-a,1) for i in range(n//2)]+[rng.gauss(a,1) for i in range(n-n//2)]
        sigma=c/n**2
        y=[t+sigma*rng.gauss(0,1) for t in x]
        order=sorted(range(n),key=x.__getitem__)
        survived+=all(y[order[j]]<y[order[j+1]] for j in range(n-1))
    prop=survived/reps
    print('n=%d trials=%d event_freq=%.6f limit=%.6f error=%.6f'%(n,reps,prop,target,prop-target))
    assert abs(prop-target)<.065
    checks+=1

# Numerical independent integration check of the density overlap.
h=20/8000
v=0.0
for i in range(8001):
    x=-10+i*h
    f=math.exp(-.5*(x+a)**2)/math.sqrt(2*math.pi)
    g=math.exp(-.5*(x-a)**2)/math.sqrt(2*math.pi)
    v+=(0.5 if i in (0,8000) else 1.0)*((f+g)/2)**2*h
assert abs(v-(1+math.exp(-a*a))/(4*math.sqrt(math.pi)))<1e-6
checks+=1
print('all_checks_passed',checks)
