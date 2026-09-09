"""Replay verifier for lane-299 certificate (stdlib + mpmath only).

Recomputes from output/artifacts/chars_integer_data.json:
 (1) completeness: sum_{d|q} Nprim(d) + 1 == phi(q) for all q<=32;
 (2) orthogonality of the enumerated primitive characters (float check);
 (3) rigorous L(1,chi) enclosures in mpmath iv arithmetic:
     odd  chi: L = (pi/2q) sum chi(a) cot(pi a/q);
     even chi: L = -S/tau(bar chi), S = sum bar chi(a) Log(1-e^{-2 pi i a/q});
     chi values as iv.cos/iv.sin of exact rational multiples of pi;
 (4) checks: every Re/Im width <= 1e-6, every |L|^2-box lower bound > 0,
     minimum-modulus pair (q=19, k=5/k=13 conjugates) upper endpoint strictly
     below every other box lower endpoint;
 (5) rigorous L(1/2,chi) nonzero witness for EVEN chi only: iv partial sums
     over NBLOCKS whole periods + corrected block-mean-zero tail majorant
     U = Emax/sqrt(N+1), N = NBLOCKS*q, Emax <= phi(q)/2 (valid for every
     nonprincipal chi with block mean M = sum_{a=1..q} chi(a) = 0; the old
     q*(1/sqrt(N+1)-1/sqrt(N+q)) majorant with the '|C|<=q telescoping'
     justification was WRONG -- it fails already for the odd character mod 3
     at B=300, where the true tail ~1.09e-02 exceeds the old T ~1.11e-04 --
     so the proof is restricted to even chi with the explicit M=0 lemma and
     uses U throughout; odd central values are NOT claimed).

Options: --half-nblocks K (default 1500; smaller e.g. 300 is faster but the
smallest witness q=5 needs K>=~200 to keep |S|-tail>0 at 50 dps).
Prints VERIFY_OK on full pass.
"""
import json, math, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(BASE, "chars_integer_data.json")))

