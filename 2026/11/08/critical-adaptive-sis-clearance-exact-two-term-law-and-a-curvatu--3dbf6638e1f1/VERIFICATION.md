---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reassessed complete replacement /workspace/repairs/3/RESULT.md. Inward boundary signs and y'=y times a bounded coefficient give forward invariance and finite-time positive prevalence. Scalar comparison gives (z−z0)_+ exponentially small and y'≤−y²+g(t)y with integrable nonnegative g; the integrating factor gives y=O(1/t). Stable linear forcing for z−z0 tends to zero, so (log y)'→0. Forcing O(y^j) in a stable scalar equation implies response O(y^j) by choosing a late relative-variation rate ε with jε below the eventual damping, then convolving the exponentials. In succession this gives w=O(y), w−h1 y=O(y²), and w−h1 y−h2 y²=O(y³). Matching y² in w' gives A2−L1 h1−L0 h2=−Kh1. Thus r'=K+KB/r+O(r⁻²), r∼Kt, then r−Kt=O(log t); the derivative of r−Kt−B log t is absolutely integrable. Exact substitution gives h2=−κ/4−1/16 and B=κ/3−1/4, including zero at κ=3/4. Original lines 129–130 incorrectly said no lower-order constant changes with curvature if read for the finite asymptotic constant C. Indeed take common initial data y=s, z=z0+h1 s, with s small. Here y≤(1/s+t)⁻¹ and the stable expansion, now with initial quadratic defect O(s²), leaves r'=K+KB/r+O(r⁻²+s exp(−ηt)) with constants uniform in small s for each fixed κ (the log-variation bound is O(s)). Integrating (r−B log r)'−K gives C=1/s+B log(Ks)+O(s); for κ=0 and 1 the difference is nonzero for sufficiently small s. The repair removes this assertion and clarifies model dependence without changing the valid finding. Replay: repaired proof §§1–5 and this comparison; frozen verify.py was inspected but not run. Deterministic ODE only, no uniform-in-model or stochastic claim.

## originality

PASS

Pass for the model-specific critical global law with explicit positive-baseline response-jet logarithmic term, finite remainder, and curvature crossing. Neither the adaptive SIS equations, the threshold, the generic critical normal form, nor all first-order critical behavior are claimed new. The repaired text adds no priority claim.

## value

PASS

The repaired result resolves nonlinear clearance at the critical boundary left by a zero Jacobian eigenvalue for every physical infected initial state. Its leading and logarithmic jet formulas distinguish response curvature at the same equilibrium and leading decay rate, including a sharp sign boundary; the finite remainder makes this distinction precise. This is a deterministic mathematical prediction, not a stochastic or empirical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
