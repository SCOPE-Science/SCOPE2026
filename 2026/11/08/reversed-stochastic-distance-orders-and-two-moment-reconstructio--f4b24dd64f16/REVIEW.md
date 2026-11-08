# Scientific review

## Correctness — PASS

Conditioning on a uniformly chosen ordered pair of edges gives the exact weights \(1/P\), \((n-2)/P\), and \((P-n+1)/P\). The shortest paths on coincident, incident, and nonincident edges are, respectively, \(|U-V|\), \(U+V\), and \(2-|U-V|\). Integrating their elementary CDFs proves both branches and the moments. The equality \(6m_2+8-15\mu=4/P\) reconstructs the product, and the first moment determines the sum. For fixed sum, the CDF is an affine function of reciprocal product with strictly positive slope; this establishes the strict arclength order. Exact enumeration of vertex pairs establishes the reverse vertex order. The symbolic checker verifies the first and second moments and recovery formulas; randomized checks use a separately computed shortest-path matrix.

Boundary checks: \(K_{1,1}\) has the interval-law mean \(1/3\), and \(K_{1,q}\) has no disjoint-edge component. For \(K_{2,2}\), the disjoint-edge distance law is the opposite-edge distance on the metric circle. The tail expression holds exactly on \(0<\varepsilon<1\).

## Originality — PASS (qualified)

An archival metric-geometry comparison, Sánchez (arXiv:1108.0451, primary MSC 51F99), computes p-negative type for the discrete vertex metric on the same bicliques, but not the continuous intrinsic distance distribution. The other closest accessible literature addresses general metric-graph reconstruction (Lecci–Rinaldo–Wasserman), inverse problems for global distance distributions (Mémoli–Needham), mean distances (Baptista–Kennedy–Mugnolo), and discrete vertex-pair averages in bipartite graphs (Shang). The inspected portions do not give the same complete continuous-distance law or the two-moment reconstruction and measure-dependent stochastic reversal. Earlier star mean formulas, generic density structure, and discrete vertex averages are not claimed as new. Exact equivalence with an unindexed older biclique calculation remains a historical-priority risk. Searches of accessible published records and own prior claims found no exact matching result; that negative search alone is not treated as a uniqueness proof.

## Mathematical value — PASS

The object is the canonical one-dimensional length realization of a familiar natural graph family. The law is not an arbitrary finite calculation: it yields a complete infinite-family metric-measure statistic, reconstructs the isometry type from only two moments, and proves a sharp reversal under two equally natural measures on the same shortest-path space. It also detects the presence of cycles through a change of far-distance tail exponent. These properties distinguish the assertion from a formula for one sample shape or routine restatement of graph diameter.

## Remaining limits

This does not treat unequal edge lengths, general graphs, inverse uniqueness outside the specified family, or independently certified novelty. The star endpoint alone is known and is not the novelty claim.

Self-review: passed. Independent audit: not yet performed.
