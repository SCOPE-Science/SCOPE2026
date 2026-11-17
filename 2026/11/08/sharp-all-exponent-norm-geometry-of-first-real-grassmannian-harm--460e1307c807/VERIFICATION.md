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

Identified oriented Gr(2,4) with S^2 x S^2 using self/anti-self dual Plucker coordinates, with unoriented quotient harmless to bilinear observables. The rank-two projector trace f_A becomes U^T diag(m_1,m_2,m_3)V and sum m_i^2=tr(A^2). Conditioning on U gives E|f_A|^p=(p+1)^(-1) E(sum q_i U_i^2)^(p/2); the nondegenerate Dirichlet support makes this strictly Schur-concave for 1<=p<2 and strictly Schur-convex for p>2. Thus simplex vertex and barycentre are unique opposite extrema, yielding pair and outlier spectra, all p>=1 and infinity. E f^2=tr(A^2)/9. Independently computed exact rational even moments m=1..4 for four trace-zero spectra, including the quartic identity 4/75[(tr A^2)^2-tr A^4]. This is finite corroboration, not a substitute for strict Jensen.

## originality

PASS

The prior real-Grassmannian fourth-moment result covers part of the p=4 statement (its even-n>=6 classification, with n=4 moment formulas separately described), and Ehler-Graf supply the first-harmonic decomposition. Neither inspected primary harmonic-space paper nor the published fourth-moment result proves noninteger-p sharp envelopes, p=1 boundary, infinity extrema, and strict all-p equality classes. The full all-exponent theorem survives best-of-knowledge comparison; the known quartic corollary must not be described as new.

## value

PASS

The sharp Banach-space norm geometry of the entire nine-dimensional natural first-harmonic space, including strict phase reversal at p=2 and classification of equality spectra for all real p, is a motivated structural result that goes beyond repeating the known quartic moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
