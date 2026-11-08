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

# Reproducible checks and limits

Run `python verify.py` with Python, SymPy, NumPy and SciPy installed. The program evaluates exact trigonometric identities, the covering determinant, the quotient Jacobian at every one of the \(18\) lifts, the three potential levels and the deck-translation identity. It additionally integrates \(24\) finite-time sample trajectories as an illustrative numerical consistency check.

Expected output:

`VERIFY_OK covering_degree=3 critical_points=18 sink=3 saddle=9 source=6 energy_levels=3 numerical_orbits=24`

These finite experiments and symbolic checks do not constitute a proof that every real initial condition converges or that all invariant manifolds are transverse. Those statements follow from the analytic Lyapunov, equilibrium-classification and potential-order arguments in `RESULT.md`. This package has not received independent scientific validation.
