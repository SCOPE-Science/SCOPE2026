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

Run `python3 theta_last_radius_verify.py` in an otherwise empty directory containing the accompanying script; it requires Python 3 and only the standard library. The exact output is embedded as `verification_output.txt`.

The script constructs graph distances independently for 32 pairs \((m,L)\), checks every unordered distance-\(L\) pair, computes full face counts for 24 small cases by independent recursion, and evaluates 90 signed alternating face-trace sums under the natural symmetries. The predicted first-homology rank of each crown factor and the join formula are mathematical proof steps, not empirical extrapolation. No external package paths, precomputed chain matrices or auxiliary downloads are required.

The computational observations do not prove the infinite quantifiers and cannot by themselves establish homotopy type or integral torsion. Those follow from the complete distance classification and canonical join/graph contractions in `RESULT.md`.
