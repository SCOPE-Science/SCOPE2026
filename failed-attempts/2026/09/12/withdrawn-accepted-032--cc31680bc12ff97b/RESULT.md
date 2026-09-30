# Disproof of an explicit Wasserstein stability fragment for cone-volume measures of centroidal 4-polytopes

## Context and motivation

The logarithmic Minkowski problem asks which Borel measures on the sphere arise as
cone-volume measures of convex bodies, and a natural quantitative refinement asks
whether closeness of cone-volume measures implies closeness of the bodies. The
admitted target proposed one explicit optimal-transport stability fragment in
R^4: for centroidal polytopes with at most 12 facets trapped between
(1/2)B^4 and 2B^4, optimal-translation Hausdorff distance should be controlled by
20 times the 1/4 power of the geodesic 2-Wasserstein distance between normalized
cone-volume measures, whenever that Wasserstein distance is at most 10^{-3}.
Either a proof with exactly those constants or an explicit violating pair counts
as a complete resolution.

## Definitions

For a convex body K containing the origin in its interior, the (unnormalized)
cone-volume measure is V_K(omega) = (1/n) int_{nu_K^{-1}(omega)} x . nu_K(x) dH^{n-1}(x).
For a polytope with facets F_i and outward unit normals u_i at support heights
h_i, this is the discrete measure sum_i |F_i| h_i / n delta_{u_i}. Its
normalization V_K / V_K(S^{n-1}) is a probability measure on the sphere; here
n = 4. W_2 denotes 2-Wasserstein distance on S^3 with geodesic cost. d_H after
optimal translation means min_t d_H(P, Q+t) with Euclidean Hausdorff distance.

## Result (headline claim)

The stated inequality is FALSE. The pair

  P = [-1,1]^4,
  Q = [-1.2,1.2] x [-0.9,0.9]^3

both lie in the admitted class, have identical normalized cone-volume measures

  V_P = V_Q = (1/8) sum_{i=1}^4 (delta_{e_i} + delta_{-e_i}),

so W_2(V_P,V_Q) = 0 <= 10^{-3}, yet their optimal-translation Hausdorff distance
equals 0.2. Hence 0.2 <= 20 * 0^{1/4} = 0 is false. In fact no finite constant
and no exponent can repair the estimate, since distance is positive while
Wasserstein distance is exactly zero.

## Proof / evidence

Class membership. Both boxes are centrally symmetric about 0, hence have
centroid 0, and each has 8 facets (at most 12). Minimum half-side lengths are
1.0 and 0.9, both above 1/2, so (1/2)B^4 is contained in each body. Vertex norms
are |v_P| = 2 and |v_Q| = sqrt(1.44 + 3*0.81) = sqrt(3.87) approx 1.967 <= 2, so
each body is contained in 2B^4.

Identical normalized measures. For B(a) = prod_i [-a_i,a_i] in R^4, the facet
{x_i = +a_i} has 3-volume 2^3 prod_{j != i} a_j and support height a_i, so its
cone-volume is |F| h / 4 = 2 a_1 a_2 a_3 a_4, the same number for every facet.
Summation over all 8 facets gives total volume 16 a_1 a_2 a_3 a_4, so each facet
carries normalized weight exactly 1/8, independent of the side lengths. Applied
to P and Q, both normalized measures are the uniform 8-point measure on
{+-e_1,...,+-e_4}. The identity coupling gives W_2 = 0.

Hausdorff distance. Coordinate projection x -> x_1 is 1-Lipschitz, so for any
translation t, d_H(P,Q+t) >= d_H([-1,1],[-1.2+t_1,1.2+t_1]) = 0.2 + |t_1| >= 0.2.
At t = 0, vertex enumeration gives sup_{x in P} dist(x,Q) = sqrt(0.03) approx
0.173 (0.1 in L_inf metric) and sup_{y in Q} dist(y,P) = 0.2, so d_H(P,Q) = 0.2
in Euclidean metric. Thus min_t d_H(P,Q+t) = 0.2, attained at t = 0.

Conclusion. Left side 0.2 versus right side 0 falsifies the inequality, and the
W_2 = 0 versus d_H > 0 gap falsifies every finite-constant variant.

## Limitations

This disproves exactly the stated fragment with its class, constants 20 and
1/4, and threshold 10^{-3}. It does not rule out corrected stability statements
with additional hypotheses such as prescribed total volume together with the
normalized measure, symmetry-breaking data, restricted subclasses, or weaker
moduli; those were not investigated.

## Reproducibility

All numbers are analytic (inner/outer ball bounds, per-facet cone-volume
2*prod(a), vertex norms, projection bound 0.2+|t_1|) plus finite vertex
enumeration over 16 vertices per box. The script
output/artifacts/verify_counterexample_original.py (numpy only) reproduces every
number: class membership, weight 1/8, W_2 = 0, and Hausdorff distance 0.2.

## References

K. Boeroeczky and M. Henk, Cone-volume measure of general centered convex
bodies, Adv. Math. 286 (2016); K. Boeroeczky, E. Lutwak, D. Yang, G. Zhang, The
logarithmic Minkowski problem, J. Amer. Math. Soc. 26 (2013); M. Henk and
E. Linke, Cone-volume measures of polytopes, Adv. Math. 253 (2014); G. Zhu, The
logarithmic Minkowski problem for polytopes, Adv. Math. 262 (2014); S. Chen,
Y. Feng, W. Liu, Uniqueness of solutions to the logarithmic Minkowski problem
in R^3, arXiv:2202.10074.
