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

# Reproduction checks

Run `python3 verify_rb.py` (direct multiplication of all \(q^9\) endomorphism matrices over \(q=2,3\), tests the weight-minus-one identity on each of nine basis pairs, tests \(P^2=P\), computes ranks, and evaluates every automorphism orbit). Its complete actual standard output is embedded as `verify_rb.out`; both `ALL_IDEMPOTENT_TRIANGULAR_RB_TESTS_PASS` and `ALL_AUTOMORPHISM_ORBIT_TESTS_PASS` must appear.

Run `python3 verify_splittings.py` (independent subspace enumeration over \(q=2,3,4,5\), including an explicit characteristic-two quadratic extension field). Its actual standard output is `verify_splittings.out`, ending with `ALL_SUBALGEBRA_SPLITTING_CHECKS_PASS`.

The first program enumerates \(q^9\) **linear maps**, not just maps from the proof's classification. The second enumerates all one- and two-dimensional linear subspaces and tests actual algebra multiplication. These are finite reproducibility checks; the every-field orbit theorem rests on the symbolic subalgebra classification and group action in `RESULT.md`. No independent review or validation is asserted.
