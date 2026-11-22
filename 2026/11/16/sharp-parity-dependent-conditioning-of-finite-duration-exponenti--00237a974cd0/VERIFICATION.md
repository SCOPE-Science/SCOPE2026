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

The unitary Zak transform diagonalizes the critical integer-lattice Gabor frame operator as |Zg|^2, with Zg=e^-lambda*x S_m(r exp(-2pi i xi)), r=e^-lambda. It never vanishes for r<1. The maximum occurs at zero frequency. For even m, reverse-triangle numerator and ordinary-triangle denominator bounds are simultaneously sharp only at pi, yielding A=e^-2lambda((1-r^m)/(1+r))^2 and duration-independent condition number e^2lambda((1+r)/(1-r))^2. For m=3 the exact quadratic in cos(theta) has its vertex inside [-1,1] iff r>=2-sqrt(3), giving the claimed two branches and symmetry-broken minimum. At fixed m, expansion near the simple mth-root zeros of S_m shows minimum ~m^2 lambda^2/[4 max_k sin^2(pi*k/m)]; the global uniform-away-from-roots lower bound and local phase minimization establish the 4/even and 4cos^2(pi/2m)/odd weak-damping limits. At lambda=0 there is no positive essential lower frame bound.

## originality

PASS

Critical Zak diagonalization and polynomial zeros are classical. Available Pont et al characterization treats continuous integrable totally positive windows and qualitative frame-set regions; this finite abrupt cutoff has a jump and is at critical lattice. Kloos–Stöckler exponential B-splines are convolutions/oversampled regimes, not the single truncated exponential polynomial. Earlier Resultary jumped two-sided exponential has different support/window; no inspected source implies duration independence for all even m plus the m=3 interior transition and fixed-duration damping coefficients. Best-of-knowledge PASS with recorded risks; no failure-to-find-is-proof-of-novelty inference.

## value

PASS

This explicitly quantifies conditioning of a natural fixed-band critically sampled time-frequency basis, with a robust parity law and nontrivial min-Zak frequency bifurcation and sharp weak-damping coefficients. It is materially more than a generic frame-existence test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
