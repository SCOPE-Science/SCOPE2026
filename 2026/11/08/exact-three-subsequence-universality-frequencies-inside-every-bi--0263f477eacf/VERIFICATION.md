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

# Reproduction and limits

Run `python3 verify.py` using Python 3 with only the standard library. The program independently generates all binary words of each composition with \(3\leq A,B\leq8\), computes their \(ab\)-subsequence counts by scanning, and tests the eight length-three patterns via greedy embeddings. It checks all 1,125 two-deck fibers against the six-avoider formula and a separate Gaussian-fiber dynamic program. It additionally compares the canonical collision model against the closed formula for all 17,885 parameter triples with \(3\leq A,B\leq16\).

Observed output: `VERIFY_OK: 48200 direct words, 1125 Parikh fibers, 17885 additional candidate-fiber comparisons`.

The program supplies exhaustive finite checks only in those displayed ranges. The unrestricted result is justified by the mathematical proof in `RESULT.md`, including the uniqueness argument, collision classification, and summation. No independent external verification has been performed.
