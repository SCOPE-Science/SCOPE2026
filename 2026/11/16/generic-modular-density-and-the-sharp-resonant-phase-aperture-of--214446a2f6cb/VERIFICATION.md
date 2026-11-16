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

# Verification record

A standalone standard-library script `CHECK.py` was executed on the packaged scientific formulas, yielding:

`CHECK_OK q_samples=6 stationary_grid=1542 tangency_samples=4 asymptotic_sweeps=18`

It tests the positive-root stationarity identity on 1,542 parameter-grid points, sampled monotonicity and endpoints, trial-point lower-bound comparisons, the predicted square-root asymptotics, and exact rational coalescent identities at the model double zero. The script can be rerun with `python3 CHECK.py` from the directory containing it.

The main claims have *analytic* rather than finite computational proofs. Their essential steps are the triangular phase equation, Kronecker--Weyl equidistribution on two- and three-tori, Rouché's theorem on disjoint translated zero disks, unique positive stationary root of a quadratic, and the envelope derivative at the resonance boundary. No computational experiment establishes an assertion about all irrational ratios or infinitely many zeros by itself.

The originality assessment compares the actual assertion about genuine zero heights modulo a length with published work on real projections and geometric phase feasibility; an independent publication-priority audit has not been performed.
