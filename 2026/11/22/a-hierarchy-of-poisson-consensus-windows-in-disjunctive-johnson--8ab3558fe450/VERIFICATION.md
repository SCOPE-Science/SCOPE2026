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

# Reproducibility

Run `python check.py` and `python moment_check.py` using Python 3.10 or later. Both scripts depend only on the standard library. The adjacency checker constructs a graph from genuine one-element swaps, computes repeated synchronous OR updates, and compares those results with the formula based on common labels of initial and target subsets. It also compares the all-one event with the exact empty-shadow-clique predicate for each eligible intermediate time.

Observed output: 1,422 states and 4,266 update comparisons for \((6,3)\); 2,072 and 8,288 for \((8,4)\); 1,254 and 6,270 for \((10,5)\); 1,226 and 7,356 for \((12,6)\); total 26,180 comparisons. All assertions passed. Cases are deterministic sampled inputs plus singleton and all-equal configurations; this is not an exhaustive census.

The moment checker separately counts the size of unions of forbidden neighborhoods of two candidate targets, using four disjoint regions of the ground set. Its exact finite-size first and second factorial moments approach the analytical Poisson predictions as \(n\) increases. This checks bookkeeping of the overlap terms, not every fixed higher factorial moment.

The infinite convergence follows from the explicit combinatorial bound on all overlapping patterns, the factorial-moment limit, and the deterministic timing argument in `RESULT.md`. There is no machine or independent proof certification.
