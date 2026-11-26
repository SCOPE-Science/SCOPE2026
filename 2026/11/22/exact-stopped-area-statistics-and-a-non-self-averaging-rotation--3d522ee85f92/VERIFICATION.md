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

The predictable orthonormal radial/tangential Brownian projections have identity bracket and are independent Brownian coordinates. The squared-radius SDE has a pathwise unique nonnegative solution driven by the radial coordinate alone, including at s=0, so the exit and Q are radial. Integrating the tangential projection gives A|Q normal with mean omega Q/2 and variance DQ/2. Its conditional transform gives q=t+Dk^2/4-i omega k/2. The regular solution to D(F''+F'/r)=q r^2 F, F(R)=1, gives the ratio of I_0 values; uniqueness and nonvanishing normalization for Re(q)>=0 follow from the weighted energy identity for a homogeneous zero-boundary solution, and q=0 gives 1. Poisson equations using the radial Laplacian of r^m equal to m^2 r^(m-2) give E Q=(R^4-s^4)/(16D) and Var Q=(R^8-s^8)/(512D^2). The area-only variance is 2D/E Q + omega^2 Var Q/(E Q)^2. Stopped Girsanov gives log likelihood omega A/D-omega^2 Q/(4D): use finite-time localization and pass on the events of disk exit before the cutoff, whose probabilities tend to one under both drifts. The two sufficient statistics retain the full-path score and information E Q/(2D), yielding the claimed multiplier. As R tends to infinity with fixed s,D, the Laplace transform of DQ/R^4 converges to the unit-disk transform at s=0, D=1. That exposure is strictly positive and nondegenerate. Thus the area estimate has limiting variance omega^2/2, and the exposure-normalized estimate's conditional variance 2D/Q tends to zero in probability, giving consistency without a finite-sample efficiency claim.

## originality

PASS

The distinct result is the evaluated joint stopped area–occupation law for rigid rotation together with the exact information and estimator contrast. The radial I_0 ratio itself is a classical Bessel first-hit transform in a different clock, not a new passage-time identity. Prior expected-signature calculations include drift-free area moments on the disk. The inspected statements do not already give the rotating-disk joint law with the observed physical radial exposure or the exact specified estimator loss and recovery under that stopping rule.

## value

PASS

For the natural sampling rule of following one rotating diffusive trajectory until it leaves the field of view, increasing the radius supplies more expected information but leaves this simple area-only estimate with order-one fluctuations. The exact risk identifies their cause as random exposure, and recording just one additional integral retains the full likelihood and permits a consistent estimate. This distinction is not contained in a Bessel passage law or a fixed-time stochastic-area law alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
