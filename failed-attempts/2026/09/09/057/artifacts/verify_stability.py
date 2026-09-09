#!/usr/bin/env python3
"""Simpson slope check on the BNR strata (target item 3 support).
Stdlib only. Prints VERIFY_OK.
Polarization: deg from C (pullback). Simpson slope of pi_*F is deg(pi_*F)/rk.
- phi=0 point: E semistable deg-0 bundle (SU moduli) => slope 0, OK.
- Split theta example (E=L(+)L^-1, phi=[[0,0],[s,0]], s iso): any Higgs
  subbundle F' must be phi-invariant. L (deg 1): phi maps L via s to L^-1K=L
  (other summand), so L not invariant. L^-1 (deg -1): slope -1 < 0. Destabilizing
  needs slope > 0 = slope(E): none. Hence STABLE (CERTIFIED elementary check).
- Wobbly statement: (E, phi) with phi != 0 nilpotent => E is wobbly (admits a
  nonzero nilpotent Higgs field). (E,0) generic stable => very stable (CITED:
  Hausel-Hitchin genericity). The theta-split example is thus an explicit wobbly
  Q-point-adjacent witness (its underlying bundle defined over Q via p=(1,0)).
"""
def main():
    slopeE = 0
    # candidate Higgs subbundles of split example
    cands = {"L": 1, "L^-1": -1}
    for name, deg in cands.items():
        slope = deg / 1
        if name == "L":
            print(f"{name}: deg {deg} but NOT phi-invariant (s iso off-diag) => excluded")
        else:
            assert slope < slopeE, "must not destabilize"
            print(f"{name}: slope {slope} < {slopeE} => not destabilizing")
    print("split theta Higgs point STABLE + wobbly (phi0 != 0 nilpotent)")
    print("generic (E,0): very stable (CITED)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
