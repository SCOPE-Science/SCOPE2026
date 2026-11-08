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

The standard-library exact checker `choice_multipartite_exact.py` enumerates 58 connected complete multipartite types on two through eight vertices and 29 types on nine vertices. It solves, with `fractions.Fraction` arithmetic, every partwise visited-count/current-part Bellman system, checking the full optimal Bellman equality for each state. Totals: 7,391 states through eight vertices and 11,956 states at order nine. All mixed-status offers in smaller graphs admit an optimal unseen-first action; exactly the \(K_{1,2,6}\) type at nine vertices has strict counterexamples, consisting of three reduced decision-state types.

The exact checker also verifies the two displayed rational witness continuation values and their positive rational difference. It terminates by assertions if a classification, Bellman identity or rational value differs.

An independent labeled-subset value-iteration cross-check is implemented in `choice_multipartite_independent.py` (requires NumPy). Its numerical solution converged after 183 iterations and agreed with both exact witness values to within \(10^{-9}\). The numerical check supports but does not certify the finite classification.

No code proves anything about graphs of order at least ten. No independent audit was performed.
