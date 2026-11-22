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

The proof establishes the local sign criterion by the standard three-step Lanczos polynomial identity and tree path uniqueness. The explicit family was checked using SymPy exact rational algebra, including a Sturm-chain positive-root count for all three sign polynomials, and independent rational CG recurrences at nine parameter values. The accompanying `verify.py` is the executable checker; it also checks five general rooted-tree identities. This is a mathematical derivation plus reproducible finite algebra; numerical sampling is not used as an infinite proof. Independent external validation has not been performed.
