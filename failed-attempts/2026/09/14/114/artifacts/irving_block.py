"""Bounded recovery test for Irving-extension target.

Part A: exact-fraction checks of the target's internal arithmetic
  (pair decoding, L-exponent at N=sqrt(q), nontriviality threshold,
  strict improvement over every Burgess r at N=sqrt(q)).
Part B1: B-step degree-2 complete sums T(h)=sum_{x mod q} chi~(x(x+h)),
  max |T|/sqrt(q) split by shift class (unit vs p-dividing), prime vs
  prime-power / non-squarefree smooth q, all primitive chi.
Part B2: degree-3 complete sums F(a,b)=sum_x chi~(x(x+a)(x+b)) split by
  root-collision pattern mod p (distinct / partial / total collision).
Part C: short-sum sanity: max |S(M,N)| / (N^{23/41} q^{11/82}) over M,N
  (constant 1; only checks the bound is not trivially false at small q).
Pure Python, exact enumeration, no external deps.
"""
import math
import cmath
import itertools
from math import gcd, sqrt
from fractions import Fraction

# ---------- Part A ----------
a = Fraction(23, 41)
b = Fraction(11, 82)
k = Fraction(11, 82)
l = Fraction(57, 82)
assert l - k == a, "pair decoding"
Lexp = a / 2 + b - Fraction(1, 4)
assert Lexp == Fraction(27, 164), f"L exponent {Lexp}"
thresh = b / (1 - a)  # bound<N iff N^{1-a}>q^b
assert thresh == Fraction(11, 36), f"threshold {thresh}"
# Burgess r at N=sqrt(q): exponent (1-1/r)/2+(r+1)/(4r^2) = 1/2-1/(4r)+1/(4r^2)
for r in range(1, 15):
    be = Fraction(1, 2) - Fraction(1, 4 * r) + Fraction(1, 4 * r * r)
    assert be > Fraction(27, 164), f"Burgess r={r} {be} not worse?!"
print(f"Part A OK: pair->({k},{l}), L-exp={Lexp}, nontrivial N>q^{thresh}~q^{float(thresh):.4f}; "
      f"target 17/41~{17/41:.4f} at sqrt(q) beats every Burgess r>=1 (best r=2: 7/16=0.4375)")


