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

# Reproducibility and claim boundaries

Run `python3 CHECK_DOM_Q4.py` from the extracted package and compare its complete stdout with `CHECK_OUTPUT.txt`. Python 3 standard library is the only dependency. The checker regenerates all vertex masks and faces from a four-bit Hamming graph, validates two equivalent face criteria and a third explicit dominating-cover test, computes the face and facet vectors, constructs and audits two independent greedy pivot-order Morse matchings, checks every oriented codimension-one incidence by full Kahn topological sorting, verifies Euler characteristic and minimum domination number, and computes the critical-cell homology pattern. Its final expected line is `FOUR_CUBE_DOMINANCE_EXHAUSTIVE_CHECK_PASS`.

No external program, downloaded certificate, or prior-run artifact is required. The checks are exhaustive over the finite four-cube; they are not an infinite-family proof. The computation does not test the unstable homotopy attaching map of the nine-cell, and no complete sphere-wedge homotopy decomposition is claimed. Independent mathematical audit has not been performed.
