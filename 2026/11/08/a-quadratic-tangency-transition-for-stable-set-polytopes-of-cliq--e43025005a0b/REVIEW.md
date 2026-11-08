# Self-review

## Correctness — PASS

The domain is all integers \(a\ge2\), \(t\ge1\), for the standard Euclidean stable-set polytope of the graph join \(K_t\vee C_{2a+1}\). Miyazaki (arXiv:2205.01409v1, Section 2) records the t-perfect complete inequality description for an odd cycle. Homogenizing those facets with the hub simplex gives exactly \(N\) coordinate, \(2a+1\) lifted edge, and one odd-hole facet. Every norm is computed in the actual ambient metric. Coordinate inequalities force every center coordinate to be at least the radius; summing their contribution to both families yields the two global upper bounds. The equal-coordinate center attains them, and equality forces all coordinates. Rationalizing the difference of the competing denominators gives the unique nonnegative equality point \(t=a^2-2a-1\). Verified finite hull/facet-rank and LP checks are separate numerical corroboration, not infinite proof.

## Originality — PASS; priority provisional

Read the primary full texts of Miyazaki, *Non-Gorenstein locus and almost Gorenstein property of the Ehrhart ring of the stable set polytope of a cycle graph* (arXiv:2205.01409v1), and de Vries–Friedrich–Perscheid, *An extended formulation for the 1-wheel inequalities of the stable set polytope* (doi:10.1002/net.21906), comparing the complete facet premises with the proposed inball and tangency statements. Their cycle/1-wheel inequality descriptions do not cover the Euclidean metric classification. A related published perfect-graph stable-set inradius theorem cannot cover graphs containing induced odd cycles; wheel stable-set circumball results optimize a different objective. Wheel *symmetric-edge* polytope inradius results concern a different convex body. Targeted mathematical search and accessible earlier findings disclosed no equivalent exact tangential classification. Search failure does not certify uniqueness or historical priority.

## Value — PASS

The theorem gives the exact Euclidean inradius, unique incenter and all-facet contact structure for a natural infinite family of imperfect-graph stable-set polytopes. Particularly, the sharp quadratic integer threshold creates infinitely many fully tangential polytopes while all immediately adjacent clique sizes have fewer contacts. This is a geometric transition in an established polytope family rather than just a facet enumeration or numerical calculation.

## Limits and audit status

Only \(K_t\vee C_{2a+1}\), \(a\ge2\), \(t\ge1\), and unweighted indicator-coordinate Euclidean geometry are covered. The historical comparison is necessarily provisional; older equivalent statements under different terminology remain possible. The finite solver tests do not establish the infinite theorem or prove novelty.

Self-review: passed. Independent audit: not yet performed.
