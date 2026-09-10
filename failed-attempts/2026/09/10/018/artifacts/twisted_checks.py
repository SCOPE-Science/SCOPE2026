"""Brute-force checks for lane-529 target (twisted sum-product dichotomy).

F_{p^l} = F_p[t]/(m), stdlib only. sigma=Frob_p. Checks:
 (1) QF SIZE-GAP (Fp-coefficient slice): every NONZERO F with totdeg<=D has
     |{x:F(x,sig x)=0}| <= D*p  OR  G(x):=F(x,x^p) is zero as a function.
 (2) STRUCT families: Fix, intermediate subfields, norm-1 torus, trace kernel,
     QR set (quantified comparison): sizes, |A+A|, |A.sig(A)|.
Outputs VERIFY_OK + JSON summary.
"""
import json, itertools

def pdeg(a):
    d = len(a) - 1
    while d > 0 and a[d] == 0: d -= 1
    return d

def pmod(a, m, p):
    a = list(a)
    while len(a) < 1: a = [0]
    dm = pdeg(m)
    while pdeg(a) >= dm or len(a) > dm:
        if pdeg(a) < dm: break
        da = pdeg(a); c = a[da] % p; s = da - dm
        for i in range(dm + 1):
            a[s + i] = (a[s + i] - c * m[i]) % p
        while len(a) > 1 and a[-1] == 0: a.pop()
    a += [0] * (dm - len(a))
    return a[:dm]

def pmul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] = (r[i + j] + x * y) % p
    return r

def padd(a, b, p):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p for i in range(n)]

# Hardcoded irreducible moduli (each verified below: no factor of deg<=l//2).
MODS = {
    (2, 2): [1, 1, 1],   # t^2+t+1
    (3, 2): [1, 0, 1],   # t^2+1
    (5, 2): [2, 0, 1],   # t^2+2
    (2, 3): [1, 1, 0, 1],# t^3+t+1
    (3, 3): [1, 2, 0, 1],# t^3+2t+1
    (2, 4): [1, 1, 0, 0, 1], # t^4+t+1
}

