# Optimal Lipschitz nearest-point selections for real \(\ell_1\) balls

## Finding
For any nonempty index set \(I\), let \(X=\ell_1(I;\mathbb R)\), and, for any radius \(r>0\), let \(B_r=\{x\in X:\|x\|_1\le r\}\). Write
\[
\mathcal P_r(x)=\{y\in B_r:\|x-y\|_1=\operatorname{dist}_1(x,B_r)\}
\]
for the generally set-valued nearest-point map. A *selection* is any mapping \(F:X\to B_r\) satisfying \(F(x)\in\mathcal P_r(x)\) for every \(x\). No regularity, linearity, symmetry, or equivariance is required of a selection. Define its optimal Lipschitz constant by \(\operatorname{Lip}(F)=\sup_{x\ne y}\|F(x)-F(y)\|_1/\|x-y\|_1\), possibly infinite.

**The exact optimum over all selections** is
\[
\boxed{
\inf_{F(x)\in\mathcal P_r(x)\ (\forall x)}\operatorname{Lip}(F)
=
\begin{cases}
1,&|I|=1,\\
2-2/|I|,&2\le |I|<\infty,\\
2,&|I|\text{ infinite}.
\end{cases}}
\]
The infimum is attained in every case. Specifically, when \(\|x\|_1>r\), choose the unique \(\tau>0\) such that
\[
\sum_{i\in I}(|x_i|-\tau)_+=r,
\qquad
Q_r(x)_i=\operatorname{sgn}(x_i)(|x_i|-\tau)_+;
\]
when \(\|x\|_1\le r\), set \(Q_r(x)=x\). Then \(Q_r(x)\in\mathcal P_r(x)\) and \(\operatorname{Lip}(Q_r)\) equals the displayed optimum. In particular, no choice of nearest points can be nonexpansive in real dimension three or greater, and the sharp optimal constants tend to two as the dimension grows.

## Assumptions and scope
The scalar field is real, the \(\ell_1\) norm is \(\|x\|_1=\sum_{i\in I}|x_i|\), and \(r>0\) is arbitrary. The result concerns the **ordinary metric projection** in that same norm, not the unique Euclidean nearest-point projection onto an \(\ell_1\)-ball. At an exterior point, \(\mathcal P_r(x)\) usually has many elements. The theorem minimizes the *global* Lipschitz constant across **all** single-valued selections, including nonlinear, nonequivariant, or discontinuous ones. The infinite-index statement covers arbitrary index sets and uses the usual absolutely summable support convention. No claim concerns complex scalars or other convex targets.

## Proof
**1. Characterization of the set-valued nearest-point map.** If \(\|x\|_1\le r\), the distance is zero, so every selection must fix \(x\). If \(\|x\|_1>r\), the triangle inequality gives \(\|x-y\|_1\ge\|x\|_1-\|y\|_1\ge\|x\|_1-r\) for \(y\in B_r\). Equality holds precisely when \(\|y\|_1=r\) and, coordinatewise, \(y_i\) has the sign of \(x_i\) with \(0\le|y_i|\le|x_i|\). (At \(x_i=0\), equality forces \(y_i=0\).) Such \(y\) exist, so
\[
\operatorname{dist}_1(x,B_r)=(\|x\|_1-r)_+.
\]
This characterization also proves that, if \(x\) is supported on a finite coordinate set, **every** closest point is supported on the same set.

**2. The canonical selection exists and is nearest.** When \(\|x\|_1>r\), the continuous function \(s_x(t)=\sum_i(|x_i|-t)_+\) decreases from \(s_x(0)=\|x\|_1>r\) to zero for sufficiently large \(t\). It is strictly decreasing whenever positive, and therefore has one positive solution \(\tau\) of \(s_x(\tau)=r\). Since \(x\in\ell_1(I)\), only finitely many coordinates can have magnitude strictly greater than this positive \(\tau\); thus the formula for \(Q_r(x)\) is well defined even if \(I\) is infinite. It preserves input signs, only decreases coordinate magnitudes, and has output norm \(r\). Part 1 implies \(Q_r(x)\in\mathcal P_r(x)\).

