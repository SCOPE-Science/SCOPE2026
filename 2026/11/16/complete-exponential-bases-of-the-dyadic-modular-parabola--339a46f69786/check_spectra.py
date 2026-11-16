"""Exact integer-cyclotomic verification of dyadic quadratic-graph spectra."""
from collections import Counter


def gauss_zero(k, a, b):
    n = 1 << k
    counts = [0] * n
    for t in range(n):
        counts[(a*t+b*t*t) % n] += 1
    return all(counts[j] == counts[j+n//2] for j in range(n//2))


def count_complete_orthogonal_sets(k):
    n = 1 << k
    v = n*n
    adj = [0]*v
    for u in range(v):
        a,b = divmod(u,n)
        for w in range(u+1,v):
            c,d = divmod(w,n)
            if gauss_zero(k,(a-c)%n,(b-d)%n):
                adj[u] |= 1<<w
                adj[w] |= 1<<u
    counts=[0]
    def recurse(depth,P,X):
        if depth == n:
            counts[0]+=1
            return
        if depth+P.bit_count()<n:
            return
        possible=P|X
        if possible:
            pivot=max((i for i in range(v) if possible>>i&1),
                      key=lambda i:(P&adj[i]).bit_count())
            candidates=P &~adj[pivot]
        else:
            candidates=P
        while candidates:
            bit=candidates & -candidates
            vertex=bit.bit_length()-1
            recurse(depth+1,P&adj[vertex],X&adj[vertex])
            P ^= bit
            X |= bit
            candidates ^=bit
    recurse(0,(1<<v)-1,0)
    return counts[0]


def run():
    for k in range(1,6):
        n=1<<k
        for a in range(n):
            for b in range(n):
                actual=gauss_zero(k,a,b)
                if k>=2 and a%2==0 and b%2==1:
                    assert not actual, (k,a,b)
                if k>=2 and a%2==1:
                    assert actual, (k,a,b)
                if k>=2 and a%2==0 and b%2==0:
                    assert actual==gauss_zero(k-1,a//2,b//2),(k,a,b)
        print('FULL_GAUSS_CANCELLATIONS_PASS k=',k,'N=',n)
    for k,target in ((1,4),(2,64),(3,16384)):
        actual=count_complete_orthogonal_sets(k)
        assert actual==target,(k,actual,target)
        print('COMPLETE_CLIQUE_CENSUS_PASS k=',k,'count=',actual)
    print('DYADIC_PARABOLA_COMPLETE_SPECTRA_PASS')

if __name__=='__main__':
    run()
