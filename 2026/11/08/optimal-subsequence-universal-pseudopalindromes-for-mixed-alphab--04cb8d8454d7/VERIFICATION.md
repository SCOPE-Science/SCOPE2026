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

The accompanying `verify.py` uses only Python 3's standard library. Run `python3 verify.py` to re-enumerate the small test configurations. It checks the canonical structural characterization, exact optimum counts, and, in its smaller cases, every length-\(k\) subsequence pattern directly. Expected final summary:

`OK cases=34, enumerated_palindromes=1385969, extremizers=7632, direct_full_pattern_checks=79828`

The 34 listed configurations include pure involutions as independent reference controls; the scientific claim is restricted to mixed involutions. This computation does not establish the infinite theorem; the proof in `RESULT.md` supplies the general argument. No independent mathematical audit has been performed.
