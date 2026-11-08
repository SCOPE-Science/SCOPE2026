"""Standalone finite checks for maximal edge-open packings of full clique subdivisions.
Run: python3 eop_skn_replay.py (standard library only).
"""
from itertools import combinations
from collections import Counter
from math import factorial

def incidence_graph(n):
    # Old vertices 0,...,n-1; new vertices n,...,n+binom(n,2)-1.
    names={pair:n+t for t,pair in enumerate(combinations(range(n),2))}
    edges=[]
    for (i,j),s in names.items():
        edges.extend(((i,s),(j,s)))
    edge_index={e:t for t,e in enumerate(edges)}
    adj={v:set() for v in range(n+len(names))}
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    # Raw witness enumeration: a third edge joining distinct endpoints.
    bad=[0]*len(edges)
    for i,e in enumerate(edges):
        for j in range(i+1,len(edges)):
            f=edges[j]
            endpoints_e=set(e);endpoints_f=set(f)
            bridge=False
            for u in endpoints_e:
                for v in endpoints_f:
                    if u!=v and v in adj[u] and frozenset((u,v)) not in (frozenset(e),frozenset(f)):
                        bridge=True
            if bridge:
                bad[i]|=1<<j;bad[j]|=1<<i
    return names,edges,edge_index,bad

def predicted_poly(n):
    p=Counter()
    c=n//2 if n%2==0 else (n-1)//2
    p[2*c]+=factorial(n)//(2**c*factorial(c))
    for c in range((n-2)//2+1):
        r=n-2*c
        for a in range(1,r):
            u=r-a
            if (a,u)==(1,1):continue
            p[2*c+a*u]+=factorial(n)//(2**c*factorial(c)*factorial(a)*factorial(u))
    return +p

def maximal_packing(bits,bad):
    rest=bits
    while rest:
        low=rest&-rest
        v=low.bit_length()-1
        rest-=low
        if bad[v]&rest:return False
    return all((bits>>v&1) or (bad[v]&bits) for v in range(len(bad)))

def get_matchings(vertices):
    vertices=tuple(vertices)
    if not vertices:
        yield ()
        return
    v,*tail=vertices
    for m in get_matchings(tail):yield m
    for k,w in enumerate(tail):
        other=tail[:k]+tail[k+1:]
        for m in get_matchings(other):yield ((v,w),)+m

def generate(n,names,edge_index):
    V=tuple(range(n))
    for cycles in get_matchings(V):
        used={v for uv in cycles for v in uv}
        rem=tuple(v for v in V if v not in used)
        core=sum((1<<edge_index[(i,names[tuple(sorted((i,j)))])]) |
                 (1<<edge_index[(j,names[tuple(sorted((i,j)))])]) for i,j in cycles)
        if len(rem)<=1:
            yield core
        for a in range(1,len(rem)):
            u=len(rem)-a
            if (a,u)==(1,1):continue
            for A in combinations(rem,a):
                U=tuple(set(rem)-set(A))
                bits=core
                for i in A:
                    for j in U:
                        bits|=1<<edge_index[(i,names[tuple(sorted((i,j)))])]
                yield bits

def main():
    total_examined=0;total_found=0;total_generated=0
    for n in range(2,9):
        names,edges,ei,bad=incidence_graph(n)
        pred=predicted_poly(n)
        forms=set(generate(n,names,ei))
        assert len(forms)==sum(pred.values()), (n,len(forms),pred)
        form_counts=Counter(v.bit_count() for v in forms)
        assert form_counts==pred, (n,form_counts,pred)
        for bits in forms:assert maximal_packing(bits,bad), (n,bits)
        total_generated+=len(forms)
        if n<=5:
            actual=set()
            for bits in range(1<<len(edges)):
                if maximal_packing(bits,bad):actual.add(bits)
            assert forms==actual,(n,len(actual),len(forms))
            total_found+=len(actual)
            total_examined+=1<<len(edges)
        print('n=',n,'poly=',sorted(pred.items()),'generated=',len(forms),
              'exhaustive=',n<=5)
    print('VERIFY_OK raw_bridge_conflicts=PASS exact_families_n2_to5=PASS '
          'maximal_generated_n2_to8=PASS subset_masks=',total_examined,
          'exhaustive_maximal=',total_found,'generated=',total_generated)
if __name__=='__main__':main()
