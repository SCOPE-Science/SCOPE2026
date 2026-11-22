---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The final claimed theorem is the all-length **positional pair-query support classification** and its partition-matroid/Stirling enumerator. Necessity follows from the impossible pair of answers for edges sharing their left endpoint (a 231 triple). Sufficiency follows by right-to-left extremal insertion, preserving avoidance and realizing every binary labeling; no computation is used for the universal proof.

The unchanged `verify.py` and `depth8_tree.json` are retained as original evidence. The former checks finite coefficient profiles (lengths 1–8), while the latter is a complete 255-query depth-eight online tree. The online depth eight at length seven is previously covered by the 2 November 2026 Wilf-equivalence classification after permutation inversion, and is **not** claimed as an original theorem here. An independent replay of the original tree verified all 256 leaves among 429 avoiding seven-permutations. Independently regenerated shattered-support profiles for lengths 2–6 agreed with the polynomial.

Full mathematical correctness uses the explicit universal proof, not finite extrapolation. Alternative literature under Catalan inversion-set terminology remains a priority risk. No Lean proof or expert attestation is claimed.
