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

# Reproducible checks

Execute `python checker.py` using Python 3 and SymPy. The code:

- constructs the full 7-state matrix from logical mask-overlap and odd-closure rules, checking the displayed matrix;
- verifies that the third power of the 7-state matrix is strictly positive, and the second power of the reduced 5-state matrix is positive;
- computes the 5-state characteristic polynomial and exact rational resolvent, and checks the 7-to-5-state row-symmetry intertwining identity;
- independently brute-forces all \(4^n\) mask patterns on each open ladder for \(0\le n\le8\), checking components by graph search rather than transfer logic.

Observed results: \(1,3,11,37,127,445,1559,5451,19061\); every exact assertion passed. The asymptotic entropy and all-length formula are proved by the matrix and finite-to-infinite language sandwich in `RESULT.md`. The finite checks alone do not prove those infinite claims. No independent external audit has been conducted. An unavailable unpublished source leaves historical priority qualified.
