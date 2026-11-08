"""Independent exact verification for maximum-independent-set transversals in cycle powers."""
from collections import Counter
from math import comb


def formula_count(n, q, k, t):
    if t == 0:
        return 0
    val = 0
    for j in range((n-t)//k+1):
        val += (-1)**j * comb(t,j) * comb(n-j*k-1,t-1)
    assert (n*val) % t == 0
    return n*val//t


def graph_independent(mask, n, q):
    vs = [v for v in range(n) if (mask>>v)&1]
    return all(min((u-v)%n,(v-u)%n) >= q for i,u in enumerate(vs) for v in vs[i+1:])


def run():
    instances = []
    for q in range(2,6):
        for k in range(2,7):
            n=k*q+1
            if n<=17:
                instances.append((q,k))
    examined=0
    for q,k in instances:
        n=k*q+1
        independents = [mask for mask in range(1<<n) if mask.bit_count()==k and graph_independent(mask,n,q)]
        expected = {sum(1 << ((j+i*q)%n) for i in range(k)) for j in range(n)}
        assert len(independents)==n and set(independents)==expected, (q,k,'maximum')
        # Independent upper bound: no k+1 mutually q-separated positions, since (k+1)q>n.
        actual=Counter()
        for mask in range(1<<n):
            if all(mask & m for m in independents):
                actual[mask.bit_count()]+=1
        theory={t:formula_count(n,q,k,t) for t in range(q+1,n+1)}
        assert dict(actual)==theory, (q,k,actual,theory)
        assert actual[q+1] == n*comb(k+q-1,q)//(q+1)
        examined += 1<<n
    print('DIRECT_GRAPH_AND_TRANSVERSAL_EXHAUSTIVE_OK',len(instances), examined)
    # Independent gap DP for larger examples, comparing inclusion-exclusion formula.
    for q,k in [(2,10),(3,9),(5,8),(8,5)]:
        n=k*q+1
        for t in range(q+1,n+1):
            dp=[0]*(n+1);dp[0]=1
            for _ in range(t):
                nd=[0]*(n+1)
                for s,ways in enumerate(dp):
                    if ways:
                        for gap in range(1,k+1):
                            if s+gap<=n:nd[s+gap]+=ways
                dp=nd
            assert dp[n]*n//t==formula_count(n,q,k,t)
            assert dp[n]*n%t==0
    print('INDEPENDENT_COMPOSITION_DP_OK',[(2,10),(3,9),(5,8),(8,5)])
    print('VERIFY_OK')

if __name__=='__main__':
    run()
