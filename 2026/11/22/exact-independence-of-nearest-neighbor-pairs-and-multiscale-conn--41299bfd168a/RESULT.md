# Exact independence of nearest-neighbor pairs and multiscale connectivity on a random circle

## Finding

Let \(n\ge3\) independent uniform sites lie on a circle of circumference one. Let \(M_n\) be the number of *reciprocal nearest-neighbor pairs*: unordered site pairs in which each site is the other's nearest site under circular geodesic distance. For each connection distance \(r\ge0\), let \(C_n(r)\) be the number of connected components of the hard circular geometric graph obtained by joining sites at distance at most \(r\).

**The entire random variable \(M_n\) is independent of the *whole function* \(\{C_n(r):r\ge0\}\)**, not merely uncorrelated at any fixed radius. More strongly, \(M_n\) is independent of the entire unordered multiset of circular spacings, and therefore of any statistic invariant under permutation of those spacings, including all spacing order statistics and the component-count path. The law of \(M_n\) obeys
\[
\mathbb E[M_n]=n/3,\qquad
\operatorname{Var}(M_n)=\begin{cases}0,&n=3,\\ 2/9,&n=4,\\ 2n/45,&n\ge5.\end{cases}
\]
Thus for any finite collection of radii and any bounded functions \(f,g\),
\[
\mathbb E\bigl[f(M_n)g(C_n(r_1),\dots,C_n(r_m))\bigr]
=\mathbb E[f(M_n)]\,\mathbb E[g(C_n(r_1),\dots,C_n(r_m))].
\]

## Assumptions and scope

The point locations are iid continuous uniform, with exactly \(n\ge3\) sites, a unit circumference, and circular geodesic distances. All ties have probability zero. To define indexed gaps, begin at one site chosen uniformly among the sampled sites and proceed clockwise; the statistics themselves do not depend on the mark. The independence holds at *all* radii simultaneously, without any asymptotic limit. It concerns component *counts*, not the component-size process or isolate count, which depend on the cyclic placement of gaps.

## Proof

Write \(G_1,\ldots,G_n\) for the successive clockwise gaps from the marked site. Their joint distribution is uniform on the positive simplex \(\sum_iG_i=1\), namely \(\operatorname{Dirichlet}(1,\ldots,1)\). Because its density is symmetric and all gaps are distinct almost surely, the vector \(S=(G_{(1)},\ldots,G_{(n)})\) of increasing gap lengths and the permutation \(\Pi\) assigning those lengths to cyclic positions are independent: conditional on \(S\), each of the \(n!\) cyclic rank assignments has equal probability.

A site is nearest to one of its two neighbors in cyclic order. Two consecutive sites separated by gap \(G_i\) are reciprocal nearest neighbors if and only if \(G_i<G_{i-1}\) and \(G_i<G_{i+1}\) (cyclic indices). The statement remains true when another gap exceeds half the circumference: the other route around the circle then includes an even closer cyclic neighbor. Hence
\[
M_n=\sum_{i=1}^{n}\mathbf1\{G_i<\min(G_{i-1},G_{i+1})\},
\]
which is measurable with respect to \(\Pi\) alone.

For \(0<r<1/2\), put \(L_n(r)=\sum_i\mathbf1\{G_i>r\}\). If at least two gaps exceed \(r\), each such gap separates two components, so \(C_n(r)=L_n(r)\). With zero or one gap exceeding \(r\), all sites connect around the complementary circular arc, so \(C_n(r)=1\). Thus
\[
C_n(r)=\max(1,L_n(r))\quad(0<r<1/2),
\]
with the same connected value at \(r\ge1/2\) and with singleton components at \(r=0\). Consequently the whole component-count path is measurable with respect to \(S\), since each \(L_n(r)\) counts order statistics above \(r\). Independence of \(\Pi\) and \(S\) proves the asserted process-level independence and the stronger symmetric-statistic statement.

Each cyclic gap has probability \(1/3\) to be smaller than its two neighboring gaps, giving \(\mathbb E M_n=n/3\). For \(n\ge5\), two adjacent local-minimum indicators are incompatible, giving covariance \(-1/9\); indicators separated by two positions are both one with probability \(2/15\), giving covariance \(1/45\); and those separated by at least three positions are independent because they inspect disjoint ranks in a uniform random permutation. Summing cyclic covariances yields \(\operatorname{Var}(M_n)=2n/45\). At \(n=3\), precisely one gap is a cyclic local minimum, while at \(n=4\) direct rank enumeration gives probabilities \(2/3\) and \(1/3\) for one and two minima, respectively, giving the stated exceptional variances.

## Verification

The standalone `verify.py` enumerates every cyclic permutation for sizes three through eight and counts local minima, comparing the exact first two moments with the stated formulas. For multiple fixed strictly ordered spacing profiles it also independently checks that every possible placement generates the identical nearest-neighbor-count distribution. The script uses only Python's standard library and exact rational arithmetic: `python3 verify.py`. The all-size independence and moment statements are proved analytically, not extrapolated from enumeration.

## Relationship to prior work

Uniform circular spacing exchangeability is classical. Decreusefond and Ferraz analyze component counts in one-dimensional Poisson geometric graphs, not their independence from reciprocal-neighbor structure in a fixed-size uniform circle sample. Existing results for reciprocal-neighbor counts give the \(n/3\) mean, and recent comparisons with *isolated-vertex counts* exhibit nonzero negative covariance. The contrast is important: the count of isolated vertices depends on adjacency of threshold-exceeding gaps, whereas the number of components depends only on their number. These closest identified statements do not supply independence of the reciprocal-pair count from the entire connected-component process; the result follows from a clean structural separation between cyclic gap ranks and their sorted magnitudes.

## Limitations

This is an exact structural independence in the uniform circular model, not in nonuniform sampling or on an interval with boundaries. It does not claim independence from all geometric-graph observables: isolated vertices, edge count, and component sizes retain positional information. The proof uses classical rank/order-statistic independence, so the primary novelty claim is the full network-process consequence and explicit finite variance, not that underlying standard theorem. An exhaustive historical-priority check of older nearest-neighbor and spacing literature remains open; independent audit has not been performed.

## References

- Laurent Decreusefond and Eduardo Ferraz, *On the One dimensional Poisson Random Geometric Graph*, first public preprint 2010-08-30, https://arxiv.org/abs/1008.5140 ; https://doi.org/10.1155/2011/350382 .
- Thierry Huillet, *Random covering of the circle: the size of the connected components*, 2003, https://doi.org/10.1239/aap/1059486818 .
- Classical elementary fact: independence of ranks and ordered observations for an exchangeable continuous sample, applied here to uniform Dirichlet spacings. No priority is claimed for this underlying probabilistic identity.
