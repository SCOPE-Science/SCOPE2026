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

# Reproducible checks

Run `python3 CHECKER.py` with only the Python standard library. The checker uses `fractions.Fraction` throughout and fixed-seed rational sample points. The output from the saved package was:

```
d=3: 26 vertices; 24 facet normals; volume=1/3; ratio=1/4; projected-face test passed
d=4: 80 vertices; 64 facet normals; volume=2/45; ratio=1/15; projected-face test passed
d=5: 242 vertices; 160 facet normals; volume=1/210; ratio=1/56; projected-face test passed
d=6: 728 vertices; 384 facet normals; volume=2/4725; ratio=1/210; projected-face test passed
PASS: 1076 candidate vertices 324016 halfspace evaluations, 640 all-face projection tests, 12 closed-form identities
```

The exact-rational projection test checks every nonempty proper face for each sampled point. It is not an exhaustive check over all real coordinates or dimensions. The analytic proof in RESULT.md supplies the universal theorem. The dimension-three cases provide a known-reference regression check; novelty is asserted only for dimension at least four.

The motivating paper's kernel definition, the companion paper's distinct cross-polytope realization and published summary records were compared as set out in REVIEW.md and AUDIT.json. Historical priority beyond these checks and external independent audit remain unresolved.
