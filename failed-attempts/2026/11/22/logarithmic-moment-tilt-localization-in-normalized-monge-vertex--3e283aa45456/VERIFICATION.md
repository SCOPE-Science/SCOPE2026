---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Erickson–Kretschmann Proposition 5.1 gives all distinct normalized corner rectangles and row/column strips for this sign convention. There are 2(n-1)^2 corners and 2n strips, also at n=2. On their supports the entries are constant, so squared norms are 1/(ab) and 1/n. Counting gives the exact Mellin formula and strip probability n^(1-s)/[(H_(n-1)^(s))^2+n^(1-s)]. Conditionally on a corner the two orientations are equiprobable and both side lengths have the independent truncated weights a^(-s). Integral comparison for partial sums proves the Beta and log-uniform limits; above s=1 the omitted zeta tail is exactly the one-coordinate total variation error. In the moving window, a partial sum to min(n-1,floor(n^t)) equals log(n) times the integral of exp(-lambda*u) on [0,t], up to bounded error, by monotone sum/integral comparison. The strip numerator is exp(-lambda), negligible compared with log(n)^2. Independence yields the joint limit. In the untilted case the inverse product of the two rescaled lengths converges in distribution to 1/(UV) because the axes are limit-null; strip probability tends to zero even though the strip variable itself is large. Integration over UV<1/z gives (1+log z)/z. Substitution of the three harmonic-sum orders into the exact formula yields all moment constants; the strip term is negligible in each. Collision conditioning is with respect to the initially uniform distinct vertex law. Read VERIFY.py and VERIFICATION.md; the finite checks of the proposed vertex list do not establish completeness, which comes from the published proposition. No execution of the submitted script is claimed.

## originality

FAIL

The prior complete uniform-vertex support list mechanically yields the full norm law and exact tilt factorization. The purported distinctive moving-window law is the same triangular Zipf log-coordinate limit already proved by the logarithmic Riemann sum in the earlier renewal record. Independence here is exact at finite n by the same rectangular enumeration; passing to two copies, dropping a negligible strip weight and transforming the untilted limit by an inverse product do not establish a materially distinct result beyond these deductions. This does not allege that a prior paper literally printed the full combined Monge statement, and does not rely on any inaccessible source.

## value

FAIL

The collision observable is natural and the assembled formulas can be useful as exposition, but its complete exact law is a direct weighted count of the known vertex types. With the exact product factorization, the three regimes and moving window transfer known one-variable Zipf normalization facts, and the heavy tail is the standard product of two uniforms under inversion. The record does not establish a distinct mathematical gap beyond those mechanically available consequences; neither a broader unsolved geometric regime nor a nontrivial new exact invariant is resolved. No repaired claim is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
