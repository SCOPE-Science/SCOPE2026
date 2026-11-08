"""Separate direct finite-field checks of nine lattice equations.

Run: python finite_models.py. Only fields of orders two and three and
ambient dimensions one to three are checked; proof is algebraic.
"""
from itertools import product

def reduced(vectors, p, n):
    rows = [list(v) for v in vectors]
    pivot = 0
    for column in range(n):
        spot = next((i for i in range(pivot, len(rows)) if rows[i][column] % p), None)
        if spot is None:
            continue
        rows[pivot], rows[spot] = rows[spot], rows[pivot]
        inv = pow(rows[pivot][column], -1, p)
        rows[pivot] = [inv * a % p for a in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [(a - factor * b) % p for a, b in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return tuple(tuple(row) for row in rows[:pivot])

def model(p, n):
    vectors = list(product(range(p), repeat=n))
    zero = reduced([], p, n)
    known = {zero}
    queue = [zero]
    for basis in queue:
        for vector in vectors:
            new = reduced(basis + (vector,), p, n)
            if new not in known:
                known.add(new)
                queue.append(new)
    bases = sorted(known, key=lambda b: (len(b), b))
    ids = {basis: idx for idx, basis in enumerate(bases)}
    ranks = [len(basis) for basis in bases]
    masks = []
    for basis in bases:
        bits = 0
        for coefficients in product(range(p), repeat=len(basis)):
            vec = tuple(sum(c * row[k] for c, row in zip(coefficients, basis)) % p for k in range(n))
            bits |= 1 << vectors.index(vec)
        masks.append(bits)
    mask_ids = {bits: idx for idx, bits in enumerate(masks)}
    s = len(bases)
    join = [[0] * s for _ in range(s)]
    meet = [[0] * s for _ in range(s)]
    for i in range(s):
        for j in range(s):
            join[i][j] = ids[reduced(bases[i] + bases[j], p, n)]
            meet[i][j] = mask_ids[masks[i] & masks[j]]
    return bases, ranks, join, meet, masks

def profile(n, ranks, joins, meets, a, b, c):
    d = lambda index: ranks[index]
    triple_join = joins[joins[a][b]][c]
    triple_meet = meets[meets[a][b]][c]
    total = d(triple_join)
    t = d(triple_meet)
    out = {
        '000': n-total,
        '100': total-d(joins[b][c]),
        '010': total-d(joins[a][c]),
        '001': total-d(joins[a][b]),
        '110': d(meets[a][b])-t,
        '101': d(meets[a][c])-t,
        '011': d(meets[b][c])-t,
        '111': t,
    }
    out['triangle'] = d(a) - sum(out[s] for s in ('100', '110', '101', '111'))
    assert all(v >= 0 for v in out.values()), (a, b, c, out)
    assert sum(out.values()) + out['triangle'] == n
    assert d(b) == sum(out[s] for s in ('010','110','011','111'))+out['triangle']
    assert d(c) == sum(out[s] for s in ('001','101','011','111'))+out['triangle']
    return tuple(out[k] for k in ('000','100','010','001','110','101','011','111','triangle'))



def main():
    from math import comb
    for n in (1,2,3):
        predicted = sum(comb(8,k) for k in range(1,min(n,8)+1))
        predicted += sum(comb(8,k) for k in range(1,min(n-2,8)+1))
        if n%2==0: predicted+=1
        for q in (2,3):
            bases, ranks, joins, meets, masks = model(q,n)
            bottom=0
            top=len(bases)-1
            detected=set()
            for a in range(len(bases)):
                for b in range(len(bases)):
                    for c in range(len(bases)):
                        xyz=(a,b,c)
                        profile_values=profile(n,ranks,joins,meets,a,b,c)
                        expected_mask=sum(1<<[0,1,2,4,3,5,6,7,8][i] for i,m in enumerate(profile_values) if m>0)
                        mask=0
                        for s in range(8):
                            left=top
                            right=bottom
                            for i in range(3):
                                if s>>i&1:left=meets[left][xyz[i]]
                                else:right=joins[right][xyz[i]]
                            if left!=meets[left][right]:mask|=1<<s
                        if meets[a][joins[b][c]] != joins[meets[a][b]][meets[a][c]]:
                            mask|=1<<8
                        assert mask==expected_mask,(n,q,xyz,mask,expected_mask)
                        detected.add(mask)
            assert len(detected)==predicted,(n,q,len(detected),predicted)
            print('PASS n={} F{} subspaces={} tuples={} fingerprint_types={}'.format(n,q,len(bases),len(bases)**3,len(detected)))
    print('PASS direct finite subspace models agree with nine-block fingerprints')
if __name__=='__main__': main()
