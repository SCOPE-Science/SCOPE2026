---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python check.py` from a directory containing the embedded `check.py` file. No nonstandard libraries or files are required. The program reports six diagnostic counts: 1,632 support values across 136 zero-baseline rational tie cases; 523,590 zero-baseline allocation-grid comparisons; 56,000 seeded random zero-baseline comparisons; 119,988 zero-baseline pairwise-shape comparisons; 552 checks around zero-baseline crossings; and 614,215 positive-baseline grid comparisons. The counters total 1,315,977; this is not a literal count of Python `assert` evaluations. These are finite diagnostics, not proofs of universal quantifiers.

The mathematical proof derives all-patch optimizer structure from the pairwise balancing lemma, unique adjacent crossings from exponential tilting, and no skipping from strict unimodality of the continuous support objective. Reproduction of the reported four-patch threshold approximations uses the equations in RESULT.md. Unavailable historical mathematical full texts leave residual priority uncertainty.
