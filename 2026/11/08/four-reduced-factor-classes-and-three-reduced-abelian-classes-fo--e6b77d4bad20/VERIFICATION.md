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

# Reproducibility and verification

Execute `python3 verify_sturmian.py` in a directory containing this extracted file and the checker, using Python 3 standard library only. The checker independently computes the slope-dependent rotation partitions for ten irrational slopes and lengths 1–300, and compares the rank-gap multiplicities, reduced class count, reduced Abelian class count, and which pair of the four classes merges. It separately enumerates distinct factors in 12,000-symbol mechanical prefixes for four irrational slopes and all lengths 1–100. All 3,000 partition tests and 400 direct-prefix tests passed during preparation.

The proof relies on exact symbolic reasoning in RESULT.md: mechanical Sturmian factor intervals, the absence of consecutive ones below slope one-half, the exact alternation identity and four threshold orders. The finite checker does not certify irrationality, exact equalities for every possible slope, or completeness for unbounded lengths. It is corroboration, not the proof. Historical novelty remains subject to unindexed-literature risk; no external mathematical audit has been performed.
