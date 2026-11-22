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

# Reproducibility and scope

`verify.py` uses only Python's standard library. Run `python verify.py` to check the exact finite distribution against a completely independent Prüfer-code traversal of all Cayley trees at four, six and eight vertices, direct recursive perfect-matching tests, independent quotient-tree/lift traversals through five matched pairs, and rational coefficient and moment identities through twenty-four matched pairs. The output prints the sizes checked and confirms successful assertions.

The all-orders claim is established by the mathematical argument in RESULT.md: unique matching, uniform contracted tree, independent lift endpoint bits, a uniformly random Prüfer code, and independent occurrence thinning. Finite enumeration alone does not establish an all-orders identity, and this verification does not constitute an independent audit.
