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

# Reproducibility and finite checks

Run `python3 verify_wave.py` with Python 3 standard library only. It independently constructs adjacency matrices, confirms the Jordan-determining nullities and the exact wave order, and computes the fixed-space nullities of 66-dimensional wave matrices at all positive divisors of 18 using modular row elimination. The actual successful output included:

```
F adjacency nullity sequences: -1 [17,18,18,18]; +1 [15,15,15,15]
F time 1,2,3,6,9,18: 17,32,35,65,36,66
H adjacency nullity sequences: -1 [16,17,18,18]; +1 [15,15,15,15]
H time 1,2,3,6,9,18: 16,31,33,63,36,66
PASS: all assertions
```

Run `python3 check_spectral.py` with Python 3 and SymPy installed. Its separately written graph constructors compute integer characteristic polynomials for both 33-vertex graphs and check equality to the same factored polynomial. The executed result was `PASS` for both.

A further direct field-three check compared the three explicit exceptional-component kernel descriptions against a separately computed matrix action on 1,000 pseudorandom vectors for each of the three powers; all comparisons passed. The main symbolic proof, rather than sampling, certifies the all-field claim.

The code verifies the prime-field matrices and the integer polynomials, not a separate exhaustive state traversal of all \(q^{66}\) states. Repeated update and finite experiments alone would not prove the arbitrary-extension formulas; their justification is the explicit modular Jordan calculation in the mathematical proof.
