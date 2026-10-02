"""Order-polytope Ehrhart census for all 406 unlabeled types n<=6.
Reads posets.json. Per type:
  e1 = linear extensions by ideal-lattice DP (bottom-up over ideals);
  e2 = linear extensions by independent backtracking over minimal elements
       (= # top simplices of Stanley canonical triangulation -> normalized volume);
  assert e1 == e2 (dual volume agreement);
  L(m), m=0..n: weak order-preserving maps P->[m+1] by ideal-fiber recursion, memoized;
  interpolate (Fractions) to Ehrhart coeffs; assert n!*lead == e1;
  h* by triangular forward substitution; assert sum h* == e1, all >= 0 integers;
  strict maps S(Q,k) by antichain-fiber recursion; reciprocity (-1)^n L(-m)=S(P,m-1);
  per-n maxima by exhaustive scan.
Writes ehrhart.json.
"""
"""Order-polytope Ehrhart census for all 406 unlabeled types n<=6."""
import json
import math
from fractions import Fraction

def ideals(le, n):
    below = [0] * n
    for x in range(n):
        b = 0
        for y in range(n):
            if (le[y] >> x) & 1:
                b |= (1 << y)
        below[x] = b
    N = 1 << n
    out = []
    for I in range(N):
        ok = True
        m = I
        while m:
            x = (m & -m).bit_length() - 1
            if below[x] & ~I:
                ok = False
                break
            m &= m - 1
        if ok:
            out.append(I)
    return out, below

def lin_ext_ideal(idl):
    E = {0: 1}
    for I in idl:
        if I == 0:
            continue
        t = 0
        m = I
        while m:
            x = (m & -m).bit_length() - 1
            J = I ^ (1 << x)
            # x minimal in I  <=> below[x] & I == {x}  <=> below[x] & J == 0
            t += E.get(J, 0) if True else 0
            m &= m - 1
        E[I] = t
    return E

def lin_ext_bt(le, n, below):
    # independent path: DFS removing minimal elements (topological-sort count)
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def c(S):
        if S == 0:
            return 1
        t = 0
        m = S
        while m:
            x = (m & -m).bit_length() - 1
            if below[x] & S == (1 << x):
                t += c(S ^ (1 << x))
            m &= m - 1
        return t
    return c((1 << n) - 1)

def main():
    data = json.load(open("posets.json"))
    rectab = []
    for t in data["types"]:
        n, idx, le = t["n"], t["idx"], t["le"]
        idl, below = ideals(le, n)
        idset = set(idl)
        # DP: lin-ext count of ideal I = sum over maximal x in I of count(I \ {x});
        # x maximal in I  <=>  le[x] & I == {x}.  (I\{x} is again an ideal.)
        E2 = {0: 1}
        for I in idl:
            if I == 0:
                continue
            t_ = 0
            m = I
            while m:
                x = (m & -m).bit_length() - 1
                J = I ^ (1 << x)
                if le[x] & I == (1 << x):
                    t_ += E2[J]
                m &= m - 1
            E2[I] = t_
        full = (1 << n) - 1
        e1 = E2[full]
        e2 = lin_ext_bt(le, n, below)
        assert e1 == e2, (n, idx, e1, e2)
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def L(S, m):
            if m == 0:
                return 1
            if S == 0:
                return 1
            # ideals of subposet S: I subset S, downward closed within S
            tot = 0
            I = S
            while True:
                ok = True
                mm = I
                while mm:
                    x = (mm & -mm).bit_length() - 1
                    if below[x] & S & ~I:
                        ok = False
                        break
                    mm &= mm - 1
                if ok:
                    tot += L(S & ~I, m - 1)
                if I == 0:
                    break
                I = (I - 1) & S
            return tot
        vals = [L(full, m) for m in range(n + 1)]
        # interpolate: solve Vandermonde V c = vals, V[m][p] = m^p
        A = [[Fraction(m) ** p for p in range(n + 1)] + [Fraction(vals[m])] for m in range(n + 1)]
        Nn = n + 1
        for c_ in range(Nn):
            piv = next(r for r in range(c_, Nn) if A[r][c_] != 0)
            A[c_], A[piv] = A[piv], A[c_]
            d = A[c_][c_]
            A[c_] = [a / d for a in A[c_]]
            for r in range(Nn):
                if r != c_ and A[r][c_] != 0:
                    f = A[r][c_]
                    A[r] = [a - f * b for a, b in zip(A[r], A[c_])]
        coef = [A[p][Nn] for p in range(Nn)]
        for m in range(n + 1):
            assert sum(coef[p] * Fraction(m) ** p for p in range(Nn)) == vals[m]
        fact = math.factorial(n)
        assert coef[n] * fact == e1, (n, idx, coef[n], e1)
        # h*: L(j) = sum_{i<=j} h_i C(j+n-i, n)
        h = []
        for j in range(n + 1):
            s = vals[j] - sum(h[i] * math.comb(j + n - i, n) for i in range(j))
            assert s == int(s) and s >= 0, (n, idx, j, s)
            h.append(int(s))
        assert sum(h) == e1, (n, idx)
        # strict maps S(Q,k): fiber over value 1 is antichain of minima
        @lru_cache(maxsize=None)
        def S(S_, k):
            if S_ == 0:
                return 1
            if k == 0:
                return 0
            mins = []
            m = S_
            while m:
                x = (m & -m).bit_length() - 1
                if below[x] & S_ == (1 << x):
                    mins.append(x)
                m &= m - 1
            tot = 0
            for r in range(1 << len(mins)):
                A_ = 0
                for i2, x in enumerate(mins):
                    if (r >> i2) & 1:
                        A_ |= (1 << x)
                tot += S(S_ & ~A_, k - 1)
            return tot
        # direct check: L(-m) vs (-1)^n S(full, m-1)
        for m in range(1, n + 2):
            Lm = sum(coef[p] * Fraction(-m) ** p for p in range(Nn))
            assert Lm == ((-1) ** n) * S(full, m - 1), (n, idx, m, Lm, S(full, m - 1))
        rectab.append({"n": n, "idx": idx, "e": e1, "Lvals": vals,
                       "coef": [str(c) for c in coef], "hstar": h})
    mx = {}
    for r in rectab:
        e = mx.get(r["n"])
        if e is None or r["e"] > e["max"]:
            mx[r["n"]] = {"max": r["e"], "arg": [r["idx"]]}
        elif r["e"] == e["max"]:
            e["arg"].append(r["idx"])
    print("counts:", {n: sum(1 for r in rectab if r["n"] == n) for n in range(7)})
    print("maxima:", mx)
    # uniqueness of antichain maximizer: check arg lists
    json.dump({"records": rectab, "maxima": {str(k): v for k, v in mx.items()}},
              open("ehrhart.json", "w"))
    print("wrote ehrhart.json with", len(rectab), "records")

main()
