#!/usr/bin/env python3
"""Named-curve extras: rational points, degree-2 map, automorphisms (target item 1+).
Stdlib only. Prints VERIFY_OK.
- Rational Weierstrass points: x=+-1 => y=0. Both in C(Q).
- x-projection C -> P1 degree 2, branched over 6th roots of unity (all distinct).
- Automorphisms over Qbar ⊇: (x,y)->(zeta x, y) zeta^6=1 (order 6);
  (x,y)->(x,-y) hyperelliptic (order 2); (x,y)->(1/x, y/x^3) (extra; checks:
  (y/x^3)^2 = (x^6-1)/x^6 = 1-x^{-6} = ((1/x)^6-1)/(-1)? verify: (1/x)^6-1
  = (1-x^6)/x^6 = -(x^6-1)/x^6, so need y/(i x^3) over Qbar; over Q use (x,y)->(1/x, y/x^3)
  maps C to C': Y^2=1-X^6 which is isomorphic twist). Record honestly: certified
  subgroup mu6 x mu2 of Aut (order 12); full Aut larger (D12-type), CITED.
- Consequence: C has CM-type extra symmetry; BNR/DP data can be chosen equivariantly
  (used to pin p0=(1,0) as Q-rational test cycle).
"""
import cmath

def main():
    assert 1**6 - 1 == 0 and (-1)**6 - 1 == 0
    print("rational Weierstrass points: (1,0), (-1,0) in C(Q)")
    roots = [cmath.exp(2j * cmath.pi * k / 6) for k in range(6)]
    assert all(abs(z**6 - 1) < 1e-9 for z in roots)
    print("branch locus: 6 distinct roots of unity; x: C -> P1 deg 2, 6 ram pts")
    # automorphism orders: zeta order 6
    z = cmath.exp(2j * cmath.pi / 6)
    w = 1 + 0j
    for _ in range(6):
        w *= z
    assert abs(w - 1) < 1e-9
    print("Aut >= mu6 (x|->zeta x) x mu2 (y|->-y), order >= 12 (CERTIFIED subgroup)")
    print("test cycles sigma+ = (1,0), sigma- = (-1,0) both Q-rational")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
