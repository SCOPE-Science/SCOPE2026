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

# Reproducibility and evidence

The all-dimension proof derives a binomial two-distance polynomial for each landmark separation, then proves the smallest nonempty coefficient using complementary coordinate-count orbits. For the central even-distance case, the count-swap symmetry and the exceptional four-cube require separate estimates. Finite verification alone does not establish the general theorem.

Run `python3 folded_formula_check.py`: it checks coefficient totals, nonnegativity and exact minima for all \(4\le n\le80\) and every possible separation. Recorded output:

```text
BINOMIAL_FORMULA_CHECK_OK n=4..80, every sensor separation
```

Run `python3 folded_direct_check.py`: it independently constructs the antipodal quotient and directly computes minimum distance signatures for every unordered landmark pair through dimension eight and every distance representative through dimension fourteen. Recorded output:

```text
EXHAUSTIVE_PAIRS 4 max 3 count 16
EXHAUSTIVE_PAIRS 5 max 4 count 40
EXHAUSTIVE_PAIRS 6 max 6 count 160
EXHAUSTIVE_PAIRS 7 max 6 count 224
EXHAUSTIVE_PAIRS 8 max 8 count 2240
DIRECT_QUOTIENT_CHECK_OK
```

Python 3 standard library is the only dependency. The exact proof rather than finite tests supplies the infinite quantifier. No external audit or exhaustive historical-priority certification has been performed.
