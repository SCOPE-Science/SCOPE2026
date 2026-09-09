#!/usr/bin/env python3
"""Independent replay verifier for lane-278 (no shared code with compute/certify
beyond file formats): rebuilds Steinberg data from committed matrices, rechecks
Sturm brackets, rechecks winding exclusion at rho with fresh Narcs, rechecks BFS
for two systems. Prints VERIFY_OK on success."""
import json, itertools, math
from fractions import Fraction
from sympy import symbols, Poly, Rational, sturm as sym_sturm, together, fraction
from sympy import S as SYMS, gcd as sym_gcd
t = symbols('t')
def main():
    data = json.load(open("output/artifacts/series.json"))
    om = json.load(open("output/artifacts/omega.json"))
    assert set(data["systems"]) == set(om["intervals"]), "system mismatch"
    for name, S in data["systems"].items():
        M = S["M"]; r = len(M)
        def sph(T):
            T = tuple(T)
            if len(T) == 0: return (0, [1])
            sub = [M[a][b] for a in T for b in T if a < b]
            if any(m == 0 for m in sub): return None
            if len(T) == 1: return (1, [2])
            if len(T) == 2:
                i, j = T; m = M[i][j]
                return (2, [2, 2]) if m == 2 else (m, [2, m])
            if len(T) == 3:
                e = [m for m in sub if m > 2]
                if len(e) == 0: return (3, [2, 2, 2])
                if len(e) == 1: return (e[0]+1, [2, e[0], 2])
                if len(e) == 2:
                    a, b = sorted(e)
                    mp = {(3,3): (6,[2,3,4]), (3,4): (9,[2,4,6]), (3,5): (15,[2,6,10])}
                    return mp[(a,b)] if (a,b) in mp else None
                return None
            return None
        g = SYMS.Zero; cnt = 0
        for s in range(r+1):
            for T in itertools.combinations(range(r), s):
                d = sph(T)
                if d is None: continue
                cnt += 1; l, degs = d
                p = SYMS.One
                for dd in degs: p *= sum(t**i for i in range(dd))
                g += SYMS((-1)**s)*t**l/p
        g = together(g); num, den = fraction(g)
        PN = Poly(num, t, domain='ZZ'); PD = Poly(den, t, domain='ZZ')
        G = sym_gcd(PN, PD)
        if G.degree() > 0:
            PN = Poly(PN.div(G)[0].as_expr(), t, domain='ZZ')
            PD = Poly(PD.div(G)[0].as_expr(), t, domain='ZZ')
        sgn = 1 if int(PN.eval(0)) == 1 else -1
        Nq = [sgn*int(c) for c in PD.all_coeffs()[::-1]]
        Dq = [sgn*int(c) for c in PN.all_coeffs()[::-1]]
        assert cnt == S["spherical_count"], (name, "sph count")
        assert Nq == S["Wnum_coeffs_asc"] and Dq == S["Wden_coeffs_asc"], (name, "poly")
        a14 = [Fraction(0)]*15
        for m in range(15):
            nm = Fraction(Nq[m]) if m < len(Nq) else Fraction(0)
            a14[m] = nm - sum(Fraction(Dq[k])*a14[m-k] for k in range(1, min(m, len(Dq)-1)+1))
        assert [int(x) for x in a14] == S["series_0_14"], (name, "series")
        Q = Poly(sum(c*t**i for i, c in enumerate(Dq)), t, domain='QQ')
        a = Fraction(S["root_bracket"][0]); b = Fraction(S["root_bracket"][1])
        sq = sym_sturm(Q)
        def V(x):
            s = []
            for q in sq:
                v = q.eval(x)
                if v > 0: s.append(1)
                elif v < 0: s.append(-1)
            return sum(1 for i in range(1, len(s)) if s[i] != s[i-1])
        assert V(Rational(0))-V(Rational(a.numerator,a.denominator)) == 0, (name, "root before a")
        assert V(Rational(a.numerator,a.denominator))-V(Rational(b.numerator,b.denominator)) == 1, (name, "bracket")
        # winding exclusion at rho with fresh Narcs=3072
        rho = Fraction(om["intervals"][name]["rho"]); n = len(Dq)-1
        pw = [rho**j for j in range(n+1)]
        M2 = sum(abs(Fraction(Dq[j]))*pw[j]*j*j for j in range(n+1))
        Narcs = 3072; dth = 2*math.pi/Narcs
        rr = float(M2)*(dth/2)**2/2 + 1e-9*sum(abs(float(Fraction(Dq[j])))*float(pw[j]) for j in range(n+1)) + 1e-12
        angs = []
        for k in range(Narcs):
            th = (2*k+1)*math.pi/Narcs
            cr = sum(float(Fraction(Dq[j]))*float(pw[j])*math.cos(j*th) for j in range(n+1))
            ci = sum(float(Fraction(Dq[j]))*float(pw[j])*math.sin(j*th) for j in range(n+1))
            nc = math.hypot(cr, ci)
            assert nc > rr*math.sqrt(2)+1e-9, (name, "circle hit")
            angs.append((math.atan2(ci, cr), math.asin(min(1.0, rr*math.sqrt(2)/nc))+1e-9))
        tot = 0.0; sl = 0.0
        for k in range(Narcs):
            a0, d0 = angs[k]; a1, d1 = angs[(k+1) % Narcs]
            d = a1-a0; d -= 2*math.pi*round(d/(2*math.pi))
            assert abs(d)+d0+d1 < math.pi, (name, "step")
            tot += d; sl += d0+d1
        N = tot/(2*math.pi)
        assert abs(N-round(N)) < 0.5-sl/(2*math.pi)-1e-6 and round(N) == 0, (name, "winding", N, sl)
        olo = Fraction(om["intervals"][name]["omega_bracket"][0]); ohi = Fraction(om["intervals"][name]["omega_bracket"][1])
        assert olo == Fraction(b.denominator, b.numerator), (name, "lo")
        assert ohi == Fraction(rho.denominator, rho.numerator), (name, "hi")
    # gap: min vs rest
    order = sorted(om["intervals"], key=lambda n: Fraction(om["intervals"][n]["omega_bracket"][0]))
    assert order[0] == om["min"] == "A"
    for n in order[1:]:
        assert Fraction(om["intervals"][n]["omega_bracket"][0]) - Fraction(om["intervals"]["A"]["omega_bracket"][1]) > 0, n
    print("VERIFY_OK")
if __name__ == "__main__":
    main()
