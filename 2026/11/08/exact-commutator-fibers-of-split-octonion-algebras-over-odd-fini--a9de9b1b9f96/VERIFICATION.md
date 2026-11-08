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

# Reproducibility and limitations

Run `python3 verify_commutator_fibers.py` using Python 3's standard library. Its recorded output is `verification_output.txt`; the terminal marker must be `SPLIT_OCTONION_COMPLETE_COMMUTATOR_FIBERS_PASS`.

The checker independently constructs the seven-coordinate commutator, computes the ranks and augmented-system consistency of its adjoint matrices by finite-field Gaussian elimination, and accumulates the corresponding kernel sizes. Over \(\mathbb F_3\), all \(2187\) first-argument values are examined for each of four target types, determining each corresponding fiber by an exhaustive linear-system sum. Over \(\mathbb F_5\) and \(\mathbb F_9\), each target is compared against \(640\) reproducibly selected first arguments, which tests the rank classification but does not exhaust the fiber census. A separate exact arithmetic identity verifies that the four predicted fiber values sum to \(q^{16}\) with the stated output multiplicities for each tested field.

The proof is algebraic and valid for every odd finite field. Exhaustive computational checks are finite corroboration, not a substitute for the uniform argument; independent audit has not been performed.
