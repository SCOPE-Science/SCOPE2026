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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 (standard library only). The checker tests 900 finite instances of stochastic-row diameter contraction, both negative multipliers of an explicit nonuniform sink, four strongly-mixed multistable-network trajectories, and a long-time approximation to the closed-boundary inverse-time coefficient on the exactly invariant antisymmetric line.

Expected run signature: `VERIFY_OK dob_coefficient_samples=900 stable_heterogeneous_pairs=1 strong_mixing_convergence=4 critical_inverse_time=1 critical_tD2=1.499221639` (floating point differences can alter the trailing digits).

The analytic proof, not the finite program, establishes global convergence and exact quantified thresholds. The critical invariant line must be integrated in its scalar coordinates: in the full two-dimensional flow at \(\beta=8\), its homogeneous transverse direction is unstable, so floating-point roundoff can expel trajectories from that line. This does not affect its exact invariance or the analytic asymptotic law.

Independent audit has not been performed; the reported scientific review is a self-review.
