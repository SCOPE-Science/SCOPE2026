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

The specified unit-clock zero-temperature flips are equivalent to copying a uniformly chosen neighbor. Before coalescence two backward lineages have relative jumps at rate one in each direction; global resetting kills the relative walk at rate r with reward (-1)^n, while coalescence at 0 or N has reward 1. This gives the stated recurrence with no extra factor of two. Poisson renewal gives stationarity and first-reset coupling gives uniqueness; fair phase makes the one-spin means zero. The alternating particular solution and the bounded or two-boundary homogeneous solution give the exact kernels. The cosh ratio is strictly decreasing in r, and in n up to the midpoint; for fixed n the finite-image correction is positive and strictly decreases to zero with N. Bracketing the roots at the infinite root and any larger rate proves strict finite-size nesting and convergence. The odd infinite-chain equation gives u^m(u-1)=2. With t=kappa/2 and y=nt it yields y+log y=log n+o(1); since the derivative of y+log y is at least one, y-W(n)=o(1). This verifies the asymptotic and the fixed-rate sign-front scale. Fourier transformation of the normalized geometric periodization and (-1)^n gives the exact diffuse and Bragg terms.

## originality

PASS

Credit the classical pair closure, renewal formula and exponential/periodized Green kernel as known or directly inherited. The supported distinction is the Néel-specific sign classification: finite-size and separation nesting, algebraic odd-root thresholds, and logarithmically enhanced front, with the associated staggered response. The strongest same-day record explicitly has the same kernel but an iid reset source, hence no staggered term or sign hierarchy. No inspected result gives or directly contains the full hierarchy and asymptotics.

## value

PASS

The alternating reset ensemble directly competes with local ferromagnetic coarsening. The exact nested odd-distance crossover identifies which pair observables change sign and how the ring modifies their crossing rates. Its weak-reset front grows by a logarithmic factor beyond the exponential decay length, and its staggered plateau yields a distinct Bragg contribution. These are informative distinctions beyond evaluating a standard renewal integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
