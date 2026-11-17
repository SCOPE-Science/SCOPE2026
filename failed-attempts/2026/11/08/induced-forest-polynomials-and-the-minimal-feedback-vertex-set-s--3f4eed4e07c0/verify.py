"""Independently enumerate induced forests and maximal induced forests of crown graphs."""
from collections import Counter
from math import comb


def induced_forest(n, mask):
    # Explicit graph edge scan and union-find cycle detection.
    parent = list(range(2 * n))

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    for i in range(n):
        if not mask & (1 << i):
            continue
        for j in range(n):
            if i == j or not mask & (1 << (n + j)):
                continue
            u, v = find(i), find(n + j)
            if u == v:
                return False
            parent[u] = v
    return True


def expected_all(n):
    # Disjoint classes: one shore empty; one shore exactly one;
    # two-by-two; and two-by-three or its transpose.
    d = Counter()
    for k in range(n+1):
        d[k] += 2 * comb(n,k)
    d[0] -= 1
    for k in range(1,n+1):
        d[k+1] += 2*n*comb(n,k)
    d[2] -= n*n
    d[4] += comb(n,2) * (2*n-3)
    d[5] += n*(n-1)*(n-2)
    return {k:v for k,v in d.items() if v}


def expected_max(n):
    d = Counter()
    d[n+1] += 2*n
    d[5] += n*(n-1)*(n-2)
    return dict(d)


def classification(n, mask):
    I = {i for i in range(n) if mask&(1<<i)}
    J = {j for j in range(n) if mask&(1<<(n+j))}
    if min(len(I),len(J))==1 and max(len(I),len(J))==n:
        return 'full-shore star'
    if len(I)==2 and len(J)==3 and I.issubset(J):
        return 'induced P5'
    if len(J)==2 and len(I)==3 and J.issubset(I):
        return 'induced P5'
    return 'unclassified'


def test(n):
    all_counts=Counter(); max_counts=Counter(); types=Counter()
    for mask in range(1 << (2*n)):
        if not induced_forest(n,mask):
            continue
        k=mask.bit_count()
        all_counts[k]+=1
        maximal=True
        for v in range(2*n):
            if not mask & (1<<v):
                if induced_forest(n,mask | (1<<v)):
                    maximal=False
                    break
        if maximal:
            max_counts[k]+=1
            types[classification(n,mask)]+=1
    assert dict(all_counts)==expected_all(n),(n,all_counts,expected_all(n))
    assert dict(max_counts)==expected_max(n),(n,max_counts,expected_max(n))
    assert types['unclassified']==0,(n,types)
    assert types['full-shore star']==2*n
    assert types['induced P5']==n*(n-1)*(n-2)
    print('PROFILE_OK',n,'subsets',1<<(2*n),'forests',sum(all_counts.values()),
          'maximal',sum(max_counts.values()),'types',dict(types))


def main():
    for n in range(4,9):
        test(n)
    for n in range(4,150):
        all_coeff=expected_all(n)
        max_coeff=expected_max(n)
        assert all(k<=n+1 for k in all_coeff)
        assert all(5<=k<=n+1 for k in max_coeff)
        assert sum(max_coeff.values())==n*(n*n-3*n+4)
    print('VERIFY_OK direct_graph_profiles=5 literal_subsets=87296',
          'all_induced_forest_coefficients=PASS',
          'maximal_forest_polynomial=PASS',
          'minimal_feedback_vertex_set_spectrum=PASS',
          'arithmetic_profiles=146')


if __name__=='__main__':
    main()
