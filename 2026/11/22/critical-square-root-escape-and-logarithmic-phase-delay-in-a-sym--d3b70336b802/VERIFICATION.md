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

At a=-1 the phase exactly satisfies u_{n+1}=sin(u_n), while x_{n+1}=x_n+u_{n+1} and y_{n+1}=-x_n. If u_0 is a multiple of π then u_1=0 and the image lies on the fixed line. Otherwise 0<|u_1|≤1 and the sign s persists while |u_n| decreases to zero, since the only fixed magnitude of sine on [0,1] is zero. The reciprocal-square increment expands as 1/3+u_n²/15+O(u_n⁴). Averaging gives v_n/n→1/3 for v_n=u_n^{-2}; then summation gives v_n=n/3+O(log n), and inversion gives u_n²=3/n+O(log n/n²). Subtracting the increments of n/3+(log n)/5 leaves a summable O(log n/n²) series, proving a finite constant rather than just an asymptotic equivalent for the logarithm. Independently checked the local coefficients with python3 /workspace/branches/replay_3_5/expansion_checks.py; the accompanying .log records the result. For x_n, separate s sqrt(3/j) from each phase term in the exact sum. The phase errors are O(log j/j^{3/2}), with tail O(log n/sqrt(n)); the sum of j^{-1/2} minus 2sqrt(n) has a finite limit with tail O(n^{-1/2}), since the differences from the integrals over [j-1,j] are summable. This proves the asserted intercept and bound; y_n=u_n-x_n gives the opposite intercept. Divergence excludes all nonexceptional orbits from recurrence; points captured from outside the line never revisit a sufficiently small neighborhood. The map preserves any given invariant probability in the measure-theoretic sense even if not invertible; recurrence on a countable Euclidean base implies almost-everywhere point recurrence, hence concentration on the closed fixed line. Conversely the fixed line supports arbitrary invariant probabilities and only fixed points are periodic. These statements use exact real arithmetic; the archived floating-point diagnostic was inspected, not executed, and could not decide exact capture near rounded multiples of π or the infinite-time assertions.

## originality

PASS

Qualified for the combined sharp resonant planar orbit classification, including a finite planar escape intercept and summable renormalization of the phase. Credit prior scalar sine iteration: both the sqrt(3/n) leading law and the logarithmic coefficient 1/5 are explicitly in the Caldero exposition. Neither these two scalar facts nor the Taylor-expansion method is claimed as new by this review. The strongest checked scalar passage gives an o(log n) remainder, weaker than a finite renormalized limit; the checked exact planar antecedent does not give the reconstructed escape law or global classification.

## value

PASS

The vanishing denominator is intrinsic to the source's offset mechanism, not a gratuitous slice. The exact classification distinguishes all capture lines from irreversible signed subballistic drift and determines what happens to stationarity on the noncompact phase space. The finite intercept and renormalized phase distinguish this from merely observing that the scalar phase goes to zero or verifying one orbit. The ingredients are elementary, and value is attributed to this quantitative global boundary description, not to a new sine-iteration method or cryptographic implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
