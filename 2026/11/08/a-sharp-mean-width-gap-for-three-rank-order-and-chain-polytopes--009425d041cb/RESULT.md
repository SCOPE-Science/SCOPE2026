# A sharp mean-width gap for three-rank order and chain polytopes

## Finding

Let \(A_m\) denote an antichain of \(m\) elements, and define the three-level ordinal-sum poset \(P_m=A_m\oplus A_m\oplus A_m\), for each integer \(m\ge1\). Its standard order polytope \(\mathcal O_m\) and chain polytope \(\mathcal C_m\) both lie in \(\mathbb R^{3m}\), with the inherited Euclidean metric.

For a compact convex set \(K\subset\mathbb R^d\), define its mean directional width by
\[
w(K)=\mathbb E_{U\sim\operatorname{Unif}(S^{d-1})}\bigl[h_K(U)+h_K(-U)\bigr],\qquad h_K(u)=\max_{x\in K}\langle u,x\rangle.
\]
Set \(a=1-1/\pi\), \(b=2-1/\pi\). As \(m\to\infty\),
\[
\boxed{w(\mathcal C_m)=\sqrt{\frac{2}{3\pi}}\sqrt m+\frac{3\sqrt a}{\sqrt{6\pi}}+o(1),}
\]
\[
\boxed{w(\mathcal O_m)=\sqrt{\frac{2}{3\pi}}\sqrt m+\frac{2\sqrt a+\sqrt b}{\sqrt{6\pi}}+o(1).}
\]
Consequently, there is a **strict, dimension-independent limiting Euclidean-width separation**:
\[
\boxed{\lim_{m\to\infty}\bigl(w(\mathcal O_m)-w(\mathcal C_m)\bigr)
=\frac{\sqrt{2-1/\pi}-\sqrt{1-1/\pi}}{\sqrt{6\pi}}
\approx0.1085207903.}
\]
The order and chain polytopes have the same Ehrhart polynomial and hence the same Euclidean volume for every \(m\), so this is a metric distinction not determined by their shared lattice-counting data. The result also gives a joint weak limit for their centered Gaussian support maxima, as described below.

## Assumptions and scope

An element in an earlier level of \(P_m\) is smaller than every element of a later level; within each level, distinct elements are incomparable. Label the three levels from top to bottom by \(1,2,3\). For a Gaussian direction \(G\in\mathbb R^{3m}\), let \(G_{jk}\) denote its \(k\)-th coordinate in level \(j\), and define
\[
S_j=\sum_{k=1}^m(G_{jk})_+,\qquad T_j=\sum_{k=1}^mG_{jk},\qquad (t)_+=\max(t,0).
\]
All \(G_{jk}\) are independent standard normal random variables. No stochastic sampling of polytope vertices or of points inside either polytope is involved; randomness is solely the Euclidean direction.

## Proof

**1. Exact support reduction.** By Stanley's vertex descriptions, vertices of an order polytope are indicators of filters, and those of a chain polytope are indicators of antichains. A filter in this three-level poset is either a subset of the top level, all of the top level together with a subset of the middle, or both complete upper levels with a subset of the bottom. Antichains are subsets of a single level. Maximizing the Gaussian linear functional therefore gives the exact identities, without limiting approximations,
\[
h_{\mathcal O_m}(G)=\max\{S_1,T_1+S_2,T_1+T_2+S_3\},\qquad
h_{\mathcal C_m}(G)=\max\{S_1,S_2,S_3\}.
\]
The empty filter and antichain need not appear separately since each \(S_j\ge0\).

**2. Centering and multivariate central limit theorem.** Put \(\mu=1/\sqrt{2\pi}\) and \(v=1-2/\pi\). Define
\[
Z_{j,m}=\frac{T_j}{\sqrt m},\quad
B_{j,m}=\frac{\sum_{k=1}^m|G_{jk}|-m\sqrt{2/\pi}}{\sqrt m},\quad
Y_{j,m}=\frac{Z_{j,m}+B_{j,m}}2.
\]
The identity \((t)_+=(t+|t|)/2\) yields \(S_j=m\mu+\sqrt m\,Y_{j,m}\) exactly. The bivariate summand \((G,|G|-\sqrt{2/\pi})\) has zero cross-covariance because \(\mathbb E[G|G|]=0\). Its variance matrix is \(\operatorname{diag}(1,v)\). Independence across the levels and the multivariate central limit theorem imply joint convergence of the nine variables needed below to independent Gaussian pairs \((Z_j,B_j)\), where \(Z_j\sim N(0,1)\), \(B_j\sim N(0,v)\).

Writing \(Y_j=(Z_j+B_j)/2\), the centered support maxima divided by \(\sqrt m\) converge jointly in distribution to
\[
M_O=\max\{Y_1,Z_1+Y_2,Z_1+Z_2+Y_3\},\qquad
M_C=\max\{Y_1,Y_2,Y_3\}.
\]
These are the limits of \((h_{\mathcal O_m}(G)-m\mu)/\sqrt m\) and \((h_{\mathcal C_m}(G)-m\mu)/\sqrt m\). Each finite maximum is bounded in absolute value by a finite sum of absolute values of \(Z_{j,m}\) and \(B_{j,m}\), whose second moments are bounded uniformly in \(m\). Uniform integrability therefore upgrades both weak limits to convergence of expectations. This step is essential: convergence in distribution alone would not justify the mean-width asymptotics.

