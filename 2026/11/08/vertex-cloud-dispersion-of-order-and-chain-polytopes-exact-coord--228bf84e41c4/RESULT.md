# Vertex-cloud dispersion of order and chain polytopes: exact coordinate gaps and equality

## Finding

For every finite poset \(P\) of size \(d\geq1\), let \(\mathcal O(P)\) and \(\mathcal C(P)\) denote its standard order and chain polytopes in \(\mathbb R^d\). For a finite vertex set \(V\) and nonnegative diagonal weights \(w=(w_x:x\in P)\), define the mean weighted squared pairwise vertex separation
\[
\mathscr E_w(V)=\frac{1}{|V|^2}\sum_{u,v\in V}\sum_{x\in P}w_x(u_x-v_x)^2.
\]
Let \(N\) be the number of order ideals of \(P\). For each \(x\in P\), let \(a_x\) be the number of ideals containing \(x\), and \(b_x\) the number of ideals in which \(x\) is maximal. Then the exact identity is
\[
\boxed{\mathscr E_w(\operatorname{vert}\mathcal O(P))-\mathscr E_w(\operatorname{vert}\mathcal C(P))
=\frac{2}{N^2}\sum_{x\in P} w_x(a_x-b_x)(N-a_x-b_x).}
\]
Every summand is nonnegative. A summand with \(w_x>0\) is positive exactly when \(x\) is neither minimal nor maximal in \(P\). In particular, for every strictly positive diagonal weight vector, equality holds if and only if \(P\) has height at most two. More generally, equality for nonnegative weights holds precisely when every positively weighted element is minimal or maximal.

There is no analogous positive-semidefinite comparison of the *full covariance matrices*: for the three-element chain, the linear projection onto \((1,0,-1)\) has variance \(1/4\) for the order-polytope vertex cloud but \(1/2\) for the chain-polytope vertex cloud.

## Assumptions and scope

The order polytope has vertices \(\mathbf 1_I\) indexed by down-sets (order ideals) \(I\subseteq P\), and the chain polytope has vertices \(\mathbf 1_A\) indexed by antichains \(A\subseteq P\). The map \(I\mapsto\max(I)\) is a bijection between ideals and antichains; \(\max(\varnothing)=\varnothing\). Coordinates use the fixed labeling of the poset; no arbitrary affine equivalence between the two polytopes is assumed. The weighted Euclidean form is diagonal and has \(w_x\geq0\); negative or off-diagonal quadratic coefficients are outside the asserted inequality. The average uses *ordered* independent pairs of vertices, including identical pairs, and is normalized by \(N^2\).

## Proof

**1. Coordinate occurrence probabilities.** By the classical vertex descriptions, the order-polytope \(x\)-coordinate equals one on exactly \(a_x\) of its \(N\) vertices. By the maximal-element bijection, the chain-polytope \(x\)-coordinate equals one on exactly \(b_x\) vertices. For any family of \(N\) binary vectors with coordinate-one count \(c_x\), the number of ordered pairs with different \(x\)-coordinates is \(2c_x(N-c_x)\). Hence the coordinate contribution to the difference is
\[
\frac{2}{N^2}\bigl(a_x(N-a_x)-b_x(N-b_x)\bigr)
=\frac{2}{N^2}(a_x-b_x)(N-a_x-b_x).
\]
Summation with weights proves the identity.

**2. The two injection inequalities.** Every ideal having \(x\) maximal contains \(x\), so \(b_x\le a_x\). Deleting \(x\) from such an ideal gives another ideal not containing \(x\). The deletion map is injective, so \(b_x\le N-a_x\). Both factors in the identity are therefore nonnegative.

