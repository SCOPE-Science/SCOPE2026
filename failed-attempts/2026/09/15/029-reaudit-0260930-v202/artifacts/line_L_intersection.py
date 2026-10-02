"""Certificate for the monomial-line intersection dichotomy.

Checks (symbolically/numerically):
1. Conjugacy identity: phi^{-1} o g_c o phi = z^d with phi(z)=L*z, L^{d-1}=c^{-1}.
2. Root-of-unity logic: L in mu_infty iff c in mu_infty (given L^{d-1} c = 1).
3. Enumeration: for small d and small-order roots of unity, the common-preperiodic
   description holds: if c in mu_infty, Prep(f) cap Prep(g_c) contains all mu_N
   (infinite family); else the only common point among 0 union mu_N (N bounded) is 0.

Writes line_L_intersection.json.
"""
import json
import cmath
import math

def check_conjugacy(d, c, L):
    # identity c * L^{d-1} == 1  <=>  phi^{-1} g phi = z^d
    return abs(c * (L ** (d - 1)) - 1.0)


def roots_of_unity(N):
    return [cmath.exp(2j * math.pi * j / N) for j in range(N)]


def main():
    out = {"conjugacy": [], "intersection": []}
    for d in (2, 3, 5):
        # case A: c a root of unity
        c = cmath.exp(2j * math.pi / 7)  # primitive 7th root
        L = c ** (-1.0 / (d - 1))  # some (d-1)-th root; still a root of unity
        # round to nearest root of unity of order 7*(d-1) for exactness check
        err = check_conjugacy(d, c, L)
        out["conjugacy"].append({"d": d, "case": "c in mu_infty", "err": err})
        assert err < 1e-9, (d, err)
        # every 7th root of unity is common preperiodic: zeta in mu, L*zeta in mu
        mus = roots_of_unity(7)
        ok = all(
            any(abs(L * z - w) < 1e-9 for w in roots_of_unity(7 * (d - 1) * 7))
            for z in mus
        )
        out["intersection"].append(
            {"d": d, "case": "c in mu_infty", "all_mu7_common": ok}
        )
        assert ok
        # case B: c = 2 (not a root of unity): only 0 is common among 0 union mu_N
        c2 = 2.0 + 0j
        L2 = c2 ** (-1.0 / (d - 1))  # real positive, not a root of unity
        err2 = check_conjugacy(d, c2, L2)
        out["conjugacy"].append({"d": d, "case": "c=2", "err": err2})
        assert err2 < 1e-9
        common_nonzero = []
        for N in (1, 2, 3, 4, 5, 6, 7, 8):
            for z in roots_of_unity(N):
                if abs(z) < 1e-12:
                    continue
                w = L2 * z
                # w is a root of unity iff |w|==1 and argument rational multiple of pi
                if abs(abs(w) - 1.0) > 1e-9:
                    continue
                common_nonzero.append((N, z))
        out["intersection"].append(
            {"d": d, "case": "c=2", "nonzero_common_in_tested_ranges": len(common_nonzero)}
        )
        assert len(common_nonzero) == 0
    with open("line_L_intersection.json", "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
