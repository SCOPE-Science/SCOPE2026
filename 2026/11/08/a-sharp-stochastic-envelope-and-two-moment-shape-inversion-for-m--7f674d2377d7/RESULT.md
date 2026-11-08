# A sharp stochastic envelope and two-moment shape inversion for maximal triangles sampled on triangular boundaries

## Finding
Let \(T\subset\mathbb R^2\) be any nondegenerate triangle of area \(A\), perimeter \(P\), and opposite side lengths \(a_1,a_2,a_3\). For every integer \(N\ge3\), choose \(N\) independent points uniformly on the full boundary with respect to normalized Euclidean arclength. Let \(H_N\) be the greatest area among triangles on any three distinct sampled points. Set
\[
Z_N=N\left(1-\frac{H_N}{A}\right),\quad p_i=\frac{a_i}{P},\quad \alpha_i=1-p_i.
\]
The side ratios obey \(0<p_i<1/2\), \(\sum_i p_i=1\), and therefore \(1/2<\alpha_i<1\), \(\sum_i\alpha_i=2\). Then, with independent unit exponential variables \(E_i\),
\[
Z_N\ \xrightarrow{\mathrm d}\ Z_T=\sum_{i=1}^3\frac{E_i}{\alpha_i},\qquad
\mathbb E Z_N^r\longrightarrow\mathbb E Z_T^r\quad\text{for every fixed real }r>0.
\]
In particular, its Laplace transform is \(\mathbb E e^{-sZ_T}=\prod_i\alpha_i/(\alpha_i+s)\) for every \(s\ge0\).

There are sharp, **simultaneous first-order stochastic bounds** on the entire limiting survival function for every \(t\ge0\):
\[
e^{-2t/3}\left(1+\frac{2t}{3}+\frac{2t^2}{9}\right)
\le \mathbb P(Z_T>t)\ <\ e^{-t}+t e^{-t/2}\quad(t>0).
\]
The left equality at all \(t\) holds precisely for equilateral triangles. The strict right inequality holds at every \(t>0\) for every nondegenerate triangle; its upper envelope is attained in the limit, first as \(N\to\infty\) and then as the side proportions approach \((1/2,1/2,0)\). This is a sharp stochastic-order statement, not merely a bound on the mean.

Furthermore the limit's first two ordinary moments determine the unordered side ratios and hence the similarity class of \(T\). Writing \(\mu=\mathbb E Z_T\), \(v=\operatorname{Var}(Z_T)\), and \(q=(\mu^2-v)/2\), the three roots (with multiplicity) of
\[
z^3-\mu z^2+qz-\frac q2=0
\]
are exactly \(1/\alpha_1,1/\alpha_2,1/\alpha_3\). Consequently \(p_i=1-\alpha_i\) reconstructs the side proportions. A finite deterministic reduction also holds: for every realized sample, all maximizing-area triangles can be sought among **at most six sampled points**, the two outermost samples on each occupied side.

## Assumptions and scope
All side lengths are strictly positive and satisfy the strict triangle inequalities. Sampling is independent, with density \(1/P\) per unit boundary length; it is not sampling from the interior and not sampling from the three vertices. The fixed-shape limit takes \(N\to\infty\) before any potential shape degeneration. The area of a triangle from three sampled points is the unsigned Euclidean area. The maximum \(H_N\) is over \(\binom N3\) index triples; coincident sampled points occur with probability zero. The limiting stochastic bounds compare variables from different triangles after dividing the sampled optimum by each parent triangle's area.

## Proof
**1. Exact finite-sample localization.** On each of the three closed sides, every sampled point is a convex combination of the two outermost samples on that side (when the side is populated). Thus the convex hull of the entire sample equals the convex hull of at most six points. Holding two vertices fixed, triangle area as a function of the third vertex is the absolute value of an affine functional, so a maximum can be attained at an extreme point of the sample hull. Repeating for all three vertices gives a maximizing triangle using only this six-point set. This proves the deterministic reduction, including samples missing one or more sides.

**2. Local vertex coordinates.** Use barycentric coordinates \((\lambda_1,\lambda_2,\lambda_3)\) with respect to \(T\). For each parent vertex \(i\), put
\[
M_{i,N}=\min_{1\le j\le N}\bigl(1-\lambda_i(X_j)\bigr).
\]
For a boundary point at physical distance \(x\) from vertex \(i\) along an incident side of length \(\ell\), \(1-\lambda_i=x/\ell\); on the opposite side it is exactly one. Thus \(M_{i,N}\) is the smallest fractional side-length displacement toward vertex \(i\) from any sampled point.

