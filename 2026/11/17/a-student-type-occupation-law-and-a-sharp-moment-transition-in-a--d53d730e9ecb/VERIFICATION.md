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

# Verification performed

The standalone script `verify.py` uses Python 3 standard library only. Run `python verify.py` in the directory containing it. It calculates the derivative of the stated first integral on a rational input grid, performs a regularized direct period quadrature, and compares finite-energy dimensionless ratios with the three analytic constants \(4/\sqrt3\), \(3\), and \(\sqrt{\pi/2}\). Execution of the included version completed with `STUDENT_CUBIC_MOMENT_TRANSITION_OK`.

The first-integral derivative also simplifies symbolically to zero. These exact symbolic calculations confirm the reduction, whereas the quadrature is a finite diagnostic for normalization and constants; the asymptotic limit and every moment exponent require the proof in RESULT.md. No independent review has been performed.