def verify_irred(p, l, m):
    # every monic g of 1<=deg<=l//2 must not divide m
    for d in range(1, l // 2 + 1):
        for c in itertools.product(range(p), repeat=d):
            g = list(c) + [1]
            if pmod(m, g, p) == [0] * d:
                return False
    return True

class Fq:
    def __init__(self, p, l, m):
        self.p, self.l, self.m = p, l, m
        self.q = p ** l
        self.els = [tuple(c) for c in itertools.product(range(p), repeat=l)]
        self.z = tuple([0] * l)
        o = [0] * l; o[0] = 1 % p; self.o = tuple(o)
    def red(self, a): return tuple(pmod(list(a), self.m, self.p))
    def add(self, a, b): return self.red(padd(list(a), list(b), self.p))
    def mul(self, a, b): return self.red(pmul(list(a), list(b), self.p))
    def neg(self, a): return tuple((-x) % self.p for x in a)
    def frob(self, a):
        big = [0] * ((self.l - 1) * self.p + 1)
        for i, x in enumerate(a): big[i * self.p] = (big[i * self.p] + x) % self.p
        return self.red(big)
    def pow(self, a, e):
        r = self.o
        for _ in range(e): r = self.mul(r, a)
        return r

def sumset(F, A):
    return {F.add(a, b) for a in A for b in A}

def twprod(F, A):
    sA = [F.frob(a) for a in A]
    return {F.mul(a, b) for a in A for b in sA}

def check_case(p, l, D=2):
    m = MODS[(p, l)]
    assert verify_irred(p, l, m), "modulus not irreducible"
    F = Fq(p, l, m)
    assert len(set(F.els)) == p ** l
    # field sanity: every nonzero elt has inverse; frob is automorphism of order l
    z, o = F.z, F.o
    nz = [a for a in F.els if a != z]
    assert len(nz) == F.q - 1
    for a in F.els:
        x = a
        for _ in range(l): x = F.frob(x)
        assert x == a, "frob^l != id"
    for a in nz:
        assert any(F.mul(a, b) == o for b in F.els), "no inverse"
    fix = [a for a in F.els if F.frob(a) == a]
    assert len(fix) == p, "Fix size %d != %d" % (len(fix), p)
    def frobk(a, k):
        for _ in range(k): a = F.frob(a)
        return a
    subs = {}
    for d in range(1, l + 1):
        if l % d == 0:
            subs[d] = [a for a in F.els if frobk(a, d) == a]
            assert len(subs[d]) == p ** d
    Nexp = (F.q - 1) // (p - 1)
    torus = [a for a in nz if F.pow(a, Nexp) == o]
    assert len(torus) == Nexp, "torus order"
    def trace(a):
        s = z; x = a
        for _ in range(l): s = F.add(s, x); x = F.frob(x)
        return s
    trker = [a for a in F.els if trace(a) == z]
    assert len(trker) == F.q // p, "trace kernel size"
    qr = None
    if F.q % 2 == 1:
        qr = [a for a in F.els if a == z or F.pow(a, (F.q - 1) // 2) == o]
        assert len(qr) == (F.q + 1) // 2, "QR size"
    # (1) size-gap over Fp-coeff slice
    mons = [(a, b) for a in range(D + 1) for b in range(D + 1 - a)]
    tested = 0; small_max = 0; degen = 0; bad = 0; bad_ex = []
    for coeff in itertools.product(range(p), repeat=len(mons)):
        if all(c == 0 for c in coeff): continue
        tested += 1
        S = [x for x in F.els
             if ev(F, x, F.frob(x), mons, coeff) == z]
        if len(S) <= D * p:
            small_max = max(small_max, len(S))
        else:
            # degenerate? G(x)=F(x,x^p) zero as function?
            if all(ev(F, x, F.frob(x), mons, coeff) == z for x in F.els):
                degen += 1
            else:
                bad += 1
                if len(bad_ex) < 3: bad_ex.append((coeff, len(S)))
    fams = {}
    famlist = [("fix", fix), ("torus", torus), ("trker", trker)]
    famlist += [("sub_%d" % d, S) for d, S in subs.items()]
    if qr is not None: famlist.append(("qr", qr))
    for name, A in famlist:
        fams[name] = {"n": len(A), "sum": len(sumset(F, A)), "tw": len(twprod(F, A))}
    return {"p": p, "l": l, "q": F.q, "tested": tested, "small_max": small_max,
            "degen": degen, "bad": bad, "bad_ex": bad_ex, "fams": fams}

def ev(F, x, y, mons, coeff):
    acc = F.z
    for (a, b), c in zip(mons, coeff):
        if c: acc = F.add(acc, F.pow(F.o, 0) and scale(F, F.mul(F.pow(x, a), F.pow(y, b)), c))
    return acc

def scale(F, t, c):
    s = F.z
    for _ in range(c): s = F.add(s, t)
    return s

def main():
    out = []
    for (p, l) in [(2, 2), (3, 2), (5, 2), (2, 3), (3, 3), (2, 4)]:
        r = check_case(p, l, D=2)
        out.append(r)
        print("p=%d l=%d q=%d tested=%d small_max=%d degen=%d BAD=%d" %
              (r["p"], r["l"], r["q"], r["tested"], r["small_max"], r["degen"], r["bad"]))
        for name, f in r["fams"].items():
            print("   %-7s n=%3d |A+A|=%4d |A.sigA|=%4d" % (name, f["n"], f["sum"], f["tw"]))
        assert r["bad"] == 0
    print("VERIFY_OK")
    with open("output/artifacts/twisted_summary.json", "w") as f:
        json.dump(out, f, indent=1, default=str)

if __name__ == "__main__":
    main()
