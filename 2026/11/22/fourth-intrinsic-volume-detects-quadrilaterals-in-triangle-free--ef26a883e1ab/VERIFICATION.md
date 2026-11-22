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

# Reproducible mathematical checks

The exact forest determinant identity and all five four-edge census formulas are proved in `RESULT.md`; the general theorem is not deduced from data. The independent finite diagnostic is a standard-library-only Python program:

```sh
python3 artifacts/verify.py
```

The program reconstructs ten explicit connected regular triangle-free graphs, enumerates all four-edge subsets, computes each incidence Gram determinant using integer permutation expansion, and compares actual forest-type counts to the displayed expressions. It separately counts four-cycles from induced four-vertex subgraphs, and checks the all-three-edge forest census. The successful run ends with `GRAPHICAL_ZONOTOPE_FOURTH_VOLUME_PASS`. Cases include the nonisomorphic 14-vertex cubic bipartite circulants with four-cycle counts seven and zero. All comparisons of determinants and counts are exact integers; the radical coefficient is checked by an analytic inequality in the proof.

The finite execution does not check every graph, every possible dimension, or priority against all literature. The stated unrestricted theorem depends on the symbolic case analysis. Independent mathematical audit: not performed.
