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
# Reproducible verification and limits

All program dependencies are Python 3 standard-library modules. Execute from the directory containing these files:

```
python3 verify_census.py
python3 verify_rank30_cyclotomic.py
python3 checker_mod30.py
```

`verify_census.py` prints `UNIVERSAL_CYCLIC_TRIPLE_CENSUS_CHECKS_PASS`, checking the divisor sums and independent proportional-row/column event enumeration at eight small moduli. It also checks exact known rank partitions for orders 15, 21 and 30. `verify_rank30_cyclotomic.py` prints `EXACT_CYCLOTOMIC_N30_PASS`, with anchored ranks 180, 15192 and 149464. `checker_mod30.py` prints `MODULAR_ALL_PRIMITIVE_ROOTS_PASS`, reproducing the same anchored ranks by modular root evaluation.

The modular checker uses eight distinct primitive order-30 roots in the prime field of size 1201. The integral cyclotomic power table, derived from \(\Phi_{30}(x)=x^8+x^7-x^5-x^4-x^3+x+1\), has coefficients of magnitude at most one. Any six-term determinant therefore reduces to coefficients of magnitude at most six, smaller than the modulus. Vanishing at all eight roots is equivalent to exact integer-cyclotomic zero. The two rank computations are exact; they use no floating-point tolerance. Multiplying the anchored counts by 100 produces all \(inom{30}{3}^2\) minor counts.

This verifies only finitely many integer cases; the all-order assertion relies on the algebraic and combinatorial proof in RESULT.md. All files were inspected for their scientific content and have no external input dependencies. The historical priority comparison is bounded. Independent mathematical audit remains unperformed.
