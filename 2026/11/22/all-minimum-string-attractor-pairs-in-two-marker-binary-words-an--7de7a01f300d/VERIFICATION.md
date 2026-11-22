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

The all-parameter proof in `RESULT.md` uses a full classification by the number of marker symbols within each factor, plus two exact diagnostic-factor interval intersections. The two supplied standard-library Python verifiers run independently of the proof.

Run `python3 verify_pairs.py` and `python3 verify_intervals.py` in the extracted directory. The saved output files report 1000 exhaustive triples with full pair searches, and 512 independently constructed interval cases with direct literal-factor coverage of 4220 candidate pairs. Parameter ranges are finite; the asymptotic law rests on the analytic simplex calculation and not on extrapolation from finite samples.

Both programs and outputs are embedded at the same relative directory level as this document. No external data, libraries, computational service or separately stored artifacts are required.
