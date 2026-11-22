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

The complete theorem and its uniformity hypotheses are proved analytically in `RESULT.md`. The standalone standard-library verifier `verify.py` was run on the recorded package content and passed all declared tests. Specifically it checked 42 finite-difference instances covering integer sizes 3–16 at three exponent steps, 7168 sampled location comparisons, the previously known three-site coefficient identity, and five two-site endpoint examples. These are numerical spot checks and do not establish maximization over a continuum; the written antipodal localization, sharp two-sided test, and entropy concavity establish the mathematical claim. No external or independent audit is asserted.
