# Sharp variance and inverse anisotropy of chords in planar equilateral edge-rearrangement ensembles

## Finding
Fix an even integer \(n=2m\ge4\), an integer \(2\le k\le n-2\), and unit vectors \(e_1,\ldots,e_n\in\mathbb R^2\) satisfying \(\sum_j e_j=0\). Independently of their original cyclic order, arrange these edges in a uniformly random order, and let \(R_k\) be the **squared Euclidean length** of the chord spanning the first \(k\) reordered edges. Equivalently, choose a uniformly random \(k\)-subset \(S\subseteq\{1,\ldots,n\}\) and set \(R_k=\|\sum_{j\in S}e_j\|^2\).

Write \(e_j=(\cos\theta_j,\sin\theta_j)\), and define the second angular Fourier statistic
\[
J=\left|\sum_{j=1}^n e^{2\mathrm i\theta_j}\right|^2.
\]
Then the mean and variance over rearrangements are **exactly**
\[
\mathbb E R_k=\frac{k(n-k)}{n-1},\qquad
\operatorname{Var}(R_k)=A_{n,k}+B_{n,k}J,
\]
where
\[
A_{n,k}=\frac{kn(k-1)(n-k)(n-k-1)}{(n-2)(n-1)^2},\qquad
B_{n,k}=\frac{k(k-1)(n-k)(n-k-1)}{n(n-1)(n-2)(n-3)}>0.
\]
Consequently, **the sharp, fully attainable closed-walk range** is
\[
\boxed{\quad A_{n,k}\le\operatorname{Var}(R_k)\le
\frac{2kn(k-1)(n-k)(n-k-1)}{(n-3)(n-1)^2}.\quad}
\]
Equality at the lower end holds **if and only if** the edge directions form a unit-norm tight frame,
\(\sum_j e_j e_j^{\mathsf T}=\tfrac n2 I_2\). Equality at the upper end holds **if and only if** all edges are collinear (necessarily with \(m\) edges in each opposite direction). Every intermediate value is realized by a closed equilateral polygonal walk. Among **strictly convex equilateral polygons**, the lower endpoint and all intermediate values are realized; the upper endpoint is a strict, approachable supremum.

One observed variance for any admissible \(k\), together with known \(n\), determines the unordered eigenvalues of the directional second-moment tensor \(\sum_j e_j e_j^{\mathsf T}\):
\[
\lambda_\pm=\frac{n\pm\sqrt{(\operatorname{Var}(R_k)-A_{n,k})/B_{n,k}}}{2}.
\]
In particular the normalized excess \((\operatorname{Var}(R_k)-A_{n,k})/(n^2B_{n,k})=J/n^2\) is **independent of chord span** \(k\). This is a complete inverse classification of directional anisotropy, not of the polygon's congruence class.

## Assumptions and scope
All edges have Euclidean length exactly one and close in \(\mathbb R^2\). The original polygonal walk need not be embedded or convex, but the endpoint-interval realization additionally holds for embedded strictly convex unit-edge polygons. Different permutations are equiprobable, even if some vectors coincide; indices, rather than distinct geometric vectors, are permuted. The random variable is *squared* chord length, so its variance is a fourth-distance-moment quantity. The dimensions \(n\) and \(k\) are fixed integers in the stated range; \(n\) must be even for the attained collinear upper equality. No independence of the sampled edges is assumed.

## Proof
Put \(g_{ij}=e_i\cdot e_j\) for \(i<j\), \(I_i=\mathbf1_{\{i\in S\}}\), and \(W=\sum_{i<j}g_{ij}I_iI_j\). Unit lengths give \(R_k=k+2W\). Closure implies
\[
\sum_{j\ne i}g_{ij}=-1,\qquad
G:=\sum_{i<j}g_{ij}=-\frac n2.
\]
Set \(T=\sum_{i<j}g_{ij}^2\). Let \(M=\sum_j e_je_j^{\mathsf T}\). Its eigenvalues are \((n\pm\sqrt J)/2\), since \(\operatorname{tr}M=n\) and the difference of the two eigenvalues is the modulus of the second angular harmonic. Hence
\[
2T+n=\operatorname{tr}(M^2)=\frac{n^2+J}{2},\qquad
T=\frac{n^2+J-2n}{4}.
\]
For each unordered pair of distinct unordered index pairs, classify whether they share one index or are disjoint. Let \(H\) denote the sum of the products \(g_{ij}g_{i\ell}\) over all pair-of-pairs meeting in one index, counted once. The closure identity gives
\[
H=\frac12\sum_{i=1}^n\left[\left(\sum_{j\ne i}g_{ij}\right)^2-\sum_{j\ne i}g_{ij}^2\right]=\frac n2-T.
\]
Let \(K\) be the analogous sum over disjoint pair-of-pairs. The identity \(G^2=T+2H+2K\) yields
\[
K=\frac{n(n-4)}8+\frac T2.
\]
Define \(q_r=(k)_r/(n)_r\) for \(r=2,3,4\), where \((x)_r=x(x-1)\cdots(x-r+1)\), and set \(q_r=0\) if \(r>k\). A fixed set of \(r\) distinct indices is included in \(S\) with probability \(q_r\). Therefore
\[
\mathbb EW=q_2G,\qquad
\mathbb EW^2=q_2T+2q_3H+2q_4K.
\]
The first identity yields \(\mathbb ER_k=k+2q_2G=k(n-k)/(n-1)\). Combining the remaining identities,
\[
\begin{aligned}
\operatorname{Var}(R_k)
&=4\bigl[q_2T+2q_3H+2q_4K-q_2^2G^2\bigr]\\
&=4\biggl[\left(q_2-2q_3+q_4\right)\frac{n^2+J-2n}{4}
+nq_3+\frac{n(n-4)}4q_4-\frac{n^2}{4}q_2^2\biggr].
\end{aligned}
\]
Elementary cancellation gives \(q_2-2q_3+q_4=B_{n,k}\), and the \(J\)-free part simplifies to \(A_{n,k}\), proving the exact formula. The identities apply when \(k=2\) or \(3\) because the zero falling-factorial convention eliminates nonexistent selections.

