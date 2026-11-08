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

# Reproducibility checks and limits

Execute `python3 verify_edge_general_position_trees.py` with Python 3.10 or later; it uses only standard-library modules. The script constructs all labelled trees of orders three through seven using Prüfer codes and 450 seeded additional trees of orders eight through ten. Independently from the subtree characterization, it reconstructs every unique shortest vertex-to-vertex path and checks every edge subset by the definition that no three selected edges lie on one geodesic. It then tests inclusion-maximality through all possible one-edge additions and compares the two complete cardinality polynomials with separately implemented rooted recurrences. Separate computations check the proposed lower and upper values, the number of maximal two-edge sets obtained from maximal degree-two chains, and the number of maximum sets obtained from terminal chain products.

Output from execution against the actual packaged checker:

`VERIFY_OK labeled_trees_n3_to7=18247 additional_trees_n8_to10=450 instances=18697 valid_edge_sets=556214 maximal_edge_sets=172716 both_polynomials=PASS lower_number=PASS upper_number=PASS extremal_counts=PASS`

The script's exhaustive claim covers **labelled trees of orders three through seven only**, not all trees. The 450 larger trees are deterministic samples, not an exhaustive census. Neither computation implies correctness for every order; the general proof is the mathematical basis of the theorem. Polynomial-time arithmetic complexity refers to dense exact-integer polynomial operations and does not claim a bit-complexity bound. The literature comparison does not constitute a formal priority certificate. No independent external audit or certification has been performed.
