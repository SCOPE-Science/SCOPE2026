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

# Exact reproducibility checks

Run `python3 verify_cuboctahedral_representation.py` with Python 3 (standard library only). The program constructs every graph vertex and edge, independently enumerates each matching cardinality, reduces the six augmented boundary maps over the two-element field, verifies all signed automorphism-induced simplicial boundary relations, evaluates all 48 Lefschetz traces, checks ten-by-ten character orthogonality, and computes every multiplicity by exact inner products.

All test assertions completed; the output is included verbatim in `verification_output.txt`. A zero mod-two Betti number forces zero rational rank, and the integral Euler characteristic yields rational rank 57 in degree three. This does not prove integral torsion-freeness; the latter is prior published work and is not needed for this representation calculation.

The orbit-space ring argument uses rational averaging after barycentric subdivision and does not determine integral quotient cohomology. The calculations are exhaustive only for the specified finite graph. No independent audit has been performed.
