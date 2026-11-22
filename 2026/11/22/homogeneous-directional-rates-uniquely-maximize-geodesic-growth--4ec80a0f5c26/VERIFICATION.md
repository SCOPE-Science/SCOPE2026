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

## Reproduction

1. Run `python verify_symbolic.py` with a current SymPy installation. Both independent state descriptions are enumerated from the stated three-cube graph, with rates \((1,1,t)\). Expect an exact PASS for three probability polynomials and the derivative identity.
2. Run `python verify_histories.py` using standard Python. This constructs all 7,368 edge-parent histories directly and checks all three path-length probabilities as exact fractions for six parameter values.

## Successful checks and limitations

Both programs passed before packaging. The symbolic code checked 289 reachable depth-label states and 265 Boolean geodesic states; their rational-function equality was verified identically in \(t\). The second code enumerated all 7,368 elementary histories per parameter, with exact rational values at \(t=1/4,1/2,1,2,5,10\). These checks are sufficient for the finite symbolic certificate; no large-dimension statement is inferred from them. Exponential-memorylessness and uniqueness of the shortest weighted path are explicit mathematical assumptions. An independent scientific audit is not part of these checks.
