"""Direct finite checks for a mixed Hamming-graph resolving threshold theorem."""
from itertools import product, combinations, combinations_with_replacement
from math import comb, prod

def prediction(sizes):
    n = prod(sizes)
    q = max(sizes)
    b = sum(x == 2 for x in sizes)
    t = sum(x == 3 for x in sizes)
    c = sum(x == 4 for x in sizes)
    if q >= 5:
        return n * (q - 2) // q, sum(comb(x, 2) for x in sizes if x == q)
    if q == 4:
        return n // 2, 6*c + 2*comb(b, 2)
    if b >= 2:
        return n // 2, 2*comb(b, 2)
    if q == 3:
        return n // 3, 3*t + 6*comb(t, 2) + 6*b*t
    assert len(sizes) >= 2 and b >= 2
    return n // 2, 2*comb(b, 2)

def test(sizes):
    v = list(product(*(range(x) for x in sizes)))
    N = len(v)
    dist = [[sum(a != b for a,b in zip(u,w)) for w in v] for u in v]
    bisectors = {}
    pair_types = set()
    for i in range(N):
        for j in range(i+1,N):
            S = frozenset(k for k in range(N) if dist[i][k] == dist[j][k])
            bisectors.setdefault(S, []).append((i,j))
    best = max(map(len,bisectors))
    extreme = [S for S in bisectors if len(S) == best]
    expected_size, expected_number = prediction(sizes)
    assert (best,len(extreme)) == (expected_size,expected_number), (sizes,best,len(extreme),expected_size,expected_number)
    # Every maximum non-resolving set is a full bisector: independently check direct resolving sets on small graphs.
    if N <= 12:
        actual = 0
        for indices in combinations(range(N),best):
            signatures = {tuple(dist[i][w] for w in indices) for i in range(N)}
            if len(signatures) != N:
                actual += 1
                assert frozenset(indices) in bisectors
        assert actual == expected_number
    # Check exact classification by coordinate support of all extremal pairs.
    q = max(sizes)
    b = sum(x==2 for x in sizes)
    for S in extreme:
        for i,j in bisectors[S]:
            T = [k for k in range(len(sizes)) if v[i][k]!=v[j][k]]
            qs = sorted(sizes[k] for k in T)
            if q>=5:
                allow = (qs==[q])
            elif q==4:
                allow = (qs==[4] or qs==[2,2])
            elif b>=2:
                allow = (qs==[2,2])
            else:
                allow = (qs==[3] or qs==[3,3] or qs==[2,3])
            assert allow, (sizes,qs)
    return N,N*(N-1)//2,best,len(extreme)

if __name__=='__main__':
    profiles=[]
    for d in range(2,5):
        for sizes in combinations_with_replacement((2,3,4,5,6),d):
            if prod(sizes) <= 100:
                profiles.append(sizes)
    total_pairs=0; total_vertices=0
    for sizes in profiles:
        N,npairs,best,numb=test(sizes)
        total_pairs+=npairs;total_vertices+=N
        print('PROFILE_OK',sizes,'N',N,'max_failure_size',best,'failure_sets',numb)
    print('VERIFY_OK',len(profiles),'profiles',total_pairs,'distinct_vertex_pairs', 'full_bisector_enumeration=PASS','critical_nonresolving_set_count=PASS','pair_support_classification=PASS')

