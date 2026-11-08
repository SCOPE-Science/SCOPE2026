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

The mathematical derivation in RESULT.md proves the reduced Markov generator, rational Laplace transform, nonnegative first-moment drift, second-factorial-moment estimate, and an explicit uniform asymptotic error bound.

Run `python3 verify_kinetics.py` with Python 3. The script independently enumerates full labeled vertex-mask states and compares exact rational mean and transform values to the compressed computation for sizes \(2\le n\le7\) and two positive Laplace arguments. It also reports a separate large-size floating-point check, which is illustrative rather than a proof.

Finite enumeration does not certify the all-size result; its proof is the preceding analytic argument. Neither independent auditing nor a machine-checked infinite formal proof has been performed.
