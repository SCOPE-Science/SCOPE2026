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

# Finite exact verification

Execute `python3 verify_desargues.py` in a standard Python 3 interpreter. No third-party dependencies or external documents are required. This script constructs the bipartite double cover of \(\operatorname{KG}(5,2)\), checks all 30 graph edges, enumerates 6212 faces including the empty face, and performs full mod-two augmented simplicial boundary elimination. The ranks for dimensions zero through nine are \((1,19,141,519,991,932,383,97,18,2)\), giving mod-two Betti numbers one and five in dimensions four and five.

The verifier checks the Petersen adjacency relation \(A^2=2I-A+J\), enumerates and checks all 240 graph automorphisms from \(S_5\times C_2\), calculates signed Lefschetz values for all automorphisms using vertex-orbit independence polynomials, and independently computes oriented fixed-simplex traces for fourteen class representatives. It verifies the degree-four sign character, degree-five five-point permutation character and invariant dimensions for \(S_5\), \(A_5\), deck \(C_2\) and the full group. `verification_output.txt` records the successful run. The crucial passage from mod-two *upper bounds* to rational dimensions is proved using actual characteristic-zero involution traces in the mathematical proof, not assumed from computation.

The finite checks are exhaustive for this twenty-vertex graph. They do not prove results for graph families, integral quotient torsion or equivariant homotopy types, and they do not constitute independent validation.
