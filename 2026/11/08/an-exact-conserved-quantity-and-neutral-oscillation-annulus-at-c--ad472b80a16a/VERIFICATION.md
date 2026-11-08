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

# Computational and analytical verification

The proof in `RESULT.md` contains the general identity, the positive-definite Hessian, and the periodic-level argument. Execute `python verify.py` to reproduce symbolic and numerical checks. The program requires Python 3, SymPy, SciPy, and NumPy.

For every pair of positive integers \(1\le m,n\le5\), the verifier checks the integrating-factor differential identity, the imaginary-eigenvalue frequency, and the curvature at the binomial maximum: 75 exact symbolic assertions. It also integrates the primary source's case with \(N=6\), \(M=3\), \(b=1\), \(c=1/10\), and \(\varepsilon=1/10\), and checks that the conserved expression stays fixed to within \(10^{-9}\) along a sampled near-center trajectory. The numerical quadrature and time-stepping cannot prove the identity for untested parameters or for infinite time; the proof supplies that conclusion.

No external or independent audit is claimed.
