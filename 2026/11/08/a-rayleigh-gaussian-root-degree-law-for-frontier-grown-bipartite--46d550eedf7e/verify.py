"""Exact verification of root-degree law in uniform-frontier growth on K_{2,b}."""
from collections import defaultdict
from fractions import Fraction
from math import comb


def proposed(b):
    out=defaultdict(Fraction)
    surv=Fraction(1)
    for j in range(1,b+1):
        mass=surv*Fraction(j,b)
        for k in range(b-j+1):
            out[j+k]+=mass*Fraction(comb(b-j,k),2**(b-j))
        surv*=Fraction(b-j,b)
    return dict(out)


def state_dp(b):
    # 0: root; 1: other hub; 2..b+1: common neighbors
    full=(1<<(b+2))-1
    states={(1,0):Fraction(1)}
    for _ in range(b+1):
        new=defaultdict(Fraction)
        for (mask,rd),p in states.items():
            if mask==full:
                new[(mask,rd)]+=p
                continue
            edges=[]
            for v in range(2,b+2):
                for u in (0,1):
                    if bool(mask&(1<<u)) != bool(mask&(1<<v)):
                        edges.append((u,v))
            for u,v in edges:
                nxt=v if mask&(1<<u) else u
                new[(mask|(1<<nxt),rd+(1 if (u==0 or v==0) else 0))]+=p/Fraction(len(edges))
        states=new
    assert all(mask==full for mask,rd in states)
    ans=defaultdict(Fraction)
    for (mask,rd),p in states.items():ans[rd]+=p
    return dict(ans)


def ust(b):
    return {j:Fraction(comb(b-1,j-1),2**(b-1)) for j in range(1,b+1)}

for b in range(1,10):
    a=proposed(b); d=state_dp(b)
    assert a==d,(b,a,d)
    assert sum(a.values())==1
    U=ust(b)
    for k in range(0,b+1):
        assert sum(v for j,v in a.items() if j>=k)>=sum(v for j,v in U.items() if j>=k)
    print('b=',b,'D mean=',sum(k*p for k,p in a.items()),'UST mean=',sum(k*p for k,p in U.items()),'pJ1=',Fraction(1,b))
print('PASS exact independent frontier DP, derived mixed binomial law and UST dominance b=1..9')