**3. Sharp upper Lipschitz bound in finite dimensions.** Let \(|I|=n<\infty\). The soft-threshold map is continuous and piecewise affine, with finitely many cells determined by input coordinate signs, active output coordinates, and whether the input is inside the ball. On the interior of the ball its derivative is the identity. On an open exterior cell with exactly \(k\) active coordinates, and fixed signs, its derivative restricted to those coordinates is a sign conjugate of
\[
C_k=I_k-\frac1k\boldsymbol1\boldsymbol1^{\mathsf T},
\]
with zero output elsewhere. Indeed, on such a cell the threshold is the active signed coordinate sum minus \(r\), divided by \(k\). When \(k=1\), this derivative is zero; for \(k\ge2\), each column of \(C_k\) has absolute sum
\[
\left(1-\frac1k\right)+(k-1)\frac1k=2-\frac2k,
\]
so \(\|C_k\|_{\ell_1^k\to\ell_1^k}=2-2/k\). Integrating these slopes along the finitely subdivided line segment between any two inputs shows
\[
\operatorname{Lip}(Q_r)\le \max\{1,2-2/n\}.
\]
All-active exterior cells are nonempty (take equal positive input coordinates larger than \(r/n\)); there a small one-coordinate perturbation realizes the column norm \(2-2/n\). The interior identity cell realizes the bound one. Thus \(\operatorname{Lip}(Q_r)=1\) for \(n=1\), and \(\operatorname{Lip}(Q_r)=2-2/n\) for \(n\ge2\).

**4. A universal finite-dimensional lower bound, independent of the selector.** Suppose \(n\ge2\), let \(b=(1/n,\ldots,1/n)\), fix \(0<\varepsilon<1/n\), and let \(e_j\) be the standard basis. Take the exterior point \(x=b+\varepsilon e_1\) and the \(n\) boundary points
\[
y_0=b,
\qquad y_j=b+\varepsilon(e_1-e_j)\quad (2\le j\le n).
\]
Every \(y_j\) lies on the unit sphere and is therefore fixed by **every** nearest-point selection; each has distance \(\varepsilon\) from \(x\). By Part 1 any nearest point \(F(x)\) lies on the positive simplex of norm one. Put \(q=(F(x)-b)/\varepsilon\). Necessarily \(\sum_iq_i=0\). Hence
\[
\operatorname{Lip}(F)\ge
\Phi(q):=\max\bigl\{\|q\|_1,
\max_{2\le j\le n}\|q-(e_1-e_j)\|_1\bigr\}.
\]
On the entire real hyperplane \(\sum_iq_i=0\), the function \(\Phi\) is convex and invariant under permutations of coordinates \(2,\ldots,n\). Averaging any \(q\) under those permutations cannot increase \(\Phi\), and gives the symmetric form
\[
\bar q=(a,-a/(n-1),\ldots,-a/(n-1)).
\]
For \(0\le a\le1\), a direct calculation yields
\[
\Phi(\bar q)=\max\left\{2a,2-\frac{2a}{n-1}\right\}.
\]
The minimum occurs at \(a=(n-1)/n\), where the value is \(2-2/n\). For \(a<0\) the second term before simplification is \(2-2a>2\); for \(a>1\) the first term is \(2a>2\). Therefore \(\Phi(q)\ge2-2/n\) for *every* zero-sum \(q\), even if \(q\) is not realizable by a nearest point. Since \(F\) was arbitrary,
\[
\operatorname{Lip}(F)\ge2-2/n.
\]
This lower bound does not assume that the selector is continuous, differentiable, symmetric, or of threshold form. The one-dimensional lower bound is one because every selection fixes the entire interior ball, so Part 3 proves optimality in every finite dimension.

