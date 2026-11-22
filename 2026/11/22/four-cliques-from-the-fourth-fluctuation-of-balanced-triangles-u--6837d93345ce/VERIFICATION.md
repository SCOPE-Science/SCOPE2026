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

# Verification of the balanced-triangle cumulant identity

Reproduce with `python3 signed_triangle_checker.py`. The checker constructs the edge list of each small graph, enumerates its triangles and four-cliques, and enumerates all independent fair edge-sign assignments. It verifies \(\mathbb ES^2=t\), \(\kappa_4(S)=24q-2t\), and the converted variance, fourth cumulant and exact recovery equations for \(B=(t+S)/2\). It uses integer sums and `fractions.Fraction`, without floating point.

Executed outcome: `PASS: 1103 labeled graphs, 117154 exact sign assignments; 5 assertions per graph`. Coverage includes **every** labeled graph with one to five vertices and four selected six-vertex graphs. The finite enumeration is not a proof for larger graphs; the separate parity classification in `RESULT.md` proves the universal formula.

No independently commissioned validation or external mathematical audit is claimed.
