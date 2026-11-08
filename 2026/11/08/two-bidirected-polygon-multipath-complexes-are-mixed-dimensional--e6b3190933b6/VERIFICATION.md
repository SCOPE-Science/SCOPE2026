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

The reproducible proof certificate is `verify.py`, executable with `python3 verify.py` and no third-party packages. `verification_output.txt` contains the captured output of an actual successful run.

For the five-vertex cycle, direct enumeration gives 80 faces, 190 Hasse incidences, 38 matched pairs, and critical-cell counts one in dimension zero, one in dimension two and two in dimension three. Exact rational boundary ranks in dimensions two and three are 21 and 8.

For the six-vertex cycle, direct enumeration gives 196 faces, 576 Hasse incidences, 96 matched pairs, and critical-cell counts one in dimension zero, one in dimension two and two in dimension four. Integral computations verify the 8-term two-cocycle on all 48 tetrahedra, the embedded octahedral cycle with pairing 1, and a zero Alexander–Whitney cochain square on all 12 four-simplices.

Acyclicity is proved by checking that topological sorting visits every node of each explicitly reconstructed reversed-incidence graph. This is exhaustive for the specified two finite graphs. Homotopy conclusions additionally use the discrete-Morse CW theorem and the classical Hopf invariant description of maps from the three-sphere to the two-sphere. The package does not certify the result independently and does not address all polygon lengths.
