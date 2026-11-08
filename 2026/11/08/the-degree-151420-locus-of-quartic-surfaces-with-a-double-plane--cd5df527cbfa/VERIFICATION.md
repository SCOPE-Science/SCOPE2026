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
# Reproducibility and limits

Run `python3 verify_degree.py` with Python 3.9 or later, then compare with `verification_output.txt`. The two independent methods are (i) a formal Segre expansion and projective-bundle pushforward and (ii) torus localization using 24 fixed conics with rational exact arithmetic. The output must report 151420 for both and `ALL_CHECKS_PASSED`.

The code verifies the finite arithmetic component and rank-14 monomial bases at all torus fixed points. The proof in RESULT.md separately justifies the integral formula, generic one-to-one incidence projection, and the translation into generic-point enumerative counting. The verification is not an independent mathematical audit.
