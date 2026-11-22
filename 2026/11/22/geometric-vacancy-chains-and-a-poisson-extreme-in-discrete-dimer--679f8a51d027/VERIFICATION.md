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

# Reproducibility

Run `python3 verify.py` in the directory containing the extracted files, with Python 3 and no third-party packages. The script performs exhaustive exact rational enumeration of every dimer edge-priority permutation for sizes 2 through 9, tests the finite chain and canonical-start formulas and endpoint recursion, and prints the number of successful assertions.

The checks do not establish the infinite-volume or maximum-length limits. These are proved by the analytical stabilization, dependency and independent-block arguments in `RESULT.md`. Historical priority has not been independently established, and a full copy of Page (1959) was not inspected.
