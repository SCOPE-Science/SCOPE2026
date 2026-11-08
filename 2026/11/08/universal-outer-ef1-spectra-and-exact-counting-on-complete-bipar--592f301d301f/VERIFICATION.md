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

# Reproduction and limits

With Python 3 and only the standard library, execute `python3 checker.py`. The script exactly enumerates every labeled allocation for small bipartite resource graphs and binary profiles and compares against an independent four-category dynamic program. It also compares a separate all-one coefficient calculation with the general enumerator, checks the predicted universal feasibility interval, and checks existence for a bounded set of all shared binary profiles.

Expected summary: `PASS 304 independent exhaustive comparisons; 252 unit-count and threshold comparisons; 1611 binary universal-existence checks`. The checker uses exact integers; no floating point certification is involved. On a standard Python runtime the code prints sample sequences for \(K_{2,4}\), \(K_{3,7}\), and \(K_{4,4}\). The analytic proof, not this bounded enumeration, establishes the universal quantifiers and polynomial-time existence/counting statements. Full-text overlap risk in one relevant 2026 source remains; independent scientific validation has not been performed.
