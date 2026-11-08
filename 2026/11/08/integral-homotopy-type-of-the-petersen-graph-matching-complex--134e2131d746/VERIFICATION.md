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
# Reproducibility and verification

From the extracted package root, run `python3 verification/petersen_matching_verify.py`. The only dependencies are Python 3 standard-library modules. The program independently defines the Petersen graph as \(\operatorname{KG}(5,2)\), checks every possible 15-edge mask with two disjointness predicates, enumerates all incidence relations and checks acyclicity, performs exact integer unit-pivot reductions, and verifies the critical differential against its explicitly written matrix. It separately computes unreduced simplicial boundary ranks over four prime fields, testing that all degree-two and degree-three homology ranks agree with the integer calculation.

The expected stdout is stored in `verification/verification_output.txt`. It is evidence of the executed finite test, not a substitute for the mathematical argument that the reduced degree map determines the attaching maps in the simply connected two-/three-dimensional CW model.

The exact Smith factors follow because every row except the first, second, and sixth is zero, the sixth row is minus the first two, and the first-two-rows/first-two-columns determinant equals \(-1\). Therefore no integral torsion occurs. This proves the homotopy decomposition after applying the Hurewicz theorem and standard elementary CW basis transformations. Tests only address the stated finite graph, not arbitrary graph families or publication priority.
