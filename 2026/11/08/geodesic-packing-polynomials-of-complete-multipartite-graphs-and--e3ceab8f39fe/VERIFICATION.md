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

Run `python3 verify.py` using Python 3 standard library. The independent finite checker constructs the complete multipartite graph from labelled part sizes, enumerates all unordered length-two shortest paths, recursively lists vertex-disjoint path families and tests inclusion-maximality directly. It separately calculates the directed-type polynomial and doubleton formulas for comparison.

Observed exact successful output:

```
VERIFY_OK direct_profiles=18 twin_profiles=6 enumerated_path_families=38436 general_formula=PASS twin_formula=PASS maximality=PASS symbolic_purity_r2to30=PASS
```

The direct finite tests cover 18 distinct general part-size profiles, six all-doubleton orders from two through seven, and 38,436 enumerated vertex-disjoint path families; additional symbolic comparisons cover orders two through thirty. The tests cannot establish a universal graph-family theorem or publication priority. The combinatorial proof in RESULT.md supplies the unbounded argument, and independent audit has not yet occurred.
