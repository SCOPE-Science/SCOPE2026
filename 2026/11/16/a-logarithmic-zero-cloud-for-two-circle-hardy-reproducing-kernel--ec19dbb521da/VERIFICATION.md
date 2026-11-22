---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Monomial orthogonality gives norms (1+a^(n-N))/(1+a^-N) and correct unnormalized kernel. Positive coefficients c_n=(1+a^(n-N))^-1 have successive ratios c_{n-1}/c_n strictly increasing with minimum R_N=(a^N+a)/(a^N+1)>a. Enestrom-Kakeya on each finite Taylor polynomial excludes |s|<R_N; local uniform limit and Hurwitz transfer zero exclusion. In annulus a<|s|<1, H_N=s^-N F_N=sum_{j>=-N}s^j/(1+a^j) converges normally with derivatives to bilateral G_a. The classical Ramanujan 1psi1 product has numerator/denominator factors zero-free in that annulus, and net winding zero around a<|s|=r<1: each 1+c*s factor has zeros outside; each 1+c/s factor has one zero and one pole inside. Argument principle on F_N=s^N H_N then gives exactly N zeros inside each fixed circle. A second inner circle arbitrarily close to a and zero exclusion below R_N give radial collapse. For k>=1, sum of kth powers of N zeros equals contour integral s^k H_N'/H_N, which is uniformly O(1); divide by N and use radii -> a>0, plus conjugate negative moments, to prove Haar angular limit. Finite winding numerics are supporting only.

## originality

PASS

The bilateral q-product and zero exclusion machinery is classical. This claim concerns the one-sided N-dependent two-circle Hardy kernel, not the annular Laurent Szego kernel or step-area Bergman kernel. Crucial prior related Bergman theorem has m-1 bulk zeros for derivative-related series, but does not imply the count for the primitive F_N.

## value

PASS

The scalar zeros of a natural reproducing kernel are a substantive invariant. The example produces an exact unbounded logarithmic bulk zero count and limiting angular law while the Hilbert space as a set remains H2, identifying a concrete geometry-of-norm rather than set-of-functions effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
