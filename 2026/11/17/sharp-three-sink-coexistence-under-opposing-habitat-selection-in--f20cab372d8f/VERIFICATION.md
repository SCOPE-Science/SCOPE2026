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

# Verification of the local three-sink wedge

The proof uses: direct differentiation of the planar polynomial flow; the one-sign-change cubic \(H(m)\) to prove exactly one anti-diagonal root; monotonicity of its simple positive root as habitat bias increases; diagonalization of a symmetric two-by-two Jacobian; and an exact positive difference of the two threshold squares. The rational witness has exact eigenvalues for all three claimed sinks.

Execute `python3 verify.py`. This script checks the vector field and Jacobians using rational arithmetic, the closed-form threshold identities on six parameter pairs, and representative strict-wedge eigenvalue inequalities. It does not certify all parameter values computationally; universality comes from the written algebraic proof.

Limitations: the finite test cases cannot rule out other equilibria; no stochastic or global-basin conclusion is made. Independent auditing has not been performed.
