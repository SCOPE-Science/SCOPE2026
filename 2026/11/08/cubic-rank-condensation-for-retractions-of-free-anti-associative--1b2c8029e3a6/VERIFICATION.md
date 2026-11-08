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

# Verification of cubic-rank condensation

Running `python verify.py` exercises the explicit free anti-associative multiplication table in odd prime characteristic. It constructs homomorphisms from arbitrary assignments to free generators and checks composition-idempotency and image rank directly. Its actual completed checks were:

```
EXHAUSTIVE_ONE_GENERATOR_OK 3 {0: 1, 1: 1}
EXHAUSTIVE_ONE_GENERATOR_OK 5 {0: 1, 1: 1}
CANONICAL_RANK_ONE_AFFINE_FIBER_OK 3 S 81 lifts 531441
RANDOM_UNIPOTENT_CONJUGACY_OK 2 3
RANDOM_UNIPOTENT_CONJUGACY_OK 3 3
VERIFY_OK
```

The rank-one two-generator check exhausts all second-degree choices over \(\mathbb F_3\) and uses exact modular linear equations for the third-degree extensions. Each of its \(81\) valid quadratic choices has \(3^8\) cubic completions. The resulting \(3^{12}\) fixed-projection count agrees with the formula. The full enumeration for the complete \(n=2\) algebra is not attempted; random conjugacy checks are not exhaustive. The asymptotic assertions are mathematical deductions from the quartic exponent and are not computer certified. There has been no independent mathematical audit.
