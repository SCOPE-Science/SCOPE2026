---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For fixed integer alpha>=2 and gamma>0, the equispaced periodic Korobov kernel has Fourier coefficients 1 at zero and gamma |h|^(-2alpha) elsewhere, while the sine-periodization density has m_0=1,m_odd=0,m_even_nonzero=-1/(h^2-1). Exact Fourier aliasing of G w=kappa produces discrete transform W(r)=sum_{h≡r}a_h m_h/sum_{h≡r}a_h, and zero-mode W(0)=(1+gamma A_N)/(1+gamma B_N). Bounds on alias tails (a_h=O(|h|^-2alpha)) and density Fourier coefficients O(|h|^-2) give uniformly w_j=mu(j/N)/N+O(N^-2), hence negative total mass O(N^-2). Expanding B_N=2 zeta(2alpha)N^-2alpha and A_N=O(N^-2alpha-2) proves N^(2alpha)(1-sum w)->2gamma zeta(2alpha). For each fixed even N, the large-gamma limit at the endpoint is strictly negative by the even-h alias sign. Independent Fourier-alias computations across alpha=2,3, gamma=0.25,3 and N=8..128 verify the scaling, and alpha=2,3 on even N=4,6,8 at gamma=10^7 confirm endpoint negativity. High-precision mass defects at large alpha and N are cancellation-sensitive; the analytic expansion is the proof.

## originality

PASS

Original and motivated high-order (alpha>=2) one-dimensional asymptotic sign-stability result, distinct from the already solved first-order sharp threshold and distinct from the still-open multivariate positivity question.

## value

PASS

Negative quadrature weights affect noise amplification and stability even for a nonnegative target density. The higher-smoothness regime is the natural unresolved extension of a widely used periodized lattice method; proving O(N^-2) *total negative mass* with exact nonunit-mass defect and finite-grid negative endpoint exhibits a genuine stability boundary. This is not just routine consistency or parameter renaming, and does not falsely assert per-weight positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
