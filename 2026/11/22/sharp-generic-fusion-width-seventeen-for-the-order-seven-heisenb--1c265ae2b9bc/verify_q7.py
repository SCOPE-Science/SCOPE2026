"""Self-contained exact certificate for the order-seven fusion-channel filling bound.

Run: python verify_q7.py
Requires Python 3.10+ standard library only; finite field and elimination are exact.
"""
import hashlib
import itertools
import struct

Q, N, CHANNELS = 7, 49, 17
NCOLS = 3 * N * CHANNELS
NROWS = N * N
REPRESENTATIVES = ((0, 0), (0, 1), (1, 1), (1, 2))
EXPECTED = {
    (0, 0): (1, "bb0c78b1653184ed834995a78cec30ee99b5177a2fc591e3c592daab01142a57", "017456ef766c2107278432c333b41af1deabf15fa1a40f6bd1e4354154c2c38e"),
    (0, 1): (6, "48e9e7b30f10c6d229d89a2a2c2c124fcce73c873516a9af1c4b8c8e233bdafc", "b4d9deaba3dd3991c64f3005404a99d9677dbd1a0c3d1f31f5c74cfadf1894b9"),
    (1, 1): (6, "ec0035959d1ac0f7e1bb9b4325d47791ed42a78718f540eca84a51f1471133ba", "7f2ff53d01c5d0defc9ffc649cf3c130d642ae1058f72e8a9e19d2c478fdee6f"),
    (1, 2): (1, "828da0983eef85ce78b4b558bdaaed75f0292ed73435d1754a366a427d0e604c", "959248f102def108b238bfd8b0bb5558ef34e1bc6f8c463eaf8309ffc468bb07"),
}

# GF(8) = F_2[a]/(a^3+a+1), with binary encoding 1,a,a^2.
def gf_mul(x, y):
    z = 0
    for i in range(3):
        if (y >> i) & 1:
            z ^= x << i
    for d in (4, 3):
        if (z >> d) & 1:
            z ^= 0b1011 << (d - 3)
    return z

MUL = tuple(tuple(gf_mul(x, y) for y in range(8)) for x in range(8))
INV = (0,) + tuple(next(y for y in range(1, 8) if MUL[x][y] == 1) for x in range(1, 8))
ROOT = (1, 2, 4, 3, 6, 7, 5)  # a^j, j=0..6


def orbit_representatives():
    unseen = {(s, t) for s in range(7) for t in range(7)}
    sizes = {}
    for s, t in REPRESENTATIVES:
        triples = (s, t, (-s-t) % 7)
        orbit = set()
        for perm in set(itertools.permutations(triples)):
            for lam in range(1, 7):
                orbit.add((lam*perm[0] % 7, lam*perm[1] % 7))
        assert orbit <= unseen, (s, t, len(orbit & unseen), len(orbit))
        unseen.difference_update(orbit)
        sizes[(s, t)] = len(orbit)
    assert not unseen, unseen
    assert sorted(sizes.values()) == [1, 12, 18, 18], sizes
    return sizes


def parameters(s, t):
    seed = f"q7-fill-certificate-v1|s={s}|t={t}".encode('ascii')
    data = b"".join(hashlib.sha256(seed + b'|block=' + str(i).encode('ascii')).digest()
                    for i in range(240))
    integers = [b & 7 for b in data[:CHANNELS*3*N]]
    assert len(integers) == CHANNELS*3*N
    return [(integers[(3*z+0)*N:(3*z+1)*N],
             integers[(3*z+1)*N:(3*z+2)*N],
             integers[(3*z+2)*N:(3*z+3)*N])
            for z in range(CHANNELS)]


