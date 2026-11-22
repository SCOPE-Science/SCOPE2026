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

`verification/three_rc_verifier.py` is a standalone Python 3 exact enumerator (no external packages) and `verification/three_rc_verifier.out` is the stdout captured from a successful execution. It computes optimal oriented permutation arrangements and maximum legal greedy lengths, enumerating all three-class input sets for lengths three through seven. It independently verifies the critical three-window overlap lemma by full host enumeration through length twelve and the sharp family through length twenty.

All finite checks passed. The infinitely quantified result relies on the eight-case proof in `RESULT.md`, not induction inferred from the finite table. No independent external audit or formal proof assistant certification was performed.
