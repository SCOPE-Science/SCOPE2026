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

# Verification of the physical-time theorem

The accompanying `CHECK.py` was executed using Python with SymPy and SciPy, and printed `VERTICAL_HOPF_FULL_PHASE_CLOCK_AND_PULSE_OK`. It symbolically checks conservation of the stated quadratic first integral with \(\omega^2=A(D-A)\), substitutes the rational pulse directly into both polynomial ODEs, and numerically reproduces physical periods and concentration means at several noncritical energies for the three-reaction example. It also checks the total critical-pulse exposure by independent improper quadrature.

The analytic proof, not a finite computation, establishes the full positive parameter range, the normalization of angular time, the strict positivity of all inner and critical levels, and the all-energy completeness and asymptotic classifications. The checker does not verify the uncountably many initial conditions by enumeration. No independent audit has been performed; in particular, no external certification or formally checked proof is claimed.
