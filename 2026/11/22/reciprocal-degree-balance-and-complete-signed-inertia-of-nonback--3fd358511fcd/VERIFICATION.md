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
# Verification

The exact proof is in `RESULT.md`. Its critical steps are (1) common predecessor and successor counts; (2) the inverse-form radical rank identity; (3) the incidence kernel's odd-cycle/bipartite parity classification; and (4) the edge-reversal sign symmetry. No unproved numerical leap occurs in those steps.

Execute `python verify.py` in an environment with Python, NumPy and NetworkX. Direct matrix construction was compared against the independent weighted-incidence formula, the reversal relation, inertia/nullity predicted by exact rational reciprocal-degree sums, the Frobenius trace identity, and, for regular graphs, all ordered eigenvalues of the adjacency-derived spectrum. The checked script returned `VERIFICATION_OK 474`. Finite tests are supplementary, not a proof for all graphs or a historical-priority certificate. Independent external validation has not been performed.