**3. The three-Gaussian-maximum identity.** If \(X_1,X_2,X_3\) are jointly centered Gaussian, then
\[
\mathbb E\max(X_1,X_2,X_3)
=\frac1{2\sqrt{2\pi}}\sum_{1\le i<j\le3}
\sqrt{\operatorname{Var}(X_i-X_j)}.
\]
Indeed, represent \(X_i=\langle g,v_i\rangle\) with a standard Gaussian \(g\) and deterministic vectors \(v_i\). The three vectors form a possibly degenerate planar triangle. On its two-dimensional difference span, the Gaussian direction has independent radial and angular parts, with mean radial length \(\sqrt{\pi/2}\). The Cauchy perimeter formula says that the angular mean of the triangle's support function is its perimeter divided by \(2\pi\). Orthogonal translation components have mean zero. This proves the identity; degenerate triangles follow by continuity.

For \(M_C\), every one of the three pairwise Gaussian differences has variance
\[
a=\operatorname{Var}(Y_i-Y_j)=1-1/\pi.
\]
For \(M_O\), successive pair differences have variance \(a\) while the first-to-third difference has variance \(b=2-1/\pi\). These follow by expanding the independent \(Z_j,B_j\) terms. Hence
\[
\mathbb EM_C=\frac{3\sqrt a}{2\sqrt{2\pi}},\qquad
\mathbb EM_O=\frac{2\sqrt a+\sqrt b}{2\sqrt{2\pi}}.
\]
In particular \(\mathbb EM_O-\mathbb EM_C=(\sqrt b-\sqrt a)/(2\sqrt{2\pi})>0\).

**4. Gaussian-to-spherical normalization.** For \(G\sim N(0,I_{3m})\), write \(G=RU\), where \(R=\|G\|_2\) is independent of \(U\), and \(U\) is uniformly distributed on the sphere. By positive homogeneity of support functions,
\[
w(K)=\frac{2\mathbb E h_K(G)}{\mathbb ER},\qquad
\mathbb ER=\sqrt2\frac{\Gamma((3m+1)/2)}{\Gamma(3m/2)}=\sqrt{3m}\,(1+O(m^{-1})).
\]
Steps 1–3 yield
\[
\mathbb E h_{\mathcal C_m}(G)=m\mu+\sqrt m\,\frac{3\sqrt a}{2\sqrt{2\pi}}+o(\sqrt m),
\]
\[
\mathbb E h_{\mathcal O_m}(G)=m\mu+\sqrt m\,\frac{2\sqrt a+\sqrt b}{2\sqrt{2\pi}}+o(\sqrt m).
\]
Substitution proves both displayed expansions and the positive limiting difference. The \(O(m^{-1})\) radial correction affects only the \(o(1)\) terms of the spherical expansions.

## Verification

The standalone program `check_mean_width.py` enumerates all binary vertices for the smallest three values of \(m\), checks the support formulas against direct linear optimization, and independently tests the Gaussian maximum identity and the finite-size asymptotic gap using seeded Gaussian simulation. Execute with `python3 check_mean_width.py` (NumPy required). It reports `THREE_RANK_ORDER_CHAIN_MEAN_WIDTH_CHECKS_PASSED` when all tests succeed. The computed limit is about \(0.1085207903\). These numerical checks are corroboration, not an infinite proof; the proof is the exact reduction, central limit argument, and Gaussian-perimeter identity above.

## Relationship to prior work

Stanley (1986) introduced order and chain polytopes and established their Ehrhart equivalence. Ahmad–Fourier–Joswig (arXiv:2309.01626, first version September 4, 2023) study the same maximal ranked posets and the face-number monotonicity of chain–order interpolants. Freij-Hollanti–Lundström (arXiv:2312.13890) study face-number inequalities and geometric operations under ordinal sums. Fourier (arXiv:2609.23629), Lee (arXiv:2610.07413), and Goel (arXiv:2610.40703) provide stronger later face-count and edge-length comparisons. These results concern combinatorial data or edge lengths and do not calculate directional mean width or the specific Gaussian support limit and constant obtained here. Ehrhart equivalence does not preserve Euclidean mean width because a unimodular transformation need not be an isometry.

The rank-three family is a natural first test beyond the two-level case: for an ordinal sum of two antichains, complementing every coordinate in the upper level gives an actual Euclidean isometry between the order and chain polytopes, so their mean widths agree exactly. The strict three-level asymptotic gap is consequently a metric separation not explained by their common lattice-point enumeration. The assertion of historical originality is provisional, not a priority certificate.

## Limitations

The theorem is for three equal-sized levels and standard coordinate Euclidean geometry, with \(m\to\infty\). It does not claim a non-asymptotic strict mean-width inequality in every finite dimension, an explicit convergence rate, or the same constant for unequal level sizes, arbitrary posets, or alternative metric embeddings. Finite simulations do not certify any infinite limit. Independent mathematical audit has not been performed. An equivalent result in older Gaussian-maximum or intrinsic-volume literature could affect historical priority.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, https://doi.org/10.1007/BF02187680.
2. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first posted 2023-09-04, https://arxiv.org/abs/2309.01626.
3. R. Freij-Hollanti, T. Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first posted 2023-12-21, https://arxiv.org/abs/2312.13890.
4. G. Fourier, *The Hibi–Li Face-Number Conjecture*, arXiv:2609.23629, https://arxiv.org/abs/2609.23629.
5. J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413, https://arxiv.org/abs/2610.07413.
6. D. Goel, *The Hibi–Li (2016) conjecture is fully resolved*, arXiv:2610.40703, https://arxiv.org/abs/2610.40703.
