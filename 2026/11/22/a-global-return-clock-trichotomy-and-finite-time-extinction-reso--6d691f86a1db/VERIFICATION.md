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

For the prospective linear right orbit with x0>0, write x_j=C rho^j sin(phi+j theta), 0<phi<pi, using the distinct roots rho exp(±i theta). The first crossing of pi happens by ceil(pi/theta), cannot skip the nonpositive half-cycle, and has y_j=-d x_(j-1)<0 including x_j=0. A left iterate lands on the horizontal axis and a negative landing is made positive by the next iterate. For (u,0), the phase is theta and the recurrence gives x_j=u rho^j sin((j+1)theta)/sin(theta); at j=k-1 this gives exactly (-Au,-Bu). Hence the next landing has sign of bA-B; a negative landing adds exactly one step and multiplies its magnitude by b. All intervening right iterates have negative second coordinate, so the positive-ray return is primitive at M=1. At k theta=pi, A=0 but B>0, hence there is no cancellation at any b>0; otherwise b=B/A is the only cancellation and k+2+k bounds full-plane extinction. For 0<M<1 the rate sigma=M^(1/h) works up to a fixed multiplicative constant, by bounded reset time, bounded operator norms on the finite prefix and the finitely many ray phases. The same nonzero ray phases give norm divergence for M>1 unless the orbit reaches zero. Exact examples: (r,d)=(1,3) gives (u,0)→(u,-3u)→(-2u,-3u); neutral gains are 1/2,1,2. The exact-angle test (r,d)=(2,2) gives (0,-4u) at step 3, then (-4u,0), then (4bu,0). Supporting checker read as finite regression only, not executed. The proof gives a sufficient, not claimed sharp, uniform extinction exponent, and does not establish stability under forcing or nonlinear perturbations.

## originality

PASS

Best of inspected evidence, for the exact homogeneous mixed-sign family only. The right-branch sine coefficients and rank-one return mechanism are prior ingredients; the contribution is the exact admissible positive-ray clock with the second left reset, its angular obstruction to nilpotence, and the all-orbit conclusion, not a new matrix power formula or a new general theory of first returns.

## value

PASS

The unforced switching fixed point is a natural outstanding slice of the originating normal form. The exact return not only tests stability but identifies which periodic clocks can occur, and an extinction resonance which depends on whether the right focus reaches the switching line exactly. The r=1,d=3 example shows how exponential attraction, escape and finite annihilation can occur in one fixed pair of branch entries. These outcomes cannot be read from separate branch eigenvalue stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
