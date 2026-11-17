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

# Verification details

The standalone `verify_star_fixed.py` file uses only Python's standard library. Execute `python3 verify_star_fixed.py` in the same directory. The expected output is stored in `verification_output.txt`.

The code builds the A/B occupancy-vector graph model for an unordered star configuration. Under each arm-permutation generating set, an A- or B-vertex is fixed precisely when its coordinate tuple is constant on each arm orbit; an edge is fixed precisely when its chosen arm is individually fixed. It exhaustively enumerates all fixed graph vertices and edges and calculates the connected components and their cycle ranks. Independently, it enumerates all weighted nontrivial-orbit occupancies and compares the predicted homology rank of each component against the graph count.

The output reports 245 group-and-particle instances, with 7,504 fixed vertices, 13,119 fixed edges, 510 components and 6,125 total first Betti rank accumulated across instances. The five-arm transposition at four particles gives three components and seven independent circles. This is a finite validation of formulas and boundaries, not a substitute for the arbitrary-particle topological proof or for a historical originality assessment. Full correctness also relies on the explicitly cited ordinary star configuration theorem.
