# Independent mathematical audit

## correctness

PASS

On the clique the centered balls have sizes 1 and n, so the map on positive data is T_i=max(x_i,cΣx) with 1/n<c<1. The absolute-value reduction does not increase the input Euclidean distance. A strict active set of size k>0 must satisfy kc<1 by summing active inequalities, and every such set is feasible with its coordinates equal to one and the others positive and sufficiently small; k=0 occurs for constant positive data. For each cell, counting each undirected edge once gives energy nΣ_{i∈S}|h_i−mean_S(h)|²+k(n−k)|mean_S(h)−cΣh|². The two terms act on orthogonal subspaces: active contrasts with squared singular value n when k≥2, and the rank-one direction u=1_S/k−c1, with eigenvalue k(n−k)||u||²=(n−k)[1+kc(nc−2)]. The empty branch contributes zero. Segment decomposition and continuity give the global upper bound, including tied inputs, and norming directions within strict positive cells give actual distinct positive real attaining inputs. At c=1/2 only k=1 is possible; near it from below both k=1 and k=2 occur and their limiting rank-one values are n(n−1)/4 and (n−2)²/2. Taking the maximum including the k=2 contrast n gives strict left loss for n=3,4 from the contrast and for n≥6 from the rank-one k=2 mode, with equality for n=5. The n=2 case has no admissible c=1/2. At n=6 the two squared values are 8 and 15/2.

## originality

PASS

Pass for the all-size fractional clique Euclidean-to-edge coefficient, feasible-mask spectral formula, and dimension-dependent threshold behavior. The broad phenomenon of jumps for two-input maximal averaging has a close comparison on P₃; no claim of novelty for that general phenomenon alone. The available clique comparisons change the norm, fractionality, or one-input versus two-input structure and do not imply the stated formula.

## value

PASS

An exact perturbation modulus for a standard graph maximal operator answers a stability question not addressed by single-input inequalities. Its spectrum separates contrast and rank-one modes, and strict feasibility rather than continuity of individual maximal outputs controls the jump. The exceptional dimension n=5 and switches in the dominating mode give concrete consequences that a routine upper bound would miss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