**3. Exact equality for an individual coordinate.** We have \(a_x=b_x\) if and only if \(x\) is maximal: if \(x\) is maximal, its membership always implies maximality within an ideal; conversely, if \(x<y\), the principal ideal \(\downarrow y\) contains \(x\) without making it maximal. Also \(b_x=N-a_x\) if and only if \(x\) is minimal: for a minimal \(x\), adding \(x\) to an ideal that omits it gives an ideal with \(x\) maximal, inverse to deletion; if \(x\) has a predecessor, the empty ideal cannot be obtained by deleting maximal \(x\), since adding \(x\) to the empty set is not an ideal. Consequently the product is strictly positive exactly at the elements having both a strict predecessor and a strict successor. Such an element exists if and only if \(P\) contains a three-element chain. With strictly positive weights this is precisely the strictness criterion; allowing zero weights gives the stated coordinatewise equality description.

**4. Quantitative unbounded separation.** For a chain on \(d\geq3\) elements, order-polytope vertices are indicators of its \(d+1\) initial intervals, and chain-polytope vertices are \(0,e_1,\ldots,e_d\). Under unit weights, direct summation over ordered pairs yields
\[
\mathscr E_{\mathbf1}(\operatorname{vert}\mathcal O(P))
=\frac{d(d+2)}{3(d+1)},\qquad
\mathscr E_{\mathbf1}(\operatorname{vert}\mathcal C(P))
=\frac{2d^2}{(d+1)^2}.
\]
Their ratio is \(\frac{(d+1)(d+2)}{6d}\), which diverges linearly with \(d\). Thus the all-pairs comparison is not a negligible perturbation of the edge-level comparison.

**5. Sharp limitation on oblique metrics.** For the three-element chain \(1<2<3\), the two four-point vertex clouds are \(\{000,100,110,111\}\) and \(\{000,100,010,001\}\). Under the linear functional \(x_1-x_3\), their uniform distributions are respectively \(\{0,1,1,0\}\) and \(\{0,1,0,-1\}\), with variances \(1/4\) and \(1/2\). Hence the coordinatewise comparison does not assert Loewner domination of covariance matrices or domination for arbitrary positive-semidefinite quadratic metrics.

## Verification

The standalone file `verify.py` enumerates every poset admitting an increasing labeling on at most six elements (including redundant edge specifications), using exact integer arithmetic. It reconstructs all ideals and maximal antichains independently, compares ordered-pair Hamming-distance sums and each coordinate's contribution with the claimed factorization, checks the strictness criterion, tests chain examples through twenty elements, and checks the oblique-projection counterexample. Running `python3 verify.py` prints `VERTEX_DISPERSION_EXACT_OK 33867 posets; chain checks 18; boundary check PASS`. The finite enumeration is supplementary; the proof covers every finite poset and every nonnegative diagonal weight vector.

## Relationship to prior work

Stanley's theory gives the order/chain-polytope vertex descriptions and the bijection between ideals and antichains. Lee's 2026 edge theorem identifies correspondences between edges and shows edge-length domination and matching edge-direction counts; a later abstract also mentions pair counts stratified by the number of connected symmetric-difference components. Those statements do not yield an exact *coordinatewise all-vertex-pair* second-moment identity, nor its equality classification, by their stated conclusions. The three-element chain already has different all-pairs distance distributions despite matching edge counts. The present result studies the uniform vertex cloud, rather than the uniform geometric volume measure or only edges.

## Limitations

The finding is an exact identity for standard coordinate embeddings and diagonal metrics; it is not affine-invariant and does not imply any stochastic ordering of the complete pair-distance distributions, nor a positive-semidefinite covariance inequality. No assertion is made about continuous uniform samples from the polytopes. The final October 2026 revision of Lee's paper was available in abstract form, whereas its complete later text could not be inspected; this is a residual historical-priority risk. Independent mathematical audit has not been performed.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. Classical vertex descriptions, cited in the paper below.
2. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413, first public version October 5, 2026; later revision October 24, 2026. https://arxiv.org/abs/2610.07413
3. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, December 21, 2023. https://arxiv.org/abs/2312.13890
