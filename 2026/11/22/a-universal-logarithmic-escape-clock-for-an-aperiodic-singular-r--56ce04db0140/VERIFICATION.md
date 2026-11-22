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

Execute `python3 verify.py` from the directory containing the extracted files. The script uses standard-library `fractions.Fraction` to compare the original expression with the conjugated recurrence for 90 initial fractions over six steps, and to confirm the signed recurrence and monotonic squared drift. It also numerically compares the asymptotic remainder at two long finite times for seven initial conditions. These checks do **not** certify an infinite-time result; that follows from the exact inequalities and harmonic-sum proof in `RESULT.md`. The full theorem assumes real inputs other than the pole and does not require a statistical or symbolic-computation library. Independent audit has not been performed.
