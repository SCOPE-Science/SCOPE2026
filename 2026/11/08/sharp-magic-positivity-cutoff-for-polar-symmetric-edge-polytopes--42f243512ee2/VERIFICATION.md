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

# Verification and limits

The accompanying `verify.py` is self-contained Python 3 code using exact integers and `fractions.Fraction`. Running `python3 verify.py` yields `EXACT_CHECKS_OK 410`, followed by coefficient vectors for right-part sizes 1 through 12. The verifier uses Newton interpolation of the exact lattice-point counting function, rather than hard-coded symbolic polynomials; it separately computes direct bounded graph potentials at small dilations and Bernoulli coefficients from their recurrence. This cross-checks the proof's critical rational values and coefficient formulas. The analytic Euler-zeta inequalities and their residue-class applications are detailed in RESULT.md and establish the unbounded parameter range. The 410 finite checks alone cannot establish that range. No Lean, external proof certificate, or independent human or software audit was performed; historical-priority comparisons remain provisional.
