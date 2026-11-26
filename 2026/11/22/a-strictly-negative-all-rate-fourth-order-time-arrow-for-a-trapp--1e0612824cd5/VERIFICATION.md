---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the two moment resolvents for the stationary position with heading flip rate g, not redraw rate 2g. Thermal independence can be checked separately: the arrow is a difference of fourth joint cumulants because the stationary covariance contractions are identical in the two orderings. An additive independent Gaussian process contributes zero fourth cumulant, so the calculation may set D=0. In that case put p=2g and P=z+p, L=z+k, Q=z+p+2k, R=z+3k. Eliminating the stationary moments and forward hierarchy gives the numerator over PLQR as v E[X^3 S] times (2PQ+QR−3PL−2(p+3k)(P+k)) = −4kp v E[X^3 S]; E[X^3 S]=3v^3/[k(p+k)(p+3k)]. This recovers the exact prefactor in RESULT.md lines 10–20. The inverse transform is strictly signed by integration over a simplex of positive volume for each t>0, with leading simplex volume t^3/6. Coincident rates create no exceptions; at t=0 the arrow is zero. Stationarity and global sign symmetry remove all lower-total-degree two-time antisymmetries. Replay the stationary balances and hierarchy at RESULT.md lines 31–66 with the reduction above. An independently reconstructed symbolic resolvent also verified cancellation of D. The frozen checker was inspected, not executed.

## originality

PASS

Credit the existing all-lag g=k case, arbitrary-rate local asymptotics where previously established, and the full ordered telegraph input cumulant. The supported distinction is the all-positive-rate, all-positive-lag one-dimensional ordering, with a manifestly signed convolution valid through rate coincidences. No checked stronger result establishes that ordering; priority beyond the inspected passages is not certified.

## value

PASS

Stationary covariance cannot detect the direction of time in this scalar signal. The lowest possible polynomial two-time witness works using position alone, at every positive lag and rate ratio, without observing the heading or knowing the independent thermal diffusivity. Beyond the known resonant case the result eliminates both lag-sign and switching-rate exceptions, and the positive convolution handles resonances without singular partial fractions. It makes no inference about entropy production or finite-data power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
