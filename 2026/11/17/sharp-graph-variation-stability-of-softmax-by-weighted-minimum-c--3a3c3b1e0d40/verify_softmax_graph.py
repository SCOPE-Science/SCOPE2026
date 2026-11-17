"""Exact integer diagnostics for a weighted graph-softmax variation theorem.

All computations use integer mass vectors q; the covariance Jacobian
is represented by the integer matrix m*diag(q)-q q^T.
These finite tests are diagnostics, not substitutes for the universal proof.
"""
import itertools
from fractions import Fraction


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for q in range(total + 1):
            for rest in compositions(total - q, n - 1):
                yield (q,) + rest


def edges_of_mask(n, mask):
    pairs = list(itertools.combinations(range(n), 2))
    return [p for i, p in enumerate(pairs) if mask >> i & 1]


def connected(n, edges):
    seen = {0}
    while True:
        new = seen | {v for u,v in edges if u in seen} | {u for u,v in edges if v in seen}
        if new == seen:
            return len(seen) == n
        seen = new


def tv(x, edges):
    return sum(abs(x[i]-x[j]) for i,j in edges)


def candidate(n, edges):
    d=[0]*n
    for u,v in edges:
        d[u]+=1;d[v]+=1
    maxr=Fraction(0,1)
    for i,j in itertools.combinations(range(n),2):
        minimum=min(sum(int((mask>>u&1)!=(mask>>v&1)) for u,v in edges)
                    for mask in range(1,1<<n-1)
                    if (mask>>i&1)!=(mask>>j&1))
        maxr=max(maxr,Fraction(d[i]+d[j],4*minimum))
    return maxr


def test(n, edges, mass_total=4):
    constant = candidate(n, edges)
    checked=0
    for mask in range(1,(1<<n)-1):
        h=[(mask>>i)&1 for i in range(n)]
        vt=tv(h,edges)
        if vt == 0: continue
        for q in compositions(mass_total,n):
            mass_in=sum(q[i]*h[i] for i in range(n))
            out=[qi*(mass_total*h[i]-mass_in) for i,qi in enumerate(q)]
            numer=tv(out,edges)
            assert Fraction(numer,mass_total**2 * vt)<=constant, (n,edges,q,mask,numer,vt,constant)
            checked+=1
    return checked


def test_weighted(n,edges,weights,mass_total=5):
    d=[0]*n
    for (u,v),w in zip(edges,weights):d[u]+=w;d[v]+=w
    val=Fraction(0)
    for i,j in itertools.combinations(range(n),2):
        c=min(sum(w for (u,v),w in zip(edges,weights) if ((m>>u)&1)!=((m>>v)&1))
              for m in range(1,(1<<n)-1) if ((m>>i)&1)!=((m>>j)&1))
        val=max(val,Fraction(d[i]+d[j],4*c))
    checked=0
    for mask in range(1,(1<<n)-1):
        h=[(mask>>i)&1 for i in range(n)]
        v0=sum(w*abs(h[u]-h[v]) for (u,v),w in zip(edges,weights))
        for q in compositions(mass_total,n):
            mass_in=sum(q[i]*h[i] for i in range(n))
            z=[qi*(mass_total*h[i]-mass_in) for i,qi in enumerate(q)]
            v1=sum(w*abs(z[u]-z[v]) for (u,v),w in zip(edges,weights))
            assert Fraction(v1,mass_total**2*v0) <= val
            checked+=1
    return checked


def test_covariance_pair_bound():
    # Exhaust over integer triples/quadruples of sample values and rational masses.
    cases=0
    for n in (3, 4):
        vs=list(itertools.product((-1,0,1),repeat=n))
        for u in vs:
            for v in vs:
                bound=max([0]+[(u[i]-u[j])*(v[i]-v[j]) for i in range(n) for j in range(i+1,n)])
                for q in compositions(4,n):
                    a=sum(q[i]*u[i] for i in range(n))
                    b=sum(q[i]*v[i] for i in range(n))
                    c=sum(q[i]*u[i]*v[i] for i in range(n))
                    assert (4*c-a*b)<=4*bound, (u,v,q)
                    cases+=1
    return cases


def main():
    print('EXACT_COVARIANCE_PAIR_DIAGNOSTICS_PASSED',test_covariance_pair_bound())
    count_graphs=0; count_cases=0
    for n in range(2,6):
        for mask in range(1,1<<(n*(n-1)//2)):
            es=edges_of_mask(n,mask)
            if not connected(n,es):continue
            count_graphs+=1
            count_cases+=test(n,es,4)
    print('ALL_CONNECTED_GRAPHS_N_LE_5_EXACT_P_AND_CUT_CHECKS_PASSED',count_graphs,count_cases)
    count_weighted=0
    for n in range(2,5):
        for mask in range(1,1<<(n*(n-1)//2)):
            es=edges_of_mask(n,mask)
            if not connected(n,es):continue
            ww=[1+(3*i+j)%5 for i,j in es]
            count_weighted+=test_weighted(n,es,ww,5)
    print('WEIGHTED_GRAPH_EXACT_P_AND_CUT_CHECKS_PASSED',count_weighted)
    # Exact interior approximations of the two-mass limiting extremizer on stars.
    for k in range(1,15):
        n=k+1;es=[(0,i) for i in range(1,n)]
        exact=Fraction(k+1,4)
        assert candidate(n,es)==exact
        # Hub/first-leaf masses 500 each, remaining leaves mass 1 each.
        q=[100000,100000]+[1]*(k-1)
        total=sum(q)
        h=[0,1]+[0]*(k-1)
        z=[qi*(total*h[i]-sum(q[j]*h[j] for j in range(n))) for i,qi in enumerate(q)]
        got=Fraction(tv(z,es),total*total*tv(h,es))
        assert got<=exact and got>exact-Fraction(k+1,1000)
    print('STAR_SHARPNESS_LIMIT_RATIONAL_WITNESSES_PASSED',14)
    for a in range(1,6):
        for b in range(a,6):
            n=a+b;edges=[(i,j) for i in range(a) for j in range(a,n)]
            value=candidate(n,edges)
            assert value==max(Fraction(1,2),Fraction(a+b,4*a)),(a,b,value)
    print('COMPLETE_BIPARTITE_PARAMETER_IDENTITIES_PASSED',15)
    print('ALL_GRAPH_SOFTMAX_VARIATION_DIAGNOSTICS_PASSED')

if __name__=='__main__':main()
