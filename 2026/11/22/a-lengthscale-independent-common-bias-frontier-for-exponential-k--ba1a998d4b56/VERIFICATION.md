---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Final result at /workspace/repairs/2/RESULT.md. The original proof's unqualified endpoint-only minimizer was false below the frontier: for example n=2, λ=1, τ=0 gives both weights u>0, so endpoint samples (1,1) produce 2u>0, whereas (0,0) realizes the minimum 0. The corrected proof sets samples to 1 on strictly negative coefficients, 0 on strictly positive coefficients, with zeros free, and distinguishes the two regimes. The original weight and negative-mass formulas do not change. The cross-covariance of the integral with Y is the original kernel mean (2−r^{i−1}−r^{n−i})/λ because the offset is independent of the integrand. The tridiagonal AR(1) inverse verified row by row (including the two endpoints for n=2) gives Qm=u(1,2,…,2,1) and Q1=(1,1−r,…,1−r,1)/(1+r). Thus w=Qm−(τ·2(n−1)u/D)Q1 and the endpoint numerator reduces to u(1−(n−2)τ), while the interior numerator is 2u(1+τ). All denominators and interior numerators are positive; this includes no offset and zero endpoints at equality, and n=2 has no finite boundary. Given h=1/(n−1), u/h→1/2 and D→1+τ(1+λ/2); separating the two endpoints from the interior Riemann sum gives the signed weak limit against every continuous function. For independent noise, (I+ηQ)w=Qm. At a nonpositive minimum coordinate, the positive row sum and nonpositive off-diagonals would give a nonpositive left-side component, contradicting Qm>0. Independent numerical replay of 136 bounded direct covariance systems matched the weights within 1.492×10⁻¹¹; 16 diagonal-nugget solves were positive; weak-limit diagnostics up to n=2000 corroborated convergence. Evidence and replay details: /workspace/branches/5012c8b8-039e-434d-beb2-406d2f93f559/independent-check.md. The submitted code was read, not run. Numerical tests are diagnostics, not uniform proofs or authority for mixed noise models.

## originality

PASS

The verified surviving contribution is the common-measurement-offset threshold and signed dense limit; Gaussian conditioning, AR(1) precision, and Sherman–Morrison are prior methods. The independent-noise statement is explicitly comparative in the repaired result, with the stronger diagonal-nugget finding cited. The corrected sharpness witness is not claimed as novel in isolation.

## value

PASS

The finite threshold answers when nonnegative readings can yield a negative posterior integral estimate under a simple sensor-calibration model, with a sharp worst-case magnitude and exact correlation-length cancellation. The sign effect does not disappear with arbitrarily many observations at fixed positive shared variance; the limit identifies its boundary atoms. This is a structural stability result, not a claim that positive weights guarantee lower numerical or statistical error. The minimizer repair makes the operational interpretation correct in all regimes without weakening those contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
