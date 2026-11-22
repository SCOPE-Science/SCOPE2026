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

Run `python verify.py` from the same directory as this document. The script uses only Python's standard library and performs brute-force word enumeration, independently checking the exact coefficient formulas in `RESULT.md`. Expected output is in `verification_output.txt`. It tests varying alphabets, motifs, lengths, fixed compositions, and biased iid weights. The runs were performed from the packaged code and matched the recorded output byte-for-byte.

These computations establish no infinite-range result by themselves. The infinite formula is derived combinatorially; the Poisson–binomial representation additionally uses the published Chudnovsky–Seymour real-rootedness theorem. Full-text availability limits for the most recent related sources are identified in `REVIEW.md`.
