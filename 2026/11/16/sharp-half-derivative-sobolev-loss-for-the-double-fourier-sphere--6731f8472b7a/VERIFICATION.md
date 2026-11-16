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
# Verification of the DFS Sobolev threshold

The statement and proof are in `RESULT.md`. The critical external ingredient is the fractional Hardy estimate \(\int_{\mathbb R^2}|u(x)|^2/|x|\,dx\le C\|u\|_{H^{1/2}(\mathbb R^2)}^2\), obtained by taking \(N=2\), \(p=2\), and fractional order \(1/2\) in Frank--Seiringer, *Non-linear ground state representations and sharp Hardy inequalities*, Theorem 1.1. The assumptions \(0<1/2<1\) and \(2<2/(1/2)\) hold, and the exponents are exactly one for the weight and three for the double-integral denominator. A local polar Jacobian and the chain rule give all integer bounds. Sobolev interpolation gives noninteger bounds. The annular smooth counterexamples supply the sharpness for each pair of nonnegative exponents below the boundary.

Run `python3 check_scaling.py` to reproduce `SCALING_CHECK.txt`, which evaluates the exact sphere-versus-torus \(L^2\) and radial \(H^1\) formulas by numerical quadrature for a smooth profile and five shrinking annuli. The results exhibit the predicted \(\varepsilon^{-1/2}\) norm-ratio growth, but are not used to establish the abstract theorem.

The source date of the motivating article is the first arXiv submission date 2021-08-12 (arXiv:2108.05662). The mathematical limitations and related literature are identified in `RESULT.md` and `REVIEW.md`. The numerical check does not test all real Sobolev exponents. Independent validation and historical-priority certification have not been performed.
