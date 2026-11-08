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

Run `python checker.py` with Python 3 and NumPy. The source independently constructs the unrestricted linear Leibniz system (all matrix entries, every basis pair and output coordinate), computes rank modulo primes, separately constructs coefficient vectors using signed-doubling congruences, and directly evaluates products. Recorded output:

```
VERIFY_OK rank_cases=30 orbit_examples=4
```

Thirty finite-field matrix-rank calculations use odd orders \(3,5,7,9,11,13\) and primes \(2,3,5,7,11,13\) when coprime. Four further orbit-construction examples cover \((11,3)\), \((13,5)\), \((23,89)\), and \((15,7)\). The size-23 test verifies constructed maps, not exhaustive unrestricted derivation dimension. Characteristic-zero and general-order assertions are verified in the symbolic proof, not by experiments. This is not independent mathematical validation.
