---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Any feasible selection requires at least two vertices on each side. For a selected a_i the number of unselected neighbors is n-1-y+1_{i in J}; analogous expression holds for b_j. Thus capacity and domination give precisely the two classified overlap regimes, and binomial index-subset counts yield the polynomial. Minimization gives 4 at r=1; 2r for n>=2r and 2r+2 otherwise, with the displayed equality cases. Fresh independent adjacency-mask brute force tested 101,952 subsets for n=3..7 across all allowable k and checked every coefficient.

## originality

PASS

Božović et al. (2026) formulate k-limited domination and give K_{m,n} minima, but not the matching-deleted crown predicate or all bivariate counts. Earlier crown graph paired/tuple/perfect/Roman domination indexed results concern different predicates. The same graph and capacity parameter were explicitly compared; no stronger matching-deleted k-limited enumeration found.

## value

PASS

The full feasible-set enumerator and sharp nonmonotonic response to matching deletion quantify a natural capacity-constrained domination problem, beyond the known complete-bipartite scalar minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
