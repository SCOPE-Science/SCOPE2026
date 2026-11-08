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
# Verification of the exact rank-one projection tail

The standalone `verify.py` was run against the displayed fixed \(2\times2\) matrices. SymPy checked the exact original coupled equations, the positive definiteness of each coefficient matrix, the four nonzero Sylvester spectral gaps, the projected scalar denominator and the integral substitution. SciPy then numerically integrated the **exact conditional tail formula**, giving

| \(R\) | \(R\Pr(\|\widetilde X\|_F>R)\) |
|---:|---:|
| 10 | 0.178764655840 |
| 20 | 0.178643789318 |
| 50 | 0.178610051269 |
| 100 | 0.178605235264 |
| 500 | 0.178603694339 |

The analytic limit is \(2\operatorname{arsinh}(1)/\pi^2\approx0.178603630136\). This quadrature is supplementary; it does not verify the infinite tail or moment boundary without the proof in `RESULT.md`. All computations are reproducible with `python verify.py` and standard NumPy, SciPy, SymPy. No independent mathematical audit has been performed.
