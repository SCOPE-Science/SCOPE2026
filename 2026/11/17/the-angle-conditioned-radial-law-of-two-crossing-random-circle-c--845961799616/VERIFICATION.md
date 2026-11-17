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

# Verification record

The analytic proof is in `RESULT.md`. The standalone Python 3 standard-library script `verify.py` was executed from its actual package source, reporting `PASS 3057 tests; global mean 0.6079271017640973 target 0.6079271018540267`. Its tests compare Cartesian line intersections against the factorization, independent quadrature against conditional product moments, independent randomized conditional samples against the exact CDF, local tail coefficients, and the known marginal-moment consistency check. Tests are finite numerical checks; they do not independently certify the global theorem or historical novelty.

For reproducibility, extract all embedded files into one directory and run `python verify.py`. There are no external package requirements and no unavailable supporting files.
