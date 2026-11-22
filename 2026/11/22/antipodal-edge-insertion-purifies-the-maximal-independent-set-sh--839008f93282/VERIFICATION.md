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

# Reproducible finite verification

Run the bundled standard-library Python program with `python3 verify_folded.py`, and independently compile and run the C++17 implementation with `c++ -std=c++17 -O2 verify_quotient.cpp -o verify_quotient && ./verify_quotient`. Both programs construct all maximal independent sets of the folded five-cube and of the ordinary four-cube from their adjacency definitions, enumerate all 65,536 vertex supports for each graph, and test equality of the distinct trace count to the complete powerset size. The implementations do not share graph-construction routines.

The Python program checks the equality of every shattered support to the independent-support condition in the folded five-cube, its two 40- and 80-element facet orbits under the 1,920 affine symmetries, and all 32 hexadecimal witnesses. It confirms the ordinary four-cube's eight antipodal lower-dimensional maximal supports.

Observed exact output:

```
FOLDED_FIVECUBE_MIS_SHATTER_PASS concepts=56 faces=1,16,80,160,120 facets=40+80
ANTIPODAL_PERTURBATION_PASS q4_facets=8x2+104x4 folded_facets=120x4
QUOTIENT_CLEBSCH_Q4_EXHAUSTIVE_PASS 65536_supports_per_graph
```

The structural proof in `RESULT.md` does not treat sampled output as an infinite-family proof: the stated graphs are finite, the complete search domain has exactly 65,536 supports each, and independent finite arithmetic proves the orbit reduction and upper obstruction. No assertion about higher-dimensional folded cubes or independent external verification is made.
