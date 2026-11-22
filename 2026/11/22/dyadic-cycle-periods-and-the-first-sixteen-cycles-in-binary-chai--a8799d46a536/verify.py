"""Reproducible computations for cycle periods of a finite-ring Vieta map.
Python 3 standard library; run `python verify.py`.
"""
from collections import Counter


def prod(a, b, m):
    mask = (1 << m) - 1
    out = 0
    while b:
        if b & 1:
            out ^= a
        a = (a << 1) & mask
        b >>= 1
    return out


def prod_reference(a, b, m):
    # Independent coefficient-by-coefficient implementation.
    out = 0
    for n in range(m):
        parity = 0
        for j in range(n + 1):
            parity ^= ((a >> j) & 1) & ((b >> (n-j)) & 1)
        out |= parity << n
    return out


def poly_product(A, B, degree_bound):
    C = set()
    for x, y in A:
        for z, w in B:
            exp = (x+z, y+w)
            if sum(exp) < degree_bound:
                if exp in C:
                    C.remove(exp)
                else:
                    C.add(exp)
    return C


def jet_certificate():
    D = 9
    u, b = {(1, 0)}, {(0, 1)}
    for _ in range(8):
        uu = u ^ b
        bb = b ^ poly_product(u, b, D)
        u, b = uu, bb
    U = u ^ {(1, 0)}
    B = b ^ {(0, 1)}
    expected_u = {(2,6),(4,4),(6,2),(7,1)}
    expected_b = {(1,7),(3,5),(5,3),(6,2)}
    assert U == expected_u, (U, expected_u)
    assert B == expected_b, (B, expected_b)
    # Each degree-eight form vanishes at all four binary pairs.
    for a in range(2):
        for c in range(2):
            assert sum((a**i)*(c**j) for i,j in U) % 2 == 0
            assert sum((a**i)*(c**j) for i,j in B) % 2 == 0
    return {'u_degree8': sorted(U), 'b_degree8': sorted(B)}


def one_step(a, b, m):
    return a ^ b, prod(a, b, m)


def census_full(m):
    Q = 1 << m
    N = Q*Q
    successors = [0]*N
    for a in range(Q):
        for b in range(Q):
            aa, bb = one_step(a,b,m)
            successors[a*Q+b] = aa*Q+bb
    visited = bytearray(N)
    orbit_counts = Counter()
    for start in range(N):
        if visited[start]:
            continue
        path = []
        position = {}
        v = start
        while not visited[v] and v not in position:
            position[v] = len(path)
            path.append(v)
            v = successors[v]
        if v in position:
            orbit_counts[len(path)-position[v]] += 1
        for p in path:
            visited[p] = 1
    assert all(visited)
    return dict(sorted(orbit_counts.items()))


def fixed_core(m):
    Q = 1 << m
    K = Q//2
    fixed_counts = Counter()
    for U in range(K):
        a0 = 1 ^ (U << 1)
        for B in range(K):
            b0 = B << 1
            a,b=a0,b0
            for s in range(1,17):
                # Alternative arithmetic routine independent of full census.
                a,b=a^b, prod_reference(a,b,m)
                if s in (1,2,4,8,16) and (a,b)==(a0,b0):
                    fixed_counts[s] += 1
    return dict(sorted(fixed_counts.items()))


def witness():
    m=10
    a,b=3,4   # 1+t and t^2
    values={0:[a,b]}
    for i in range(1,17):
        a,b=one_step(a,b,m)
        if i in (1,2,4,8,16):values[i]=[a,b]
    assert values[8] == [515,4] and values[16] == [3,4]
    return values


def main():
    import json
    print('JET', json.dumps(jet_certificate(),sort_keys=True))
    for m in range(1,11):
        counts = census_full(m)
        assert set(counts).issubset({1,2,4,8,16})
        if m <= 9:
            assert counts.get(16,0)==0
        if m==10:
            assert counts == {1:1024,2:1280,4:5888,8:17152,16:6144}
        print('CYCLES',m,json.dumps(counts,sort_keys=True))
    fix=fixed_core(10)
    assert fix == {1:512,2:3072,4:26624,8:163840,16:262144}, fix
    print('CORE_FIXED',json.dumps(fix,sort_keys=True))
    print('WITNESS', json.dumps(witness(),sort_keys=True))
    print('VERIFY_OK')

if __name__=='__main__':main()
