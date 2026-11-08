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

# Verification of the power-cutoff hub theorem

Run `python3 verify.py` using a Python 3 interpreter without external packages. The script enumerates the finite parent-choice sample space for each \(n=2,\ldots,8\) and cutoff \(\gamma\in\{0.2,0.5,0.8\}\), checks the child-count means and all relevant negative-quadrant inequalities by exact rational arithmetic, then verifies the calculated phase root and the uniqueness-consistent variational upper grid for nine cutoff parameters. The observed run reported `CHECKS_PASSED 19519` with no failed assertion, and \(\gamma_*=0.278652479555518\ldots\).

These calculations test finite identities and the optimization formulas. They are not an exhaustive finite tree census beyond size eight, do not prove any asymptotic claim and are not independent validation. The proof's infinite steps rely instead on the written uniform harmonic approximation, Chernoff bounds, elementary symmetric-polynomial lower bound, negative-dependence argument, and dyadic Borel--Cantelli interpolation. Statistical or simulation evidence is not substituted for those steps.
