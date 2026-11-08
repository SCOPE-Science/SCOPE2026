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

# Verification of the exact quintic local energy

The attached `verify_quintic_prime_power_energy.py` is standalone standard-library Python. It calculates the predicted counts from the stated recurrence and separately forms all ordered pair sums \((x+y,x^5+y^5)\bmod q\) and their multiplicities; the latter directly determine the energy. It also enumerates the simple, double, and origin strata of the collision polynomial over \(\mathbb F_p\) independently of the formula.

Successful execution of `python3 verify_quintic_prime_power_energy.py` produced:

```text
VERIFY_OK strata_primes=7 local_cases=17 composite_cases=9 max_local_modulus=729 crossed_singular_k6=PASS
```

The seven strata primes were \(3,7,11,13,17,19,23\). The seventeen local cases included exponents \(1\) through \(6\) for \(p=3\), through \(3\) for \(p=7\), and further tests for \(p=11,13,17,19,23\). The nine composite moduli were \(21,33,39,63,77,91,99,143,231\). The \(k=6\) check for \(p=3\) explicitly exercises the recursive origin branch; the test for \(p=7\), \(k=2\) gives \(E_7(2)=14\,161\).

These are finite direct computations, not a proof for every prime or exponent. The unrestricted conclusion depends on the explicit invertible variable change, exact finite-field strata, transverse Hensel lifting, and homogeneous origin recursion. The verifier does not test the excluded primes \(2,5\), where the reduction is inapplicable. No independent audit or external certification has occurred.
