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

# Reproducible checks and limits

Run `python3 check_comaximal.py` using Python 3 with no third-party dependencies. The exact output for the tested configurations is included as `verification_output.txt`.

The program enumerates all RREF subspaces of the ambient Heisenberg Lie algebra in the tested prime fields; checks bracket closure for each; then directly takes vector spans of pairs together with their cross-brackets and determines whether each pair generates the full Lie algebra. This is an independent test of the claimed quotient-spanning criterion, not merely an evaluation of the same formula. It separately checks the predicted quotient-image fiber sizes. Finally it evaluates the integer Gaussian/symplectic formula over twenty configurations. The complete directly enumerated cases are \((m,q)=(1,2),(1,3),(2,2),(2,3)\), with exact edge counts \(27,96,3805,100905\). The two rank-one cases are prior-literature boundary checks.

The direct code uses modular inverses and RREF over **prime** fields only; the larger field sizes in the symbolic test are evaluations of integer cardinality formulas, not finite-extension-field enumerations. This limitation is explicit. The theorem covers all finite fields because the mathematical proof invokes finite symplectic linear algebra independently of the code. Neither finite enumeration nor symbolic value checks constitute an exhaustive verification of the universal theorem. No separate independent mathematical audit has been performed.
