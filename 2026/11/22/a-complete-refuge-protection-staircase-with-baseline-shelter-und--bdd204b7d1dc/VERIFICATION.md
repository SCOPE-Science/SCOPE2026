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

Run `python check.py` from a directory containing the embedded `check.py` file. No nonstandard libraries or files are required. The program prints six counts: 1,632 exact rational zero-baseline ties; 523,590 allocation-grid comparisons; 56,000 seeded random allocation comparisons; 119,988 pairwise-shape checks; 552 boundary checks; and 614,215 positive-baseline grid comparisons, totalling 1,315,977 passing assertions. The actual program was run against the packaged source during this review. These are finite diagnostics, not proofs of universal quantifiers.

The mathematical proof derives all-patch optimizer structure from the pairwise balancing lemma, unique adjacent crossings from exponential tilting, and no skipping from strict unimodality of a continuous support-envelope derivative. Reproduction of the reported four-patch threshold approximations uses the equations in RESULT.md. There is no independent audit. Unavailable historical mathematical full texts leave residual priority uncertainty.
