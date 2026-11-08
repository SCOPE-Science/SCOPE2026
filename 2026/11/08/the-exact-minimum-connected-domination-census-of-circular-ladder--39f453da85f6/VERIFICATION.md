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
# Computational verification

Run `python3 verify_prism_cds.py` with Python 3.10+ without external packages. The program is supplied verbatim as a standalone artifact.

It enumerates all \(2^{2n}-1\) nonempty subsets of \(C_n\square K_2\) for each integer \(3\le n\le10\), computes graph-connectedness and domination directly, selects minimum-cardinality instances, compares them by *set equality* with a separately generated structural family, and compares the full double-column profile. In total, this checks 1,398,072 nonempty subsets, including 81,456 connected dominating sets. The program additionally constructs and checks all 43,570 prescribed minimum subsets across orders \(11\le n\le40\), verifying connectedness, domination and cardinality.

Observed execution terminal line:

```
VERIFY_OK exhaustive_orders=3..10 nonempty_subsets=1398072 connected_dominating_subsets=81456 explicit_sets_orders=11..40 43570 minimum_set_profiles=PASS disjoint_construction=PASS
```

Finite enumeration is not a substitute for the unrestricted proof. The proof in `RESULT.md` uses cyclic occupied-column connectivity, the two-empty-column domination obstruction, and exhaustive equality-case classification. No independent audit has been conducted; the checks reported here are the actual self-review.
