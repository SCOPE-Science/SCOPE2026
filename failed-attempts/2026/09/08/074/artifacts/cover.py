"""Deterministic covering toolkit (stdlib only). Masks as Python ints mod L."""
def build_masks(moduli, L):
    mask = {}
    for m in moduli:
        assert L % m == 0, (m, L)
        mm = []
        for r in range(m):
            b = 0
            for n in range(r, L, m):
                b |= (1 << n)
            mm.append(b)
        mask[m] = mm
    return mask

def pop(x):
    return bin(x).count('1')

def check_cover(modres, L):
    """Return (covered_count, uncovered_list). Covers Z_L iff uncovered empty."""
    cov = 0
    # modres: list of (m, r)
    # build on the fly
    for (m, r) in modres:
        b = 0
        for n in range(r % m, L, m):
            b |= (1 << n)
        cov |= b
    full = (1 << L) - 1
    R = full ^ cov
    bad = []
    n = 0
    while R:
        if R & 1:
            bad.append(n)
        R >>= 1
        n += 1
    return pop(cov), bad

def dfs_cover_exists(moduli, L, node_cap=4000000, time_cap=240):
    """Decide whether full moduli set admits residues covering Z_L.
    Branch on first uncovered n; each remaining modulus forced to r=n mod m.
    Monotone: if any subset covers, full set covers (extra moduli arbitrary)."""
    import time
    t0 = time.time()
    mods = tuple(sorted(moduli))
    mask = build_masks(mods, L)
    full = (1 << L) - 1
    inv = {m: L // m for m in mods}
    nodes = [0]
    result = [None]
    outcome = ['UNSAT']
    def rec(assigned, covered, un):
        nodes[0] += 1
        if result[0] is not None:
            return True
        if nodes[0] > node_cap:
            outcome[0] = 'CAP'
            return True
        if covered == full:
            result[0] = list(assigned)
            outcome[0] = 'COVER'
            return True
        R = full ^ covered
        u = pop(R)
        s = 0
        for m in un:
            s += inv[m]
        if s < u:
            return False
        if time.time() - t0 > time_cap:
            outcome[0] = 'CAP'
            return True
        n = (R & -R).bit_length() - 1
        cand = sorted(un, key=lambda m: inv[m])  # small moduli first
        for i, m in enumerate(cand):
            r = n % m
            rest = cand[:i] + cand[i+1:]
            if rec(assigned + ((m, r),), covered | mask[m][r], rest):
                if result[0] is not None or outcome[0] == 'CAP':
                    return True
        return False
    rec((), 0, mods)
    return outcome[0], result[0], nodes[0], time.time() - t0
