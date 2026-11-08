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

The theorem is proved in `RESULT.md` by a matching constructive upper bound and a rank-monotone shortest-path potential. The only computation-dependent assertions are the supplementary finite comparisons reported below; the universal statements do not depend on their exhaustion.

Run `python checker.py` using Python 3 and the standard library. An actual execution of the packaged standalone script returned:

```
VERIFY_OK
exact_BFS_pairs 451
witness_pairs 451
histogram_entries 220
potential_transitions 23014
```

`exact_BFS_pairs` tests all 451 pairs over \(4\le n\le14\), calculating independent shortest distances by breadth-first search. `witness_pairs` executes all matching witness words. `histogram_entries` tests the exact distance multiplicities across the same range. `potential_transitions` checks local transitions on every image subset of rank \(n,n-1,n-2\), for \(4\le n\le40\), including the transitions that stay within the potential's domain.

Checks were executed using the files included with this finding. No computation certifies historical originality, establishes all infinite parameter cases independently of the written proof, or constitutes an independent external audit.
