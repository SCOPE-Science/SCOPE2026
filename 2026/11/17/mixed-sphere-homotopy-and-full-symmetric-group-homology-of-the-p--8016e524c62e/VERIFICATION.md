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

# Verification instructions and scope

Run `python3 verify.py` in a directory containing the file. It requires only Python 3 standard library and no external input. Recompute from the lexicographically enumerated graph representation and all 331 matching faces.

The program checks the complete 160-pair oriented Hasse acyclicity and enumerates the 11 critical faces. A recursive signed integral gradient path reduction computes the exact Morse 3-to-2 boundary (zero). The homotopy wedge follows from the standard 2-sphere wedge attaching map classification, not from a mod-prime rank alone.

For the symmetry calculation it reconstructs all 120 S5 actions, chain traces, and an invariant rank-79 boundary image. It computes the trace of each transformation on this image using two independent prime fields (1009 and 1013), recovers unique integer traces using the finite-order rank bound, verifies Specht and signed-permutation characters and the quotient subgroup averages.

Observed run: see `verification_output.txt`; the final marker is `PETERSEN_MATCHING_MIXED_WEDGE_CHARACTER_PASS`. The finite exhaustive computation and mathematical homotopy deductions together prove the stated result. Numerical enumeration without the verified exhaustive predicates would not establish an infinite-family theorem; none is claimed.

Limits: no independent mathematical audit; no equivariant homotopy inverse established; quotient statements are rational and do not determine integral torsion.
