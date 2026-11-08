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
# Verification instructions and limits

The supporting `verify.py` is a self-contained Python 3 checker requiring only `math` and `fractions` from the standard library. Run `python3 verify.py` from a directory containing that file. It performs the complete rational-divisibility test at \(n=-1\) for every lower binomial index and every order below each modulus, with bounds \(2\le d\le36\), \(1\le t\le d\), and \(0\le c<d\). These finite bounds are logically sufficient because the binomial finite-difference identity propagates the congruence to all \(n\in\mathbb Z\), and orders \(t\ge d\) are identities.

It reconstructs elementary symmetric coefficients by an integer recurrence, factors each modulus, and evaluates exact \(p\)-adic valuations of rational coefficients without floating-point arithmetic. A second recurrence for elementary symmetric functions of reciprocals checks the resulting rational coefficient formula independently. The script asserts the entire threshold table for \(2\le d<36\), the full order profile at \(d=36\), and the exact reduced rational counterexample at lower index \(c=32\).

The local execution printed:

```
VERIFY_OK moduli=35 filter_orders=665 finite_coefficient_cases=16205
first_nonmonotone_modulus=36; valid_orders=15,17..infinity; invalid_orders=1..14,16
counterexample d=36 t=16 c=32 valuation_2=1 required_2=2; rational= 196839814746004676662011581276685234/1506938033147421875
thresholds_d2_to_d35: [1, 1, 2, 1, 4, 1, 2, 2, 7, 1, 2, 22, 3, 12, 1, 26, 1, 3, 15, 30, 8]
```

The displayed thresholds line is complete and is enforced by assertions in the checker. This same-model checker is not an independently performed mathematical audit. It verifies exactly the stated finite classification and makes no claim for moduli above \(36\).
