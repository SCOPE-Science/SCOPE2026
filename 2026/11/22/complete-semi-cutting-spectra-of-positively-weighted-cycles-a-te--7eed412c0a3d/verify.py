"""Standalone independent distance-enumeration checks for cyclic terminal semi-cutting spectra."""
from collections import deque
from itertools import combinations
from math import comb


def graph_distances(n, removed):
    adj=[[] for _ in range(n)]
    for e in range(n):
        if not ((removed>>e)&1):
            u,v=e,(e+1)%n
            adj[u].append(v);adj[v].append(u)
    dist=[]
    for s in range(n):
        row=[n+1]*n;row[s]=0
        todo=deque([s])
        while todo:
            x=todo.popleft()
            for y in adj[x]:
                if row[y]>n:
                    row[y]=row[x]+1;todo.append(y)
        dist.append(row)
    return dist

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def formula(n,terminals):
    terms=sorted(terminals)
    gaps=[(terms[(i+1)%len(terms)]-terms[i])%n for i in range(len(terms))]
    assert sum(gaps)==n
    large=max(gaps)
    omit=gaps.index(large) if 2*large>n else None
    result=[1]
    for i,g in enumerate(gaps):
        if i==omit: factor=[comb(g,j) for j in range(g+1)]
        else:factor=[0]+[comb(g,j) for j in range(1,g+1)]
        result=multiply(result,factor)
    return result,gaps,omit

def test(limit=9):
    totals=0
    for n in range(3,limit+1):
        old=graph_distances(n,0)
        hist={s:[0]*(n+1) for t in range(2,n+1) for s in combinations(range(n),t)}
        for removed in range(1<<n):
            new=graph_distances(n,removed)
            undamaged={(u,v) for u in range(n) for v in range(u+1,n) if new[u][v]==old[u][v]}
            # the set is semi-cutting iff its vertices contain no undamaged terminal pair
            k=removed.bit_count()
            for terminals,poly in hist.items():
                if all((u not in terminals) or (v not in terminals) for u,v in undamaged):
                    poly[k]+=1
                totals+=1
        for terms,actual in hist.items():
            expected,gaps,omit=formula(n,terms)
            assert actual==expected,(n,terms,gaps,actual,expected)
            low=next(j for j,v in enumerate(actual) if v)
            assert low==len(terms)-(omit is not None)
            assert actual[low]==__import__('math').prod(g for i,g in enumerate(gaps) if i!=omit)
        print('CYCLE_N_PASS',n,'terminal_sets',len(hist))
    print('ALL_ORDERS_DISTANCE_ENUMERATION_PASS',totals)
    # Several larger patterns, parity boundary, spectrum and root characterization identities.
    for n in range(3,101):
        for t in range(2,min(n,8)+1):
            terms=tuple(sorted({(i*n)//t for i in range(t)}))
            if len(terms)<2:continue
            coeff,gaps,omit=formula(n,terms)
            assert len(coeff)==n+1
            assert sum(coeff)==(2**max(gaps) if omit is not None else 1)*__import__('math').prod(2**g-1 for i,g in enumerate(gaps) if i!=omit)
            lo=next(i for i,c in enumerate(coeff) if c)
            a=coeff[lo:]
            assert all(a[i]*a[i]>=a[i-1]*a[i+1] for i in range(1,len(a)-1))
            assert coeff[-1]==1
    print('LOG_CONCAVITY_AND_TOTAL_COUNTS_SAMPLE_PASS')
    print('VERIFY_OK')

if __name__=='__main__':test()

# Separate weighted-path witness, using Dijkstra rather than the gap criterion.
def weighted_distances(n, removed, weights):
    import heapq
    adj=[[] for _ in range(n)]
    for e in range(n):
        if (removed>>e)&1: continue
        u,v=e,(e+1)%n
        adj[u].append((v,weights[e]));adj[v].append((u,weights[e]))
    answer=[]
    for s in range(n):
        d=[float('inf')]*n;d[s]=0;heap=[(0,s)]
        while heap:
            a,x=heapq.heappop(heap)
            if a!=d[x]:continue
            for y,w in adj[x]:
                if a+w<d[y]:
                    d[y]=a+w;heapq.heappush(heap,(d[y],y))
        answer.append(d)
    return answer

def weighted_formula(n,terminals,weights):
    terms=sorted(terminals);gaps=[];ws=[]
    for i,a in enumerate(terms):
        b=terms[(i+1)%len(terms)]
        count=(b-a)%n;gaps.append(count)
        ws.append(sum(weights[(a+j)%n] for j in range(count)))
    big=max(ws);omit=ws.index(big) if big*2>sum(ws) else None
    poly=[1]
    for i,g in enumerate(gaps):
        fac=[comb(g,j) for j in range(g+1)] if i==omit else [0]+[comb(g,j) for j in range(1,g+1)]
        poly=multiply(poly,fac)
    return poly

def weighted_test():
    total=0
    for n in range(3,9):
        for h in range(4):
            weights=[1+((e*7+h*3+e*e)%5) for e in range(n)]
            old=weighted_distances(n,0,weights)
            hist={s:[0]*(n+1) for t in range(2,n+1) for s in combinations(range(n),t)}
            for removed in range(1<<n):
                new=weighted_distances(n,removed,weights)
                survivors={(u,v) for u in range(n) for v in range(u+1,n) if new[u][v]==old[u][v]}
                for terms,p in hist.items():
                    if all((u not in terms or v not in terms) for u,v in survivors):p[removed.bit_count()]+=1
                    total+=1
            for terms,p in hist.items():
                expected=weighted_formula(n,terms,weights)
                assert p==expected,(n,h,weights,terms,p,expected)
        print('WEIGHTED_CYCLE_N_PASS',n)
    print('WEIGHTED_DIRECT_DISTANCE_ENUMERATION_PASS',total)
    print('WEIGHTED_VERIFY_OK')

if __name__=='__main__':weighted_test()
