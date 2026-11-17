---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For each target A in {left,right,either}, first-reset renewal from y to fixed z gives F_A(y;z)=(1-phi_A(y))/(r phi_A(z)). Independent Neumann/Dirichlet ODEs yield the three phi functions; max(tau_0,tau_L)=tau_0+tau_L-min(tau_0,tau_L) is a pathwise identity even with retained visit flags. With y=L/2 and u=cosh(s(z/L-1/2)), algebra gives H_c(u)=2c(2c^2-1-c)u/(u^2+c^2-1)-(c-1)/u, 1<=u<=c. An independently performed exact SymPy derivative check verifies N_c(u²) and endpoint factorization (c-1)^2(4c³-6c-3)/(c(2c²-1)). The derivative numerator has one positive zero (interior maximum), so endpoints alone compete; critical root c=1.42366105 corresponds rL²/D=3.1738039310. All boundary reset hits count immediately.

## originality

PASS

Best-of-knowledge original fixed-midpoint-start, freely optimized reset-site phase transition. Closest exact prior global optimizer theorems set initial site equal to reset site and have a different critical quadratic and threshold, while Linn–Lawley derives equal-site interval cover times and Ghosh–Sabhapandit fixes the midpoint site while varying rate. The submitted cubic arises in the distinct independent-initial-site problem; no direct prior theorem was found in inspected material.

## value

PASS

The choice of reset site after a fixed initial position is a natural independent control for search design. The proof gives a sharp global continuum classification with only endpoints or midpoint optimal, an explicit algebraic transition and exclusion of all interior competitors; importing the old y=z threshold would lead to an incorrect location policy. Exact all-rate boundary is a reusable physical design invariant rather than a numerical anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
