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

# Verification and replay

Execute the self-contained Python 3 script from the same directory:

```sh
python3 verify_ellipse.py
```

Observed output:

```text
ELLIPSE_PHASE_INTENSITY_CHECK_PASS exact_cases=49 fourier_cases=66
```

The exact component uses rational parametrization of axis-aligned ellipses and Fraction-only elimination for degrees 1 through 6, checking predicted ranks \(4d\) versus \(2d+1\) on the circle and verifying the defining conic equation. The second component checks DFT recovery of polynomial intensities and the exact expected ranks at nonsingular and singular grid offsets, using reproducibly seeded finite tests.

The all-degree theorem and the grid criterion are proved algebraically in `RESULT.md`; the finite checks do not prove the infinite statements, certify optimal nonlinear phase retrieval, or supply uniform stability constants. Mathematical review was conducted without an independent audit.
