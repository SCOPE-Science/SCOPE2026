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
# Verification

This finding has a full all-index symbolic proof in `RESULT.md`. The finite exact computations provide independently reproducible base and boundary evidence, not a substitute for the induction.

`verify_sumsets.py` implements interval Minkowski sums for \(n=2,\ldots,8\), counts their cardinalities, checks the explicit base-eight complement and confirms the fifteen gaps of \(\langle6,7\rangle\). The expected standard output appears in `sumset_output.txt`; the interval table appears in `interval_certificate.tsv`.

`verify_direct.py` independently enumerates sets of sums from the original \(G\) for \(n=2,\ldots,14\), verifies \(\beta_G\), and checks the finite range that matters for additive closure. Its expected stdout is `direct_output.txt`.

Both programs were run successfully with Python 3 and use only standard-library integers. Both were also extracted from the completed embedded finding record and replayed, with outputs compared to the embedded logs. Exact data are finite; correctness for infinitely many \(n\) follows separately from the proof's (i) deficit-exclusion argument, (ii) interval-covering induction and (iii) representation of each of the final thirty nonexcluded deficit classes.

The source and originality comparisons are described in `REVIEW.md` and `AUDIT.json`. Independent scientific audit remains not performed. The programs do not certify novelty.
