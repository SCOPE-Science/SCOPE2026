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

# Reproducibility checks and limits

Run the three independently embedded scripts with Python 3.10 or later, using only its standard library:

```
python verify_burning.py
python verify_independent.py
python verify_family.py
```

The first script enumerates every stable state, applies Dhar's burning criterion, and checks the cube and octahedron event totals. The second generates every recurrent state via the grain-addition orbit from the maximal stable configuration, and independently checks exact size/burst histograms and the distance-resolved nondissipative counts. The third checks the explicit \(n\)-prism recurrence witness for six finite sizes and all recurrent bipyramid additions for four finite sizes. These computations replay the exact \(384\) state counts and the distinct positive nondissipative totals \(64\) and \(0\).

The all-\(n\) statements rely on the analytic burning proof in `RESULT.md`, not on finite testing. The published group-duality theorem and an elementary graph-embedding argument supply the isomorphism premise. Full external independent validation and a global priority guarantee have not been performed.
