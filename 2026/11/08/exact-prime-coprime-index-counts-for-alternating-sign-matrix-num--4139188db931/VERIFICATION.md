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

# Verification of the stated prime-coprime index counts

The attached `verify.py` uses only Python's standard library. It computes factorial valuations through Legendre's formula and uses the difference of four factorial valuations to update the valuation of each consecutive alternating sign matrix count. It **does not** use the digit-tree recurrence to decide coprimality. For thirteen odd primes from five through forty-seven and the finite prime-power ranges specified in the program, it counts all relevant indices and compares with the theorem. The total number of directly checked indices is 160861.

Actual command: `python3 verify.py`.

Actual result: `VERIFY_OK primes=13 individual_indices=160861 triangular_layer_checks=9615 factorial_valuation_comparisons=PASS endpoint_prefixes=PASS`.

The program also reconstructs 9615 nonnegative triangular-layer values from the original floor increments, and checks that both interval endpoints at every tested level remain valid at all smaller prime-power levels. These calculations are finite sanity checks only; correctness for arbitrary primes and exponents rests on the written proof. No independent audit is represented by these checks.
