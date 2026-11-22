---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Theorem reconstructs a finite height-at-most-two poset transfer with each upper coordinate subtracting t_b times its largest lower-neighbour coordinate, t_b in [0,1]. The image inequalities (1-t_b)y_a <= y_b <=1-t_by_a for each a<b yield a convex bijective target and the stated inverse. On a unique-max chamber its Jacobian splits orthogonally into triangular weighted star blocks; eigenvalues of S^TS outside the identity space solve z^2-(2+U)z+1=0. The largest possible squared star weight is W=max_a sum_{b>a}t_b^2; a strictly interior order-polytope point can force every upper neighbour of a maximizing a to choose it, giving infinitesimal equality for both map and inverse. Convexity and finite piecewise-affine decomposition give global bounds, including zero weights and disconnected graphs. Independent NumPy singular-value check and source-reviewed checker.py corroborate but do not prove the universal theorem.

## originality

PASS

Qualified PASS: existing marked-poset transfer and chain/order polytope papers construct the same map or much broader piecewise-linear families, but the mathematical results inspected do not establish the exact Euclidean Lipschitz operator norm of both directions, the maximum weighted-star statistic or equality for all independent interpolation weights. An abstract homeomorphism result is not a statement about sharp numerical stability. Actual Resultary searches find the assigned theorem and unrelated star metric distortions; searching is not proof of global novelty.

## value

PASS

The sharp distortion and equality cases quantify metric stability of a natural combinatorial transfer map for all height-two posets; an explicitly computable weighted maximum makes it useful for perturbation bounds in order/chain geometry. It is not just an existence theorem or a single numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
