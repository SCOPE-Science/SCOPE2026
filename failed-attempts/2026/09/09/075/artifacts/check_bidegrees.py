"""Lane-480 target bidegree check (reproducible, stdlib only).

Verifies the fixed Adams bidegrees for the h_7^2 killing-window target:
 - |h_j| = (stem 2^j - 1, filt 1); h_7^2 = (stem 254, filt 2).
 - d_r: (s,t) -> (s+r, t+r-1); stem drops by 1, filt rises by r.
 - Target window r=6..9 at stem 253, filts 8..11; floor leg r=5 at (253,7).
 - Window [6,9] lies strictly above published E5 floor (d_2=d_3=d_4=0, BX Cor 1.14).
 - Ext nonzero status at the five target bidegrees is UNKNOWN here (not assumed);
   nonzero proof for y is the missing datum flagged in WORKLOG Leg A.

Run: python3 output/artifacts/check_bidegrees.py  -> prints BIDEGREE_CHECK_OK
"""
import sys

def hj(j):
    return (2**j - 1, 1)  # (stem, filt)

def main():
    s7, f7 = hj(7)
    assert (s7, f7) == (127, 1), (s7, f7)
    src = (2 * s7, 2 * f7)
    assert src == (254, 2), src
    s_src, f_src = 2, 256  # (s,t) with t = stem + s
    assert s_src + 0 == 2 and (256 - 2) == 254
    targets = {}
    for r in (5, 6, 7, 8, 9):
        s, t = s_src + r, 256 + (r - 1)
        stem, filt = t - s, s
        targets[r] = (stem, filt, s, t)
    assert targets[5][:2] == (253, 7), targets[5]
    assert targets[6][:2] == (253, 8), targets[6]
    assert targets[7][:2] == (253, 9), targets[7]
    assert targets[8][:2] == (253, 10), targets[8]
    assert targets[9][:2] == (253, 11), targets[9]
    for r in (6, 7, 8, 9):
        assert r > 4, "window must lie strictly above E5 floor (r<=4 vanish by BX Cor 1.14)"
    for r, (stem, filt, s, t) in targets.items():
        print(f"d_{r}: (s,t)=({s},{t}) stem={stem} filt={filt} Ext_nonzero=UNKNOWN")
    print("BIDEGREE_CHECK_OK")

if __name__ == "__main__":
    sys.exit(main())
