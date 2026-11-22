"""Reproducible exact tests for height of two-predecessor attachment trees.
No external packages required. The analytic proof establishes all-size properties.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb

checks=0

def check(statement):
    global checks
    assert statement
    checks += 1

def plus(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return trim(out)

def scale(a,x):return trim([v*x for v in a])
def shift(a,k=1):return [Q(0)]*k+a
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def recurrence(prob):
    # prob[i-2] = probability that new vertex i attaches to i-1.
    a=[Q(1)];b=[Q(0),Q(1)]
    if len(prob)==0:return b
    for p in prob:
        a,b=b,shift(plus(scale(b,p),scale(a,1-p)))
    return b

def enumerate_heights(prob):
    n=len(prob)+1
    ans=[Q(0)]*(n+1)
    for choices in product([0,1], repeat=len(prob)):
        depth=[0,1];weight=Q(1)
        for i,(p,bit) in enumerate(zip(prob,choices),start=2):
            if bit:
                depth.append(depth[i-1]+1);weight*=p
            else:
                depth.append(depth[i-2]+1);weight*=1-p
        ans[max(depth)]+=weight
    return trim(ans)

def variance(p):
    mean=sum(i*x for i,x in enumerate(p))
    return sum(Q(i*i)*x for i,x in enumerate(p))-mean*mean,mean

def lower_benchmark(n,mu):
    j=mu.numerator//mu.denominator
    t=mu-j
    a=[Q(0)]*(n+1)
    a[j]=1-t
    if t:a[j+1]=t
    return trim(a)

def benchmark(n,m):
    r=n//2
    a=m/Q(r)
    v=[Q(0)]*(n+1)
    for k in range(r+1):v[n-r+k]=Q(comb(r,k))*a**k*(1-a)**(r-k)
    return trim(v)

# Trees over 2,...,n with heterogeneous attachment probabilities.
for n in range(2,9):
    for pp in product([Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)],repeat=n-1):
        if n>=7 and pp[1:-1] and any(x not in (0,1) for x in pp[1:-1]):
            continue  # keep exact exhaustive tests bounded
        a=recurrence(pp);b=enumerate_heights(pp)
        check(a==b)
        check(sum(a)==1)
        check(all(x>=0 for x in a))
        v,mu=variance(a)
        r=n//2;low=n-r
        check(low<=mu<=n)
        check(v<=(mu-low)*(n-mu)/r)
        opt=benchmark(n,mu-low)
        tiny=lower_benchmark(n,mu)
        # All convex functions on finite integer support equivalent to stop-loss calls.
        for k in range(low,n+1):
            ex=sum(max(j-k,0)*a[j] for j in range(len(a)))
            ey=sum(max(j-k,0)*opt[j] for j in range(len(opt)))
            check(ex<=ey)
            ez=sum(max(j-k,0)*tiny[j] for j in range(len(tiny)))
            check(ez<=ex)
    # Exact surjectivity onto arbitrary independent Bernoulli-sum laws.
    for ts in product([Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)],repeat=n//2):
        pp=tuple(ts[i//2-1] if i%2==0 else Q(1) for i in range(2,n+1))
        dist=[Q(1)]
        for t in ts:dist=plus(scale(dist,1-t),shift(scale(dist,t)))
        check(recurrence(pp)==shift(dist,n-n//2))
    # Sharp schedule: odd i (>=3) deterministic nearest; even i Bernoulli(a).
    for a in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        pp=tuple(a if i%2==0 else Q(1) for i in range(2,n+1))
        check(recurrence(pp)==benchmark(n,(n//2)*a))
    # For every admissible mean on a half-step grid, minimal two-point law.
    for j in range(0,n//2+1):
        for f in [Q(0),Q(1,2)]:
            if j==n//2 and f:continue
            levels=[Q(1)]*j + ([f] if j<n//2 else [])
            levels += [Q(0)]*(n//2-len(levels))
            pp=tuple(levels[i//2-1] if i%2==0 else Q(1) for i in range(2,n+1))
            mu=Q(n-n//2)+Q(j)+f
            check(recurrence(pp)==lower_benchmark(n,mu))

print('PASSED',checks,'exact assertions')
