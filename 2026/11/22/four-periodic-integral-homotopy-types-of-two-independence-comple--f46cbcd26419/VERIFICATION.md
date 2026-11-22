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

Run `python3 verify.py` using Python 3.9+ (standard library only) in the extracted directory. The script independently constructs connected triples and the entire finite face posets for \(3\le\ell\le14\), reproduces the declared vertex-toggle matching, checks Hasse acyclicity for \(3\le\ell\le11\), independently checks face membership via induced connected components for \(3\le\ell\le10\), and verifies 90 explicit endpoint-state four-step recurrence instances. `expected_output.txt` records an actual run. The infinite assertion follows from the analytic recurrence and base-table proof in `RESULT.md`, not extrapolation from the finite checks. No independent mathematical audit or external certification has been performed.
