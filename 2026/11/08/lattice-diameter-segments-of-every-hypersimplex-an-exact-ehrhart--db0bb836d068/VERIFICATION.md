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
# Mathematical verification

All assertions in the included `verify.py` passed using Python standard-library integer and rational arithmetic. Direct unordered endpoint-pair enumeration in \(t\Delta_{n,k}\) was compared to the closed signed-support enumeration for \(2\le n\le7\), every rank, and dilations \(t=1,2,3\). Separate exact checks evaluated finite differences, Eulerian leading coefficients, and the closed rank-two identity up to \(n=14\). Terminal result: `PASS 333 independent exact assertions`.

The infinite mathematical argument is the balanced-direction classification and the Ehrhart-polynomial reduction proved in `RESULT.md`. The finite checker does not establish infinite statements, and no independent review is claimed. No additional data, proprietary software, or external services are needed to reproduce the checks.
