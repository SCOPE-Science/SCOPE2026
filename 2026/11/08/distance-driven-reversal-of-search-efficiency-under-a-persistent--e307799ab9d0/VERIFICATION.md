---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Set B=diag(r+delta,r-delta)-Q, E=exp(-L sqrt(B/D)), F=B^{-1}(I-E). The first-excursion survival integral is F, and the phase-preserving reset kernel is F Lambda. Strong Markov at reset gives (I-F Lambda)m=F 1, equivalently m=(h_L(B)-Q)^(-1)1; this does not falsely reinitialize the environmental phase. The symmetric/antisymmetric 2x2 spectral projector has eigenvalues r+nu±sqrt(nu²+delta²) and weights c,1-c, giving the stated mean. As L downarrow0, Jensen for b^(-1/2) and barycenter r forces a positive difference from constant rate; as L increases, b_-<r gives exponential ratio zero. Numerical independent matrix-renewal reconstruction agreed with scalar formula at 15 test parameter-distance combinations to 1e-7 relative (ill-conditioned at L=10 with large mean); e.g D=r=nu=1,delta=.5: at L=.02 0.0209616>0.0202013, L=8 2190.9232<2979.9580. No claim of unique crossing.

## originality

PASS

Arutkin–Reuveni 2025 studies a phase-fluctuating reset intensity and its stationary spatial law, but its accessible model-level abstract does not supply this phase-retaining target first-passage comparison. A 2026 square-root telegraph result studies zero-versus-positive hazard (boundary delta=r), and optimizes over nu rather than proving near/far comparison at every strictly positive pair of rates. The new two-target-distance universal sign reversal is a nontrivial FPT outcome.

## value

PASS

An explicit exact FPT for correlated nonrenewal search and a parameter-uniform sign reversal is a motivated substantive distinction between reset-rate variability and a constant mean-rate policy. The near/far contrast and far-field exponential ratio are scientifically useful without any uniqueness theorem for intermediate crossings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
