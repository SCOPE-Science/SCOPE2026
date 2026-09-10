"""Phase-1b checks: D=3 qf size-gap slice, Artin-Schreier fiber structure,
sigma-invariance flags for STRUCT families. Stdlib only."""
import itertools
from twisted_checks import Fq, MODS, verify_irred, sumset, twprod, scale

def qf_gap(p, l, D):
    m = MODS[(p, l)]; assert verify_irred(p, l, m)
    F = Fq(p, l, m); z = F.z
    mons = [(a, b) for a in range(D + 1) for b in range(D + 1 - a)]
    tested = 0; small_max = 0; whole = 0; bad = 0; bad_ex = []
    for coeff in itertools.product(range(p), repeat=len(mons)):
        if all(c == 0 for c in coeff): continue
        tested += 1
        S = [x for x in F.els if ev(F, x, F.frob(x), mons, coeff) == z]
        if len(S) <= D * p:
            small_max = max(small_max, len(S))
        elif len(S) == F.q:
            whole += 1
        else:
            # allow: G zero-as-function on S but check whole-field degeneracy only;
            # record as bad (proper intermediate zero set)
            bad += 1
            if len(bad_ex) < 5: bad_ex.append((coeff, len(S)))
    return {"p": p, "l": l, "q": F.q, "D": D, "tested": tested,
            "small_max": small_max, "whole": whole, "bad": bad, "bad_ex": bad_ex}

def ev(F, x, y, mons, coeff):
    acc = F.z
    for (a, b), c in zip(mons, coeff):
        if c: acc = F.add(acc, scale(F, F.mul(F.pow(x, a), F.pow(y, b)), c))
    return acc

def as_fibers(p, l):
    """phi(x)=sig(x)-x: image size, fiber sizes, A_B=phi^{-1}(B) sizes."""
    m = MODS[(p, l)]; F = Fq(p, l, m); z = F.z
    phi = {x: F.add(F.frob(x), F.neg(x)) for x in F.els}
    im = set(phi.values())
    from collections import Counter
    fib = Counter(phi.values())
    return {"p": p, "l": l, "q": F.q, "im_size": len(im),
            "fiber_sizes": sorted(set(fib.values())),
            "exp_im": F.q // p}

def invariance(p, l):
    m = MODS[(p, l)]; F = Fq(p, l, m); z, o = F.z, F.o
    fix = [a for a in F.els if F.frob(a) == a]
    Nexp = (F.q - 1) // (p - 1)
    torus = [a for a in F.els if a != z and F.pow(a, Nexp) == o]
    def sigset(A): return {F.frob(a) for a in A}
    out = {}
    for name, A in [("fix", fix), ("torus", torus)]:
        out[name] = {"n": len(A), "sig_invariant": sigset(A) == set(A)}
    if F.q % 2 == 1:
        qr = [a for a in F.els if a == z or F.pow(a, (F.q - 1) // 2) == o]
        out["qr"] = {"n": len(qr), "sig_invariant": sigset(qr) == set(qr)}
    return {"p": p, "l": l, **out}

def main():
    for (p, l) in [(2, 2), (3, 2)]:
        r = qf_gap(p, l, 3)
        print("QF-GAP D=3: p=%d l=%d q=%d tested=%d small_max=%d whole=%d BAD=%d %s" %
              (r["p"], r["l"], r["q"], r["tested"], r["small_max"], r["whole"], r["bad"], r["bad_ex"]))
        assert r["bad"] == 0
    for (p, l) in [(2, 2), (3, 2), (2, 3), (3, 3)]:
        r = as_fibers(p, l)
        print("AS: p=%d l=%d q=%d im=%d (exp q/p=%d) fibersizes=%s" %
              (r["p"], r["l"], r["q"], r["im_size"], r["exp_im"], r["fiber_sizes"]))
        assert r["im_size"] == r["exp_im"] and set(r["fiber_sizes"]) == {p}
    for (p, l) in [(2, 2), (3, 2), (5, 2), (3, 3)]:
        print("INV:", invariance(p, l))
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
