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

With y=ell+1 the Peter–Weyl scalar has the sign of a_y+b(a_{y-1}+a_{y+1}); division by the irrep dimension does not change the sign. The neighbor-ratio tail is 2+12/y^2+O(y^-4), so the maximum is attained and exceeds 2. An independent exact symbolic check recovered both the x-derivative (the prime in Step 2 is partial_x at fixed q) and the polynomial for the adjacent difference. R_2>R_1; for q<=0 the displayed polynomial is positive on x>=2, while for q>0 it has a unique sign change in x>1 by its u-derivative and its value at u=1. Strict continuous unimodality precludes nonadjacent or triple maximizing ties. Descartes plus the endpoint signs gives a unique positive adjacent crossing; unimodality at a tie orders the next crossing strictly later. The crossings cannot accumulate at a finite q, since at any q beyond that bound all integer ratios from index 2 would then strictly increase, contrary to their tail. Scaling u=qt locates the continuous turning point at u/q tending to 3; the discrete maximum is one of its two integer neighbors. In this range the central second difference of a divided by a equals a''/a+O(q^-2)=12(x^2-q)/(x^2+q)^2+O(q^-2), giving the sharp large-mass formula. At a PSD threshold the finitely many missing blocks can only support a measure with a finite Fourier polynomial density; a nonzero finite atomic measure cannot have such a density. For uniform density, a missing matrix block annihilates the RKHS by a Haar-functional, whereas positive weights everywhere include all matrix coefficients. The supplied checker was inspected, not executed. Separate bisection on the exact-ratio expression at y=2,3 corroborated the given approximate roots.

## originality

PASS

Positive type and universality reductions are standard, and an every-mode staircase is already known on the same S^3 geometry for different radial weights and a different character mask. The exact unsuppressed staircase, transition polynomials and large-mass sharp boundary for the squared-resolvent weights do not follow from the inspected statements. Priority is assessed on that distinct content rather than on the existence of spectral switching in general.

## value

PASS

The sharp one-parameter admissibility boundary is useful for a natural signed perturbation of a standard covariance. Which irreducible block goes singular is nontrivial and changes without skipping through an unbounded set of modes; the large-mass formula quantifies the loss of admissibility. The strict-positive-definiteness versus universality distinction describes what remains usable exactly at the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