The triangle inequality gives \(0\le J\le n^2\). Since \(B_{n,k}>0\), these are the sharp variance extremes. Vanishing \(J\) is equivalent to \(M=(n/2)I_2\). Equality \(J=n^2\) in the complex triangle inequality forces all \(e^{2\mathrm i\theta_j}\) to coincide, i.e. all edge directions lie on one line; closure then forces precisely \(m\) copies of each sign. Both extrema occur (regular even polygons and balanced backtracking walks, respectively).

To prove full attainability and the stronger convex statement, for \(0<t\le1\) take the directions
\[
\theta_j(t)=\frac{\pi tj}{m},\quad
\theta_{j+m}(t)=\pi+\frac{\pi tj}{m},\qquad j=0,\ldots,m-1,
\]
and use the indicated angular order. The vectors are antipodally paired, so their sum vanishes. Every successive turning angle, including the wrap-around angle, lies strictly between \(0\) and \(\pi\). The walk is strictly convex: for each directed edge, the cross products with successive other edges are nonnegative until their directions pass the opposite ray and are nonpositive thereafter. Their full sum is zero by closure, so all partial sums are nonnegative, proving every vertex lies in that edge's closed left supporting half-plane. Strict turns then give an embedded strictly convex polygon. Its second harmonic obeys
\[
J(t)=4\left|\sum_{j=0}^{m-1}e^{2\pi\mathrm i tj/m}\right|^2,
\qquad J(1)=0,\quad \lim_{t\downarrow0}J(t)=n^2.
\]
Continuity supplies every value strictly below \(n^2\) along these strictly convex polygons; the limit at \(t=0\) is the collinear extremizer. Since the eigenspectrum of \(M\) is \((n\pm\sqrt J)/2\), solving the variance formula recovers the stated anisotropy. This completes the proof.

## Verification
The standalone pure-Python program `chord_variance_verifier.py` constructs closed unit-vector sets using rational parametrizations of the circle. It exhaustively enumerates all \(k\)-subsets for \(n=4,6,8,10\), checks the exact means and variances against the formulas using rational arithmetic, verifies the sharp inequalities, and checks both equality cases at \(n=4,k=2\). The actual output on extraction and execution was `VERIFY_OK exact_subsets=16 geometry_equalities=2`. Separately, symbolic rational-function simplification verifies the displayed variance and upper-end identities (zero residuals). Exhaustive finite cases serve as reproducibility checks, not as a substitute for the quantified analytic argument above.

As an illustrative small case, \(n=4,k=2\) has \(\mathbb ER_k=4/3\), minimum variance \(8/9\) at orthogonal opposite edge pairs, and maximum variance \(32/9\) at balanced collinear edge pairs; the mean alone cannot distinguish the two.

## Relationship to prior work
Zirbel and Millett (arXiv:1204.1366, first public 2012-04-05) compute mean squared interior distances for ideal random rings, using a different distribution over polygons. Cantarella, Deguchi and Shonkwiler (arXiv:1206.3161, first public 2012-06-14), Section 6 and Proposition 15, explicitly define the edge-set permutation ensemble and determine the mean squared chord for a fixed edge set; its dependence on chord span, rather than frame anisotropy, is the corresponding first-moment benchmark. They discuss distinct chord distributions having the same expectation. The result proved here determines the conditional *fourth* moment through the squared-chord variance, its complete sharp shape range for all even \(n\), the convex attainability and the inverse directional tensor spectrum. Cantarella and Shonkwiler (arXiv:1310.5924, first public 2013-10-22) study chord moments under a different global symplectic measure on spatial equilateral polygons. Searches for direct higher-moment edge-set ensemble formulas, finite-population vector subsums, dual frames and dominating results revealed no statement covering the combined theorem, although generic sampling-moment identities remain a historical priority risk. Nonmatching titles or search omissions alone do not establish novelty.

## Limitations
The result is **conditional on a fixed multiset of edges**. It does not give moments under a global distribution of polygon shapes, determine a polygon up to congruence, or address odd edge counts with a sharp attainable upper bound. Rearranged polygons may self-intersect. The extremal upper endpoint requires a degenerate collinear walk, though it is the sharp supremum within strictly convex equilateral polygons. No statistical inference guarantee from finitely many observed permutations is claimed. Historical priority is provisional; the argument and citations should be checked independently before formal publication.

## References
1. L. Zirbel and K. C. Millett, *Characteristics of shape and knotting in ideal rings*, arXiv:1204.1366, first public 2012-04-05. https://arxiv.org/abs/1204.1366
2. J. Cantarella, T. Deguchi and C. Shonkwiler, *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, arXiv:1206.3161, first public 2012-06-14; relevant Section 6, Definition of edge set ensemble and Proposition 15. https://arxiv.org/abs/1206.3161
3. J. Cantarella and C. Shonkwiler, *The Symplectic Geometry of Closed Equilateral Random Walks in 3-Space*, arXiv:1310.5924, first public 2013-10-22; relevant chord moment section. https://arxiv.org/abs/1310.5924
