"""Lane-772 recovery probe: lambda-algebra E2 anchoring attempt for stem 53.

WHAT THIS IS: bounded stdlib-only attempt (Route A) to anchor the target's E2
input Ext_A^{s,53+s}(F2,F2) via Lambda-algebra homology, plus known-answer
validation on low stems.

RESULT: FAIL (documents the block). Two concrete defects found:
  D1. The complex uses the same index-sum for every filtration, but the Lambda
      differential lowers index-sum by 1 (d(l_n) lands in index-sum n-1), so a
      fixed internal-degree complex is required. Consequence: every computed
      differential matrix is empty/zero -> degenerate "homology = basis count".
  D2. The monomial filter drops all lambda_0-containing monomials, deleting the
      h_0-multiple sector. Known-answer check: Ext^{2,5} (stem 3, filt 2) is
      F2^2 = {h_1^2, h_0 h_2}, but the code returns dimension 1.
USAGE: python3 lambda_probe.py  (stdlib only, deterministic)
"""
from functools import lru_cache


def binom_mod2(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return 1 if (k & ~n) == 0 else 0


def admissible_monomials(deg):
    res = []

    def rec(remaining, max_next, cur):
        if remaining == 0:
            res.append(tuple(cur))
            return
        for a in range(1, min(remaining, max_next) + 1):
            cur.append(a)
            rec(remaining - a, min(a // 2, remaining - a), cur)
            cur.pop()

    rec(deg, deg, [])
    return res


def adem(a, b):
    if a >= 2 * b:
        return {(a, b): 1}
    out = {}
    for c in range(0, b):
        if binom_mod2(b - c - 1, 2 * c - a):
            out[(a + b - c, c)] = out.get((a + b - c, c), 0) ^ 1
    return {k: v for k, v in out.items() if v}


def to_admissible(mon):
    cur = {mon: 1}
    for _ in range(10000):
        for m in list(cur.keys()):
            for i in range(len(m) - 1):
                a, b = m[i], m[i + 1]
                if a < 2 * b:
                    del cur[m]
                    rep = adem(a, b)
                    for (na, nb), v in rep.items():
                        nm = m[:i] + (na, nb) + m[i + 2:]
                        cur[nm] = cur.get(nm, 0) ^ v
                        if cur[nm] == 0:
                            del cur[nm]
                    break
            else:
                continue
            break
        else:
            break
    return {k: v for k, v in cur.items() if v}


def diff_monomial(mon):
    if len(mon) == 1:
        n = mon[0]
        out = {}
        for j in range(1, n):
            if binom_mod2(n - j - 1, j):
                for m, v in to_admissible((n - j - 1, j)).items():
                    out[m] = out.get(m, 0) ^ v
                    if out[m] == 0:
                        del out[m]
        return out
    A, B = (mon[0],), mon[1:]
    dA, dB = diff_monomial(A), diff_monomial(B)
    out = {}
    for m, v in dA.items():
        for mm, vv in to_admissible(m + B).items():
            out[mm] = out.get(mm, 0) ^ (v & vv)
            if out[mm] == 0:
                del out[mm]
    for m, v in dB.items():
        for mm, vv in to_admissible(A + m).items():
            out[mm] = out.get(mm, 0) ^ (v & vv)
            if out[mm] == 0:
                del out[mm]
    return out


def adm_basis(stem, filt):
    res = []

    def rec(rem, maxv, cur, last):
        if len(cur) == filt:
            if rem == 0:
                res.append(tuple(cur))
            return
        for a in range(0, rem + 1):
            if last is not None and last < 2 * a:
                continue
            if a > maxv:
                continue
            cur.append(a)
            rec(rem - a, a, cur, a)
            cur.pop()

    rec(stem, stem, [], None)
    return [m for m in res if all(x >= 1 for x in m)]  # DEFECT D2: drops lambda_0


def rank_mod2(rows, ncols):
    M = [r[:] for r in rows]
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                for j in range(c, ncols):
                    M[i][j] ^= M[r][j]
        r += 1
    return r


def ext_dims(stem, fmax=6):
    # DEFECT D1: same index-sum `stem` at every filtration; the Lambda
    # differential lowers index-sum, so in/out matrices below are vacuous.
    bases = {f: sorted(adm_basis(stem, f)) for f in range(0, fmax + 1)}
    idx = {f: {m: i for i, m in enumerate(bases[f])} for f in bases}
    ranks = {}
    for f in range(0, fmax):
        A, B = bases[f], bases[f + 1]
        rows = []
        for m in A:
            d = diff_monomial(m)
            row = [0] * len(B)
            for mm in d:
                if mm in idx[f + 1]:
                    row[idx[f + 1][mm]] ^= 1
            rows.append(row)
        ranks[f] = rank_mod2(rows, len(B)) if rows and B else 0
    dims = {}
    for f in range(0, fmax + 1):
        r_in = ranks.get(f - 1, 0) if f > 0 else 0
        dims[f] = len(bases[f]) - r_in - ranks.get(f, 0)
    return bases, dims, ranks


def main():
    print("== admissible Steenrod monomial counts (sanity probe) ==")
    for d in [5, 10, 15, 20, 30, 53]:
        print(f"deg {d}: {len(admissible_monomials(d))}")
    print("== known-answer check: stem 3, filt 2 (Ext^{{2,5}} = F2^2) ==")
    b3, d3, r3 = ext_dims(3, 4)
    print(f"computed dimH={d3[2]} bases={b3[2]} ranks={r3}")
    print("MISMATCH" if d3[2] != 2 else "MATCH",
          f"(computed {d3[2]}, expected 2: h_1^2 and h_0 h_2)")
    print("== stem 53 E2 attempt ==")
    b53, d53, r53 = ext_dims(53, 6)
    for f in sorted(d53):
        print(f"filt {f}: nbasis={len(b53[f])} dimH={d53[f]}")
    allzero = all(v == 0 for v in r53.values())
    print(f"all differential ranks zero: {allzero} -> DEGENERATE (defect D1)")
    print("PROBE VERDICT: FAIL (E2 route uncertified; defects D1+D2 logged)")


if __name__ == "__main__":
    main()
