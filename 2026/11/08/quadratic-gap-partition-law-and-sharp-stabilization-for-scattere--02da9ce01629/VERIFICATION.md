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

# Verification instructions and limits

Use Python 3 with the standard library and execute the two embedded standalone programs:

```sh
python3 verify_gap.py
python3 verify_stream.py
```

Both programs raise an exception if a tested identity fails and print `PASS` statements upon completion.

`verify_gap.py` independently enumerates every one of the \(2^n\) binary words at each length \(0\leq n\leq14\), counting `010` occurrences with a one-pass subsequence dynamic update. It compares the resulting frequencies \(1\leq k\leq40\) to the coefficients of independently enumerated quadratic-weight gap polynomials. It checks predicted polynomial degree, top multiplicity, sharp boundary defect, and the first twelve slope/intercept pairs for \(1\leq k\leq40\).

`verify_stream.py` uses a separate finite-state count-by-appending recurrence on the numbers of zeros, `01` subsequences and `010` subsequences. It compares the exact counts to a second implementation of the gap-weight recurrence for every \(0\leq n,k\leq30\), including the zero-frequency boundary.

These computations verify the implementation and small instances. The proof for arbitrary \(k,n\) is the symbolic zero-gap bijection, coefficient identity and extremal-length argument in `RESULT.md`. Neither script purports to search all word lengths or to replace that proof. This verification was performed without an independent external mathematical audit.
