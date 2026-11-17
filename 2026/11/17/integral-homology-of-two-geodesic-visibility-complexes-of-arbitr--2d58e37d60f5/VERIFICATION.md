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
# Reproducibility

Run the standard-library-only script `python verify.py` to regenerate the results in `VERIFIER_OUTPUT.txt`. This script enumerates the Alexander-dual simplices for five part-size tuples, computes the mod-two simplicial boundary ranks with exact integer bit operations, and checks all \(1,048,576\) vertex subsets of the twenty-vertex \(K_{5,5,5,5}\) directly against the complement predicate.

The predicted nonzero reduced Betti numbers of the Alexander dual are \((3,96,224)\) in degrees \((1,2,3)\) for \((5,5,5,5)\), and \((3,108,180,70)\) in degrees \((1,2,3,4)\) for \((5,6,5,5)\). In the original visibility complexes, integral Alexander duality places those free ranks in the corresponding reversed degrees. The code checks only the finite mod-two and face-combinatorial consequences; integrality, torsion-freeness and the unrestricted homotopy equivalence follow from the separate written graph-of-spaces proof, not from mod-two ranks or a successful log.

No independent mathematical audit has been performed.
