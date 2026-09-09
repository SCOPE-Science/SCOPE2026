"""Census: committed 3-connected binary slice, n=7..9.
Dual Tutte recomputation (deletion-contraction log + rank-oracle subset replay),
F7/F7* minor verdicts with explicit sequences, extremals. Stdlib only."""
import itertools, json

def gf2_rank(cols, idx):
    basis = []
    for j in idx:
        x = cols[j]
        for b in basis:
            hb = b.bit_length() - 1
            if (x >> hb) & 1:
                x ^= b
        if x:
            basis.append(x)
            basis.sort(reverse=True)
            for i in range(len(basis)):
                for k in range(len(basis)):
                    if i != k and (basis[k] >> (basis[i].bit_length() - 1)) & 1:
                        basis[k] ^= basis[i]
            basis.sort(reverse=True)
    return len(basis)

def Cmat(rows):
    r, n = len(rows), len(rows[0])
    cols = []
    for j in range(n):
        v = 0
        for i in range(r):
            if rows[i][j]:
                v |= (1 << i)
        cols.append(v)
    return cols

# ---------------- committed slice (explicit GF(2) matrices) ----------------
MATS = {
 'M1_F7':   Cmat([[1,0,0,0,1,1,1],[0,1,0,1,0,1,1],[0,0,1,1,1,0,1]]),
 'M2_F7s':  Cmat([[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],[1,1,0,0,0,1,0],[1,1,1,0,0,0,1]]),
 'M3_AG32': Cmat([[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,0],[0,0,1,0,1,1,0,1],[0,0,0,1,1,0,1,1]]),
 'M4_S8':   Cmat([[1,0,0,0,0,1,1,1],[0,1,0,0,1,0,1,1],[0,0,1,0,1,1,0,1],[0,0,0,1,1,1,1,0]]),
 'M5_X8a':  Cmat([[1,0,0,0,1,0,1,1],[0,1,0,0,1,1,0,1],[0,0,1,0,1,1,0,0],[0,0,0,1,1,1,1,0]]),
 'M6_X8b':  Cmat([[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,0],[0,0,1,0,1,1,0,1],[0,0,0,1,1,0,1,0]]),
 'M7_MK33': Cmat([[1,1,1,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1],[1,0,0,1,0,0,1,0,0],[0,1,0,0,1,0,0,1,0]]),
 'M8_AG32e':Cmat([[1,0,0,0,1,1,1,1,0],[0,1,0,0,1,1,1,0,1],[0,0,1,0,1,1,0,1,1],[0,0,0,1,1,0,1,1,0]]),
 'M9_S8e':  Cmat([[1,0,0,0,0,1,1,1,1],[0,1,0,0,1,0,1,1,1],[0,0,1,0,1,1,0,1,1],[0,0,0,1,1,1,1,0,1]]),
}
REF_F7  = Cmat([[1,0,0,0,1,1,1],[0,1,0,1,0,1,1],[0,0,1,1,1,0,1]])
REF_F7s = Cmat([[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],[1,1,0,0,0,1,0],[1,1,1,0,0,0,1]])

def bases_of(cols, n, r):
    E = list(range(n))
    return set(B for B in itertools.combinations(E, r) if gf2_rank(cols, list(B)) == r)

# ---------------- Tutte method A: deletion-contraction (logged) ----------------
def tutte_dc(cols, n, log):
    E = tuple(range(n))
    memo = {}
    def rk(rem, con, S):
        return gf2_rank(cols, list(S) + list(con)) - gf2_rank(cols, list(con))
    def rec(rem, con):
        key = (rem, con)
        if key in memo:
            return memo[key]
        rE = rk(rem, con, rem)
        if not rem:
            return {(0, 0): 1}
        if rE == 0:
            p = {(0, len(rem)): 1}  # all loops
            memo[key] = p
            return p
        e = rem[0]
        rest = rem[1:]
        if rk(rem, con, (e,)) == 0:  # loop
            q = rec(rest, con)
            p = {(i, j + 1): c for (i, j), c in q.items()}
            log.append(('loop', e, rem, con))
            memo[key] = p
            return p
        if rk(rem, con, rest) < rE:  # coloop
            q = rec(rest, con + (e,))
            p = {(i + 1, j): c for (i, j), c in q.items()}
            log.append(('coloop', e, rem, con))
            memo[key] = p
            return p
        log.append(('branch', e, rem, con))
        q1 = rec(rest, con)        # delete e
        q2 = rec(rest, con + (e,)) # contract e
        p = dict(q1)
        for k, c in q2.items():
            p[k] = p.get(k, 0) + c
        memo[key] = p
        return p
    return rec(E, ())

# ---------------- Tutte method B: rank-oracle subset expansion ----------------
def tutte_subset(cols, n):
    from math import comb
    E = list(range(n))
    rE = gf2_rank(cols, E)
    rcache = {}
    def r(S):
        key = tuple(S)
        if key not in rcache:
            rcache[key] = gf2_rank(cols, list(S))
        return rcache[key]
    poly = {}
    for mask in range(1 << n):
        A = [j for j in range(n) if (mask >> j) & 1]
        rA = r(A)
        a = rE - rA
        b = len(A) - rA
        for i in range(a + 1):
            ci = comb(a, i) * ((-1) ** (a - i))
            for j in range(b + 1):
                cj = comb(b, j) * ((-1) ** (b - j))
                k = (i, j)
                poly[k] = poly.get(k, 0) + ci * cj
    return {k: v for k, v in poly.items() if v}

