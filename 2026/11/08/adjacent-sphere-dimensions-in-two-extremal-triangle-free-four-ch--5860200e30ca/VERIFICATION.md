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

# Finite verification procedure

Use Python 3 with the standard library only. From this directory run `python3 verify.py`. The included `verification_output.txt` is the exact output reproduced by that command.

The checker uses a fixed, explicit edge list for each graph; exact backtracking excludes proper three-colorings and verifies a proper four-coloring. It independently enumerates admissible subsets by induced maximum degree and by forbidden triples. It also constructs sequential bitmask pivot matchings and verifies a complete topological sort of the directed Hasse diagram, considering every covering incidence. The recorded critical cells are one singleton and one positive-dimensional simplex for each example. Independently reduced mod-two simplicial boundary matrices give one nonzero reduced homology class in the claimed degree.

This is a finite exhaustive proof for the specified labeled instances, with a theoretical discrete-Morse implication to integral homotopy. The auxiliary mod-two calculations alone would not imply integral homotopy. The script does not verify novelty or generalize the claim to arbitrary triangle-free four-chromatic graphs. Independent audit has not been performed.