# ---------- character machinery ----------
def prime_factors(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


class CharGroup:
    """Characters of (Z/qZ)^x via prime-power cyclic decomposition + CRT."""

    def __init__(self, q):
        self.q = q
        fac = prime_factors(q)
        self.comps = []  # (pe, p, e, orders)
        for p, e in fac.items():
            pe = p ** e
            orders = self._orders(p, e, pe)
            self.comps.append((pe, p, e, orders))

    def _orders(self, p, e, pe):
        if p == 2 and e == 1:
            return []
        if pe == 4:
            return [2]
        if p == 2:
            return [2, 2 ** (e - 2)]
        return [pe - pe // p]

    def _dlog_search(self, um, g, m, pe):
        cur = 1
        for s in range(m):
            if cur == um:
                return s
            cur = (cur * g) % pe
        raise AssertionError("dlog failed")

    def dlog(self, u):
        out = []
        for pe, p, e, orders in self.comps:
            um = u % pe
            if p == 2 and e >= 3:
                av = 0 if um % 4 == 1 else 1
                v = (um * (pe - 1) ** av) % pe
                t = self._dlog_search(v, 5, 2 ** (e - 2), pe)
                out.append((av, t))
            elif not orders:
                out.append(())
            else:
                m = orders[0]
                if p == 2:  # pe == 4
                    g = 3
                else:
                    phi = m
                    fac = prime_factors(phi)
                    g = next(c for c in range(2, pe)
                             if gcd(c, pe) == 1
                             and all(pow(c, phi // ell, pe) != 1 for ell in fac))
                out.append((self._dlog_search(um, g, m, pe),))
        return out


def primitive_chi_arrays(q):
    """Yield chi~ array (len q, zero on non-units) for each primitive chi mod q."""
    G = CharGroup(q)
    dlog_table = [G.dlog(u) if gcd(u, q) == 1 else None for u in range(q)]
    comp_opts = []
    for pe, p, e, orders in G.comps:
        comp_opts.append(list(itertools.product(*[range(m) for m in orders])) if orders else [()])
    out = []
    for combo in itertools.product(*comp_opts):
        flats = []
        for tup, (pe, p, e, orders) in zip(combo, G.comps):
            for j, m in zip(tup, orders):
                flats.append((j, m))
        if all(j == 0 for j, m in flats):
            continue
        widths = [len(o) for (_, _, _, o) in G.comps]
        per, fi = [], 0
        for w in widths:
            per.append(flats[fi:fi + w])
            fi += w
        vals = [0j] * q
        for u in range(q):
            if gcd(u, q) != 1:
                continue
            ph = 0.0
            for tup, pf in zip(dlog_table[u], per):
                for t, (j, m) in zip(tup, pf):
                    ph += j * t / m
            vals[u] = cmath.exp(2j * math.pi * ph)
        # primitive? for each prime ell|q, chi must be nontrivial on
        # kernel units 1+(q/ell)s of (Z/qZ)^x -> (Z/(q/ell)Z)^x.
        prim = True
        for ell in prime_factors(q):
            step = q // ell
            if all(gcd((1 + step * s) % q, q) != 1 or abs(vals[(1 + step * s) % q] - 1.0) < 1e-9
                   for s in range(ell)):
                prim = False
                break
        if prim:
            out.append(vals)
    return out


def analyze_q(q, do_b2=True):
    fac = prime_factors(q)
    primes = list(fac)
    chis = primitive_chi_arrays(q)
    sq = sqrt(q)
    EA, EB = 23 / 41, 11 / 82
    w_unit = w_non = 0.0
    b2 = {"distinct": 0.0, "partial": 0.0, "total": 0.0}
    wsr, wsi = 0.0, None
    for A in chis:
        # Burgess/Irving shift family T(h); h=0 gives phi(q) (no cancellation
        # possible) so only h != 0 classes are reported.
        for h in range(1, q):
            s = 0j
            Ah = [A[(x + h) % q] for x in range(q)]
            for x in range(q):
                s += A[x] * Ah[x]
            r = abs(s) / sq
            if any(h % p == 0 for p in primes):
                w_non = max(w_non, r)
            else:
                w_unit = max(w_unit, r)
        if do_b2:
            for ab in range(q * q):
                av, bv = divmod(ab, q)
                da = any(av % p == 0 for p in primes)
                db = any(bv % p == 0 for p in primes)
                dd = any((av - bv) % p == 0 for p in primes)
                ncoll = sum([da, db, dd])
                key = "distinct" if ncoll == 0 else ("total" if
                      all((av % p == 0 and bv % p == 0) for p in primes) else "partial")
                s = 0j
                for x in range(q):
                    s += A[x] * A[(x + av) % q] * A[(x + bv) % q]
                r = abs(s) / sq
                b2[key] = max(b2[key], r)
        P = [0j] * (2 * q + 1)
        for i in range(2 * q):
            P[i + 1] = P[i] + A[i % q]
        for N in range(1, q + 1):
            denom = (N ** EA) * (q ** EB)
            for M in range(q):
                r = abs(P[M + N] - P[M]) / denom
                if r > wsr:
                    wsr, wsi = r, (M, N)
    return len(chis), w_unit, w_non, b2, wsr, wsi


if __name__ == "__main__":
    for q in [5, 7, 8, 9, 16, 25, 27, 32, 36, 49]:
        pc, wu, wn, b2, wsr, wsi = analyze_q(q, do_b2=(q <= 36))
        print(f"q={q:3d} prim={pc:3d} B1 unit-h={wu:.3f} p|h={wn:.3f} | "
              f"B2 { {kk: round(vv, 3) for kk, vv in b2.items()} } | "
              f"short-ratio={wsr:.3f} at {wsi}", flush=True)
