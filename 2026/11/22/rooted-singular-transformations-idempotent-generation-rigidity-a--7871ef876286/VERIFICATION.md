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

# Verification checks and limits

The arithmetic and finite semigroup checks can be reproduced with `python3 verify.py` from the same folder. It uses no external packages, constructs all fixed-point singular transformations as tuples, enumerates every nonroot tournament for \(n=4\) and \(n=5\), independently tests strong connectivity, computes right-composition closure, and verifies the cardinalities and complete-tournament criterion. It also checks the four-arrow case \(n=3\), the unique singular map at \(n=2\), the cyclic tournament construction at \(n=6\), and the strong-tournament recurrence through six vertices. The recorded output is in `VERIFY_OUTPUT.txt`.

The proof of the universal statement is the rank/kernel and factorization argument given in `RESULT.md`. The classical Howie criterion that strong tournaments generate the full singular transformation semigroup is a published theorem and is cited there. The finite computation is a consistency test, not a proof at arbitrary \(n\). Historical priority remains provisional where source access was incomplete; no independent audit is asserted.
