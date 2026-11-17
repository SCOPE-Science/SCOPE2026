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

The included `verification/verify_chain.py` is self-contained Python using only the standard library. It was executed from the provided package directory. Output was:

```
PASS: finite kernels, endpoint multiplicities, and chain BFS checks.
Exact assertions performed: 32161
At m=2: 38 facets; 164 facet-adjacency edges; distance counts (164,374,156,9).
All m>=2 theorem: diameter m+2; exactly nine diametral facet pairs.
```

The script constructs the twenty-four type-\(D_4\) roots and ninety-six adjacency edges, checks isometric eight-vertex seams within all three local blocks, the exact internal transfer kernel and min-plus powers through four intervening blocks, and all endpoint pair cases at zero, odd and even internal-block parity. It independently reconstructs the complete quotient adjacency graph for chains of two through eight cells and checks diameter, the nine extremal pairs, and the facet/edge counts. These are finite exact checks. The proof for unrestricted chain length uses the min-plus identity in `RESULT.md`; no numerical extrapolation is treated as proof. Independent mathematical audit has not been performed.
