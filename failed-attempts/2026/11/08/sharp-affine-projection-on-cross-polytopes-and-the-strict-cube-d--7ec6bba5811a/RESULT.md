# Sharp affine projection on cross-polytopes and the strict cube-duality gap

## Finding

For every integer \(d\ge1\), set
\[
 B_{1}^{d}=\{x\in\mathbb R^{d}:\textstyle\sum_{i=1}^{d}|x_i|\le1\},
 \qquad B_{\infty}^{d}=[-1,1]^d.
\]
Both bodies carry normalized Lebesgue volume. Let \(P_{1,d}\) and \(P_{\infty,d}\) be the real \(L^2\)-orthogonal projectors onto the affine functions on the respective bodies, viewed as operators on \(L^\infty\). Their sharp norms are denoted by \(\Lambda_{1,d}\) and \(\Lambda_{\infty,d}\).

**Theorem.** The cross-polytope projector has the exact rational norm
\[
 \boxed{\Lambda_{1,d}=1+\frac{d+2}{2}
 \left(\frac{d(d+3)}{(d+1)(d+2)}\right)^{d+1}.}
\]
Exactly its \(2d\) vertices \(\{\pm e_i:1\le i\le d\}\) maximize the evaluation-kernel norm. For each such vertex \(v\), precisely the functions \(\pm\operatorname{sgn}(1+c_d v\cdot y)\), up to null sets, are norming real \(L^\infty\) inputs for evaluation at \(v\), where \(c_d=(d+1)(d+2)/2\). For \(0\le f\le1\), the sharp possible negative value of \((P_{1,d}f)(x)\) is
\[
 \boxed{-\frac{\Lambda_{1,d}-1}{2}.}
\]
The sequence \(\Lambda_{1,d}\) increases strictly with dimension, and
\[
 \boxed{\Lambda_{1,d}=\frac d2+1+\frac1d-\frac{11}{3d^2}+O(d^{-3}).}
\]
For the polar dual pair of regular polytopes, the sharp dimensional comparison is
\[
 \boxed{\Lambda_{1,d}=\Lambda_{\infty,d}\quad(d=1,2),\qquad
 \Lambda_{1,d}>\Lambda_{\infty,d}\quad(d\ge3).}
\]
Moreover, \(\Lambda_{\infty,d}\sim\sqrt{6d/\pi}\), so
\[
 \frac{\Lambda_{1,d}}{\Lambda_{\infty,d}}\sim\sqrt{\frac{\pi d}{24}}.
\]
Thus duality between the cube and cross-polytope does not preserve the uniform instability of their affine least-squares projectors: the former has square-root growth, the latter linear growth.

## Assumptions and scope

The input functions and coefficients are **real**, with \(L^\infty\) understood relative to normalized \(d\)-dimensional volume, not surface measure or vertex counting. The projector is \(L^2\)-orthogonal projection onto degree-at-most-one algebraic polynomials; it is not nearest-point projection in \(\mathbb R^d\) or a Banach-space minimal projection constant. Norming functions are measurable and may be discontinuous. For continuous inputs the same operator-norm supremum follows by approximation, but equality need not be attained by a continuous input.

## Proof

**1. Projection kernel and cross-polytope moments.** Let \(Y\) be uniformly distributed in \(B_1^d\). Sign and permutation symmetry give \(\mathbb EY_i=0\) and \(\mathbb E(Y_iY_j)=0\) for \(i\ne j\). In a positive orthant, the absolute values and unused radial slack have the uniform simplex distribution, whence
\[
 \mathbb EY_i^2=\frac{2}{(d+1)(d+2)}=c_d^{-1}.
\]
Therefore the affine orthogonal projection has the continuous kernel
\[
 (P_{1,d}f)(x)=\int_{B_1^d}K_d(x,y)f(y)\,d\mu_d(y),
 \qquad K_d(x,y)=1+c_dx\cdot y.
\]
Its norm is \(\sup_{x\in B_1^d}L_d(x)\), where \(L_d(x)=\int|K_d(x,y)|\,d\mu_d(y)\).

**2. Unique norming evaluation sites.** The map \(x\mapsto L_d(x)\) is convex and invariant under signed coordinate permutations. Since \(B_1^d\) is the convex hull of \(\{\pm e_i\}\), every point has \(L_d(x)\le L_d(e_1)\). The inequality is strict for every nonvertex. Indeed, for any two distinct vertices \(v,w\), choose \(y=-tv\) with \(1/c_d<t<1\). Then \(K_d(v,y)<0<K_d(w,y)\); by continuity this sign disagreement holds on an open subset of positive volume. Hence the triangle inequality for any nontrivial convex combination of distinct vertex kernels is strict after integration. All and only vertices are norming evaluation sites. Equality in \(|\int K_df|\le\int|K_d|\) with \(|f|\le1\) gives the asserted kernel-sign norming inputs.

**3. One-dimensional beta integration.** The variable \(|Y_1|\) has density \(d(1-u)^{d-1}\), \(0<u<1\). Pairing the signs of \(Y_1\) yields
\[
 \begin{aligned}
 L_d(e_1)&=\mathbb E\max\{1,c_d|Y_1|\}\\
 &=1+d\int_{1/c_d}^{1}(c_du-1)(1-u)^{d-1}\,du\\
 &=1+\frac{c_d}{d+1}\left(1-\frac1{c_d}\right)^{d+1},
 \end{aligned}
\]
which is the claimed rational expression. Since \(\int K_d(x,y)\,d\mu_d(y)=1\), its negative mass is \((L_d(x)-1)/2\), proving the exact global positivity defect with input \(f=\mathbf1_{\{K_d(v,\cdot)<0\}}\).

