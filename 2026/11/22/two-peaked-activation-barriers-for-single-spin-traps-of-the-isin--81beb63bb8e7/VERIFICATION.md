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

Independent exact replay: `python3 /workspace/reviews/check_5.py`. Using the midpoint-coordinate graph and down-spin subsets S of its twelve vertices, the normalized energy is 24-8|S|+4e(S)-x(12-2|S|), with e(S) the induced edge count. Exhaustion of all 4096 subsets gives the strict and weak counts at x=0,2,4, nine common ground states at the endpoint envelopes x=0 and x=4, exactly 108 ground states at x=4, and all-plus above x=4. The energy gaps are affine, and equality at an interior point of [0,4] requires equality at both ends; local stability changes only at 0,2,4. The replay gives 36 and eight excited strict minima in the two open field ranges and confirms the stated energy/magnetization census and 12,24 / 8 orbits. Every first-flip cost bounds the barrier from below at both ends of each affine branch. Independently enumerating ordered triples of distinct flips gives feasible three-flip routes at both ends of every branch: 4–6 routes per lower-field trap and six per upper-field trap. Both bounds extend to the full intervals by affinity, so this does not extrapolate from sampled barrier values. The proof's 'different magnetization parity' means different parity of down-spin counts, equivalently magnetization modulo four (ordinary parity is even in both cases). With a single flip ruled out by strict stability, this gives shortest length three. The frozen program was inspected but not executed.

## originality

PASS

The one-third equilibrium plateau, the nine perfect matchings and the total of 108 cube matchings are not credited as new. The supported distinction is the excited strict-minimum classification, threshold stability census beyond the saturation matching count, and the complete minimax barrier and optimal-path profile to the ground-state set, with trap orbits. The consulted same-graph equilibrium results and general blocked-state work do not supply this dynamical extremum.

## value

PASS

On a standard frustrated spin cluster, the equilibrium ground family is fixed in the whole interval 0<x<4, yet the excited strict traps change at x=2 and the minimax escape barrier has two distinct peaks. The exact census and field-uniform optimal paths make that equilibrium–dynamics distinction testable rather than a report of a single arbitrary finite value. This is a combinatorial energy barrier, not a physical lifetime or a kinetic prefactor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
