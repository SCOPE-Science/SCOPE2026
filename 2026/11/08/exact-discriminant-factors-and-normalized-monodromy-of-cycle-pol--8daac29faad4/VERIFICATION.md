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
# Verification evidence and limits

The included `verify.py` is self-contained, deterministic, and uses only the Python standard library. Run `python3 verify.py`. It evaluates all \(d(d-1)/2\) squared root differences for each test instance, and independently builds the product over all nonempty proper sign-index subsets. Thirty-five instances test \(m\) from two to eight (five per value, degree at most 128). Another thirty instances verify the reduction to lower-cycle factors for subset cardinalities three through eight. The expected successful terminal messages are `ALL_DISCRIMINANT_IDENTITY_TESTS_OK` and `ALL_COMPONENT_TESTS_OK`.

All checks in the certificate were actually executed using the included program. Computations use exact finite-field arithmetic; coincident mod-prime reductions are possible but do not affect the literal equality checks. No computational run proves an identity for all dimensions. The universal result instead follows from the written signed-root orbit argument and the established monic root formula in [1]. The Galois, normalization and ramification claims are not tested by the finite-field script and are established only in the written algebraic proof. Independent audit has not been performed.
