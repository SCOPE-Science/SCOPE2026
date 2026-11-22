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

The proof derives the stationary Poisson-cluster generating functional, factorial differentiation, the exact Bessel-K common-age kernel, a uniform nondegenerate saddle expansion, Cauchy–Schwarz equality and a second-order transverse Taylor expansion. The checker independently evaluates 3 age-integrals, 4 triplet identities, 6 far-field slopes, 6 shell-profile instances and 3 scale-regime cases. Tests are finite and do not replace the exact arguments.

Run `python checker.py` with NumPy and SciPy available. The checker has no external data, random seeds, network accesses or hidden inputs.

The order parameter must be an integer at least three with finite positive burst factorial moment. The normalized correlation is defined from factorial cumulants, not from ordinary pointwise concentration cumulants. Prior two-point results and the general Poisson cluster functional are credited, and publication priority beyond the inspected corpus has not been independently established.
