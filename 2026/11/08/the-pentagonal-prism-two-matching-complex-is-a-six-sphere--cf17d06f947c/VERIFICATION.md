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

# Reproduction and limits
Run `python verify.py` from the extracted package. This standard-library program constructs the graph, performs two logically independent degree/forbidden-star face enumerations, counts all 10,895 faces (including the empty one), checks the f-vector and facets, pairs all face incidences, checks disjointness and critical-cell dimensions, builds all 64,005 oriented Hasse incidences and verifies the directed graph has no cycles by visiting all 10,894 nonempty simplices. The complete ordinary matching has 5,446 pairs, one critical vertex and one critical six-cell, so the discrete-Morse CW complex has exactly those cells and is homotopy equivalent to a six-sphere.

`verification_output.txt` records the output from an executed verifier; the proof depends on the reconstructible checker, not a log alone. The scope is only the stated finite graph, and no external independent review has been performed.