**5. Arbitrary infinite index sets.** For any finite subset \(J\subset I\), apply Part 4 with the points supported on \(J\). Part 1 forces every nearest point at those exterior points to stay supported on \(J\), while every boundary point is fixed. Thus any global selector on \(\ell_1(I)\) has Lipschitz constant at least \(2-2/|J|\) for \(|J|\ge2\). With arbitrarily large finite \(J\), the lower bound is two. For the upper bound, exhaust the countable union of supports of any fixed pair \(x,y\in\ell_1(I)\) by increasing finite sets \(J_m\). Their truncations converge to \(x,y\) in norm. If \(x\) lies inside the ball, its truncated canonical projections equal its truncations. If \(x\) lies outside, let \(\tau>0\) be its threshold; the finitely many active coordinates eventually belong to \(J_m\), and the truncated threshold is then **exactly the same** \(\tau\), so \(Q_r(x|_{J_m})=Q_r(x)\) for all sufficiently large \(m\). The analogous statement holds for \(y\). Apply the finite-dimensional uniform upper bound \(\operatorname{Lip}(Q_r|_{\ell_1^{J_m}})\le2\) and pass to the limit to get \(\|Q_r(x)-Q_r(y)\|_1\le2\|x-y\|_1\). The lower bound completes the proof. Finally, scaling \(x\mapsto x/r\) gives the asserted independence from \(r\).

## Verification
Run `python verification/check.py` using Python 3.10 or later; it requires only the standard library. The exact-rational script verifies soft-threshold feasibility and exact nearest-point distances, the optimal centering-matrix column sums, finite-dimensional Lipschitz inequalities on seeded rational pairs, and the boundary-simplex minimax witnesses. An actual run printed `L1_METRIC_SELECTION_SHARP_OK 10589`. Its 10,589 rational assertions are finite consistency checks, not a substitute for the proof of the universal lower bound or the infinite-dimensional extension.

## Relationship to prior work
Jinlu Li's 2026 work gives an explicit *set-valued* \(\ell_1\)-ball metric projection and studies Mordukhovich derivatives and covering constants; its publicly available abstract does not state an optimal Lipschitz constant over all selections. The full preprint could not be inspected here, and overlap with an unexamined theorem remains a specific priority risk. Duchi, Shalev-Shwartz, Singer, and Chandra (2008) describe Euclidean projection onto the \(\ell_1\) ball and its familiar soft-threshold algorithm, which is not itself claimed new. Published work on nearest-point projection in \(\ell_p\) geometry for \(1<p<\infty\) determines a common soft-threshold map and sharp Lipschitz constants (see the two 2026 research records in the references); those results concern a **single-valued** map in strictly convex geometries and exclude the multivalued \(p=1\) endpoint. Their constants, and classical minimal norms for *linear* hyperplane projections, do not alone prove a sharp lower bound for *every nonlinear selection* at the endpoint. The contribution assessed here is precisely this optimality over all selections, including the infinite-index limit, rather than the threshold formula in isolation.

## Limitations
This theorem does not classify all optimal selectors or give a complete Lipschitz theory for arbitrary target convex bodies. It applies only to real \(\ell_1\) spaces. Older literature on Lipschitz metric selections and the inaccessible full text of Li's 2026 preprint might already imply part or all of the quantitative result; no assertion of exhaustive priority or independent audit is made.

## References
1. J. Li, *Mordukhovich Derivatives and Covering Constant for Set-Valued Metric Projection in General Banach Spaces*, arXiv:2608.28961v1, first submitted 29 August 2026, https://arxiv.org/abs/2608.28961.
2. J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML (2008), 272–279, DOI:10.1145/1390156.1390191.
3. *Exponent-invariant cross-polytope projection and its sharp Lipschitz threshold*, published mathematical research record (2026), identifier 5177ec842d41.
4. *Exact Lipschitz stability and contractivity threshold for weighted cross-polytope projections*, published mathematical research record (2026), identifier c92b6dad1bd0.
5. W. Li, *Lipschitz Continuous Metric Selections in \(C_0(T)\)*, SIAM Journal on Mathematical Analysis 21 (1990), DOI:10.1137/0521011. This concerns metric projections onto finite-dimensional subspaces of continuous-function spaces.
6. M. Finzel and W. Li, *Piecewise Affine Selections for Piecewise Polyhedral Multifunctions and Metric Projections*, Journal of Convex Analysis 7 (2000), 73–94. The publicly inspected abstract describes existence and piecewise-affine structure of selections for polyhedral metric projections; it does not report a best Lipschitz constant for the \(\ell_1\) ball.
