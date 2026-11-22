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

# Finite exact verification

The supplied `verify_state_dp.py` and `verify_orbit_dp.py` use only Python 3's standard library. Run each separately from the same directory as this file.

The first program builds the Petersen graph using its five outer-cycle edges, five inner step-two-cycle edges, and five spokes; it enumerates every one of the \(1024\) masks, computes all allowed majority flips and recursively evaluates exact absorption probabilities using `fractions.Fraction`. It checks all \(14\) absorbing masks, every flip's strict cut decrease, the full eleven Bernstein coefficients and the final rational probability.

The second program constructs the Petersen graph independently as the Kneser graph \(KG(5,2)\). It enumerates all \(120\) permutations on the five base points, joins the global spin complement, verifies that the resulting \(18\) orbits partition all \(1024\) masks, and checks transition-count equivariance for every orbit member. It solves the downward orbit recurrences exactly and matches the full coefficient vector, as recorded in `orbit_table.csv`. It also verifies that the twelve mixed absorbers form a single \(S_5\)-orbit.

Both programs check the closed-form polynomial at eleven distinct rational values of the initial density; both sides have degree at most ten, so agreement establishes the polynomial identity. Both programs passed when executed on their supplied source files. The computations certify this finite state space only. They do not establish a general-graph theorem, external historical priority, or independent scientific audit.
