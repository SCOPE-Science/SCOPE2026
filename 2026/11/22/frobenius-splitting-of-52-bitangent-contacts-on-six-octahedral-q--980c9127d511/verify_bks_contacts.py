"""Exact, exhaustive finite-field verification of the bitangent-contact spectrum
for the six non-Hermitian smooth members over the nine-element field.
Pure Python 3 standard library; no files, packages, or network needed.
"""
from collections import Counter


def field(m, coeffs):
    q = 3 ** m
    powers = [3 ** k for k in range(m)]
    digs = [tuple((u // w) % 3 for w in powers) for u in range(q)]
    add = [[sum(((digs[a][k] + digs[b][k]) % 3) * powers[k]
                for k in range(m)) for b in range(q)] for a in range(q)]
    neg = [sum(((-digs[a][k]) % 3) * powers[k] for k in range(m))
           for a in range(q)]
    mul = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            arr = [0] * (2 * m - 1)
            for i in range(m):
                for j in range(m):
                    arr[i+j] += digs[a][i] * digs[b][j]
            for degree in range(2*m-2, m-1, -1):
                t = arr[degree] % 3
                for j in range(m):
                    arr[degree-m+j] -= t * coeffs[j]
            mul[a][b] = sum((arr[i] % 3) * powers[i] for i in range(m))
    inv = [0] * q
    for a in range(1, q):
        inv[a] = next(b for b in range(1, q) if mul[a][b] == 1)
    is_square = {mul[t][t] for t in range(q)}
    assert len(is_square) == (q+1)//2
    i = next(x for x in range(q) if mul[x][x] == 2)
    return q, add, neg, mul, inv, is_square, i


def counts(m, mod):
    q,add,neg,mul,inv,squares,i = field(m, mod)
    out = {}
    for u in range(3):
      for v in (1,2):
        lam = add[u][mul[v][i]]
        E = add[1][neg[lam]]
        assert E != 0
        stats = Counter(hyperflex=1, split_pairs=0, nonsplit_pairs=0)
        for a in range(q):
          a2 = mul[a][a]
          a3 = mul[a2][a]
          for b in range(q):
            b2 = mul[b][b]
            b3 = mul[b2][b]
            ab = mul[a][b]
            A = neg[add[add[mul[lam][a2]][a]][a3]]
            B = add[mul[lam][ab]][neg[b]]
            C = mul[lam][add[a][neg[b2]]]
            D = add[mul[lam][b]][neg[b3]]
            K = mul[2][add[mul[E][C]][neg[mul[D][D]]]]
            if mul[mul[E][E]][B] != mul[D][K]:
                continue
            if mul[mul[E][mul[E][E]]][A] != mul[K][K]:
                continue
            eta = mul[mul[2][D]][inv[E]]
            theta = mul[K][mul[inv[E]][inv[E]]]
            assert A == mul[E][mul[theta][theta]]
            assert B == mul[E][mul[2][mul[eta][theta]]]
            assert C == mul[E][add[mul[eta][eta]][mul[2][theta]]]
            assert D == mul[E][mul[2][eta]]
            disc = add[mul[eta][eta]][neg[theta]]
            if disc == 0:
                stats['hyperflex'] += 1
            elif disc in squares:
                stats['split_pairs'] += 1
            else:
                stats['nonsplit_pairs'] += 1
        total = sum(stats.values())
        out[(u,v)] = (stats['hyperflex'],stats['split_pairs'],stats['nonsplit_pairs'])
        assert (total <= 28)
    return out


if __name__ == '__main__':
    small = counts(2, (1,0))                # T^2+1
    big = counts(4, (1,0,1,1))              # T^4+T^3+T^2+1
    for u in range(3):
      for v in (1,2):
        a = small[(u,v)];b = big[(u,v)]
        assert a == ((4,0,0) if u in (0,1) else (4,0,12))
        assert b == ((4,12,12) if u==1 else (4,24,0))
        assert sum(b)==28
        print('real_part',u,'imag_part',v,'F9',a,'F81',b)
    print('BKS_CONTACT_FROBENIUS_CLASSIFICATION_PASS')
