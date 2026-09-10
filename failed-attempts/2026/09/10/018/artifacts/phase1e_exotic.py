"""Phase-1e (target stress): (i) qf gap with RANDOM F_q coefficients
(generalizes Fp-slice: proof does not need Fp coeffs); (ii) exotic quantified
candidates: norm-QR preimage N(x) in QR(Fix), AS-image, subfield-QR preimage.
Stdlib only."""
import random
from twisted_checks import Fq, MODS, verify_irred, sumset, twprod, scale
from phase1b_checks import ev
import itertools

def load(p, l):
    m = MODS[(p, l)]; assert verify_irred(p, l, m)
    return Fq(p, l, m)

def rand_coeff_gap(p, l, D=2, trials=300, seed=5290):
    F = load(p, l); z = F.z
    mons = [(a, b) for a in range(D + 1) for b in range(D + 1 - a)]
    rng = random.Random(seed)
    bad = 0; mx = 0
    for _ in range(trials):
        coeff = [rng.choice(F.els) for _ in mons]
        if all(c == z for c in coeff): continue
        S = [x for x in F.els if ev_gen(F, x, F.frob(x), mons, coeff) == z]
        if len(S) <= D * p:
            mx = max(mx, len(S))
        elif len(S) == F.q:
            pass  # whole field: degenerate (only possible if G zero-poly; rare)
        else:
            bad += 1
            if bad <= 3: print("   VIOL size=%d q=%d" % (len(S), F.q))
    print("RAND-GAP p=%d l=%d D=%d trials=%d maxsmall=%d BAD=%d" % (p, l, D, trials, mx, bad))
    return bad

def ev_gen(F, x, y, mons, coeff):
    acc = F.z
    for (a, b), c in zip(mons, coeff):
        if c == F.z: continue
        acc = F.add(acc, F.mul(c, F.mul(F.pow(x, a), F.pow(y, b))))
    return acc

def exotic(p, l):
    F = load(p, l); z, o = F.z, F.o
    q = F.q
    fix = [a for a in F.els if F.frob(a) == a]
    fixset = set(fix)
    # QR(Fix): {t in Fix: exists z in Fix, z^2=t}
    def mul(a, b): return F.mul(a, b)
    qrfix = {t for t in fix if any(F.mul(u, u) == t for u in fix)}
    Nexp = (q - 1) // (p - 1)
    def norm(a): return F.pow(a, Nexp)
    # A1 = {x != 0 : N(x) in QR(Fix)} (quantified: N via sigma when l=2; QR via exists)
    A1 = [x for x in F.els if x != z and norm(x) in qrfix]
    # A2 = AS image {sig(y)-y}: additive subgroup = trker
    A2 = {F.add(F.frob(y), F.neg(y)) for y in F.els}
    # A3 = Fix-QR lifted: {x : Tr(x) in QR(Fix) U {0}} (l=2 only order-1)
    def trace(a):
        s = z; x = a
        for _ in range(l): s = F.add(s, x); x = F.frob(x)
        return s
    A3 = [x for x in F.els if trace(x) in qrfix or trace(x) == z]
    out = {}
    for name, A in [("normQRpre", A1), ("ASimage", sorted(A2)), ("traceQRpre", A3)]:
        A = list(A); n = len(A)
        s = len(sumset(F, A)); t = len(twprod(F, A))
        out[name] = (n, s, t)
        print("  p=%d l=%d q=%d %-11s n=%3d |A+A|=%3d |A.sigA|=%3d n^(1.1)=%.1f" %
              (p, l, q, name, n, s, t, n ** 1.1 if n else 0))
    return out

def main():
    tot = 0
    for (p, l) in [(3, 2), (5, 2), (2, 3), (3, 3)]:
        tot += rand_coeff_gap(p, l)
    for (p, l) in [(3, 2), (5, 2), (2, 3), (3, 3)]:
        exotic(p, l)
    print("VERIFY_OK" if tot == 0 else "VERIFY_FAIL")

if __name__ == "__main__":
    main()
