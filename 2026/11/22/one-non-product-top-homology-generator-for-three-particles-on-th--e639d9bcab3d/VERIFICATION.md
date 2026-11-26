---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify_nauru.py NAURU_WITNESS.json`. The verifier uses exact Python integer and rational arithmetic, with no external package dependencies. It rebuilds the weight-three reduced Świątkowski complex, checks 16,192 degree-three generators and 39,600 touched degree-two coordinates, verifies rank 16,132 modulo three, and checks all 130 distinct unordered triples of disjoint unoriented simple cycles. The witness's oriented indexing is retained for its selected cycles. The script checks the boundary of every product torus and the supplied 5,034-term cycle, the explicit 60-by-60 integer minor of determinant \(-1\), and the vanishing of the complementary coordinate functional on all the products.

The rank over \(\mathbb F_3\) supplies a lower bound on rational differential rank; the unimodular cycle family supplies the opposite bound. Thus the integral conclusion does not assume a modular calculation alone proves rational rank, and does not infer integral generation from mere finite-field spanning. No assertion is made about other graph configuration homology groups or independence from external human review.