**4. Strict dimension growth and expansion.** For real \(s\ge1\), put
\[
 z(s)=\frac{2}{(s+1)(s+2)},\quad
 h(s)=(s+1)\log(1-z(s)).
\]
As \(0<z(s)<1\), the elementary strict bound \(\log(1-z)>-z/(1-z)\) implies
\[
 h'(s)>\frac{-z(s)-(s+1)z'(s)}{1-z(s)}
 =\frac{z(s)(s+1)}{(s+2)(1-z(s))}>0.
\]
Thus \((1-z(d))^{d+1}\) increases strictly with \(d\), as does its product with \((d+2)/2\). Taylor expansion at \(d^{-1}=0\) gives
\[
 (d+1)\log(1-z(d))=-\frac2d+\frac4{d^2}-\frac{10}{d^3}+O(d^{-4}),
\]
which yields the displayed expansion. In addition, strict Bernoulli's inequality gives
\[
 \left(1-\frac2{(d+1)(d+2)}\right)^{d+1}>
 1-\frac2{d+2}=\frac d{d+2},
\]
so \(\Lambda_{1,d}>1+d/2\) for every \(d\ge1\).

**5. Comparison with the cube.** On \([-1,1]^d\), covariance is \(I_d/3\). Convexity and vertex symmetry similarly yield
\[
 \Lambda_{\infty,d}=\mathbb E\left|1+3\sum_{i=1}^{d}U_i\right|,
\]
where the \(U_i\) are independent uniform variables on \([-1,1]\). Consequently Cauchy--Schwarz gives \(\Lambda_{\infty,d}\le\sqrt{1+3d}\). For \(d\ge8\),
\[
 \Lambda_{1,d}>1+\frac d2\ge\sqrt{1+3d}\ge\Lambda_{\infty,d},
\]
using \((1+d/2)^2\ge1+3d\iff d\ge8\).

For \(1\le d\le7\), compute the cube norm without numerical integration. If \(T=\sum_{i=1}^d(U_i+1)/2\), then \(T\) is Irwin--Hall distributed; put \(a=(3d-1)/6\). Integration of its exact distribution function gives
\[
 \Lambda_{\infty,d}=1+\frac{12}{(d+1)!}
 \sum_{k=0}^{\lfloor a\rfloor}(-1)^k\binom dk(a-k)^{d+1}.
\]
The exact differences \(\Lambda_{1,d}-\Lambda_{\infty,d}\), for \(d=1,2,3,4,5,6,7\) respectively, are
\[
 0,\quad0,\quad\frac{25441}{324000},\quad
 \frac{1157537}{5400000},\quad
 \frac{95570849}{245046060},\quad
 \frac{65888467818191}{110658879959040},\quad
 \frac{18078122324483}{21941965946880}.
\]
These establish all remaining cases. Finally, the classical central limit theorem and uniform integrability give \(\Lambda_{\infty,d}/\sqrt d\to\sqrt{6/\pi}\), because \(3\sum U_i\) has variance \(3d\). Combining with the cross-polytope expansion proves the ratio asymptotic.

## Verification

The independent exact-rational script `check_crosspoly.py` recomputes the cross-polytope integrals by expanding the beta density, verifies the covariance and closed formula in 63 dimensions, checks strict monotonicity there as a diagnostic, and computes the low-dimensional cube comparison by Irwin--Hall integration. Its terminal message is `ALL_CROSSPOLY_AFFINE_CHECKS_PASSED`. The infinite-dimensional-parameter theorem is established by the preceding analytical inequalities, not by finite testing.

## Relationship to prior work

Least-squares projector \(L^\infty\) stability is classical; Hangelbroek, Narcowich, Sun and Ward (2010) study local kernel spaces on smooth manifolds and prove boundedness using local stable bases, not the present full-dimensional cross-polytope affine kernel or a dimension-by-dimension norm. Białas-Cież, Kenne, Sommariva and Vianello (2023/2024) develop numerical polynomial meshes for evaluating Lebesgue constants on cubes, simplices and Euclidean balls; their general polytope framework does not present this exact cross-polytope volume-projection formula or its strict comparison with the cube. The affine cube projector, its convex vertex reduction and the Irwin--Hall formula are not claimed as new. The claimed contribution is the cross-polytope exact law together with its complete norming classification and sharp dimension-uniform duality gap. A targeted check of mathematical research records and accessible related claims found no statement implying the full theorem, but this is not a proof of publication priority.

## Limitations

The result does not assert a comparison for all polar convex bodies, all Hanner polytopes or arbitrary sampling measures. It does not treat higher-degree polynomial subspaces, complex-coefficient normers or optimal projections among all possible linear projectors. Continuous functions need not realize the \(L^\infty\) norm exactly, although their supremum norm equals it. Bibliographic incompleteness remains possible.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first posted 2010-05-13). https://arxiv.org/abs/1005.2424
2. L. Białas-Cież, D. J. Kenne, A. Sommariva, M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656 (first posted 2023-11-30); ETNA 60 (2024), 428–445. https://arxiv.org/abs/2311.18656
