# A sharp dimension-four dependence onset and common-shock Poisson law for sinks of adjacent cube facets

## Finding

For each integer \(d\ge2\), independently orient every edge of the Boolean cube \(Q_d\), each way with probability \(1/2\). For any facet \(F\), let \(S(F)\) be the number of vertices with no outgoing edge **within the induced orientation of \(F\)**; edges leaving \(F\) are ignored. Choose any two distinct facets \(F,G\). Then \(\mathbb E S(F)=\mathbb E S(G)=1\), and the complete two-facet dependence classification is:

- **Opposite facets** (fixing the same coordinate to opposite values) have independent sink counts at every dimension.
- **Adjacent facets** (fixing different coordinates) satisfy the exact identity

\[
\operatorname{Cov}(S(F),S(G))=\frac14-\frac{d-1}{2^d}.
\]

For adjacent facets the counts are independent **exactly when** \(d=2\) or \(d=3\), but have strictly positive covariance for every \(d\ge4\). Their marginal variance is \(1-d/2^{d-1}\). In all dimensions \(d\ge2\), the pair of adjacent-facet counts obeys, in ordinary total-variation distance,

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(S(F),S(G)),\mathcal L(U+W,V+W)\bigr)
 \le 63(d+1)2^{-d},
\]

where \(U,V,W\) are independent Poisson variables with means \(3/4,3/4,1/4\), respectively. In particular, as \(d\to\infty\), the adjacent-facet joint distribution approaches a **non-independent** bivariate Poisson law with both marginals \(\operatorname{Pois}(1)\) and covariance \(1/4\). For opposite facets, each marginal approaches \(\operatorname{Pois}(1)\) and they remain independent. A consequence for two adjacent facets is

\[
\Pr(S(F)=S(G)=0)\longrightarrow e^{-7/4},
\]

rather than the \(e^{-2}\) limit of opposite facets.

## Assumptions and scope

The vertices are \(\{0,1\}^d\); vertices differing in exactly one coordinate are adjacent. Every edge receives an independent fair orientation. A facet fixes one coordinate. The random variable \(S(F)\) counts sinks of the **induced subgraph** on that facet, not sinks in the entire \(d\)-cube. There is no acyclicity, unique-sink, or sink-free conditioning. All finite identities hold for each integer \(d\ge2\), and the total-variation assertion concerns the limit as \(d\to\infty\) with two adjacent facets of any coordinate choices. Cube automorphisms reduce adjacent facets to \(A=\{x_1=0\}\), \(B=\{x_2=0\}\).

## Proof

**1. Exact means, marginal variances and covariance.** Each facet is a copy of \(Q_{d-1}\). Its \(2^{d-1}\) vertices are each a sink with probability \(2^{-(d-1)}\), hence its mean is one. Distinct sink indicators within one facet are independent unless the corresponding vertices are adjacent; adjacent vertices cannot both be sinks. Counting the \(2^{d-1}(d-1)\) ordered adjacent pairs gives

\[
\operatorname{Var}S(F)=1-\frac{d}{2^{d-1}}.
\]

For adjacent facets \(A,B\), write \(H=A\cap B\), which has \(2^{d-2}\) vertices. If \(v\in H\), the events that \(v\) is a sink of each facet simultaneously demand that all \(d\) incident cube edges point into \(v\), giving probability \(2^{-d}\). The same-vertex contribution to the covariance is therefore \(2^{d-2}(2^{-d}-2^{-2d+2})=1/4-2^{-d}\). For distinct \(v\in A,w\in B\), their sink requirements use disjoint sets of oriented edges unless \(v,w\) are adjacent **inside \(H\)**. Each such ordered pair then requires opposite orientations of their shared edge, so the joint event is impossible and the covariance is \(-2^{-2d+2}\). There are \(2^{d-2}(d-2)\) such ordered pairs. Every other distinct pair has independent events. Adding these contributions yields

\[
\operatorname{Cov}(S(A),S(B))=\frac14-2^{-d}-(d-2)2^{-d}
=\frac14-\frac{d-1}{2^d}.
\]

For opposite facets, the induced edge sets are disjoint, giving exact independence. The adjacent-facet covariance is zero at \(d=2,3\) and strictly positive thereafter: \(2^{d-2}>d-1\) for \(d\ge4\).

**2. Exact independence in the two exceptional dimensions.** For \(d=2\), adjacent facets have no shared edges, so their sink counts are independent. For \(d=3\), adjacent facets are squares whose induced edge sets share precisely one edge \(e\). Given its direction, the remaining edge sets of the two squares are disjoint, so their sink counts are conditionally independent. The conditional distribution of the number of sinks on either square does not depend on the direction of \(e\): an automorphism of the square interchanging the endpoints of \(e\) preserves sink count and swaps the two conditional ensembles. Thus the two counts are unconditionally independent. These arguments and the strictly positive covariance for \(d\ge4\) establish the exact threshold.

