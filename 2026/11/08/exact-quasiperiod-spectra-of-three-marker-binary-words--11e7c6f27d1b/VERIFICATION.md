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

# Verification of the fixed-weight-three quasiperiod theorem

The checker `verify.py` is a standalone Python 3 program using only the standard library. Run it from the package root using:

```
python3 verify.py
```

The direct method enumerates every length-\(n\) binary word with precisely three ones for \(3\le n\le25\). For each word, it independently tests every proper prefix against every occurrence in the word and checks coverage of each position; it then compares the exact set of lengths with the two structural candidates. It checks 14,950 indexed words.

The second verification computes coefficients through degree 65 by integer convolution of the three displayed rational generating functions. A separate enumeration of parameter quadruples, including the intersection parameterization, produces the same three arrays. Both methods compare to the word-level counts on the fully enumerated range.

Observed output begins with `VERIFY_OK words 14950 lengths 3..25 GF coefficients 0..65`. Its output prints the one-cover and two-cover counts for lengths 3 through 15.

These checks test finite cases and arithmetic only; the proof of the complete infinite family is mathematical and contained in `RESULT.md`. No external independent mathematical audit has been performed.
