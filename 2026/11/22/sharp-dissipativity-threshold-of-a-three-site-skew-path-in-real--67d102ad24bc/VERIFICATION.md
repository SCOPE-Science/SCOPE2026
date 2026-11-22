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

The proof's critical identities, branch inequalities, isolating cubic, uniqueness, and semigroup differentiation have been checked in the written derivation. Run the standalone file `verify_path_skew.py` with `python3 verify_path_skew.py` (Python standard library only). Its observed output was:

```
THREE_SITE_SKEW_PATH_CHECKS_OK 15626 c=0.667939452729616 z=0.233103217096491
```

The script tests exact integer and rational polynomial identities, a rational upper bound on 4,912 nonzero integer triples, root isolation to floating-point tolerance, the unique explicit extremizing ray, and finite-difference slopes. Finite tests alone cannot establish the universal theorem, and the numerical root is not an exact certificate. The complete analytic argument is in RESULT.md. The first-public-source date is the arXiv submission date, not a subsequent revised or journal date. No independent audit has been performed.
