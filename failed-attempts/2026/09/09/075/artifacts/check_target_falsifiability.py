"""Lane-480: falsifiability condition for the killing-window target (stdlib only).

Rigorous logic (no Ext computation):
  Target T: exists r in [6,9] with d_r(h7^2) = y, y nonzero on E_r at (253,2+r).
  Claim: T => exists r in [6,9] with Ext_A^{2+r,255+r}(F2,F2) != 0.
  Proof: y nonzero on E_r is represented by an E2 class [y] at the same (s,t)
    (Adams pages are subquotients at fixed bidegree) that is nonzero, not hit by
    any d_k (k<r) from another bidegree, and supports no nonzero d_k (k<r) itself
    that would remove it... precisely: survival to E_r requires [y] != 0 in E2
    and [y] not a boundary on pages < r. Hence the E2 group is nonzero.
  Contrapositive (usable obstruction): if ALL FOUR groups
    Ext^{8,261}, Ext^{9,262}, Ext^{10,263}, Ext^{11,264} vanish,
    then T is FALSE (h7^2 cannot die in [6,9]; by HHR it must die at r>=10
    or the HHR killing uses a target outside this filtration range — either way
    the admitted window claim fails as stated).
  This makes T sharply testable: one citable E2 table at stem 253, filts 8-11
  decides between "window witness possible" and "window excluded".
  Note: a NONZERO E2 group does not imply T (y could die before E_r, or the
  differential could land elsewhere); nonzero is necessary, not sufficient.
  Full sufficiency = (WIT-E2) + (WIT-D: no entering differential kills y before
  E_r; convergent shuffle/comparison giving d_r(h7^2)=y).

Run: python3 output/artifacts/check_target_falsifiability.py -> FALSIFIABILITY_OK
"""
import sys

def main():
    groups = {6: (8, 261), 7: (9, 262), 8: (10, 263), 9: (11, 264)}
    for r, (s, t) in groups.items():
        assert t - s == 253 and s == 2 + r, (r, s, t)
        print(f"r={r}: T needs Ext^({s},{t}) [stem 253, filt {s}] nonzero (necessary)")
    print("Contrapositive: all four Ext vanish => T FALSE (death at r>=10 or outside range)")
    print("Nonzero E2 alone does NOT imply T (entering differentials + shuffle still needed)")
    print("FALSIFIABILITY_OK")

if __name__ == "__main__":
    sys.exit(main())
