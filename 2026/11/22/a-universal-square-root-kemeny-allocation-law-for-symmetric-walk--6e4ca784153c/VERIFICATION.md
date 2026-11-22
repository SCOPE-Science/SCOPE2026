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

The accompanying `check_corona.py` program uses SymPy exact rational linear algebra. It constructs independently the core and corona Laplacians, computes inverse traces on the orthogonal complement of constants, compares them with the derived spectral transfer, verifies the radical optimizer algebra, and tests large-size asymptotic consequences. Executed with Python 3 and SymPy 1.14: `PASS: 775 independent algebraic/matrix/asymptotic assertions`.

The proof of infinite-size and unrestricted optimization rests on the strict-convexity argument, orbit averaging, exact spectral decomposition, and scalar minimization in RESULT.md. Finite tests check implementations and algebra; they do not independently certify all parameter choices.
