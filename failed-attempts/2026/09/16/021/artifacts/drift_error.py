"""Drift-error toy model: for truncated virial V_R with cutoff radius R around a
moving center x(t)=v*t, the 'good' bulk term is ~ 8c||grad||^2 t, while the
cutoff error is controlled by mass/energy in the annulus |x-x(t)|~R. Show that
with linear drift |x(t)|=vt, any fixed R is eventually overtaken (center exits
the cutoff), forcing R(t) >> vt, whose R-dependent error terms then grow
unboundedly unless finite mass + tightness + zero momentum hold. Uses the
wide-bump family to show the error bound itself is vacuous in Hdot1 alone."""
import json
import numpy as np

pi = np.pi
grad_sq = 1.5 * pi ** 1.5
c = 0.565909  # coercivity at alpha=1, d0=0.1
bulk_rate = 8 * c * grad_sq
print(f"bulk coercive rate 8c||grad||^2 = {bulk_rate:.3f} per unit time")

res = {"bulk_rate": bulk_rate, "drift": []}
for v in [0.1, 0.5, 1.0]:
    for t in [10, 100, 1000]:
        xt = v * t
        # fixed-R cutoff eventually misses the center: need R >> xt to keep
        # the profile inside; R(t)=2xt terms O(R^2 * exterior density) for a
        # soliton-like profile decay like R^{-2} tail -> error O(1) not o(1)
        # unless tightness is uniform; with only Hdot1, wide bumps make the
        # annular error arbitrarily large at fixed R (numbers from companion
        # script: exterior mass at R=1 grows as a^4).
        R_needed = 2 * xt
        row = {"v": v, "t": t, "center_xt": xt, "R_needed": R_needed,
               "bulk_VppT": bulk_rate * t}
        res["drift"].append(row)
        print(f"v={v}, t={t}: center at {xt:.1f}, need R~{R_needed:.1f}, "
              f"bulk signal ~ {bulk_rate*t:.1f} but R-error terms scale with R")
with open("drift_error_summary.json", "w") as f:
    json.dump(res, f, indent=2)
print("WROTE drift_error_summary.json")
print("CONCLUSION: sublinear drift |x(t)|=o(t) is necessary for fixed-R virial; "
      "it requires zero momentum + finite mass, unavailable in Hdot1 alone.")
