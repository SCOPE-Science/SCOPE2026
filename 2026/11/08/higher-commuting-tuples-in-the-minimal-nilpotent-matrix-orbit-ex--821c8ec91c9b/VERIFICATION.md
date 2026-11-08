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

# Finite-field verification

Run `python3 verify_minimal_orbit_tuples.py` using Python 3 and no external dependencies. The checker constructs all nonzero rank-one square-zero matrices by outer products, tests actual pairwise matrix products, checks the equivalence of commutation and annihilation, then independently enumerates all ordered commuting tuples using adjacency bitsets and computes the dimension of the sum of their images by Gaussian elimination. Each histogram is compared exactly with the finite-sum formula.

The six tested parameter choices and their measured distributions are recorded in `verification_output.txt`; the only main-theorem in-scope case is dimension four, tuple length three, field order two, with count 30345. Several dimension-two and dimension-three cases check boundaries and the four-element extension field. These finite tests cannot certify all dimensions or fields, nor historical novelty. The proof, not the checker, establishes the unbounded claim.

Independent audit has not been performed.
