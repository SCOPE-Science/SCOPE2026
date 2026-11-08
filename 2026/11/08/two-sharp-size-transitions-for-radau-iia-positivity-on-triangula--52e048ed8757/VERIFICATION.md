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

# Verification procedure and limits

The reproducible program `check.py` uses only the Python standard library (not floating-point arithmetic or network access). From the files in this package, run:

```sh
python3 check.py
```

It reconstructs the triangular graph for \(n=4,5,6,7,8\), forms the exact rational graph Laplacian, and checks the complete matrix identity \((h^2L^2+4hL+6I)T(h)=6I-2hL\) at five positive rational timesteps each. It verifies exact row sums and symmetry; polynomial certificates for the two small cases; the cubic discriminant \(-24660792741888\) at \(n=74\); explicit sign-loss witnesses from \(n=6\) and \(n=75\); and thousands of additional rational polynomial identities.

The replay completed with output: `PASS: 3770 exact-rational checks; 25 full-matrix rational identities; distinct 6/75 transitions`.

These are finite algebraic regression checks. The proof of the universal statements, root counts, and sharpness of the two graph-size thresholds is in `RESULT.md`, by spectral interpolation, positivity bounds, Descartes' rule, and the intermediate value theorem. No independent external mathematical audit or certification is represented.
