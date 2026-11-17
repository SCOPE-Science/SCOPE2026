---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The Fourier basis has independent stationary variances sigma^2/(2 lambda_j) and point variance v_L=(sigma^2/(2L))*sum_j lambda_j^-1; the series has O(j^-4) tail. Gaussian E[u(x)^3 u(y)]=3v_L Cov(u(x),u(y)) proves cubic score minus 3v_L times identity-linear score is orthogonal to every admissible deterministic linear nuisance via Ito isometry, while 3v_L times identity is itself in that nuisance span. Wick-cubic variance E[(u^3-3vu)^2]=6v^3 yields J_L=6v^3/sigma^2 for any positive finite T. At fixed L, resonant modes j=0 (r=1) or +/-j (r=2) give v~sigma^2*r/(2La) hence coefficient 3*sigma^4*r^3/(4L^3). Off resonance finite by summability. For L->infty at fixed a, Riemann sum becomes integral with rescaling q=(a/Gamma)^(1/4) z; elementary quartic integral gives Phi(eta) with limiting eta=0 value pi/sqrt2 and eta->infty pi/eta, yielding both claimed exponents and constants. Independent high-precision quadrature matched Phi at five eta values; it does not replace limits.

## originality

PASS

Best-of-knowledge PASS for the joint exact conditional Wick-score information and three-regime volume/resonance crossover. Gaussian chaos orthogonality, covariance divergence and standard Fourier SPDE preliminaries are prior mathematics.

## value

PASS

Distinguishing fixed-volume off-resonance, discrete-mode resonance, and two thermodynamic pattern-onset exponents resolves a naturally relevant identifiability/information question in noisy pattern formation. The exact crossover quantifies an experimentally meaningful order-of-limits effect beyond standard variance-early-warning observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
