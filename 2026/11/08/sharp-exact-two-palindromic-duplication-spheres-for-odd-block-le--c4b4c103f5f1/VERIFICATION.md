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

# Reproduction notes

1. Use Python 3 with no dependencies beyond the standard library.
2. Run `python3 checker.py` beside this file.
3. The checker independently implements a length-\(k\) palindromic duplication as insertion of the reversed \(k\)-symbol source block immediately after that block.
4. For pairwise-distinct source letters, it checks the exact output set and compares every doubleton history fiber with the two commuting histories \((a,b+k)\) and \((b,a)\) arising from disjoint original starts \(a<b\) with \(b-a\ge k\), for all \(2\le k\le8\) and \(k\le n\le19\).
5. For binary and ternary sources with length at most \(7\), it checks the general upper bound and verifies a \(k=1\) counterexample to the distinct-letter history statement.

These finite tests do not prove an infinite theorem. The formal proof is the first-occurrence/gap decomposition in `RESULT.md`. The independent audit status has not been asserted or inferred from the local tests.
