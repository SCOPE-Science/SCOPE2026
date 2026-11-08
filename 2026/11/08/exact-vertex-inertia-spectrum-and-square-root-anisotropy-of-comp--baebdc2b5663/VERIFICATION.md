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

The accompanying `verify.py` requires Python 3 with only standard-library dependencies (`fractions`, `itertools`, `math`). Run `python verify.py` from the directory containing the file. The successful local execution reported:

`COMPLETE_MATCHING_COVARIANCE_CHECKS_PASSED exact_vertices= 3728 basis_checks= 285 parameter_cases= 147`

It enumerates every matching for each complete graph of order 4 through 9 (3,728 in total), checks the telephone recurrence, evaluates every coordinate pair's covariance by exact rational arithmetic, and checks exact eigenvector identities on representative star and four-cycle modes. It also checks strict inequalities for all integer sizes 4 through 150 using exact rational recurrence computations. The asymptotic tests are finite plausibility checks, while the paper's ratio-bound argument establishes its infinite conclusion.

The manuscript states complete domain restrictions, counts, recurrences, eigenbasis construction, strictness proof, and asymptotic error estimates. It uses the standard edge-coordinate Euclidean norm and samples vertices uniformly, not interior points. It does not claim any independent validation or formal proof certification.
