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

# Reproducibility of exact finite checks

Run `python3 verify_dual.py` and `python3 verify_exhaustive.py` on the attached, unchanged source files. Both use only the Python standard library. They must each exit successfully and print `PASS` lines.

`verify_dual.py` embeds the dodecahedral edge/face incidences, verifies that all thirty edges bound precisely two of twelve pentagons, constructs the dual graph, and recursively enumerates every perfect matching of its twelve vertices. It checks exactly 125 matchings, 250 distinct spin lifts, the complete magnetization histogram, and all twenty-by-twenty spin correlation entries. This is exhaustive finite combinatorics, not a random experiment.

`verify_exhaustive.py` starts instead with the primal edge list and traverses every one of the \(2^{20}\) possible spin configurations. It tests the minimum number of frustrated bonds and the ground state count, then obtains the integer characteristic polynomial of the 20-by-20 correlation numerator matrix from exact traces and Newton's identities. Its factored target polynomial can be multiplied and checked directly from the source.

The physical limiting response identity is mathematical and is not estimated by code: \(\chi(\beta)/\beta\to C\) follows from differentiating a finite partition function at zero field and isolating its ground states. The checkers do not validate novelty, finite-temperature behavior, or effects of additional interactions.
