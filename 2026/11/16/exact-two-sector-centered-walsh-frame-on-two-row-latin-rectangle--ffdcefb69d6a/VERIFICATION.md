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
# Reproducible finite checks

Run `python latin_enum_verify.py` and `python latin_mode_verify.py` with Python 3.10 or later. Neither program requires external libraries. Both assert the exact rational formulas for orders 2–5 and print the check outcome; the first covers every relative pair type and the second independently builds the random rows via a permutation and a derangement and compares contrast energies. The full all-order proof is in `RESULT.md` and does not rely on finite tests.

The characters are centered and probability-normalized. The nonzero sampling singular values are the square roots of the corresponding Gram eigenvalues. The exceptional order-two rank is one; the stated main condition number requires order at least three. Independent external validation has not been performed.
