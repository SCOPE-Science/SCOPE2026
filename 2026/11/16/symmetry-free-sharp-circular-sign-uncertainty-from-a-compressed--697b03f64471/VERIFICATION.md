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

# Verification

The analytical proof reduces the sharp last-sign radius to a Hermitian generalized eigenvalue problem, with no symmetry hypothesis. Its critical nonstandard step, the arc nonnegativity factorization, is derived from the real Markov–Lukács formula and verified by the Cayley transform identities in `RESULT.md`. The treatment of the finite-support boundary is exact and separate.

Execute `python3 CHECK.py` in this directory. It uses only Python's standard library. One run checked six distinct asymmetric atomic weights, twelve Hermitian eigen-equation residuals, six exact integral identities (within roundoff), thirty-six sign tests, six strict comparison tests, and twelve Haar degree benchmarks; it returned `CHECK_OK`. Floating-point checks are supporting diagnostics only, not a proof of interval SOS or the universal sharpness theorem.

Limitations: no finite numerical run can prove the all-degree or all-measure claims. Independent mathematical audit: not performed.
