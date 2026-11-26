---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In open-interval BV, f modulo constants is the Bochner integral of h_t=1_(t,1) against df; t maps continuously to h_t in L2 and the measure is finite. Projecting the integral gives the upper bound by the largest single-jump residual, and an atom realizes it. Differentiating the finite Parseval expression for E_n(t) gives -t plus the telescoping sum of P_j(P_{j-1}-P_{j+1}), hence E_n'=-P_n P_{n+1} also at n=0. The proposed closed form has that derivative by the two consecutive Legendre derivative identities and vanishes at t=1. Interlacing and the sign at 1 make exactly the P_{n+1} zeros the interior maxima. For g=P_{n+1}, put W=(1-x^2)g'; then W'=-lambda g, so the derivative of W^2+lambda(1-x^2)g^2 is -2lambda xg^2. Integrating between any two nonnegative distinct zeros, including 0 when applicable, strictly orders the critical values because W(z)=(n+1)P_n(z). Evenness and zero endpoint values finish the maximization. For equality, the derivative measure must be supported on maximizing nodes and its signed residuals must agree in direction by equality in Hilbert-space integration; distinct jumps cannot give collinear residuals because their linear combination cannot be a polynomial unless both coefficients vanish. The central binomial value yields the even constant, Stirling and nested projections squeeze both parities, and the odd jump tends to zero: for even ell=n+1, w=sqrt(1-x^2)P_ell satisfies w''+[ell(ell+1)/(1-x^2)+1/(1-x^2)^2]w=0 with w'(0)=0; comparison with a cosine of frequency sqrt(ell(ell+1)+1) bounds the first positive zero by pi/(2 sqrt(ell(ell+1)+1)). At n=3 the exact square is (225+12 sqrt(30))/3430, agreeing with the stated decimal. This proof uses dx, not dx/2, and no endpoint variation.

## originality

PASS

The supported distinct claim is the exact global residual norm, parity-dependent maximizing nodes, and exhaustive BV equality, not the classical projector identities or generic single-jump reduction. The evidence does not establish historical priority.

## value

PASS

The exact worst-case projection error is a natural invariant for approximating discontinuous BV data. The optimizer shifts off the midpoint in every odd degree, in contrast to common fixed-step examples, and the strict equality classification excludes mixtures of jumps. The closed constant answers both finite-degree estimates and the leading sharp scaling rather than supplying isolated degree computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