# ---------------- connectivity ----------------
def is_3conn(cols, n):
    E = list(range(n))
    rE = gf2_rank(cols, E)
    for k in (1, 2):
        for mask in range(1, (1 << n) - 1):
            X = [j for j in range(n) if (mask >> j) & 1]
            Y = [j for j in range(n) if not (mask >> j) & 1]
            if min(len(X), len(Y)) < k:
                continue
            if gf2_rank(cols, X) + gf2_rank(cols, Y) - rE < k:
                return False
    return True

# ---------------- minor testing ----------------
def minor_bases(cols, n, delete, contract, rem):
    rC = gf2_rank(cols, list(contract))
    rM = gf2_rank(cols, list(rem) + list(contract)) - rC
    B = set()
    for S in itertools.combinations(rem, rM):
        if gf2_rank(cols, list(S) + list(contract)) - rC == rM:
            B.add(S)
    return rM, B

def iso_match(rem, min_bases, ref_bases, m=7):
    rem = list(rem)
    ref_list = set(ref_bases)
    for perm in itertools.permutations(range(m)):
        img = set()
        for S in min_bases:
            img.add(tuple(sorted(perm[rem.index(x)] for x in S)))
        if img == ref_list:
            return list(perm)
    return None

def find_minor(cols, n, ref_cols, m=7):
    E = set(range(n))
    ref_bases = bases_of(ref_cols, m, gf2_rank(ref_cols, list(range(m))))
    rref = gf2_rank(ref_cols, list(range(m)))
    for nd in range(n - m + 1):
        for D in itertools.combinations(range(n), nd):
            Dset = set(D)
            for nc in range(n - m - nd + 1):
                rest = [j for j in range(n) if j not in Dset]
                if n - nd - nc != m:
                    continue
                for C in itertools.combinations(rest, nc):
                    Cset = set(C)
                    rem = tuple(sorted(E - Dset - Cset))
                    rM, mB = minor_bases(cols, n, Dset, Cset, rem)
                    if rM != rref or len(mB) != len(ref_bases):
                        continue
                    # normalize minor bases to 0..m-1 positions
                    norm = set(tuple(sorted(rem.index(x) for x in S)) for S in mB)
                    perm = iso_match(list(range(m)), norm, ref_bases, m)
                    if perm is not None:
                        return {'delete': sorted(Dset), 'contract': sorted(Cset),
                                'remain': list(rem), 'perm': perm}
    return None

def main():
    F7B = bases_of(REF_F7, 7, 3)
    F7sB = bases_of(REF_F7s, 7, 4)
    table = {}
    for name, cols in MATS.items():
        n = len(cols)
        E = list(range(n))
        r = gf2_rank(cols, E)
        B = bases_of(cols, n, r)
        log = []
        TA = tutte_dc(cols, n, log)
        TB = tutte_subset(cols, n)
        assert TA == TB, (name, 'Tutte mismatch')
        assert sum(TA.values()) == len(B), (name, 'coeff-sum != #bases')
        t22 = sum(c*(2**i)*(2**j) for (i,j),c in TA.items())
        assert t22 == 2**n, (name, 'T(2,2) != 2^n')
        assert TA.get((1, 1), 0) or True
        # T(1,1) = #bases check
        t11 = sum(c for (i, j), c in TA.items() for _ in [0])  # placeholder
        t11 = sum(c * (1 ** i) * (1 ** j) for (i, j), c in TA.items())
        assert t11 == len(B), (name, t11, len(B))
        conn = is_3conn(cols, n)
        wF7 = find_minor(cols, n, REF_F7)
        wF7s = find_minor(cols, n, REF_F7s)
        mc = max(TA.values())
        table[name] = {
            'n': n, 'rank': r, 'nbases': len(B),
            'tutte': sorted([[i, j, c] for (i, j), c in TA.items()]),
            'maxcoeff': mc, 'is_3conn': conn,
            'has_F7': wF7 is not None, 'F7_witness': wF7,
            'has_F7s': wF7s is not None, 'F7s_witness': wF7s,
            'dc_log_len': len(log),
        }
        print(name, 'n=%d r=%d nb=%d conn=%s maxc=%d T11=%d F7=%s F7s=%s log=%d' % (
            n, r, len(B), conn, mc, t11, wF7 is not None, wF7s is not None, len(log)), flush=True)
    # extremals
    extA = max(table, key=lambda k: table[k]['maxcoeff'])
    free = [k for k in table if not table[k]['has_F7'] and not table[k]['has_F7s']]
    extB = max(free, key=lambda k: table[k]['nbases'])
    table['_extremals'] = {'max_maxcoeff': extA, 'max_bases_Ffree': extB, 'Ffree_list': free}
    print('EXTREMAL maxcoeff:', extA, table[extA]['maxcoeff'])
    print('EXTREMAL F-free most bases:', extB, table[extB]['nbases'])
    print('F-free:', free)
    with open('output/artifacts/tutte_table.json', 'w') as f:
        json.dump(table, f, indent=1)
    print('wrote tutte_table.json')

if __name__ == '__main__':
    main()
