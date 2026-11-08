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

# Verification and limitations

The proof uses the exact associated-Legendre formula for spherical harmonics and azimuthal orthogonality to diagonalize concentration over antipodal caps. All nonstandard computations are the exact normalized polynomial integrals and their pairwise difference factorizations in RESULT.md; their sign patterns determine the continuous phase diagram and boundary ties.

To reproduce, install SymPy and execute `python check_spherical_caps.py`. The expected output is:

```
ANTIPODAL_FOURTH_DEGREE_PASS assertions=70 exact_sectors=14 phase_intervals=5
```

The checker reconstructs all azimuthal integrals for degrees 1–4, each degree-four defect polynomial, every degree-four pairwise difference, root inequalities, and selected strict interval comparisons. Sampling and symbolic checks supplement but do not replace the universal analytical proof. No external independent audit was performed. A closely relevant 2021 spherical Slepian paper could not be read in full; novelty remains provisional.
