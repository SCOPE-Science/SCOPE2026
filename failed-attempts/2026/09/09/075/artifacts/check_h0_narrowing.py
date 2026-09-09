"""Lane-480: h0-linearity necessary condition for any killing target (stdlib only).

Lemma (Leibniz narrowing, E2-level, rigorous):
  d2(h8) = h0 h7^2 != 0 (Adams Hopf differential, j=7 case of d2(h_j)=h0 h_{j-1}^2).
  Hence on E3+, the class h0*{h7^2} = 0.
  If h7^2 survives to E_r (r>=3) and d_r(h7^2)=y, then by the Leibniz rule
  on E_r, h0*y = d_r(h0*{h7^2}) = d_r(0) = 0 on E_r.
  So ANY killing target y for h7^2 at r>=6 is necessarily h0-torsion on E_r.

This does not identify r or prove y nonzero; it is logged as a target-narrowing
consistency condition (audit-plan "shuffle/restriction-adjacent" narrowing).
It rules out any candidate target that is h0-periodic/free at E_r, pending Leg A.

Run: python3 output/artifacts/check_h0_narrowing.py -> prints H0_NARROWING_OK
"""
import sys

def main():
    # Bidegree check: h8 at (255,1); d2 target (s+2, t+1): stem 254, filt 3.
    # h0=(0,1), h7^2=(254,2); product h0*h7^2 = (254,3). Matches d2(h8) bidegree.
    h8 = (255, 1)  # (stem, filt)
    d2_target = (h8[0] - 1, h8[1] + 2)
    h0h72 = (254, 3)
    assert d2_target == h0h72, (d2_target, h0h72)
    # Leibniz consequence is formal; record the implication chain.
    chain = [
        "d2(h8)=h0 h7^2 (Adams, j=8)",
        "=> h0*{h7^2}=0 on E3 and hence on every E_r, r>=3",
        "=> if d_r(h7^2)=y with r>=3, h0*y = d_r(h0*{h7^2}) = 0 on E_r",
        "=> any r in [6,9] killing target at (253,2+r) is h0-torsion on E_r",
    ]
    for line in chain:
        print(line)
    print("H0_NARROWING_OK")

if __name__ == "__main__":
    sys.exit(main())