For a fixed \(t\ge0\) and sufficiently large \(N\), the set \(\{x\in\partial T:1-\lambda_i(x)\le t/N\}\) consists of two incident subsegments, of total arclength \((a_j+a_k)t/N=P\alpha_i t/N\). Therefore
\[
\mathbb P(NM_{i,N}>t)=\left(1-\frac{\alpha_i t}{N}\right)^N\ \longrightarrow e^{-\alpha_i t}.
\]
For any fixed \(t_1,t_2,t_3\ge0\), the three such corner neighborhoods are pairwise disjoint for all sufficiently large \(N\), and their joint empty-set probability is exactly
\[
\mathbb P(NM_{i,N}>t_i\ \forall i)
=\left(1-\frac{\sum_i\alpha_i t_i}{N}\right)^N
\longrightarrow e^{-\sum_i\alpha_i t_i}.
\]
These joint survival functions prove that \((NM_{1,N},NM_{2,N},NM_{3,N})\) converges to independent exponentials with rates \(\alpha_i\).

**3. From local distances to the maximal triangle area.** The full area \(A\) is the unique possible maximal area for a triangle inscribed in \(T\): equality of area for a convex subtriangle forces equality of the convex sets, and hence the three original vertices. Compactness therefore forces any sampled triangle of area \(A(1-o(1))\), after relabeling, into vanishing neighborhoods of the three parent vertices.

For one point near each parent vertex, write its barycentric coordinates as the corresponding basis vector plus a displacement of fractional size \(u_i=1-\lambda_i\). The normalized signed area is the determinant of the matrix of these three barycentric columns. Multilinearity gives the uniform expansion
\[
\frac{\operatorname{area}(Y_1Y_2Y_3)}{A}
=1-(u_1+u_2+u_3)+O\bigl((u_1+u_2+u_3)^2\bigr)
\]
for all small nonnegative \(u_i\), uniformly over the two possible incident sides at each corner. Choosing the sampled point achieving each \(M_{i,N}\) gives an admissible candidate with deficit \(\sum_iM_{i,N}+O((\sum_i M_{i,N})^2)\) with probability tending to one. Conversely, a maximizing sampled triangle is localized by the previous paragraph, and its displacement at vertex \(i\) is at least \(M_{i,N}\). Since the candidate already has deficit \(O_{\mathbb P}(N^{-1})\), the linear lower bound from the displayed expansion forces every maximizing displacement to be \(O_{\mathbb P}(N^{-1})\); its quadratic remainder is then \(O_{\mathbb P}(N^{-2})\). Therefore
\[
Z_N-\sum_i NM_{i,N}\xrightarrow{\mathbb P}0.
\]
Together with the joint exponential limit this proves the distributional assertion.

**4. Uniform integrability and all moments.** Select one sampled point achieving each \(M_{i,N}\), allowing repetitions only to construct a zero-area candidate. The determinant of barycentric columns lies in \([-1,1]\), and a telescoping determinant comparison with the identity matrix gives \(|1-\det|\le2\sum_iM_{i,N}\). If selected indices are distinct, their triangle is a valid candidate; otherwise their area is zero and the same determinant bound gives \(1\le2\sum_iM_{i,N}\). Hence, deterministically, \(0\le Z_N\le2\sum_i NM_{i,N}\). For \(0\le t<N\),
\[
\mathbb P(NM_{i,N}>t)=\left(1-\frac{\alpha_i t}{N}\right)^N\le e^{-\alpha_i t},
\]
and the probability is zero for \(t>N\). Thus the right side has uniformly bounded moments of every positive order. Uniform integrability of every fixed positive power of \(Z_N\), together with distributional convergence, proves convergence of the asserted moments.

**5. Sharp stochastic envelopes.** For two independent exponentials of rates \(r-d,r+d\) with \(0<d<r\), the survival of their sum at \(t\ge0\) is
\[
e^{-rt}\left(\cosh(dt)+\frac r d\sinh(dt)\right).
\]
At fixed \(r\), this increases strictly with \(d>0\) when \(t>0\), because both \(\cosh(dt)\) and \(\sinh(dt)/d\) increase with \(d\). At \(d=0\), it is \(e^{-rt}(1+rt)\). This ordering is preserved after addition of an independent exponential. Replacing any pair of rates by a more balanced pair (keeping their sum fixed) therefore strictly decreases the sum in usual stochastic order. The rate vectors in this problem have sum two and lie strictly between one-half and one. Every such vector majorizes \((2/3,2/3,2/3)\) and is majorized by \((1,1/2,1/2)\). The elementary pair-balancing characterization of majorization, or successive two-coordinate transfers, yields
\[
\operatorname{Gamma}(3,2/3)\ \le_{\rm st}\ Z_T\ \le_{\rm st}\ \operatorname{Exp}(1)+\operatorname{Gamma}(2,1/2).
\]
The equal-rate survival is the displayed cubic Erlang survival, and direct convolution gives the upper survival \(e^{-t}+te^{-t/2}\). Equality on the left requires all rates equal and thus all sides equal. Equality on the right requires a zero side length, excluded by nondegeneracy. The family with side lengths \((1,1,\varepsilon)\) as \(\varepsilon\downarrow0\) proves sharpness of the upper bound in the indicated iterated limit.

