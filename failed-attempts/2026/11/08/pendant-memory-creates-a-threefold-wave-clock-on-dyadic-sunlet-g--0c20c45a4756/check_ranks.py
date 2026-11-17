"""GF(2) operator-rank verification using explicit graph-neighbor lists."""


def neighbors(n):
    adj = []
    for i in range(n):
        adj.append(((i-1) % n, (i+1) % n, i+n))
    for i in range(n):
        adj.append((i,))
    return adj


def step(state, n, adj):
    graph_mask = (1 << (2*n))-1
    u = state & graph_mask
    v = state >> (2*n)
    new_u = v
    for i, neigh in enumerate(adj):
        bit = 0
        for j in neigh:
            bit ^= (u >> j) & 1
        new_u ^= bit << i
    return new_u | (u << (2*n))


def gf2rank(cols):
    pivots = {}
    for val in cols:
        while val:
            key = val.bit_length()-1
            if key not in pivots:
                pivots[key] = val
                break
            val ^= pivots[key]
    return len(pivots)


def test_one(n):
    N = 4*n
    adj = neighbors(n)
    columns = [1 << j for j in range(N)]
    identity = columns[:]
    dims = {}
    query_steps = {3*(1<<j) for j in range(n.bit_length())}
    query_steps |= {1,2,3*n}
    for t in range(1,3*n+1):
        columns = [step(val,n,adj) for val in columns]
        if t in query_steps:
            delta = [columns[j] ^ identity[j] for j in range(N)]
            dims[t] = N-gf2rank(delta)
    for j in range(n.bit_length()):
        k = 3*(1<<j)
        expected_dim = 4*(1<<j)
        assert dims[k]==expected_dim, (n,k,dims[k],expected_dim)
    assert dims[1]==0 and dims[2]==0
    assert columns==identity
    assert dims[3*n]==N
    assert dims[3*n//2] == 2*n
    print(f'n={n}: dimension={N}, fixed dimensions at times 3*2^j=' +
          str([dims[3*(1<<j)] for j in range(n.bit_length())]) +
          f', order={3*n}')


if __name__=='__main__':
    for n in [4,8,16,32,64]:
        test_one(n)
    print('PASS: exact binary operator ranks and full-order checks')
