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

# Verification

Compile and run `verify_affine_gp.cpp` as C++17. It exhaustively enumerates all vertex subsets at affine-field orders two and three and uses independently computed all-pairs shortest-path distances, not the theorem's combinatorial classification, as its general-position criterion. Expected order-two maximum: size 4, count 5, mixed maximum count 4. Expected order-three maximum: size 9, count 1, mixed size 7, count 12, coefficient at degree seven 48.

Run `python3 verify_direction_tuples.py` to enumerate one-line-per-direction families. At order two, their union sizes occur with multiplicities {3:4,4:4}; at order three, {7:72,9:9}. These are finite exhaustive checks, not proof for all affine planes or all orders. The all-order result is proved in RESULT.md via incidence axioms and the odd-projective-plane exclusion at order three.

Independent scholarly audit has not been performed.
