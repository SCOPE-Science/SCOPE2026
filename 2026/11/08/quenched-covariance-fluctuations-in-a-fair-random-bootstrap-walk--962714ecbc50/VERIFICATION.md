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

# Reproducibility and verification

Run `python verify.py` with standard Python 3. The script uses only the standard library and performs exact integer and rational checks. The observed output on the supplied script was:

```text
PASS: 670,074 exact integer/rational assertions; n <= 8 for variance, n <= 6 for conditional iid transform
```

It enumerates all coefficient configurations through eight variables, all sign sceneries and coin paths through eight transitions, and all coin-to-martingale-increment maps through six transitions. It verifies the Pascal-parity bijection, exact pathwise decomposition, first two finite-horizon moments, and bijectivity of each fixed-scenery transformation from independent coins to the martingale increments. These are finite consistency checks; they do not imply any almost-sure, functional, or infinite-horizon assertion.

The proof of the infinite claims is in RESULT.md: the deterministic Pascal matrix establishes iid scenery; a pathwise telescoping identity gives a conditional fair-sign martingale; iid-scenery strong laws and bounded martingale functional CLTs establish conditional walk-pair independence; dyadic Hoeffding bounds and an Azuma maximal bound establish a uniform random-index replacement; independent Donsker limits give the two variance rates; an iid-sign law of the iterated logarithm establishes failure of uncentered conditional tightness.

No independent mathematical audit or external formal certification has been performed.
