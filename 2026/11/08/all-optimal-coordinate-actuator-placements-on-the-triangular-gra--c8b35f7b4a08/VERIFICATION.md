---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify.py` using the standard library. The checker enumerates each labelled minimum-cardinality set for \(n=3,4,5,6,7\), derives independent finite-field ranks for the two nonconstant eigenspaces and compares them to the stated graph classification. It also checks \(A=B^\top B-2I\), \(BB^\top=(n-2)I+J\) at test orders and enumerates the initial coefficients of the rooted-tree formal power series with exact rational arithmetic. The computed ranks are modulo a fixed prime, not exact real-number ranks; the analytic proof in RESULT.md establishes real-rank equivalence for every size. A correct finite check does not establish originality or an infinite theorem.

The labelled count \(a_8=937440\) is from formal coefficient extraction, not an exhaustive search of order-eight actuator subsets. The full-text research comparison includes Yuan et al. (2013) and Dai (2022); the restricted Farrugia–Sciriha item is explicitly a residual risk rather than a claimed full-text negative inspection.
