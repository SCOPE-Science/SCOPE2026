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

The included `verify_symbolic.py` derives the elementary moments and substitutes their recurrence into the four Johnson eigenvalue expressions. It checks four exact rational polynomial identities using SymPy.

The included `verify.py` enumerates all Boolean constant-weight slices of dimensions six through eleven, constructs each raw cubic Walsh Gram independently, and compares all eigenvalues and ranks. It checks 57 direct Gram matrices and four further exceptional parameter choices.

The unbounded theorem follows from the stated Johnson incidence decomposition and exact factorization, not the finite checks. No independent mathematical audit has been performed.
