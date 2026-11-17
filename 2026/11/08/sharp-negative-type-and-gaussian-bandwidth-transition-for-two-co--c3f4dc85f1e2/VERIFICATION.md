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

On full M_{m,2}(F_q), q primepower m>=2, explicit rank-one Fourier sphere transform gives R1(j)=(q^m(q^{2-j}-1)-(q²-1))/(q-1); rank-two follows total character orthogonality. For Gaussian z=e^{-t}, lambda0>0 and lambda1=(1-z)+(q^m-q)(z-z^{2^alpha})>0. Only lambda2=1-(q+1)z+q z^{2^alpha} controls PSD. Convexity yields every t>0 PSD exactly if alpha<=log2(1+1/q); above it one interior threshold z* and equality rank 1+N1, below threshold indefinite. The powered-distance CND rank-two eigenvalue -(q+1)+q2^alpha changes sign at same alpha. Endpoint projective-line indicator sum precisely distinguishes rank-one and rank-two differences, and optimal Euclidean squared-distance dimension drops from N-1 to (q+1)(q^m-1). t=0 separate rank-one constant kernel. Independently checked q=2,m=2,3 frequency counts and critical alpha, plus source code logic; these are finite corroboration of Fourier proof.

## originality

PASS

The October 26 published rank-exponential positivity-islands theorem subsumes the unpowered alpha=1 case, including t_*=ln(q) and its nullity, so that part is NOT new. It does not classify all powered rank distances alpha, their conditional-negative-type endpoint, projective-line optimal realization, or alpha-dependent nontrivial bandwidth crossing. Delsarte rank-scheme transforms and the Gadouleau–Yan MacWilliams identity provide the Fourier inputs, not this full powered phase and endpoint geometry. Best-of-knowledge PASS qualified by prior special case.

## value

PASS

Two-column rank matrices are a natural error metric in rank-metric coding and harmonic analysis. Exact negative-type snowflake threshold, complete Gaussian bandwidth phase diagram and optimal q+1 projective-evaluation embedding characterize a natural nontrivial metric family; strong previously known alpha=1 slice is separated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