**3. Three disjoint types of rare events.** At every \(v\in H\), distinguish \(C\): sink in both facets, \(A\): sink in \(A\) but not \(B\), and \(B\): sink in \(B\) but not \(A\). Each event is a conjunction of exactly \(d\) required fair edge directions and hence has probability \(2^{-d}\). Indeed, all \(d-2\) directions within \(H\) must point inward; the two remaining directions select one of the indicated three outcomes. At \(v\in A\setminus H\), mark the event of a sink in \(A\); similarly at \(v\in B\setminus H\). Each exterior atom uses \(d-1\) required directions and has probability \(2^{-(d-1)}\). Let \(N_A,N_B,N_C\) be the counts of these mutually exclusive vertex marks, with exterior atoms included in the corresponding single-facet mark. Exactly,

\[
 S(A)=N_A+N_C,\qquad S(B)=N_B+N_C,
\]

and counting the \(2^{d-2}\) vertices in each of \(H,A\setminus H,B\setminus H\) gives

\[
 \mathbb EN_A=\mathbb EN_B=\tfrac34,\qquad \mathbb EN_C=\tfrac14.
\]

**4. Quantitative joint Poisson approximation.** Index all individual marked events by \(\alpha\). There are \(5\cdot2^{d-2}\) indices, and their total mean is \(7/4\). For each index, take a dependency neighborhood consisting of indices at the same vertex or an adjacent cube vertex. There are at most \(3(d+1)\) indices in any such neighborhood. The event indicators are independent of the entire collection outside their neighborhoods because their prescribed edge orientations are disjoint. Each marginal probability is at most \(2^{1-d}\), so the first Arratia–Goldstein–Gordon neighborhood sum obeys

\[
 b_1=\sum_\alpha\sum_{\beta\in B_\alpha}p_\alpha p_\beta
 \le\frac{21}{2}(d+1)2^{-d}.
\]

For distinct indices at one vertex, the marks are mutually exclusive. For indices at adjacent vertices, their edge requirements overlap in at most one edge. Their joint probability is therefore at most \(2p_\alpha p_\beta\), including the cases where incompatible arrows make it zero. Consequently \(b_2\le2b_1\); the long-range term \(b_3\) is zero. The process bound in Arratia, Goldstein and Gordon (1989), Theorem 2, gives a total-variation distance of at most \(4(b_1+b_2)\) in their doubled convention, or at most \(2(b_1+b_2)\le 63(d+1)2^{-d}\) in the ordinary convention. Grouping independent Poisson atoms by the three marks yields independent \(U,V,W\) with the exactly specified means and proves the quantitative claim. The probability statement follows from the event \(U=V=W=0\).

## Verification

The standalone dependency-free program `checker.py` supplies two independent finite validation mechanisms. It exhausts **all** \(16\) edge orientations of \(Q_2\) and all \(4096\) edge orientations of \(Q_3\), computing the full adjacent-facet joint table and checking independence. Separately it calculates exact probabilities for every ordered pair of facet-sink requirements, verifies the covariance formula for \(2\le d\le8\), and independently enumerates the five marked rare-event atom types and their local-dependence bounds for \(2\le d\le7\). Run `python3 checker.py`. The infinite-dimensional limit is proved analytically in Step 4; finite checks are not used as substitutes for that proof.

## Relationship to prior work

Arratia, Goldstein and Gordon (1989) prove a general Poisson process approximation with local dependence. Their Example 1 explicitly establishes a Poisson approximation for the **single whole-cube sink count**. The present calculation is a specific application of their theorem, not a new Poisson approximation principle: the contribution here is the geometry-dependent three-type facet-overlap decomposition, the explicit common-shock parameter, the complete opposite-versus-adjacent two-facet classification and the finite-dimensional independence threshold. Cohn, Pemantle and Propp (first public arXiv version 2001-03-27) analyze sampling sink-free orientations; they do not condition or couple two coordinate-facet sink counts. Szabó and Welzl (FOCS 2001) study the very different class of *unique-sink orientations*, in which each face is constrained to have exactly one sink. Neither paper claims the present law for unconstrained independent edge directions. Broader probability results may imply further generalizations; historical completeness is not independently established.

## Limitations

This theorem concerns exactly two facets and fair, independent edge directions. It does not assert joint independence across all \(2d\) facets, nor treat biased orientations, sink-conditioned ensembles, or orientations sampled uniformly from the unique-sink class. The finite upper bound is explicit but is not asserted to be sharp. The exact coincidence of the two counts' covariance with zero at dimension three alone would not imply independence; the separate conditioning argument proves that stronger statement. Independent specialist review and exhaustive historical priority verification remain outstanding.

## References

1. R. Arratia, L. Goldstein and L. Gordon, *Two Moments Suffice for Poisson Approximations: The Chen–Stein Method*, Annals of Probability **17** (1989), 9–25, Theorem 2 and Example 1. https://doi.org/10.1214/aop/1176991491 ; author-hosted full text https://dornsife.usc.edu/larry-goldstein/wp-content/uploads/sites/221/2023/06/AGG-1.pdf
2. H. Cohn, R. Pemantle and J. Propp, *Generating a random sink-free orientation in quadratic time*, Electronic Journal of Combinatorics **9** (2002), R10. Original arXiv submission 2001-03-27: https://arxiv.org/abs/math/0103189
3. T. Szabó and E. Welzl, *Unique Sink Orientations of Cubes*, FOCS (2001), 547–555. https://people.inf.ethz.ch/emo/PublFiles/UniqueSink_FOCS42nd_01.pdf