def main():
    from mpmath import mp, iv
    mp.dps = 50
    iv.dps = 50
    nb = 1500
    for a in sys.argv[1:]:
        if a.startswith("--half-nblocks"):
            nb = int(a.split("=")[1])

    # (1) completeness
    def phi(n):
        return sum(1 for a in range(n) if math.gcd(a, n) == 1)
    for q in sorted(D, key=int):
        qi = int(q)
        divs = [d for d in range(1, qi + 1) if qi % d == 0]
        s = sum(len(D[str(d)]["prim"]) for d in divs if d > 1) + 1
        assert s == phi(qi), ("completeness", qi, s, phi(qi))

    # (2) orthogonality (float)
    import cmath, itertools
    for q in sorted(D, key=int):
        qi = int(q)
        U = [a for a in range(qi) if math.gcd(a, qi) == 1]
        os_ = [o for _, o in D[q]["gens"]]
        em = D[q]["emap"]
        def val(ks, a):
            ang = sum(k * e / o for k, e, o in zip(ks, em[str(a)], os_))
            return cmath.exp(2j * math.pi * ang)
        P = D[q]["prim"]
        for i in range(len(P)):
            for j in range(len(P)):
                s = sum(val(P[i]["k"], a) * val(P[j]["k"], a).conjugate() for a in U)
                want = len(U) if i == j else 0
                assert abs(s - want) < 1e-6, ("orth", qi, i, j, s)

    # (3) rigorous L(1)
    import re
    def ivchi(ks, ex, os_):
        tot = iv.mpf(0)
        for k, e, o in zip(ks, ex, os_):
            tot += iv.mpf((k * e) % o) / iv.mpf(o)
        th = 2 * tot * iv.pi
        return iv.cos(th) + iv.sin(th) * iv.j
    boxes = []
    for q in sorted(D, key=int):
        qi = int(q)
        os_ = [o for _, o in D[q]["gens"]]
        em = D[q]["emap"]
        for i, ch in enumerate(D[q]["prim"]):
            ks, par = ch["k"], ch["parity"]
            if par == -1:
                tot = iv.mpf(0) + iv.mpf(0) * iv.j
                for a in range(1, qi):
                    if math.gcd(a, qi) != 1:
                        continue
                    t = iv.mpf(a) / iv.mpf(qi) * iv.pi
                    tot += ivchi(ks, em[str(a)], os_) * iv.cos(t) / iv.sin(t)
                L = tot * iv.pi / (2 * iv.mpf(qi))
            else:
                S = iv.mpf(0) + iv.mpf(0) * iv.j
                tau = iv.mpf(0) + iv.mpf(0) * iv.j
                for a in range(qi):
                    if math.gcd(a, qi) != 1:
                        continue
                    z = ivchi(ks, em[str(a % qi)], os_)
                    zb = z.real - z.imag * iv.j
                    th = 2 * iv.mpf(a) / iv.mpf(qi) * iv.pi
                    e1 = iv.cos(th) + iv.sin(th) * iv.j
                    em_ = iv.cos(th) - iv.sin(th) * iv.j
                    S += zb * iv.log(1 - em_)
                    tau += zb * e1
                L = -S / tau
            wr = float(L.real.b) - float(L.real.a)
            wi = float(L.imag.b) - float(L.imag.a)
            assert wr <= 1e-6 and wi <= 1e-6, ("width", qi, i, wr, wi)
            ra, rb, ia, ib = (float(L.real.a), float(L.real.b),
                              float(L.imag.a), float(L.imag.b))
            corners = [(ra, ia), (ra, ib), (rb, ia), (rb, ib)]
            assert not (ra <= 0 <= rb and ia <= 0 <= ib), ("zero?", qi, i)
            cand = list(corners)
            if ra <= 0 <= rb:
                cand += [(0, ia), (0, ib)]
            if ia <= 0 <= ib:
                cand += [(ra, 0), (rb, 0)]
            n2lo = min(x * x + y * y for x, y in cand)
            n2hi = max(x * x + y * y for x, y in corners)
            assert n2lo > 0, ("nonvanish", qi, i)
            boxes.append((n2lo, n2hi, qi, i, par))
    boxes.sort()
    (lo0, hi0, q0, i0, p0), (lo1, hi1, q1, i1, p1) = boxes[0], boxes[1]
    (lo2, hi2, q2, i2, p2) = boxes[2]
    # minimum pair = q19 conjugates; allow the two minima to coincide (conjugate pair),
    # require strict separation from the third box on.
    assert (q0, q1) == (19, 19) and {i0, i1} == {4, 12}, ("min-id", boxes[:3])
    assert hi0 < lo2 and hi1 < lo2, ("disjoint", hi0, hi1, lo2)
    assert p0 == p1 == -1
    print("L(1): %d boxes, widths<=1e-6, min q=19 pair |L|^2<=%.12f < next %.12f" % (
        len(boxes), hi0, lo2))

    # (4) central values, EVEN chi only, with corrected tail.
    # Lemma (block mean zero, even nonprincipal chi): with N' = nb*q a multiple
    # of the period, write the tail as blocks r = 0,1,....  For block r put
    # C_b = sum_{a=1..b} chi(N'+rq+a) (C_0 = 0, C_q = M = 0).  Summation by parts
    # on the block gives T_r = C_q f(N'+(r+1)q) + sum_{b=1}^{q-1} C_b (f_b - f_{b+1})
    # with f_b = 1/sqrt(N'+rq+b), so with M = 0,
    #   |T_r| <= max_{1<=b<=q-1} |C_b| * (f_1 - f_q) <= Emax*(f_1 - f_q),
    # Emax = max_b |C_b| <= phi(q)/2 (crudest valid: at most phi(q)/2 nonzero
    # summands of modulus 1; the verifier uses phi(q)//2).  Summing over blocks
    # telescopes: sum_r (f(N'+rq+1) - f(N'+rq+q)) <= f(N'+1) (all terms positive,
    # dropped block gaps only shrink the sum... bounded above by the integral:
    # each difference <= integral of -f' over the block span, disjoint spans, so
    # total <= f(N'+1)).  Hence the VALID majorant |R| <= Emax/sqrt(N'+1),
    # evaluated in iv arithmetic (upper endpoint).  M = 0 is checked per
    # character below (complex float, tol 1e-9; enumeration data already gave
    # max|M| = 9.8e-14 over all 99 even chi).
    nfail = 0
    for q in sorted(D, key=int):
        qi = int(q)
        os_ = [o for _, o in D[q]["gens"]]
        em = D[q]["emap"]
        for i, ch in enumerate(D[q]["prim"]):
            if ch["parity"] != 1:
                continue
            ks = ch["k"]
            # M = 0 lemma check (even nonprincipal chi): block sum over one period.
            Mose = sum(val(ks, a) for a in range(1, qi + 1)) \
                if False else None
            import cmath as _cm
            _os = os_
            _em = em
            def _val(aa):
                if math.gcd(aa, qi) != 1:
                    return 0j
                ang = sum(k * e / o for k, e, o in zip(ks, _em[str(aa % qi)], _os))
                return _cm.exp(2j * _cm.pi * ang)
            _M = sum(_val(aa) for aa in range(1, qi + 1))
            assert abs(_M) < 1e-9, ("block-mean", qi, i, _M)
            # NOTE: the M=0 lemma (hence this whole central section) holds only
            # for nonprincipal chi; every chi here is primitive of conductor >= 3
            # (hence nonprincipal), and odd chi are skipped: odd central values
            # are NOT claimed (the old majorant is false in general: odd chi mod 3
            # at B=300 has true tail ~1.09e-02 > old T ~1.11e-04).
            S = iv.mpf(0) + iv.mpf(0) * iv.j
            for B in range(nb):
                N = B * qi
                for a in range(1, qi + 1):
                    if math.gcd(N + a, qi) != 1:
                        continue
                    tot = iv.mpf(0)
                    for k, e, o in zip(ks, em[str((N + a) % qi)], os_):
                        tot += iv.mpf((k * e) % o) / iv.mpf(o)
                    th = 2 * tot * iv.pi
                    S += (iv.cos(th) + iv.sin(th) * iv.j) / iv.sqrt(iv.mpf(N + a))
            N = nb * qi
            _phi = sum(1 for aa in range(qi) if math.gcd(aa, qi) == 1)
            _Emax = _phi // 2
            t = float((iv.mpf(_Emax) / iv.sqrt(iv.mpf(N + 1))).b)
            ra, rb, ia, ib = (float(S.real.a), float(S.real.b),
                              float(S.imag.a), float(S.imag.b))
            corners = [(ra, ia), (ra, ib), (rb, ia), (rb, ib)]
            if ra <= 0 <= rb and ia <= 0 <= ib:
                lo = 0.0
            else:
                cand = list(corners)
                if ra <= 0 <= rb:
                    cand += [(0, ia), (0, ib)]
                if ia <= 0 <= ib:
                    cand += [(ra, 0), (rb, 0)]
                lo = min(x * x + y * y for x, y in cand) ** 0.5
            assert lo - t > 0, ("central", qi, i, lo, t)
    print("L(1/2) even: all nonzero (|S|-U>0, U=Emax/sqrt(N+1)), nblocks=%d" % nb)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
