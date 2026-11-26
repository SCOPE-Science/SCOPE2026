---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Using the one-dimensional mass, derivative and stiffness matrices in tensor products gives opposite off-diagonals equal to a/3−b/6, b/3−a/6, and (a+b)/6±c/2, where a=||v||²/|det J|, b=||u||²/|det J|, c=−u·v/|det J|. Positivity of both Bernoulli factors preserves each sign for every admissible edge label. A negative weight creates a positive reduced off-diagonal: the corresponding central-cell vertices are interior, and either the pair is a diagonal with a unique contributor or every contributor shares the same side-orientation weight. Conversely a nonnegative set of weights yields a Z-matrix with zero column sums before Dirichlet elimination. At least one of the two side families is strictly positive, giving a straight positive-edge path from each interior node to the boundary even at all endpoint combinations. After elimination every component has a strictly dominant column, and the bidirectional edges give irreducibility on each component, so the reduced matrix is a nonsingular M-matrix. With z=(a−b)/(a+b) and q=2c/(a+b), the admissible closed rectangle has |z|≤1/3, |q|≤2/3. Maximizing z²+q² gives 5/9, hence κ₂(J)≤(3+sqrt(5))/2 with the stated Gram-matrix extremizer. Replay q1_tensor_stiffness() in /workspace/branches/independent_replay.py for the coefficients and exact witness. The proof concerns the nonsingular M-matrix condition, not arbitrary inverse positivity, consistency for arbitrary edge data, or general quadrilaterals.

## originality

PASS

The supported distinct claim is the exact closed geometric iff for the specified complete-graph IBEAM tiling and its attained sharp Jacobian distortion. The method, weight formula, strict-positive-weight sufficiency, standard Q1 stiffness algebra and Bernoulli sign mechanism are not new. The initiating theorem alone is not the closed shape iff; the strongest retrievable anisotropic Q1 comparator uses modified quadrature. The exact classical-geometry priority risk, especially the rectangle specialization, remains open and is not counted as a separately novel claim.

## value

PASS

The full closed mesh screening rule answers a practical and mathematical question left by strict sufficiency: whether every drift preserves the M-matrix property at a given aspect and shear, and exactly where it must fail. The attaining geometric ceiling and an orthogonal inadmissible element below it show why conditioning alone does not decide admissibility. This is a motivated exact boundary for a specified discretization, not a convergence theorem or a generic claim that bad shapes cause oscillations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
