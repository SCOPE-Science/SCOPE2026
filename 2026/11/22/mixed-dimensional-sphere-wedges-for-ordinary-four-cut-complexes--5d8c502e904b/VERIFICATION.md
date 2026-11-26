---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and boundaries

The proof in `RESULT.md` is an all-parameter argument using the rectangular face poset and a model inside a product of simplices. It does not depend on computation or on the all-parameter behavior of any discrete Morse matching.

For optional finite corroboration, `python3 evidence/verify.py` uses Python 3's standard library. Its finite checks include direct reconstruction from connected induced four-subsets, comparison with the rectangular-core and transversal decomposition, matching and acyclicity checks on small boards, and mod-two simplicial homology. The saved output `evidence/verification-output.txt` is from the finite checker; its last line refers to an earlier proof route and is not a certificate for arbitrary board sizes.
