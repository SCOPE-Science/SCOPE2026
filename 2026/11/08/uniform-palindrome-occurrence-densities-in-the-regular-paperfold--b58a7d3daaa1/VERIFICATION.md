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

# Verification

The result rests on an explicit reduction of arbitrary length-at-most-\(15\) windows to the \(64\) residue/high-bit states, each of statistical weight \(1/64\), and on the absence of central palindromes of lengths \(14\) and \(15\). These lemmas are proved in `RESULT.md`.

Execute `python3 verify_paperfolding.py` using Python 3 standard library in the package directory. The checker tests every one of the \(960\) state-length cases, compares the exact word/count dictionary, checks the two forbidden central lengths, and performs a supplementary \(786432\)-window direct consistency test. The actual return was:

```
VERIFY_OK 2adic_states=64 lengths=15 state_cases= 960 palindromic_factors=28 direct_windows= 786432
```

The direct finite-window tests alone do not establish the theorem; the proof uses an infinite-to-finite reduction plus natural-density calculations. No independent external validation has been performed.
