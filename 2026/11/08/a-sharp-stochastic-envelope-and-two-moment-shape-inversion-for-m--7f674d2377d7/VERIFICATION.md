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
# Verification and reproducibility

The package contains `triangle_extreme_verifier.py` as a standalone Python program using NumPy and SciPy. Running `python triangle_extreme_verifier.py` from its directory produced:

```text
VERIFY_OK six_point_exact=20 inversion=3 rate_pair_inequalities=180 full_or_reduced_extrema=7800
```

The recorded diagnostics include exhaustive largest-triangle comparisons on 20 independent small random boundary samples, exact-cubic inversion for three side-proportion triples, 180 numerical pair-rate survival checks, and 7,800 simulated samples at sizes 20, 100 and 600 across two distinct parent triangles. They also print sample deficit means and variances alongside the predicted limiting values. These are finite checks, not infinite proofs or independent certification. The analytic derivation and boundary assumptions are in `RESULT.md`.

The stochastic bounds and the inverse theorem are exact statements for a fixed parent triangle and the asymptotic limiting law. The program requires commonly available numerical packages; nothing external is downloaded by the program.
