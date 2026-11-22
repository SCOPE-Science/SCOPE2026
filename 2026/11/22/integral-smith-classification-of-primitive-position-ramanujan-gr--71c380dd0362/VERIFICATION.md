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

# Verification record

The complete arithmetic claim is supported by the integral prime-power block decomposition, the classical Smith calculation for \(pI_p-J_p\), and the Chinese-remainder unimodular tensor argument in `RESULT.md`. These steps prove the formula at every positive modulus; this is not an inference from testing.

The bundled `verify_primitive_ramanujan_smith.py` constructs the matrix from the Möbius divisor sum and calls an exact independent integer Smith implementation in SymPy. Running `python3 verify_primitive_ramanujan_smith.py` with SymPy installed completed 39 complete Smith-form comparisons and printed `CHECK_OK 39 independent Smith forms`. Tested moduli are all \(1\le n\le30\) and \(32,36,40,45,48,49,50,60,72\).

Finite computations do not establish unlimited assertions, uniqueness in the mathematical literature, or independent validation. Historical equivalents remain possible. Independent audit is not performed.
