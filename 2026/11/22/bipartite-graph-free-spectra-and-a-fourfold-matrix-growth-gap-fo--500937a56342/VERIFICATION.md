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

Execute `python verify_free_spectrum.py` from a directory containing the provided file. A successful run prints exact scalar and matrix free-algebra cardinalities through rank eight, separately tests labelled bipartite-graph numbers by direct edge-set enumeration through five vertices, evaluates all regular scalar normal forms for ranks one through four on all six-element assignments, asserts the exact collapse/injectivity criterion, and terminates with `VERIFY_OK`.

**Scope:** This is exhaustive only over the explicitly stated finite ranges; it does not enumerate all terms for arbitrary rank or all matrix assignments. The all-rank theorem uses the published normal form for matrices and the self-contained scalar separation proof in RESULT.md. The code uses standard-library Python only, no external data, no probabilistic approximations. The asymptotic growth exponents are proved by elementary inequalities in RESULT.md; no finite experiment is substituted for the limit.

**Scientific qualification:** The matrix formula is implied by Jiao's published normal-form and separation results. External expert audit and independent validation were not performed.
