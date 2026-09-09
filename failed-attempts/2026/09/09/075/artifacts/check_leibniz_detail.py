"""Lane-480: Leibniz h0-torsion detail with explicit (stem,filt) arithmetic (stdlib only).

Conventions (classical 2-primary Adams for sphere):
 - Bidegree recorded as (stem=t-s, filt=s). Product adds bidegrees.
 - h0 at (stem 0, filt 1) [detects 2]; h7^2 at (254,2); h8 at (255,1).
 - Adams Hopf differential (j=8 case): d2(h8) = h0*h7^2 != 0 at (254,3).
   Check: d2 sends (stem n, filt s) -> (n-1, s+2): (255,1)->(254,3). Product
   h0*h7^2 sits at (0+254, 1+2) = (254,3). Degrees match.
 - Hence h0*{h7^2} = 0 on E3 and on every later page E_r (r>=3): it is a d2-boundary.
 - h0 is a permanent cycle (detects 2), so d_r(h0)=0 for all r>=2.
 - Leibniz on E_r (r>=3): if h7^2 survives to E_r and d_r(h7^2)=y at (253,2+r),
   then h0*y = d_r(h0)*{h7^2} +- h0*d_r(h7^2)... precisely:
     d_r(h0 * {h7^2}) = d_r(h0)*{h7^2} + h0*d_r({h7^2}) = 0*y + h0*y = h0*y,
   but the left side is d_r(0)=0 since h0*{h7^2}=0 on E_r. Hence h0*y=0 on E_r.
 - Bidegree of h0*y: (253+0, 2+r+1) = (253, 3+r), consistent with d_r out of (254,3+r-?):
   not needed; only torsion conclusion is claimed.

This is narrowing (N1); it does not select r or prove y nonzero.

Run: python3 output/artifacts/check_leibniz_detail.py -> LEIBNIZ_DETAIL_OK
"""
import sys

def d2_target(stem, filt):
    return (stem - 1, filt + 2)

def main():
    h0 = (0, 1)
    h72 = (254, 2)
    h8 = (255, 1)
    assert d2_target(*h8) == (254, 3), d2_target(*h8)
    prod = (h0[0] + h72[0], h0[1] + h72[1])
    assert prod == (254, 3), prod
    for r in (3, 4, 5, 6, 7, 8, 9):
        y = (253, 2 + r)
        h0y = (y[0] + h0[0], y[1] + h0[1])
        assert h0y == (253, 3 + r), (r, h0y)
        print(f"r={r}: y at {y} -> h0*y at {h0y} = 0 on E_{r} (if d_{r}(h7^2)=y)")
    print("LEIBNIZ_DETAIL_OK")

if __name__ == "__main__":
    sys.exit(main())
