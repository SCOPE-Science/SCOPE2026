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

# Verification summary

The complete proof, definitions, and boundary conditions appear in `RESULT.md`. The standalone `verify.py` reconstructs every edge of \(K_{2,n}\) and its edge-adjacency relation, checks rich edges by pairwise distinct colours on adjacent edges, and checks each edge has a *different* adjacent rich edge. It fixes the first row by colour-label symmetry and exhaustively enumerates every injective possible second row for \(2\le n\le8\), multiplying by \((n+1)!\) only after direct verification.

The actual run returned:

```
DIRECT_ADJACENCY_ENUMERATION_OK 2 proper 18 rich_neighbor 0 orbit_types 0
DIRECT_ADJACENCY_ENUMERATION_OK 3 proper 264 rich_neighbor 72 orbit_types 1
DIRECT_ADJACENCY_ENUMERATION_OK 4 proper 6360 rich_neighbor 960 orbit_types 1
DIRECT_ADJACENCY_ENUMERATION_OK 5 proper 222480 rich_neighbor 32400 orbit_types 2
DIRECT_ADJACENCY_ENUMERATION_OK 6 proper 10679760 rich_neighbor 1330560 orbit_types 2
DIRECT_ADJACENCY_ENUMERATION_OK 7 proper 672819840 rich_neighbor 74793600 orbit_types 4
DIRECT_ADJACENCY_ENUMERATION_OK 8 proper 53825627520 rich_neighbor 5382236160 orbit_types 4
VERIFY_OK
```

Reproduce with `python3 verify.py`. The verifier uses only the Python standard library. These are finite exhaustive checks under colour-name normalization; correctness for all \(n\ge3\) follows from the mathematical proof, not from an extrapolation of the tests. Literature priority was checked against the listed sources but has not been independently certified.
