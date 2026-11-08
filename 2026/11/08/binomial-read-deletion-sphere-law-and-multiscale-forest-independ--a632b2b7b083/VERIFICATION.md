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

The self-contained proof is in RESULT.md. Run `python3 checker.py` using Python 3 standard library. The verifier exhaustively enumerates small q-ary sources, computes each actual single-coordinate deletion descendant set, checks exact probability masses and cross-scale covariances, tests forest versus cyclic equality events, and checks a concrete dependence counterexample. These are finite regression checks, not a substitute for the all-parameter proof. No independent audit has been performed.
