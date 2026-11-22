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

The exact binary-word checker `check.py` was run from this package. It enumerated all balanced words through \(n=6\) and compared the source statistic's complete cutpoint minimization with the run-boundary bounds and exact zero event; it checked the constructive exact-equality lemma on additional words and verified exact run counts and moments. The calculations succeeded. Infinite-sample claims are justified by the proofs in RESULT.md, not by finite enumeration. The local isolated-pattern concentration and the classical combinatorial central limit argument are separate mathematical arguments; no external independent audit has been performed.
