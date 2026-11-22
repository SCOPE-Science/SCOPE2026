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

# Reproducibility checks and limits

The proof is in `RESULT.md` and requires only Gaussian conditioning, elementary integration, sign inequalities, compactness and the implicit function theorem. To run supplementary checks in the extracted folder, use `python verify.py` with Python 3 and installed `sympy` and `mpmath`.

The program tests exact polynomial identities for endpoint derivative numerators, numerical agreement between analytic integrated information and independent quadrature (including repeated observation sites), nine sets of strict boundary derivative signs, and three high-noise asymptotic coefficient cases. A successful run reports `PASS: 42 symbolic identities / independent quadrature / boundary / asymptotic checks`.

The derivation establishes the theorem for the full continuum of positive decay and measurement-noise parameters. The finite numerical checks do not certify universal inequalities, originality, or independent review. Uniqueness is established for sufficiently large noise only, not uniformly for every positive noise variance. A plausible related old Kriging paper and an OU path-design dissertation were not available in full text, limiting publication-priority conclusions.
