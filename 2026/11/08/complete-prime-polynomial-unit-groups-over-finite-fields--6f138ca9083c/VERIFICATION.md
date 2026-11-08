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

# Verification scope
Run the supplied standard-library Python program from the same directory:

```sh
python3 verify.py
```

It uses binary integers as exact polynomial encodings over \(\mathbb F_2\). The two verification routes are (i) the explicit irreducible-product divisibility test and (ii) enumerating every canonical representative, computing polynomial gcd and independently deciding polynomial irreducibility. Both routes are compared on every monic modulus of degrees one through eight. The program also checks the predicted classifications through degree ten, the sum of 18 complete moduli, and the exact distributions of full-unit-group orders in degrees one through six.

A successful execution prints `VERIFY_OK`. The group-order distribution is separately listed by degree and is checked using exhaustive gcd counts, independent of the polynomial Euler-totient formula in the mathematical proof.

These checks are finite; the theorem's universal statement, degree cutoff, and exclusion of larger coefficient fields use the algebraic argument in RESULT.md. They do not depend on finite extrapolation. Independent mathematical audit has not been performed.
