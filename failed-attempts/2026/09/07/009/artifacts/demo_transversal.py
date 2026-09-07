"""Transversal toolchain demo on odd-order DCLS (validates pipeline used for n=10)."""
import itertools

def transversals(L):
    n = len(L)
    cells = [(r, c, L[r][c]) for r in range(n) for c in range(n)]
    best = []
    full_count = [0]
    # order cells; simple branch and bound over rows
    rows_cells = [[(r, c, s) for (r, c, s) in cells if r == rr] for rr in range(n)]
    best_len = [0]
    full = []
    def rec(r, used_c, used_s, cur):
        # bound
        if len(cur) + (n - r) <= best_len[0]:
            # still need to explore for full count? separate; here just max
            pass
        if r == n:
            if len(cur) > best_len[0]:
                best_len[0] = len(cur)
                best[:] = list(cur)
            if len(cur) == n:
                full_count[0] += 1
                full.append(list(cur))
            return
        # option: skip row r
        rec(r+1, used_c, used_s, cur)
        for (rr, c, s) in rows_cells[r]:
            if c not in used_c and s not in used_s:
                used_c.add(c); used_s.add(s); cur.append((rr, c, s))
                rec(r+1, used_c, used_s, cur)
                cur.pop(); used_c.discard(c); used_s.discard(s)
    rec(0, set(), set(), [])
    return best_len[0], best, full_count[0]

for n, a in [(5, (0,2,4,1,3)), (3, (0,2,1))]:
    L = [[(i + a[(j-i) % n]) % n for j in range(n)] for i in range(n)]
    tau, ex, nfull = transversals(L)
    print(f"n={n} a={a} tau={tau} n_full_transversals={nfull} example={ex}")
