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
# Verification

The standalone script `check_cycles.py` was executed using SymPy and returned:

`NILPOTENT_REPEATED_HEIGHT_MULTIPLICITY_AND_PHASE_OK degrees=1..11`

It symbolically checks the nilpotent Jacobian's characteristic polynomial for the quadratic representative, the exact polynomial conjugacy, the three-step Jacobian spectrum, the factorizations at \(\kappa^2=27/4\), \(8\) and \(125/12\), and exact rational midpoint sign witnesses in degrees \(1\) through \(11\). It is not an exhaustive search of arbitrary real polynomials or an independent review.

The full mathematical proof in `RESULT.md` separately establishes the statement for **every** degree \(d\ge1\) through an analytic root-degree bound, interval signs, root simplicity, and an asymptotic multiplier argument. The finite checks supplement rather than replace those arguments. Other period-three orbits with three distinct heights are outside scope. External independent audit: not performed.
