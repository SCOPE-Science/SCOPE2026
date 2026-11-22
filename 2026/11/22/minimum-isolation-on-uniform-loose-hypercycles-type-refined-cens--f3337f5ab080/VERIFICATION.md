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

## Reproducible checks

Run `python verify_hypercycle.py` from the same directory using Python 3 standard library. The checker constructs each hyperedge, all closed vertex neighbourhoods, and uses those actual sets to test whether a chosen vertex subset isolates every hyperedge. This is independent of the cyclic arc/gap proof. A second calculation expands the claimed bivariate coefficient polynomial and compares every private-count coefficient.

Executed checks:

```
DIRECT_HYPERGRAPH_NEIGHBORHOOD_CENSUS_PASS cases= 44 candidate_subsets= 270310
DIRECT_ONE_VERTEX_EXCHANGE_CONNECTIVITY_PASS
EXACT_TYPE_ENUMERATOR_IDENTITIES_PASS ranks=3..39 orders=3..699
VERIFY_OK
```

The first test includes actual ranks 3 through 6 and cyclic orders 3 through 16, omitting only combinations with more than 70,000 candidate subsets of minimum possible size. It also directly constructs and finds all components of the minimum exchange graph for every tested instance. The second exact integer check exercises 37 ranks and 697 cycle lengths; it is an algebraic consistency check, not a proof of the unrestricted theorem. The mathematical proof establishes all parameters, including untested orders.

No theorem prover or independent human audit is claimed.
