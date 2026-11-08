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

# Reproducibility and scope of verification

The Python 3 standard-library program `verify.py` is self-contained. Run `python3 verify.py`, which must terminate with `ALL_CHECKS_PASS` and the deterministic output recorded in `verification_output.txt`. All thirty graph vertices and their thirty defining dodecahedral edges are reconstructed rather than loaded from an external graph database. Graph distances are computed by breadth-first search; increasing-index clique enumeration generates the complete face sets. At the two intermediate scales, the program constructs explicit matchings, verifies all matched pairs, checks the directed Hasse diagrams by exhaustive topological sorting, and computes signed integral cochains and their entire three-simplex coboundaries.

The matching orders and the exact counts are in `verification_output.txt`. The source constructs a closed orientable fifty-six-triangle surface and checks that its integral fundamental cycle evaluates to a unit in both Rips complexes. Those computations, together with the discrete Morse theorem, justify the claimed homotopy and persistence statements. Neither the verifier nor these notes provide an independent audit, an equivariant classification, a Euclidean-metric classification or a statement about other Archimedean graphs.
