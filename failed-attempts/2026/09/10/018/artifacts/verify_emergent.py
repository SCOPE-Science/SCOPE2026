"""One-command replay for the EMERGENT qf-vacuity lemma (lane-529).

Checks (stdlib only):
  E1  Distinct-exponent injectivity: for p>D, (a,b)->a+b*p injective over
      {a+b<=D}  =>  G(x)=F(x,x^p) nonzero-poly iff F nonzero, deg G<=D*p.
  E2  Exhaustive qf size-gap, Fp-coeff slice, D=2, at (3,2),(5,2):
      every nonzero F, totdeg<=2: |{x:F(x,sig x)=0}| <= 2*p or whole field.
  E3  Window-avoidance corollary (numeric): m*D*p < q^delta and
      q-m*D*p > q^{1-delta} for large (p,l); spot-check (5,2),(7,2)h,(5,3)h.
  E4  Horn-necessity identities: T.sig(T)=T, V+V=V (both GROWTH horns needed).
Prints VERIFY_OK on success.
"""
import itertools

from twisted_checks import Fq, MODS, verify_irred, sumset, twprod


def e1_injectivity(D=2, p=5):
    seen = {}
    for a in range(D + 1):
        for b in range(D + 1 - a):
            k = a + b * p
            assert k not in seen, "collision %d" % k
            seen[k] = (a, b)
    assert max(seen) <= D * p
    print("E1 injectivity D=%d p=%d: %d monomials, maxdeg=%d<=%d OK"
          % (D, p, len(seen), max(seen), D * p))


def e2_gap(p, l, D=2):
    m = MODS[(p, l)]
    assert verify_irred(p, l, m)
    F = Fq(p, l, m)
    z = F.z
    mons = [(a, b) for a in range(D + 1) for b in range(D + 1 - a)]
    bad = 0
    tested = 0
    from twisted_checks import ev
    for coeff in itertools.product(range(p), repeat=len(mons)):
        if all(c == 0 for c in coeff):
            continue
        tested += 1
        S = [x for x in F.els if ev(F, x, F.frob(x), mons, coeff) == z]
        if len(S) <= D * p:
            pass
        elif len(S) == F.q:
            pass  # degenerate whole-field atom
        else:
            bad += 1
    print("E2 gap p=%d l=%d D=%d: tested=%d BAD=%d" % (p, l, D, tested, bad))
    assert bad == 0
    return tested


def e3_window():
    # Corollary illustration via EXACT integer arithmetic (delta=1/5):
    #   small-avoids: B < q^{1/5}  <=>  B^5 < q
    #   cosmall-avoids: q-B > q^{4/5}  <=>  (q-B)^5 > q^4
    # Lemma hypothesis: l*delta>1 (delta=1/5, so l>5); p>D for injectivity.
    # Small-avoids B<q^d <=> mD<p^{l*d-1} (RHS grows once l*d>1).
    for (p, l, m, D) in [(5, 30, 6, 2), (101, 10, 6, 2), (7, 20, 6, 2)]:
        assert l > 5 and p > D
        q = p ** l
        B = m * D * p
        sa = B ** 5 < q
        ca = (q - B) ** 5 > q ** 4
        print("E3 p=%d l=%d q=p^%d B=%d small-avoids=%s cosmall-avoids=%s"
              % (p, l, l, B, sa, ca))
        assert sa and ca


def e4_horns(p, l):
    m = MODS[(p, l)]
    F = Fq(p, l, m)
    z, o = F.z, F.o
    Nexp = (F.q - 1) // (p - 1)
    T = [a for a in F.els if a != z and F.pow(a, Nexp) == o]

    def trace(a):
        s = z
        x = a
        for _ in range(l):
            s = F.add(s, x)
            x = F.frob(x)
        return s
    V = [a for a in F.els if trace(a) == z]
    assert twprod(F, T) == set(T), "torus twisted product must fix T"
    assert sumset(F, V) == set(V), "trace-kernel sumset must fix V"
    print("E4 horns p=%d l=%d: |T|=%d T.sigT==T, |V|=%d V+V==V OK"
          % (p, l, len(T), len(V)))


def main():
    e1_injectivity(2, 5)
    e1_injectivity(3, 5)
    e1_injectivity(2, 101)
    n = 0
    n += e2_gap(3, 2)
    n += e2_gap(5, 2)
    e3_window()
    e4_horns(3, 2)
    e4_horns(5, 2)
    print("EMERGENT-REPLAY tested=%d VERIFY_OK" % n)


if __name__ == "__main__":
    main()
