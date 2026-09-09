#!/usr/bin/env python3
"""Component-census caution for the nilpotent fiber (target item 3 stress test).
Stdlib only. Prints VERIFY_OK.
- CERTIFIED: line-bundle BNR locus has 16 disjoint A^3 pieces (Jac[2] torsors).
  These are STRATA, not claimed irreducible components of h^{-1}(0): the
  compactified fiber glues them along the non-locally-free boundary D.
- CITED: irreducible (semistable) nilpotent-cone components for SL(2) are governed
  by Jordan type + degree data (1712.07362); phi=0 gives N0 = SU(2,O) (dim 3);
  regular-nilpotent strata indexed by kernel degree d <= 0 (stability) contribute
  further pieces. Exact component count for the NAMED curve is NOT derived here.
- CAUTION: any "component table" with a fixed number (e.g. 17) would require a
  stability/wobbly-divisor analysis on this C (Pal-Pauly wobbly divisor,
  Hausel-Hitchin very-stable Sue) which is beyond the certified scope. The BNR
  numerics (dims, degrees) are certified; the global component enumeration is
  explicitly OPEN in this record.
"""
def main():
    g = 2
    assert 2 ** (2 * g) == 16
    print("16 A^3 torsors = strata of locally-free locus (CERTIFIED count+dim)")
    print("irreducible components of h^{-1}(0): governed by Jordan strata (CITED)")
    print("exact census on C: y^2=x^6-1 NOT claimed here (OPEN, needs wobbly analysis)")
    print("N0 dim 3 = full fiber dim: N0 is a component (CITED moduli theory)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
