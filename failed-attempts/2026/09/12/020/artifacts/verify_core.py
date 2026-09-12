"""CORE VERIFIER (artifact): verified bracket core.
Part A: exhaustive over equivalence triples on n=3,4 points.
Part B: explicit 8-point witness triple (violation + distributive gen-lattice).
Pure stdlib. -> VERIFY_OK.
"""
import time

def rgs_partitions(n):
    out = []
    def rec(prefix, mx):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for v in range(mx + 2):
            prefix.append(v)
            rec(prefix, max(mx, v))
            prefix.pop()
    if n == 0:
        return [()]
    rec([0], 0)
    return out

def rows_of(rgs, n):
    return [sum(1 << j for j in range(n) if rgs[i] == rgs[j]) for i in range(n)]

def compose_rows(R, S, n):
    T = []
    for i in range(n):
        m = 0
        r = R[i]
        j = 0
        while r:
            if r & 1:
                m |= S[j]
            j += 1
            r >>= 1
        T.append(m)
    return T

def meet_rows(R, S, n):
    return [R[i] & S[i] for i in range(n)]

def toint(rows, n):
    v = 0
    for i in range(n):
        v |= rows[i] << (i * n)
    return v

def join_rows(R, S, n):
    U = [R[i] | S[i] for i in range(n)]
    for k in range(n):
        Uk = U[k]
        for i in range(n):
            if (U[i] >> k) & 1:
                U[i] |= Uk
    return U

def violates(A, B, G, n):
    BG = compose_rows(B, G, n)
    AB = meet_rows(A, B, n)
    AG = meet_rows(A, G, n)
    R = compose_rows(compose_rows(AB, AG, n), AB, n)
    for i in range(n):
        if A[i] & BG[i] & ~R[i]:
            return True
    return False

def witnesses(A, B, G, n):
    BG = compose_rows(B, G, n)
    AB = meet_rows(A, B, n)
    AG = meet_rows(A, G, n)
    R = compose_rows(compose_rows(AB, AG, n), AB, n)
    return [(i, j) for i in range(n) for j in range(n)
            if (A[i] >> j) & 1 and (BG[i] >> j) & 1 and not (R[i] >> j) & 1]

def gen_lattice_distributive(A, B, G, n):
    mask = (1 << n) - 1
    BOT = toint([1 << i for i in range(n)], n)
    TOP = toint([mask for _ in range(n)], n)
    S = {toint(A, n), toint(B, n), toint(G, n), BOT, TOP}
    def fromint(v):
        return [(v >> (i * n)) & mask for i in range(n)]
    changed = True
    while changed:
        changed = False
        L = [fromint(v) for v in S]
        for x in L:
            for y in L:
                m = toint(meet_rows(x, y, n), n)
                j = toint(join_rows(x, y, n), n)
                if m not in S:
                    S.add(m)
                    changed = True
                if j not in S:
                    S.add(j)
                    changed = True
    Lf = [fromint(v) for v in S]
    for x in Lf:
        for y in Lf:
            for z in Lf:
                j = fromint(toint(join_rows(y, z, n), n))
                lhs = toint(meet_rows(x, j, n), n)
                mxy = fromint(toint(meet_rows(x, y, n), n))
                mxz = fromint(toint(meet_rows(x, z, n), n))
                if lhs != toint(join_rows(mxy, mxz, n), n):
                    return False, len(S)
    return True, len(S)

def main():
    t0 = time.time()
    for n in (3, 4):
        R = rgs_partitions(n)
        RR = [rows_of(r, n) for r in R]
        nviol = 0
        for A in RR:
            for B in RR:
                for G in RR:
                    if violates(A, B, G, n):
                        nviol += 1
                        ok, _ = gen_lattice_distributive(A, B, G, n)
                        assert not ok, (n, "distributive violator found")
        print(f"n={n}: violating triples={nviol} all-nondistributive=True", flush=True)
    n = 8
    a = (0, 0, 0, 0, 1, 0, 1, 1)
    b = (0, 1, 2, 2, 1, 1, 0, 1)
    g = (0, 1, 1, 0, 0, 2, 0, 1)
    A, B, G = rows_of(a, n), rows_of(b, n), rows_of(g, n)
    W = witnesses(A, B, G, n)
    ok, sz = gen_lattice_distributive(A, B, G, n)
    print(f"n=8: violation={bool(W)} witnesses={W} distributive={ok} size={sz}", flush=True)
    assert W and (1, 0) in W and (5, 0) in W and ok and sz == 8
    print(f"VERIFY_OK total={time.time()-t0:.1f}s")

if __name__ == '__main__':
    main()
