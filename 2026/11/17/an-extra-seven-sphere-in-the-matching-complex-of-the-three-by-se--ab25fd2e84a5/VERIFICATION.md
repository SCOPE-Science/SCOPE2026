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

Reproduce the finite calculation by running `python3 proof/verify_cylinder.py` with Python 3.10+ in the enclosing research directory. No external packages are required. The program generates all faces, computes two distinct acyclic matchings, checks each of the 2,303,210 face-cover orientations by a complete topological sort, derives signed Morse boundary matrices recursively, and verifies integral unit pivots with no remaining coefficients. The first matrix is separately included and compared entry-by-entry at `proof/morse_boundary_A_42x99.csv`; expected successful stdout is in `proof/verification_output.txt`.

The checks establish the finite combinatorial and integer-matrix premises. The homotopy conclusion additionally uses standard discrete Morse theory, Hurewicz in the first nonzero degree and elementary CW cancellations. A complete homotopy classification for arbitrary cycle lengths is not claimed. No independent audit has occurred.
