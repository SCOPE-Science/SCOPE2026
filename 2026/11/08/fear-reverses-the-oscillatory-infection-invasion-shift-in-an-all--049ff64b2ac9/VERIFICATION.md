---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The reviewed full RESULT reconstructs the no-delay disease-free planar system and rare-infection transverse equation. At d0=(1+theta)/2, Jacobian trace crosses zero with positive determinant; canonical Hopf derivatives cancel to l1=-f0/4<0 and leading Var(x)=2d0 epsilon. Integrating z-dot/z over each periodic orbit yields mean(x)=d exactly. Integrating x-dot/x and expanding to second order with the sinusoidal covariance yields mean(z)-z*(d)=C epsilon+o(epsilon), C=2d0/K*(h*f_zz*z0/(2d0*K)-f0). For theta=1/5, alpha=26/3125 and eta=92/225 or 1/100, independently evaluated exact rational C values -72008352/212226125 and +1645176/6555125. The infection Floquet exponent difference is -3C epsilon/2, and positive mu can be chosen between near-critical thresholds. This is local sufficiency, not global invasion persistence. Independently rebuilt symbolic fractions; inspected check code, did not rely on VERIFY_OK alone.

## originality

PASS

The general ecological Hopf boundary and oscillation-sensitive infection threshold are known. After reading the original model paper and relevant published-result searches, the specific exact signed predator mean coefficient and fixed-parameter reversal with positive rational floors were not found to be implied by them. General averaging is expressly excluded from novelty. This is a best-of-knowledge originality finding with a model-specific unindexed-priority risk.

## value

PASS

The signed cycle-versus-equilibrium invasion discrepancy matters for interpreting disease invasion at a Hopf-unstable ecological coexistence point. Two exact same-model positive-parameter witnesses reverse the direction while the susceptible mean is conserved; this is not a mere numerical example or general statement that Floquet averaging is possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
