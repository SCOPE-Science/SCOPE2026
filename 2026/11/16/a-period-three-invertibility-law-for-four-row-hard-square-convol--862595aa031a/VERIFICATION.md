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

# Reproducibility and proof checks

Run `python3 verify_grid4.py` using the Python 3 standard library. The program defines the eight allowed masks, independently regenerates each exact transfer matrix, tests the three nonstandard matrix identities that underpin the infinite theorem, and checks all Boolean frequencies for open four-row grids of lengths one through four.

The verified output is:

```
GRID4_WALSH_PERIOD3_PASS [(1, 8, 5, 2), (2, 41, 0, 1), (3, 227, 0, 1), (4, 1234, 11304, 2)] all_order_transfer_identities=3
```

Each tuple gives (column count, independent-set count, zero Walsh multiplier count, smallest nonzero multiplier magnitude). The direct enumerator checks graph edges and does not use the transfer-state recurrence. The Walsh transform is performed with integer butterflies. Every frequency is checked through dimension 16, and the constructed periodic witness values are also compared to transfer calculations.

The infinite proof depends on Cayley–Hamilton applied to an eight-dimensional parity transfer, invariance of a four-dimensional exact-integer Krylov span, and an exact sixfold return of a two-column transfer product. These claims are checked directly, so the finite spectra provide corroboration but are not substituted for proof. The code does not classify all higher-dimensional zero frequencies, and no independent external mathematical audit was performed.
