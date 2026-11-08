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

Execute `python3 verify.py` with Python 3.8 or newer, without third-party packages. The script checks all sixteen patterns, the six symmetry representatives, exact rational-function identities by integer-polynomial arithmetic and rational coefficients through \(k=32\), direct block enumeration through \(k=10\), and exhaustive subsequence tests for all binary words at the five smallest even lengths.

Observed output:

```
VERIFY_OK patterns=16 orbits=6 rational_terms=32 symbolic_identities=16 direct_minimal_lengths=1..5 tested_words=1364 pattern_cases=32736
0000 [2, 4, 8, 16, 32, 64, 128, 256, 512]
0001 [2, 4, 8, 16, 32, 64, 128, 256, 512]
0010 [2, 4, 7, 12, 20, 33, 54, 88, 143]
0011 [2, 4, 7, 12, 21, 37, 65, 114, 200]
0101 [2, 3, 4, 5, 7, 9, 12, 16, 21]
0110 [2, 3, 4, 5, 6, 7, 8, 9, 10]
```

The checker covers finite ranges only; the proof in `RESULT.md` establishes all \(k\ge1\) from the exact transfer identity and rational-function algebra. No independent scientific validation is asserted.
