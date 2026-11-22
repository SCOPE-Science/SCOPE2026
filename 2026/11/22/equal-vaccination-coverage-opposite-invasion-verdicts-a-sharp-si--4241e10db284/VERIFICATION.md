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

# Verification record

The analytical checks are reproducible from `RESULT.md`: strict local clipping on every vertex; exact vaccination fixed point; full triangular Jacobian; adjacency-radius comparison; boundary-edge lower bound of six; exact six-node multipliers; and the \(K_m\)-versus-\(P_m\) path spectral formula for all \(m\ge3\).

Running `python3 checker.py` with Python 3 standard library passed all tests: an exhaustive connected simple graph/sign census for sizes two through five, strict-sign checks for clique–path graphs with sizes six through one hundred, exact six-vertex disease-free equilibrium and equal vaccinated coverage checks, and finite-difference infection eigenvalue comparisons. The finite numerical tests do **not** certify the unbounded family or local nonlinear stability independently of the displayed proof. The proof does not cover equality at the invasion threshold, global attraction, or stochastic outbreaks.

Scientific review on correctness, literature-bounded originality and value is recorded separately. Independent scientific audit has not been performed.
