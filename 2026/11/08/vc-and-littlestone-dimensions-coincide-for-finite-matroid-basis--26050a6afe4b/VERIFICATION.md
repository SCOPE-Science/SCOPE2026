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

The proof is independent of enumeration. Check rank-zero and the unique-basis case; the exact dual rank identity; the matroid-intersection theorem applied to \(M\) and \(M^*\); that deletion preserves rank and contraction lowers rank precisely when \(e\) is neither loop nor coloop; the resulting partition of all subsets into sets with and without \(e\); and the standard binary-tree minimax recursion for membership queries.

Reproduce finite corroboration with `python check.py`; the actual replay is recorded in `check_output.txt`. It enumerates all traces and recursively computes exact Littlestone dimension for the displayed small examples, compares pair-basis distances and rank minima, and checks every nonconstant-coordinate split. It also exhibits a six-coordinate constant-weight nonmatroid family with unequal dimensions to show why the matroid hypothesis matters. Finite checks are not a substitute for the general proof, and they do not certify originality.

No independent audit or external mathematical validation has been performed. Historical-priority uncertainty remains.
