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

The independent file `CHECK.py` enumerates endpoint matchings for \(2\le n\le6\), checks the universal-interval identity against direct pairwise intersections, and verifies exact finite matching probabilities. It separately computes the limiting probabilities for \(k=0,1,2\), tests numerical normalization and mean, and performs seeded finite-sample simulations. Run it with Python 3 and the standard library:

```sh
python CHECK.py
```

Expected output concludes with `PASS 28 structural assertions with finite exhaustive enumerations and seeded simulations`.

These checks do not prove asymptotic joint point-process convergence; that is established analytically by disjoint-corner Laplace functionals, extreme-point tightness, and random-rectangle clipping in `RESULT.md`. External independent mathematical audit has not been performed. The 1990 and 2026 related papers' complete texts were unavailable for priority comparison.
