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

# Verification of the finite-hub theorem

The analytical proof is in `RESULT.md`. The standalone `verify.py` checks exact cycle ranks and Poisson limit specializations with rational and finite combinatorial computations. Its output is not a certificate of infinite limiting assertions.

To reproduce, use `python verify.py`. The enumeration uses no external dependencies. Distinct right vertices may share left-neighborhood types. The script enumerates bounded small cases only and therefore never certifies an unbounded statement by enumeration.

No independent audit has been performed.
