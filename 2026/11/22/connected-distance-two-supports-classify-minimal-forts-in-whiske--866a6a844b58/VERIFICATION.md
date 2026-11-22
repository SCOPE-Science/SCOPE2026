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

The embedded `VERIFY.py` reconstructs whiskered adjacency, exhaustively enumerates all forts from the definition, and filters every proper contained fort (not merely one-deletion tests). It then independently enumerates core supports and tests link-graph connectedness. The script checks combs with \(2\) through \(8\) core vertices, all labelled trees through \(5\) core vertices via Prüfer codes, and six explicit six-core tree representatives. It verifies the exact cardinality polynomial, total count and every attained size. All-order correctness depends on the symbolic proof in RESULT.md, not finite computation.

Execute: `python3 VERIFY.py` (standard-library-only Python 3.9+).

Independent audit: not performed. No external certification is claimed.
