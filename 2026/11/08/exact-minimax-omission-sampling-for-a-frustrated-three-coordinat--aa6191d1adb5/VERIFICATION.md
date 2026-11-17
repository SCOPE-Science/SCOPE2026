---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For the SPD inverse-Hessian Gram G with offdiagonal signs (+,+,-) and 0<c<=d<1, 2c²+d<1, exact minimization of the two retained coordinates leaves a rank-one H-energy residual. Its worst conditional expected retention is lambda_max(sum p_j v_jv_j^T)=lambda_max(P^{1/2}GP^{1/2}). Symmetrizing leaf probabilities is valid by convexity. For (a,b,b), antisymmetric mode T(a)=(1-a)(1+d)/2 decreases and the larger symmetric mode L(a) crosses it once at a*=d(1+d)/(2c²+d²+3d); L is increasing after crossing on this domain, establishing the global minimum. Cofactor identity makes determinant-volume sampling uniform; eigenvalue comparison gives retention (1+d)/3, strict gap for c<d and 4/3 sharp supremum. Independent numerical simplex optimization at four SPD (c,d) examples agrees with exact probabilities and eigenvalues; finite tests only corroborate the all-real proof.

## originality

PASS

Best-of-knowledge original specialization: a prior frustrated three-coordinate quadratic result optimizes one-coordinate updates and the minimum eigenvalue, NOT two-coordinate omission and largest residual eigenvalue. Prior volume-vs-uniform SPD stars has a positive/signable inverse Gram; its sufficient theorem cannot cover this negative cycle. General volume sampling and randomized sketch convergence set up the objective without computing the sharp signed-family law. Explicit residual E-optimal-design priority risk remains.

## value

PASS

Optimal sampling of exact large coordinate blocks is a natural E-spectral minimax question. The frustrated negative sign-cycle prevents the usual nonnegative Gram Perron optimization, so a sharp closed-form optimizer and strict determinant-volume gap in a full nontrivial two-parameter cone are mathematically motivated and useful, even though only one step and three coordinates are treated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
