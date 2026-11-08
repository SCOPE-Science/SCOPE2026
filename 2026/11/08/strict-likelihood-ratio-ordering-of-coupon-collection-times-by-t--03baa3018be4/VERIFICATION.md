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

# Reproduction of finite computations

In a Python 3 environment without third-party dependencies, run `python check.py` in the directory containing the present files. The script uses `fractions.Fraction` and integer factorials to avoid rounding ambiguity. It checks all distinct-weight label comparisons for 25 finite rational vectors with 2–6 coupon types over a range of integer completion times, the needed log-concavity determinants, and direct weighted enumeration of all short sample strings for at most four coupon types. The recorded successful run emitted:

`PASS: 30533 exact assertions (cross-products, log-concavity, and independent sequence enumeration).`

The program is not a proof of the infinitely quantified theorem; the formal generating-function derivation, TP2 convolution lemma and explicit strictness witnesses in `RESULT.md` provide that proof. No independent audit has been performed, and no external certification is claimed.
