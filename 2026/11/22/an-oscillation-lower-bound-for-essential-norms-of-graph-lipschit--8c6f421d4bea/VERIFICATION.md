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

# Verification of the graph Lipschitz multiplier bound

The result assumes an infinite connected locally finite graph, its graph metric and root-plus-edge-Lipschitz norm, and a bounded complex multiplication operator on either big or little Lipschitz space. The elementary \(c_0(E)\) weak-null argument and all edge-centered plateau calculations are written in `RESULT.md`. They justify the entire infinite family of lower bounds, not merely sampled graphs.

The source upper estimate \(\|M_\psi\|_{\mathrm e}\le4A(\psi)+B(\psi)\) was checked in the full open paper arXiv:2602.13534v1, Proposition 8.3, along with its definitions in Section 8 and the Banach-space definitions in Sections 2 and 3. This published estimate is the only outside theorem needed to turn the new lower bound into exact equality when \(A(\psi)=0\).

Run `python3 checker.py` with the Python standard library. The finite test produced `GRAPH_LIPSCHITZ_MULTIPLIER_TENT_CHECKS_OK 103`, verifying multiple radius-dependent profiles on finite ladder graphs, edge plateau identities, normalization, and the expected convergence of the sharpness-witness edge values toward two. The finite checks are corroboration, not a substitute for the weak convergence or asymptotic proof.

The proof does not determine a general essential-norm formula for positive \(A(\psi)\). The 2016 dissertation and 2023 unpublished manuscript mentioned in the source could not be fully inspected; their possible priority effect remains unresolved. No independent audit or external formal proof certification has been conducted.