**6. Inverse shape classification.** Since \(Z_T\) is a sum of independent rate-\(\alpha_i\) exponentials,
\[
\mu=\sum_i\frac1{\alpha_i},\qquad v=\sum_i\frac1{\alpha_i^2}.
\]
Put \(t_i=1/\alpha_i\). The first two elementary symmetric polynomials satisfy \(\sum_i t_i=\mu\) and \(\sum_{i<j}t_it_j=(\mu^2-v)/2=q\). The fixed rate-sum constraint gives \(\sum_i1/t_i=\sum_i\alpha_i=2\), so \(t_1t_2t_3=q/2\). The claimed cubic therefore has exactly these three roots. Recovering \(\alpha_i=1/t_i\), then \(p_i=1-\alpha_i\), gives the unordered normalized side lengths; the side-side-side theorem recovers the similarity class. No unobserved scale is asserted to be identifiable.

## Verification
The standalone `triangle_extreme_verifier.py` uses independent arclength samples and exact exhaustive area comparisons for small sample sizes. It verifies that restricting to the at-most-six per-edge extremes reproduces the full maximum, checks the polynomial inversion for equilateral, scalene, and nearly degenerate shapes, and compares simulated area deficits with the proved first two limiting moments at increasing sample sizes. It also checks the pairwise-rate survival comparison over a numerical grid. These finite tests are independent diagnostics, not proofs of the limiting assertions. Reproduce with `python triangle_extreme_verifier.py` after installing NumPy and SciPy.

## Relationship to prior work
Koroleva and Nikitin's 2013 *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons* establishes maximal-area laws for polygons whose vertices are sampled on a **circle**, including smooth, rotationally movable maximizers. The present model fixes a **triangular parent boundary** with exactly three corners; the maximizing configuration is isolated at the parent vertices and has a first-order, not quadratic, area deficit. Its hypoexponential limit and sharp shape-dependent stochastic interval are not implications of those circular results.

Nikitin and Simarova's 2020 *Generalized Limit Theorems For U-max Statistics* concerns smooth kernels with points distributed on a circle. Its Hessian-based Weibull framework has different hypotheses and cannot be applied directly to a nonsmooth triangular boundary and the corner-localized mechanism. Pérez-Lantero's 2014 *Area and Perimeter of the Convex Hull of Stochastic Points* concerns independent Bernoulli inclusion of a **fixed finite point set** and area of the **whole sampled convex hull**; it neither assumes arclength sampling nor characterizes the largest three-vertex area asymptotic. Existing algorithms for maximum-area triangles in finite point sets provide computational context, not the limit law or the sharp stochastic shape envelope.

The Schur-majorization step builds on the classical stochastic-ordering principle for sums of exponentials but the exact two-rate survival calculation is included here. No assertion is made that stochastic ordering or the basic exponential-spacing limit is itself new. The claimed contribution is the integrated geometric extreme-value classification, including the rates' dependence on the triangle, sharp attainable shape envelopes, and two-moment inversion.

## Limitations
The proof assumes a fixed nondegenerate triangle, independent exactly arclength-uniform boundary sampling, and a population limit as \(N\to\infty\). The upper stochastic envelope is a limit along a degenerating family and is never attained by a nondegenerate triangle. No convergence rate uniform over all shapes or finite-sample estimator consistency, error bars, or noise stability is proved. Literature coverage is not a guarantee of historical priority: a differently phrased polygon-corner extreme-value result or a stronger general theorem may exist. No shape-uniform or finite-sample quantitative guarantee is established.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (first posted 2013-01-07), https://arxiv.org/abs/1301.1360 . Full mathematical article examined, notably the introduction and inscribed-polygon area/perimeter sections.
2. Ya. Yu. Nikitin and E. N. Simarova, *Generalized Limit Theorems For U-max Statistics*, arXiv:2010.04460 (first posted 2020-10-09), https://arxiv.org/abs/2010.04460 . Full article examined, particularly the smooth-circle hypothesis and general limit theorem.
3. P. Pérez-Lantero, *Area and Perimeter of the Convex Hull of Stochastic Points*, arXiv:1412.5153 (first posted 2014-12-16), https://arxiv.org/abs/1412.5153 . Full text examined, including model and main theorem.
4. J. E. Boyce, D. P. Dobkin, R. L. Drysdale, and L. J. Guibas, *Finding Extremal Polygons*, SIAM Journal on Computing 14 (1985), 134–147, doi:10.1137/0214011 . Algorithmic comparator; abstract and available publication record examined.
5. Ya. Yu. Nikitin and T. A. Polevaya, *Limit Theorems for Areas and Perimeters of Random Inscribed and Circumscribed Polygons*, Journal of Mathematical Sciences 258 (2021), 873–882, doi:10.1007/s10958-021-05586-x . Abstract and bibliographic information examined; full text was not established accessible, so a residual coverage risk is retained.
