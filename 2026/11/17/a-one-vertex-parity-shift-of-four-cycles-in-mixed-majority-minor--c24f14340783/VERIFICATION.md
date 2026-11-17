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

# Verification performed

`verify.py` is a self-contained Python 3 program using only `math.comb`. Its update routine counts, for each vertex, ones at all its *other* vertices and directly applies the two behavioral types and tie retention. It independently constructs and follows every state-transition edge to count distinct period-one/two/four temporal orbits and the minimum entry time of each labelled configuration. The results were checked against the theorem for every nonempty population split on \(K_N\) for \(3\le N\le15\): 104 graph/type cases, and every binary configuration within each case. All checks passed; complete stdout is embedded as `verification_output.txt`.

The assertions exclude any other period or a transient longer than two on those finite graphs; the proof supplies the all-order conclusion. No external validation, independent audit, or computer-assisted infinite certification has been performed. Exact assertions about all graph orders rely on the case analysis in `RESULT.md`, not extrapolation from computation.
