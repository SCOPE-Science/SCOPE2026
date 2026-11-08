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

# Verification record

Run `python3 artifacts/verify.py`. It uses Python integer bitset propagation and, independently, a boolean array recurrence. These agree on every tested membership position for both base sets and the obstruction. The checks cover every integer from \(0\) to \(17230\) at \(n=41\), every integer from \(0\) to \(18522\) at \(n=42\), and every integer from \(0\) to \(9083\) at \(n=45\). The zero bit at \(9083\) is a complete obstruction because no larger generator is at most \(9083\).

Further checks verify the finite intervals for \(43\le n\le60\) and test the induction inequalities through \(n=500\). The latter tests are only sanity checks; the symbolic polynomial/floor inequalities in `RESULT.md` establish them for all \(n\ge43\).

There is no independent scientific audit or external verification claim.
