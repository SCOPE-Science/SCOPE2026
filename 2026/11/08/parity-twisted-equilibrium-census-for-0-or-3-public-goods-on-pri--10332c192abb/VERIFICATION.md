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

Run `python3 verify.py` from the directory containing this document and the script. The program has no third-party dependencies, constructs the six-state transfer matrix from the explicit neighbor-response rule, checks \(B^6-2B^3-B^2+I=0\), and compares the exact cyclic-gap count against transfer traces for the first 100 lengths. It also enumerates all \(4^n\) action profiles for \(n=3,4,5,6,7,8,9\), totaling 349,504 checked profiles, and compares the result with the formula. On success the script prints `VERIFY_OK`.

The program checks finite identities, not infinitely many graph sizes. The general result is proved by the exact local classification, cyclic gap count, signed generating function and Perron eigenvalue argument in `RESULT.md`. No independent external validation has been performed.
