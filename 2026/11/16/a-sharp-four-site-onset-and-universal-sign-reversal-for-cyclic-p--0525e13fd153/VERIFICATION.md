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

# Verification details

The proof uses an exact full Fourier alias sum for the classical Poisson kernel, not a truncated Fourier series. Its inverse DFT is normalized by \(1/n\), and the sample covariance retains \(P_r(0)=(1+r)/(1-r)\). The asymptotic small-\(r\) coefficients include both central Fourier classes for odd sample counts. The near-\(r=1\) expansion controls the remainder at fixed finite \(n\).

For four points the opposite-pair zero is equivalent to \(u^2-2u-4=0\) with \(u=r+r^{-1}>2\). For five points it is equivalent to \(2u^2-(3+\sqrt5)u-2=0\). In both cases \(u\) is strictly decreasing in \(r\), and nearest-neighbor factors remain strictly negative. No arbitrary-size zero-count claim is inferred from finite experiments.

The bundled standard-library script `CHECKER.py` was actually executed and printed `PASS: 3084 finite independently reconstructed checks; analytic generality in RESULT.md`. It compares Fourier inverse entries with independently inverted spatial Gram matrices for regular polygons, checks both explicit algebraic formulas, and tests the limiting asymptotic profiles. Rerun by placing the files together and executing `python3 CHECKER.py`.

Independent mathematical audit: not performed. Historical novelty beyond the cited and inspected literature: not independently established.