def jacobian(s, t, params):
    # Index (x,y) as 7*x+y. For output row (i,j), channel z and k,
    # the polynomial term is d_z[k] a_z[i-k] b_z[j-k]
    # multiplied by a^(-k_x (s*(i_y-k_y)+t*(j_y-k_y))).
    diff = [[((i//7-k//7) % 7)*7 + (i%7-k%7) % 7 for k in range(N)]
            for i in range(N)]
    rows = [[0, 0, 0] for _ in range(NROWS)]
    for i in range(N):
        for j in range(N):
            row = rows[i*N+j]
            for k in range(N):
                u, v = diff[i][k], diff[j][k]
                exponent = (-(k//7)*(s*(u%7)+t*(v%7))) % 7
                phase = ROOT[exponent]
                for z, (aa, bb, dd) in enumerate(params):
                    a, b, d = aa[u], bb[v], dd[k]
                    columns = (3*N*z+u, 3*N*z+N+v, 3*N*z+2*N+k)
                    values = (MUL[MUL[d][b]][phase],
                              MUL[MUL[d][a]][phase],
                              MUL[MUL[a][b]][phase])
                    for col, val in zip(columns, values):
                        if val & 1: row[0] ^= 1 << col
                        if val & 2: row[1] ^= 1 << col
                        if val & 4: row[2] ^= 1 << col
    return rows


def one_channel_entry(s, t, triple, i, j):
    aa, bb, dd = triple
    out = 0
    for k in range(N):
        u = ((i//7-k//7)%7)*7 + (i%7-k%7)%7
        v = ((j//7-k//7)%7)*7 + (j%7-k%7)%7
        phase = ROOT[(-(k//7)*(s*(u%7)+t*(v%7))) % 7]
        out ^= MUL[MUL[MUL[dd[k]][aa[u]]][bb[v]]][phase]
    return out


def check_direct_derivatives(s, t, params, rows):
    # Compare the polynomial coefficient formula against independent
    # finite differences at deterministic test coordinates, all families.
    for family in range(3):
        for z in (0, 5, 16):
            for h in (0, 17, 48):
                i = (13*z + 3*h + family) % N
                j = (9*z + 5*h + 2*family) % N
                col = z*3*N + family*N + h
                packed = rows[i*N+j]
                predicted = sum((1<<bit) for bit in range(3)
                                if packed[bit] & (1<<col))
                a, b, d = [v[:] for v in params[z]]
                v0 = one_channel_entry(s, t, (a, b, d), i, j)
                (a, b, d)[family][h] ^= 1
                v1 = one_channel_entry(s, t, (a, b, d), i, j)
                assert predicted == (v0 ^ v1), (s, t, family, z, h)


def scale_packed_planes(triple, scalar):
    x, y, z = triple
    b0, b1, b2 = scalar & 1, scalar & 2, scalar & 4
    w0 = (x if b0 else 0)
    w1 = (y if b0 else 0) ^ (x if b1 else 0)
    w2 = (z if b0 else 0) ^ (y if b1 else 0) ^ (x if b2 else 0)
    w3 = (z if b1 else 0) ^ (y if b2 else 0)
    w4 = (z if b2 else 0)
    return w0 ^ w3, w1 ^ w3 ^ w4, w2 ^ w4


def maximal_minor(rows):
    rank, determinant, pivots = 0, 1, []
    for col in range(NCOLS):
        mask = 1 << col
        pivot = next((i for i in range(rank, NROWS)
                      if (rows[i][0] | rows[i][1] | rows[i][2]) & mask), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pv = sum(1 << j for j in range(3) if rows[rank][j] & mask)
        assert 1 <= pv <= 7
        determinant = MUL[determinant][pv]
        for i in range(rank+1, NROWS):
            value = sum(1 << j for j in range(3) if rows[i][j] & mask)
            if value:
                product = scale_packed_planes(rows[rank], MUL[value][INV[pv]])
                rows[i][0] ^= product[0]
                rows[i][1] ^= product[1]
                rows[i][2] ^= product[2]
        pivots.append(col)
        rank += 1
        if rank == NROWS:
            break
    return rank, determinant, pivots


def verify():
    assert [MUL[x][1] for x in range(8)] == list(range(8))
    assert all(MUL[x][INV[x]] == 1 for x in range(1, 8))
    assert len(set(ROOT)) == 7 and ROOT[0] == 1
    assert all(MUL[ROOT[i]][ROOT[j]] == ROOT[(i+j) % 7]
               for i in range(7) for j in range(7))
    print('orbit sizes:', orbit_representatives(), flush=True)
    for s, t in REPRESENTATIVES:
        params = parameters(s, t)
        data = bytes(v for triple in params for array in triple for v in array)
        param_hash = hashlib.sha256(data).hexdigest()
        rows = jacobian(s, t, params)
        check_direct_derivatives(s, t, params, rows)
        rank, det, cols = maximal_minor(rows)
        col_hash = hashlib.sha256(b''.join(struct.pack('<H', col) for col in cols)).hexdigest()
        assert (rank, det, col_hash, param_hash) == (NROWS, *EXPECTED[(s, t)]), (s, t, rank, det, col_hash, param_hash)
        print(f'({s},{t}): rank={rank}, minor_GF8={det}, pivots_sha256={col_hash}, parameters_sha256={param_hash}', flush=True)
    print('PASS: four exhaustive type classes, each with a nonzero 2401 x 2401 minor')


if __name__ == '__main__':
    verify()
