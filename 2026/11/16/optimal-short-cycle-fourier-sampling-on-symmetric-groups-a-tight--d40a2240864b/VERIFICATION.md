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
# Reproduction and verification

Run `python check.py` with Python 3 and NumPy as specified in `requirements.txt`. The finite checker enumerates all five permitted conjugacy classes in dimensions 4, 5, and 6, constructs the full standard-Fourier Gram matrices in the ambient coordinate model, matches every eigenvalue and multiplicity, and verifies the proposed optimal measures. It also checks the explicit rational candidate formula in dimensions 7 through 100. The recorded successful execution ended with `SHORT_PERMUTATION_FOURIER_OPTIMUM_CHECK_PASS`.

Universal correctness follows separately from the exact four-sector decomposition and the five nonnegative classwise rational dual inequalities in `RESULT.md`. Finite enumeration is not an exhaustive argument in unbounded dimension; historical priority is not independently certified. No independent audit has been performed.
