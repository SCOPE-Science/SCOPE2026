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

# Exact reconstruction and checks

Execute `python3 verify.py` from a directory containing that file. It requires only the Python standard library. It creates the digraphs directly from the eleven residues, independently enumerates all nonempty subsets of each out-neighborhood, then verifies full-dimensional face counts, complete absolute Morse matching acyclicity by a directed Hasse-graph traversal, relative free-face pairing legality, and independent mod-two simplicial boundary ranks.

Successful execution yields precisely three absolute checks (242, 231 and 252 nonempty faces), three acyclic Morse pair totals (110, 106, 117), relative pair totals (4, 10), and the final `PASS: all 55 arcs, three absolute Morse models, and two relative collapse certificates` marker. There is no reliance on saved execution logs or external files.

The homotopy conclusion uses the discrete Morse theorem and the fact that a CW complex with one vertex and only two-dimensional cells is a wedge of two-spheres. The relative checks establish actual elementary collapses of the relative quotient complexes; the long exact sequence supplies the integral primitive maps. Mod-two rank calculations are secondary checks, not substitutes for the integral argument. The calculation is exhaustive for the specified finite graph and does not generalize without proof to larger orders or multiple arc faults.
