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

# Reproducing the verification

Run `python3 CHECK.py` with Python 3 and no external dependencies. The script constructs normalized real cycle Fourier eigenvectors and directly forms the \((2r+2)\)-by-\((2r+1)\) untreated observation matrix for each test. It calculates its column volume as a sum of squared maximal minors, separately evaluates the proposed Vandermonde/Lagrange/trigonometric product, tests the exact arithmetic order criterion, and checks the five-mode optimal-grid rule and the conditioning-versus-volume distinction.

The observed output from the included program is:

```text
CHECK_OK raw_volume_cases=801 five_mode_grid_sizes=496 demixed_vs_raw_checks=78
```

The finite tests are supplemental numerical consistency checks, not proofs for unbounded graph order or cutoff. The universal proof rests on the explicit cofactor transform identity, exact spectral blocks, real Vandermonde invertibility, trigonometric monotonicity, and the algebraic-integer argument. The determinant is not a noise-optimality or independent mathematical certification.
