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

Run `python3 verify.py` with Python 3 standard library only. It prints a line beginning `PASS 269880 words` when all checks succeed. This standalone program evaluates the closed run formula, a separate streaming implementation, and direct enumeration of all position-pair deletions. It also checks the full run-pair collision classes against local-move chains, not just their cardinalities. Testing covers every ternary word of length \(0\) through \(11\) and reproducible random words of lengths \(12,16,\ldots,60\) over alphabets of sizes \(2\) through \(5\). It separately verifies the rational expected-count formula by complete enumeration for \(q\in\{2,3\}\) and \(2\le n\le7\).

The mathematical proof in `RESULT.md` establishes the statement for all finite lengths and all alphabets. Finite checks are corroboration, not an infinite certificate. No independent external mathematical audit has yet been performed.
