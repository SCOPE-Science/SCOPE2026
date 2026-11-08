"""Reproduce exact competing-spread territory and extremal checks (Python stdlib)."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb


def exact_territory(edges, seed_a, seed_b, rate_a=1, rate_b=1, extras=None):
    """Enumerate complete continuous-time CTMC colorings via jump probabilities."""
    n = 1 + max(max(u,v) for u,v in edges)
    graph = [[] for _ in range(n)]
    for u,v in edges:
        sa,sb=(extras or {}).get(tuple(sorted((u,v))),(1,1))
        graph[u].append((v,F(rate_a*sa),F(rate_b*sb)))
        graph[v].append((u,F(rate_a*sa),F(rate_b*sb)))
    initial=[0]*n;initial[seed_a]=1;initial[seed_b]=2
    @lru_cache(None)
    def dist(state):
        if all(v!=0 for v in state):return {state.count(1):F(1)}
        transitions=[]
        for i,c in enumerate(state):
            if c==0:continue
            for j,ra,rb in graph[i]:
                if state[j]==0:
                    next_state=list(state);next_state[j]=c
                    transitions.append((tuple(next_state),ra if c==1 else rb))
        total=sum((r for _,r in transitions),F(0))
        out=defaultdict(F)
        for nxt,rate in transitions:
            for k,v in dist(nxt).items():out[k]+=rate*v/total
        return dict(out)
    return dist(tuple(initial))


def weighted_binomial(weights,p):
    m=len(weights)-2
    out={}
    for x in range(m+1):
        cnt=sum(weights[:x+1]);out[cnt]=F(comb(m,x))*p**x*(1-p)**(m-x)
    return out


def moments(d):
    E=sum((F(k)*v for k,v in d.items()),F(0))
    return E,sum(((F(k)-E)**2*v for k,v in d.items()),F(0))


def comp(m,B):
    if m==1:yield (B,);return
    for j in range(B+1):
        for rest in comp(m-1,B-j):yield (j,)+rest


def predicted_max(m,B):
    centers=[(m+1)//2] if m%2 else [m//2,m//2+1]
    j=centers[0]
    q=F(sum(comb(m,k) for k in range(j,m+1)),2**m)
    pmf=F(comb(m-1,j-1),2**(m-1))
    return F(m,4) + F(B*m,2)*pmf+ B*B*q*(1-q),centers


def run():
    path_cases=0
    for m in range(1,6):
        # path with m middle nodes and B offpath branches, each its own rooted leaf
        for config in [(),(0,),(m//2+1,),(0,m+1),(m//2+1,m//2+1)]:
            n=m+2+len(config)
            edges=[(j,j+1) for j in range(m+1)]
            weights=[1]*(m+2)
            rate_extensions={}
            for t,root in enumerate(config):
                leaf=m+2+t;edges.append((root,leaf));weights[root]+=1
                rate_extensions[tuple(sorted((root,leaf)))]=(t+2,2*t+3)
            for a,b in [(1,1),(2,1),(1,3)]:
                actual=exact_territory(edges,0,m+1,a,b,rate_extensions)
                expect=weighted_binomial(weights,F(a,a+b))
                assert actual==expect,(m,config,a,b,actual,expect)
                path_cases+=1
    extremal_cases=0
    for m in range(1,8):
        for B in range(1,6):
            best,centers=predicted_max(m,B)
            base=F(m,4)
            winners=[]
            for alloc in comp(m+2,B):
                weights=[1+x for x in alloc]
                _,var=moments(weighted_binomial(weights,F(1,2)))
                assert base<=var<=best,(m,B,alloc,var,best)
                if var==base:assert sum(alloc[1:-1])==0
                if var==best:
                    active=[i for i in range(1,m+1) if alloc[i]]
                    assert len(active)==1 and active[0] in centers and alloc[active[0]]==B,(m,B,alloc)
                    winners.append(active[0])
                extremal_cases+=1
            assert sorted(winners)==centers,(m,B,winners,centers)
    print('PASS exact CTMC-vs-binomial:',path_cases,'cases; maximum/minimum complete decoration checks:',extremal_cases,'cases')
    print('example: m=3 B=4 central maximum',predicted_max(3,4)[0],'; minimum',F(3,4))

if __name__=='__main__':run()
