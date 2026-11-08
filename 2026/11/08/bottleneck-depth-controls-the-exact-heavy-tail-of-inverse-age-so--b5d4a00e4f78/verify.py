"""Exact checks for the inverse-age threshold-cascade bottleneck law.
Run: python verify.py (Python standard library only).
These are independent finite sanity checks, not a substitute for proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import exp, factorial, log
from collections import defaultdict


def closure(adj, q, initial):
    S=initial
    while True:
        enabled=[i for i in range(len(adj)) if not (S>>i&1) and (adj[i]&S).bit_count()>=q[i]]
        if not enabled:return S
        for i in enabled:S|=1<<i


def graph_data(n, edges):
    adj=[0]*n
    for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
    return adj


def calculate(adj,q,seed):
    B=closure(adj,q,seed)
    @lru_cache(None)
    def enabled(S):return tuple(i for i in range(len(adj)) if B>>i&1 and not S>>i&1 and (adj[i]&S).bit_count()>=q[i])
    @lru_cache(None)
    def recurrence(S):
        if S==B:return (0,F(1))
        opts=enabled(S);e=len(opts)
        if not e:raise AssertionError('a transient deadlock')
        data=[recurrence(S|1<<i) for i in opts]
        depth=max(b for b,a in data)
        A=sum((a for b,a in data if b==depth),F(0))
        if e==1:return (depth+1,A)
        return (depth,A/F(e-1))
    @lru_cache(None)
    def laplace(S,z):
        if S==B:return F(1)
        opts=enabled(S)
        return sum((laplace(S|1<<i,z)/F(len(opts)+z) for i in opts),F(0))
    def path_sum():
        out=[]
        def visit(S,exits):
            if S==B:
                b=sum(e==1 for e in exits)
                A=F(1)
                for e in exits:
                    if e>1:A/=e-1
                out.append((b,A,exits))
                return
            opts=enabled(S)
            for i in opts:visit(S|1<<i,exits+(len(opts),))
        visit(seed,())
        best=max(b for b,a,es in out) if out else 0
        weight=sum((a for b,a,es in out if b==best),F(0))
        return (best,weight,out)
    return B, enabled, recurrence, laplace, path_sum


def uniform_tail(B,enabled,start,s):
    states={start};q=[start]
    for S in q:
        if S==B:continue
        for i in enabled(S):
            S2=S|1<<i
            if S2 not in states:states.add(S2);q.append(S2)
    maxr=max([len(enabled(S)) for S in states if S!=B] or [1])
    row={start:1.0}
    survival=0.0
    poisson=exp(-maxr*s)
    for k in range(150):
        survival+=poisson*sum(v for S,v in row.items() if S!=B)
        nxt=defaultdict(float)
        for S,p in row.items():
            opts=enabled(S)
            nxt[S]+=p*(1-len(opts)/maxr)
            for v in opts:nxt[S|1<<v]+=p/maxr
        row=nxt
        poisson*=maxr*s/(k+1)
    return survival


def test():
    tests=0; lap_tests=0; numeric_tests=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for emask in range(1<<len(pairs)):
            if n==5 and emask%5!=0:continue
            edges=[e for j,e in enumerate(pairs) if emask>>j&1]
            adj=graph_data(n,edges)
            q=tuple(2 if len(edges)%4==0 and adj[i].bit_count()>=2 else 1 for i in range(n))
            for seed in [1,1<<(n-1)]:
                B,enabled,rec,lap,paths=calculate(adj,q,seed)
                if B==seed:continue
                b,A=rec(seed)
                bp,Ap,allpaths=paths()
                assert (b,A)==(bp,Ap),('bottleneck mismatch',n,edges,seed,b,A,bp,Ap)
                assert b>=1 and A>0
                tests+=1
                for z in [F(1),F(3,2)]:
                    independent=sum((F(1,1) if not es else F(1) for _,_,es in []),F(0))
                    independent=sum((__import__('functools').reduce(lambda acc,e:acc/F(e+z),es,F(1)) for _,_,es in allpaths),F(0))
                    assert lap(seed,z)==independent
                    lap_tests+=1
                if tests%23==0:
                    # Via uniformized forward generator, independent of pole recursion
                    surv=uniform_tail(B,enabled,seed,2.0)
                    # Laplace inversion not used: validate monotone survival 0..1 only.
                    assert 0<surv<1
                    numeric_tests+=1
    for m in range(1,8):
        # path: seed 0, threshold one infected neighbor
        adj=graph_data(m+1,[(i,i+1) for i in range(m)])
        B,enabled,rec,lap,paths=calculate(adj,(1,)*(m+1),1)
        assert rec(1)==(m,F(1))
        # exact Erlang tail identity in logarithmic time
        s=2.3
        expected=exp(-s)*sum(s**j/factorial(j) for j in range(m))
        measured=uniform_tail(B,enabled,1,s)
        assert abs(measured-expected)<1e-11,(m,measured,expected)
    for m in range(1,8):
        adj=graph_data(m+1,[(0,i) for i in range(1,m+1)])
        B,enabled,rec,lap,paths=calculate(adj,(1,)*(m+1),1)
        assert rec(1)==(1,F(m))
        s=2.3
        expected=1-(1-exp(-s))**m
        measured=uniform_tail(B,enabled,1,s)
        assert abs(measured-expected)<1e-11,(m,measured,expected)
    print('PASS: exact graph path-sum/DP agreement:',tests,'instances')
    print('PASS: independent rational Laplace comparisons:',lap_tests)
    print('PASS: uniformization finite-state checks:',numeric_tests,'and 14 star/path checks')
    print('PASS: bottleneck exponent and path/star coefficients through size 8')

if __name__=='__main__':test()
