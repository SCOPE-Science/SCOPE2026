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

The displayed normalized H is conserved; each coordinate potential is quadratic at zero, strictly increases outward and diverges at the boundary. Thus every E>0 gives one regular compact closed orbit in the open square, and one circuit is the minimal period. In each quadrant dF_p/dt=-xy in original time, so each clock is the convolution of the two inverse radii's reciprocals. Subtracting 1 from each factor gives baseline E, the two integrated defects and a residual convolution. The defect f_z is decreasing and bounded by f_(-1), which is O(u^(-1/2)) at zero and O(1/u) at infinity. Splitting at E/2 gives an O(log E/E) residual uniformly in all branch parameters. The truncated defect is the elementary integral of 1/[(1+r)(1+zr)] to the inverse radius: its noncritical limit is J(z), with J(1)=1/2. On the critical side the potential gives inverse distance (2E)^(-1)(1+o(1)), so artanh of the radius is (log E)/2+log 2+o(1). Each side occurs twice, giving exactly one log E per critical coefficient and the stated constants. For the moving wall, put epsilon=kappa/E and evaluate the singular potential at edge distance y/E. After division by E and the change v=E(1-r), the integrand on [y,E] tends to 1/[2v(v+kappa)]; for bounded kappa and E large it is bounded by a constant times v^(-2). Convergence of the integral is uniform for kappa in [0,K] and y in any compact subset of (0,infinity), by uniform convergence on finite v intervals and the uniform integrable tail. The strictly decreasing limiting integral equals 1 at y=kappa/expm1(2kappa), continuously 1/2 at zero. It uniformly brackets that level at suitable fixed positive small and large y, and its slope is uniformly bounded away from zero in that bracket, proving uniform inversion, not just multiplication by epsilon at kappa=0. Substitution into the exact defect gives 2L=log E+log[2(1-exp(-2kappa))/kappa]+o(1), with log 4 at zero, and the regular branch tends to 1/2. Reflection with time reversal preserves period. The argument is for one moving wall, other coefficient fixed interior, and compact kappa ranges. Inspected VERIFICATION.md and verify_period_wall.py; their finite checks are recorded, not needed for the proof or independently rerun.

## originality

PASS

The interior m=0 law and exact clock are covered. The supported distinct result is the degenerate fixed-wall physical-time asymptotic, including the constant, and the compact-uniform one-wall crossover; priority is qualified to inspected material.

## value

PASS

At a natural geometric degeneracy the leading period stays 4E while its offset becomes logarithmic with exact multiplicity. The explicit, nonconstant kappa-scale law supplies the missing uniform regime where the prior strict-interior formula is quantitatively wrong. These are physical-time predictions for the original center, not a coordinate renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
