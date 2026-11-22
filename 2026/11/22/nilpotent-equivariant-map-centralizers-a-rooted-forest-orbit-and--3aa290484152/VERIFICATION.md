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

Run `python3 verify.py` with Python 3. The program uses only the standard library. It reconstructs all rooted parent forests at small sizes, verifies the nilpotent totals, computes commutants through the displayed subtree recursion, separately enumerates and tests all equivariant candidate centralizers for three cyclic groups and nonabelian \(S_3\), and separately verifies unit-conjugacy orbit sizes by direct conjugation. It exits unsuccessfully on the first discrepancy. The expected final line is `NILPOTENT_POINTED_GSET_CENTRALIZERS_PASSED`.

The finite tests are reproducible checks of the nonstandard recursion, not a proof of the quantified theorem. The proof holds for every finite group, including ones not enumerated. The total nilpotent count is credited to prior work, not introduced as a novelty witness. No independent audit has been performed.
