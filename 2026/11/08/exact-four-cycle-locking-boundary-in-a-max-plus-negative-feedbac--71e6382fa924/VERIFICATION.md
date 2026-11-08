---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and scope

Run `python3 check_exact_phase.py` with Python 3.9+; no nonstandard package is required. The checker enumerates all \(3^4=81\) affine mode words for a four-periodic scalar orbit, performs exact rational Gaussian elimination on each nonsingular word, and intersects parameter inequalities symbolically. The sole singular word `DDDD` is excluded analytically by its inconsistent cyclic sum for \(t>1\). All feasible words and their full parameter intervals are compared with the printed certificate in `RESULT.md`. The checker additionally verifies physical iterates at exact rational representative parameters and both strict-region return Jacobians.

The universal reduction from an arbitrary real planar period-four orbit to a bounded scalar recurrence is established in the proof in `RESULT.md`, not by finite computation. The exhaustive algebraic branch enumeration is finite and exact; it applies to all real \(t\in(3/2,2)\). No numerical optimization, Monte Carlo simulation, timeout-based exclusion, or unproved computer algebra assertion is used.

Scope limits: period four only; the boundary orbit is nonsmooth and has no claimed classical linearization there. Literature priority is assessed against accessible primary texts and index results, with the inaccessible 2015 precursor retained as a risk. Independent validation has not been performed.
