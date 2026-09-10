"""Phase-1c: stress-test one-sided STRUCT triviality.
For A in {trker, qr}: max over torus cosets cT, additive Fix-cosets a+Fix,
subfield F itself, of |A cap X| vs |A|^{1-eta}. Stdlib only.
"""
import itertools, math
from twisted_checks import Fq, MODS, verify_irred

def load(p, l):
    m = MODS[(p, l)]; assert verify_irred(p, l, m)
    return Fq(p, l, m)

def coset_reps(F, H):
    # H subgroup (additive or multiplicative subgroup of F^els)
    seen = set(); reps = []
    Hset = set(H)
    z = F.z
    add = (z in Hset) and all(F.add(a, F.neg(b)) in Hset for a in H for b in H)
    for c in F.els:
        if c in seen: continue
        if add:
            cos = set(F.add(c, h) for h in H)
        else:
            if c == z: seen.add(c); continue
            cos = set(F.mul(c, h) for h in H)
            cos.add(z) if False else None
        seen |= cos; reps.append(c)
    return reps, add

def max_inter(F, A, H, mult=False):
    Aset = set(A); best = (0, None)
    z = F.z
    if mult:
        base = [h for h in H if h != z]
        # cosets c*T plus {0}? cosets partition K^times; also test {0}-shift irrelevant
        reps = []
        seen = set()
        for c in F.els:
            if c == z or c in seen: continue
            cos = {F.mul(c, h) for h in base}
            seen |= cos; reps.append(c)
        for c in reps:
            cos = {F.mul(c, h) for h in base}
            k = len(Aset & cos)
            if k > best[0]: best = (k, c)
    else:
        reps, _ = coset_reps(F, H)
        for c in reps:
            cos = {F.add(c, h) for h in H}
            k = len(Aset & cos)
            if k > best[0]: best = (k, c)
    return best

def main():
    for (p, l) in [(3, 2), (5, 2), (3, 3)]:
        F = load(p, l); z, o = F.z, F.o
        Nexp = (F.q - 1) // (p - 1)
        T = [a for a in F.els if a != z and F.pow(a, Nexp) == o]
        fix = [a for a in F.els if F.frob(a) == a]
        def trace(a):
            s = z; x = a
            for _ in range(l): s = F.add(s, x); x = F.frob(x)
            return s
        V = [a for a in F.els if trace(a) == z]
        fams = {"trker": V}
        if F.q % 2 == 1:
            fams["qr"] = [a for a in F.els if a == z or F.pow(a, (F.q - 1) // 2) == o]
        print("=== p=%d l=%d q=%d |T|=%d |Fix|=%d |V|=%d" % (p, l, F.q, len(T), len(fix), len(V)))
        for name, A in fams.items():
            n = len(A)
            kT, cT = max_inter(F, A, T, mult=True)
            kF, cF = max_inter(F, A, fix, mult=False)
            kF0 = len(set(A) & set(fix))
            th = {e: n ** (1 - e) for e in (0.25, 0.5, 0.75)}
            print("  A=%-6s n=%3d max|cT cap|= %2d  max|a+Fix cap|= %2d  |A cap Fix|= %2d  thr(1-eta)=%s" %
                  (name, n, kT, kF, kF0, {e: round(v, 2) for e, v in th.items()}))
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
