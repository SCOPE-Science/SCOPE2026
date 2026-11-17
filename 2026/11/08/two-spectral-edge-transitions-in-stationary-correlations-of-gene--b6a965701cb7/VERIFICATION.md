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

For integer m>=2, 0<a<1/m, p=ma and q=1-ma, Lebesgue-invariant center-coordinate Koopman P satisfies P h0=a h0+q h1, P h_k=p h_(k-1)+q h_(k+1) for k>=1, h_k(y)={m^k y}-1/2, with inner products <h0,h_k>=1/(12m^k). In the formal resolvent, r(z) is the zero-constant solution r=qz+pzr², and coefficient functions u_k=r^k/(1-az-pzr). Summing <h0,u_kh_k> gives the claimed Cgf=[12(1-r/m)(1-az-pzr)]^-1. A positive real pole from r=m occurs only at a<1/[m(m²+1)] and a boundary-factor pole only at a>m/(m²+1); at equality each merges with the +R square-root singularity R=(2sqrt(pq))^-1. Expanding at ±R yields n^-3/2 with explicit positive even/odd amplitudes between thresholds, n^-1/2 at either critical threshold, and the two claimed pure exponential pole regimes outside. Independent exact rational recurrence/formal power-series coefficients agree to 29 terms in the assigned checker, and a separate direct rational walk recurrence for m=2,3,4 at interior/exterior a values reproduces initial C0,C1,C2,C3. This is an analytic all-parameter proof; finite checks are diagnostic.

## originality

PASS

A stronger critical-parameter exact covariance *special case* already appeared November 1 for a=1/(2m), including its parity constants and Green–Kubo sum; therefore no novelty is attributed to any neutral-only claim. The independent contribution is the full off-neutral family 0<a<1/m, exact covariance resolvent, and **two distinct off-neutral pole-to-branch thresholds** with amplitudes, not the known n^-3/2 neutral rate. General Takahasi–Tsujii 2024 operator methods prove critical decay order but do not, in inspected statements, supply this complete all-parameter observable-specific phase diagram. Best of knowledge with residual algebraic specializations acknowledged.

## value

PASS

An explicit stationary dynamical observable has two spectral transitions a_-,a_+ that are **not** the center-Lyapunov neutrality a=1/(2m). The exact covariances and sharp pole/branch-edge amplitude laws give a nontrivial quantitative refinement of known qualitative/exponential decay and neutral critical results, useful for separating stability changes from observable-specific memory. The full off-neutral phase diagram is natural, non-implied by the inspected critical-only exact formula, and extends arbitrarily many values of m and continuum a.

The dated certificate retains the supplied scientific assessment, sources and limitations.
