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

The column marginal ranges over exactly the nodally nonnegative polynomial samples: necessity follows by summing rows and sufficiency by assigning the marginal divided by N_x to every row. The normalized slice is a compact convex subset of the probability simplex. The affine constraints are a >= |b| and the moments are na and n mu_n b. The quadratic normalized slice is a polygon: a vertex must have two distinct active nodes by injectivity of evaluation, and two active nodes fix a ray. An upward quadratic with two roots is nonnegative at every node iff the roots are adjacent; a downward one requires the two endpoints. The resulting mean is -2 mu_n c/(mu_n+c^2-delta_n^2) for signed midpoint c, or zero on the downward ray. This gives both endpoints and every intervening value by mixing. The first adjacent pair gives a strictly larger bound than mu_n since mu_n<1. The midpoints become dense and the envelope converges uniformly to 2c/(1+3c^2), maximized at c=1/sqrt(3). R_2=1 at n=3, but for n>=4 every nonzero polynomial of degree <=2 has support on at least two nodes, so by compactness R_2<1. Moving a mass t from a lower occupied node to velocity 1 increases momentum by t(1-v_k) at unchanged mass, with Frobenius distance at most sqrt(2/N_x)t. The QP objective is coercive and strictly convex in the core; the feasible set is closed convex. This is nonnegativity, not strict positivity at the frontier.

## originality

PASS

Pass for the evaluated polynomial-factor frontier, its all-grid comparison, and the explicit near-frontier obstruction, not for the generic fixed-factor reduction or the QP formulation. The leading related corpus record has a genuinely overlapping general framework; the available statements do not establish its coverage of the explicit adjacent-root maximization over arbitrary n or the sharp limit in this specialization. Mathematical comparison is best-of-knowledge, not a priority ruling.

## value

PASS

The explicit frontier is a practical exact precheck for a natural low-rank correction with conservation modes. It quantifies the benefit and the limit of adding the quadratic mode, and shows that a small approximation error does not guarantee feasible exact repair. Neither the generic linear feasibility problem nor a continuum asymptotic alone gives that finite-grid diagnostic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
