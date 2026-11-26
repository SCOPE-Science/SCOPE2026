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

For a unit vector u the planar zonotope area is the sum of |u·(v_i×v_j)| over distinct index pairs. Thus the projection body has centered segments [−v_i×v_j,v_i×v_j]; converting each to [0,2v_i×v_j] translates the sum and gives the factor 8 in its three-volume. For nonnegative scalar multipliers on the generators, both normalized terms are homogeneous degree-six polynomials. Saroglou's five-segment equality annuls the restriction of their difference to every support of size at most five. Independently, every repeated-label term can be matched using (a×b)×(a×c)=det(a,b,c)a: the repeated-index patterns are a triangle for (2,2,2), two paths with the given internal labels for (2,2,1,1), and the six choices of a two-edge path and disjoint edge for (2,1,1,1). The surviving squarefree coefficient is the full six-generator deficit, nonnegative by Saroglou; lower-dimensional degeneracies have both three-volumes zero. For each six-set there are 20 ordered complementary triple terms and 15 perfect matchings. The first terms have expectation (π/8)², since the mean cross length is π/4 and the conditional mean absolute scalar projection of a uniform direction is 1/2. For each matching the three crossed vectors are independent and isotropic, with independent uniform directions and mean lengths π/4, giving (π/4)³(π/8). Subtraction of these bounded six-unit-vector contributions gives 5π²(32−3π²)/512, positive. Multihomogeneity and independence factor out the six first radial moments; the finite sum has finite expectation and no difference of divergent expectations is taken. For the example with infinite second moments, any nondegenerate triple supplies the product of the three squared radii in a lower bound for both volume terms (use the triangle of cross-product generators for the projection body). Empty six-sets give zero, including n<3. This is an exact reconstruction of the proof without executing the frozen program; its integer examples and Monte Carlo are only corroboration. No correlated or anisotropic extension is implied.

## originality

PASS

The distinct supported contribution is the evaluated finite-sample isotropic projection-volume deficit with arbitrary independent finite-mean radii. The inequality and five-segment equality are prior; the deterministic squarefree support identity is a direct coefficient consequence of that equality and the elementary zonotope formulas, and should not be read as a standalone priority claim. None of the compared statements gives the evaluated stochastic coefficient and the resulting finite expectation even in the absence of second moments. General expected-determinant machinery becomes applicable after identifying the squarefree terms and which of their random input blocks are independent.

## value

PASS

The exact expected gap in a sharp geometric inequality identifies the first generator count at which a positive average gap can occur and its dependence on heterogeneous lengths. The first-moment threshold is substantive: the natural two expected volumes can both diverge while their pointwise gap has a simple finite law for its expectation. The statistic is not a re-evaluation of the known deterministic extremal value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
