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

The analytical argument is in `RESULT.md`. Re-run the standalone checker with `python3 verify_football.py`, using only Python's standard library. All calculations concern the same normalized curvature-one football family.

The checker verifies independent numerical representations of the coefficient: a direct polar two-dimensional quadratic-domain integral; its angular antiderivative; and a direct numerical integration of the **unexpanded** spherical cosine inequality at finite \(\varepsilon\). It also verifies strict sample ordering, the antipodal quotient case \(\alpha=1/2\), and the small-angle expansion. A sample successful run is:

```
alpha=0.25 coefficient=0.022711264227 tail-ratios=0.022707708257,0.022710376345
alpha=0.50 coefficient=0.031250000000 tail-ratios=0.031246638313,0.031249078861
alpha=0.75 coefficient=0.075762911924 tail-ratios=0.075781887550,0.075767979472
alpha=0.90 coefficient=0.361270119997 tail-ratios=0.362293948264,0.361523261367
SPHERICAL_FOOTBALL_DIAMETER_TAIL_OK
```

The tail ratios use \(\varepsilon=0.05\) and \(0.025\), respectively, and approach the theoretical coefficients as \(\varepsilon\downarrow0\). These are deterministic numerical cross-checks, not independent proof, exhaustive simulation, or a certificate about arbitrary cone metrics. Exact proof requires the spherical distance law, pole localization, a convergent boundary-layer argument, and the elementary integral evaluation displayed in `RESULT.md`. No independent mathematical audit has been performed.
