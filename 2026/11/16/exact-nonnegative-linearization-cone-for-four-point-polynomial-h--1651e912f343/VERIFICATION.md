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

Exact verification: run `python CHECK.py` in this directory after installing `requirements.txt`. The verifier reconstructs the stochastic Jacobi matrix and degree-two/three polynomial matrix recurrences and asserts every entry of the complete coefficient table, along with row sums and explicit rational boundary witnesses. Expected output: `PASS: 35 symbolic/exact checks`.

The parameter inequalities are justified analytically in `RESULT.md`, not by enumeration. The four-point conclusion does not address higher cardinalities. Historical completeness beyond inspected sources has not been independently certified.
