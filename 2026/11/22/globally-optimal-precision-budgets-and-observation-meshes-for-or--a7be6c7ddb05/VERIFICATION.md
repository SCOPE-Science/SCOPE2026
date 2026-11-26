---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Gaussian projection reduces risk to a quadratic kernel energy plus noise. Cauchy–Schwarz eliminates the precisions with equality for allocation proportional to absolute weight, leaving the squared l1 penalty divided by P; compact sites and uniform coercivity in the weights give a minimizer. For distinct active sites the Markov interpolation integrates to a strictly positive vector Qb, with Q=K_T^{-1}. The inverse of the Stieltjes matrix I+N^(1/2)QN^(1/2) is entrywise nonnegative with positive diagonal, so the noisy weights are strictly positive for every active set. Aggregate coincident readings by adding precisions. At an active endpoint the inward variation strictly decreases the energy; at any distinct interior site a symmetric split gains λw²ε+O(ε²) while leaving the noise penalty unchanged. These exclude endpoints and unused or duplicate sites and give strict improvement with an additional site. On each open gap the residual solves r''−λ²r=−2λ, with r(t_i)=c=Σw/P; the average of one-sided site slopes vanishes and the jump is 2λw_i. Hence adjacent weights coincide, the inner gaps coincide, and the two Robin boundary conditions give equal margins and the stated weight equation. Its sides are strictly monotone in opposite directions, so existence plus uniqueness of the root proves global optimality. At g=d the sign of the difference is the sign of P−n. The separate n=1 case is maximization of the positive kernel mean at 1/2. Evaluating the normal equations gives the stated risk and geometric sum.

## originality

PASS

The assessed distinction is the finite-P, all-n free allocation theorem. The exact noiseless design and the fixed-equal-variance two-site geometry, risk and transition are already covered by indexed records. Neither includes the all-n optimization over freely allocated precisions, the finite-budget margin law for n≥3, or strict improvement in sensor count at fixed total precision. Other primary passages give the quadrature/energy framework, weight positivity, error rates, or different OU criteria; they do not supply this joint-design theorem.

## value

PASS

The all-n result resolves whether it is preferable to concentrate a fixed sensing budget or spread it among extra sites: the exponential cusp strictly favors splitting and the global mesh is computable by one scalar root. The co-variation of boundary margins with budget and the exact P=n transition for n≥3 are useful predictions beyond the already solved noiseless and two-site regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
