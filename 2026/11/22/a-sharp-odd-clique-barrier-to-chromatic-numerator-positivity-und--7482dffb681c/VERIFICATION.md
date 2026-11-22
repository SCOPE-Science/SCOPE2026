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

# Reproducibility

`verify.py` is a complete Python 3 standard-library script. From the directory containing this file and `verify.py`, run:

```
python3 verify.py
```

The checker uses exact integers and fractions throughout. It computes Stirling numbers, the known signed-clique chromatic polynomial, and all coefficients of the numerator by finite-difference convolution, checks the exact rational sign certificate, tests the positivity-preserving bridge recurrence through sixteen attachments, and compares small color counts against direct assignments. The finite tests cover odd core orders through thirty-one and attachments through five; they do **not** prove the infinite theorem. The displayed binomial-series inequality and the derivative recurrence in `RESULT.md` provide the unrestricted proof. No external solvers, databases, packages or missing data files are needed.

Expected final line: `VERIFY_OK`.

# Scientific limitations

The polynomial at odd arguments is a formal evaluation, not an actual zero-free coloring count for an odd palette size. The sign proof explicitly uses that distinction. No conclusions are claimed about even clique orders or nonbridge extensions. The literature comparison does not establish global publication priority. Independent mathematical validation has not been performed.
