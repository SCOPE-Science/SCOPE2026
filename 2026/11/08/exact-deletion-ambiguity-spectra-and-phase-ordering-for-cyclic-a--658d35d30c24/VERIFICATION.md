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

# Reproducibility and limits

Run `python3 checker.py` using a stock Python 3 interpreter. No third-party package, network access, hidden data, or external certificate is required.

The program independently enumerates all distinct coordinate subsequences of both sources for alphabets of sizes 2 through 8, source lengths 1 through 10, every nonzero phase offset, and every retained length. It compares the resulting set intersections with a separate bounded-composition dynamic calculation of the asserted formula. The completed run printed:

```
VERIFIED: direct subsequence sets versus bounded-composition formula
VERIFIED: 280 distinct parameter profiles, 1820 length entries, q=2..8, n=1..10
VERIFIED: exact LCS lengths, multiplicities and phase ordering
EXAMPLE q=6,n=12:
h=1: [1, 6, 36, 140, 320, 467, 467, 331, 165, 55, 11, 1, 0]
h=2: [1, 6, 36, 128, 247, 296, 236, 128, 46, 10, 1, 0, 0]
h=3: [1, 6, 36, 124, 222, 240, 166, 72, 18, 2, 0, 0, 0]
```

For larger lengths the example counts use the polynomial formula, not direct enumeration. General correctness relies on the five-part proof in `RESULT.md`; the finite checker is a regression test, not an exhaustive infinite proof. Novelty comparisons retain a priority risk, and independent validation is not performed.
