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

# Verification and reproducibility

The attached `palindrome_cover_verify.py` is a standalone Python 3 program using only the standard library. Running `python palindrome_cover_verify.py` produced:

```
VERIFY_OK constructions q=2..10; exact independent tours q=2..4
```

The construction routine uses a graph Euler tour, inserts every diagonal and (when appropriate) matching-pair target, then checks every required four-symbol cyclic window and formula circumference. The independent Held–Karp subset dynamic program finds exact minimum overlap-tour lengths among all \(q^2\) distinct target palindromes for \(q=2,3,4\) (4, 9 and 16 targets respectively). It does not substitute for the all-\(q\) mathematical proof. The proof's parity and overlap arguments cover the infinite cases without computation. The program uses numeric symbols, so the direct string implementation is exercised for \(q\le10\) only. Independent mathematical audit has not yet been performed.
