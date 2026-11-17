---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The supplied exact first-passage series F_a(beta) of Biroli et al. has positive coefficients c_k and F_a(beta)/beta² derivative sign -c1+sum_{k>=3}(k-2)c_k beta^{k-1}; positivity yields a unique global positive minimizer for each 0<=a<1. The q-Gamma ratio R(a) and its sqrt(1-a) limit, plus bounds 1-a^m<=m(1-a), dominate all rescaled entire series and their derivatives on compacts. Matching the limiting series with the OU first-passage ODE solution u''-b²x u'=-1 from x=0 to x=1 gives an exact Gaussian integral. Terms c1/b and b²/24 equicoerce minimizers away from 0,infinity; local uniform convergence plus unique limit implies convergence of global argmins. Independently evaluated the OU Gaussian-integral minimum at b≈1.280880474 and cost≈1.99986485199, consistent with stated high-precision root b*=1.280880490. Numerical decimals are approximations, not certified intervals; singular scaling is proved analytically.

## originality

PASS

The exact positive-multiplier partial-reset MFPT power series is prior work. The submitted proof supplies strict uniqueness for every a<1 and convergence of *optimized* MFPT and scaled argmin as a->1 via q-Gamma asymptotics, entire-series domination and equicoercivity, identifying an OU first-passage functional. Inspected source plots an optimum but does not give this rigorous global or joint limit theorem.

## value

PASS

Partial resetting by a small fractional contraction is a natural search protocol whose optimized rate diverges while its optimized cost remains finite. The theorem rigorously identifies the OU limit of the entire MFPT objective and optimizer, supplies universal constants and global uniqueness, and is not a routine stationary Gaussian or fixed-rate limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
