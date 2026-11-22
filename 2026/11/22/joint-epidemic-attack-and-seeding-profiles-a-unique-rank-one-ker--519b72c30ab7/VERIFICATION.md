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

# Computation and analytic scope

Run `python3 verify.py` with standard-library Python 3.11 or later. The script computes the unique positive scalar final-size and branching-survival roots at 70-digit decimal precision, checks compatibility to a prescribed tolerance, reconstructs each entry of an exactly specified rational three-type next-generation matrix, checks its Perron eigenvalue, and constructs and verifies a positive rank-two kernel with indistinguishable outcomes. It also constructs independent product-form nullspace generators for dimensions two, three and five.

The proof of necessity/sufficiency, rank-one uniqueness, affine dimension, physical realizability and positive fixed-point selection is mathematical and valid for every finite number of groups. A finite checker is not an exhaustive proof. The work does not certify statistical identifiability under measurement error, physical contact reciprocity for the rank-two counterexamples, independent priority, or independent scientific review.
