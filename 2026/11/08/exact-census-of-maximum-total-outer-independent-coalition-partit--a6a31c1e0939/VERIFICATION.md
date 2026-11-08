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

# Reproducible verification

Run `python3 verify.py` in the directory containing the extracted standalone file. No nonstandard Python dependency is needed. The script verifies the exact characteristic polynomials for both finite matrices, compares the trace and scalar recurrences for graph orders from 3 through 45, then independently enumerates every unordered three-block partition for cycles from order 3 through 12. The direct enumeration tests the graph-theoretic total domination, outer independence, and valid coalition graph, rather than reusing the transfer-matrix predicate.

Expected final line: `VERIFY_OK`. This finite check is corroboration only: the proof in `RESULT.md` establishes the unrestricted statement. A historical literature search cannot establish definitive priority. Independent validation was not performed.
