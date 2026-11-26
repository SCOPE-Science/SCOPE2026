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

For complex polynomials of degree ≤4 under normalized Haar probability, optimizing evaluation at a fixed point with P(1)=1 gives the sharp fourth-power constant by rotation. The L4 fourth power is coercive on the finite-dimensional affine space by norm equivalence and is strictly convex: distinct polynomials differ on a set of positive measure. The unique minimizer is fixed under coefficient conjugation and degree-four reversal, both norm-preserving, so is real palindromic. Parseval on P² gives exactly Q; minimizing this differentiable strictly convex function gives the unique real common zero of f and g. The independently written SymPy replay at /workspace/branches/ddc79506-dd99-436d-b4a4-da2c3dfcfd67/independent_replay.py with log independent_replay.log checks Q by convolution, both scaled gradients, resultant −189R and linear subresultant 63(Ay+B). Exact root counts show one real R-root in the stated rational interval and A positive there; reducing the recovered y equations modulo R verifies both. Independently the specified positive tangent weights sum to one, cancel the gradient and yield the global bound 14888369619/116976484375>1/8, so C_(4,4)<8 without a numerical step. The replay verifies the displayed decimal prefixes including kappa. A normalized minimizing polynomial cannot have modulus greater than one elsewhere (rotation and rescaling would improve its integral); equality is precisely given by undoing the normalization and rotation, plus the trivial zero case. Haar torus integration of a homogeneous quartic reduces to the ratio of its coordinates on the circle, and its diagonal has normalized-area fourth power |P(1)|^4/9. Thus the diagonal operator norm is (C_(4,4)/9)^(1/4), not the fourth-power value C_(4,4), and is attained. Only the frozen checker text and its recorded status were read; it was not executed.

## originality

PASS

Credit the prior identical optimization problem, uniqueness and symmetry of normalized extremizers, general contractivity, and the homogeneous reduction. The distinct surviving content is the exact evaluated degree-four fourth-moment constant and coefficients with an explicit strict upper bound of eight. Neither the same-parameter bounds nor the wider contractivity theorem determines these quantities.

## value

PASS

The named point-evaluation problem was already studied through degree four, which is the first even degree with two coupled real free coefficients after symmetry. A sharp algebraic value with normalized extremizing coefficients and a simple global strict certificate supplies independently useful exact stability information for both circle evaluation and the natural homogeneous diagonal block. This is a motivated low-degree invariant, not a randomly chosen coefficient slice, a lost norm normalization or a claim of a new general contractivity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
