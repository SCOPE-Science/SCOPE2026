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

# Reproducibility and proof checks

The theorem's proof is a local exchange classification, a formal generating-function decomposition and a sharp binomial convexity/equality argument; none relies on finite enumeration. The primary literature establishes the Dyck matroid base-polytope realization and the single-basis-exchange edge criterion.

Run `python3 catalan_degree_checker.py` using Python 3 and its standard library. It enumerates all Dyck paths of semilength \(1\) through \(9\) (up to \(4,862\) paths at the largest size), evaluates the exact number of neighbors by independently testing all \(n^2\) unlike-symbol swaps, and compares with the depth-two forest formula. In parallel, it forms each excess-degree polynomial from the recurrence without using those path swaps. It checks polynomial coefficient equality, vertex totals, exact extremal values, and equality multiplicities; the success marker is `CATALAN_POLYTOPE_DEGREES_EXACT_PASS`.

Limitations: these are exact finite cross-checks, not an infinite proof or independent audit. The proof itself covers every integer \(n\ge1\). Historic priority is conditional on the inspected literature and indexed records, rather than exhaustive verification of all possible prior sources.
