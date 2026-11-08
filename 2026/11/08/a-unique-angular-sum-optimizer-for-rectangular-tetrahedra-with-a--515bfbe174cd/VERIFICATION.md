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

# Verification details

Run `python3 verify.py` using Python 3.9 or later; no packages or downloads are required. Successful output is `ANGLE_SUM_OK 5300`. The program uses a fixed random seed, 4,000 independently computed tetrahedral angle sums, root checks at twelve anisotropies, deterministic one-variable comparisons, and four large-ratio asymptotic checks. Its independent solid-angle formula uses the absolute triple product and the four-term dot-product denominator for a trihedral spherical angle; the identity under test instead uses the sum of inverse-facet-normal arcsines.

All core mathematical statements are proved in `RESULT.md` via spherical excess, elementary derivative-sign analysis and controlled asymptotics. The finite checks are not an exhaustive proof of a continuum statement and do not constitute independent peer review. The minimizer is guaranteed unique by analytic monotonicity, not by numerical minimization.

No independent mathematical audit has been performed.
