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

# Verification scope

Run `python3 verify_fixed_window.py` in the extracted package directory with Python 3's standard library. This checker was executed successfully against the actual packaged source. It exhaustively compares the predicted inverse-fiber multiplicities with an independently constructed incidence-based census for 696 parameter cases (widths 2–30, lengths from saturation through the next 20 lengths, plus the sharp one-short boundary). It also computes 26,850 literal overlapping length-\(h\) window readings directly from source words and independently checks their incidence profiles. All tested exact counts and normalization totals passed.

The all-parameter statements, fixed-width asymptotics, and sharp threshold rely on the symbolic incidence-interval argument in `RESULT.md`, not on finite enumeration. Historical-priority comparisons remain qualified, and independent scientific audit has not been performed.
