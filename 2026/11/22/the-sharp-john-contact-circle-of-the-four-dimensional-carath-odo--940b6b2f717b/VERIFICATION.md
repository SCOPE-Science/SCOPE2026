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

# Reproducibility and verification

The exact claim is for the four-dimensional body in `RESULT.md`, with ordinary real Euclidean volume, no restrictions on competing ellipsoid orientations, translations, or shapes.

Run `python verify.py` from the directory containing the two files. The script uses the Python standard library only. A recorded execution succeeded with the lines:

```
PASS: 1001 exact-rational inequality checks; 9160 numerical checks
NOTE: universal containment, contact uniqueness, and ellipsoid optimality follow from the analytic proof.
```

The rational checks verify the polynomial-square identity, selected equality parameters, and the exact four-dimensional volume ratios. The numerical checks test thousands of points on the proposed inner ellipsoid boundary against the exact Toeplitz/Schur complement criterion, as well as the finite-grid trigonometric contact moments and both contact circles.

**Logical limits:** None of those finite checks independently proves universal containment, nonexistence of alternative ellipsoids, or historical priority. The universal inclusion proof is the analytic squared-deficit identity; exact contact classification uses equality at every step; global unrestricted John and Löwner optimality use the standard contact theorem; volume follows by a disk-fiber Fubini integral. An independent mathematical audit has not been performed.
