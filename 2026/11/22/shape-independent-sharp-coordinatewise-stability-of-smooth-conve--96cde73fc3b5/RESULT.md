# Shape-independent sharp coordinatewise stability of smooth convex-body projection

## Finding
Let \(n\ge 1\), let \(w=(w_1,\ldots,w_n)\in(0,\infty)^n\), and define the dual weighted norms
\[
\|z\|_{\infty,w}=\max_i\frac{|z_i|}{w_i},\qquad
\|z\|_{1,w}=\sum_iw_i|z_i|.
\]
For a nonempty closed convex set \(C\subset\mathbb R^n\), let \(P_C\) denote its Euclidean nearest-point map. Every such projector satisfies, separately in each weighted norm,
\[
\operatorname{Lip}_{\infty,w}(P_C),\ \operatorname{Lip}_{1,w}(P_C)
\ \le\ L_w:=\frac12\left(1+\frac{\|w\|_2}{\min_iw_i}\right).
\]
**If \(C\) is a compact convex body with nonempty interior and \(C^1\) boundary, both coefficients equal \(L_w\), independently of its shape, size, curvature, and orientation.** In particular the unweighted value is \((1+\sqrt n)/2\). For \(n\ge2\), if the body is also strictly convex, neither coefficient is attained by a pair of distinct finite inputs. For the same dimension and weights the axis-aligned rectangular box has coefficient exactly one in both norms. Consequently these global moduli are not continuous in the Hausdorff metric on convex bodies: the smooth parallel bodies \(B+\varepsilon B_2\), for a box \(B\), converge to \(B\) while retaining modulus \(L_w>1\) for all \(\varepsilon>0\).

## Assumptions and scope
All vectors and sets are real and finite dimensional. \(C^1\) boundary means every boundary point admits a local continuously differentiable hypersurface graph, equivalently a continuous unique supporting-normal field on the boundary of a convex body. The Lipschitz coefficient is the supremum over all distinct inputs in \(\mathbb R^n\); it is not an ordinary Euclidean operator norm. The weighted \(\ell_1\) and weighted \(\ell_\infty\) norms are dual under the Euclidean pairing. In the one-dimensional case any convex body is a nondegenerate interval and both coefficients are one.

## Proof
**1. A universal upper bound from firm nonexpansivity.** For distinct \(x,y\), write \(p=P_Cx\), \(q=P_Cy\), \(u=p-q\), and \(v=x-y\). The characterization of nearest points by normal cones yields \(\langle u,v-u\rangle\ge0\), or equivalently
\[
\left\|u-\frac v2\right\|_2\le\frac{\|v\|_2}{2}.
\]
With \(\delta=\|v\|_{\infty,w}\), each coordinate satisfies
\[
\frac{|u_i|}{w_i}\le\frac{|v_i|+\|v\|_2}{2w_i}
\le\frac\delta2\left(1+\frac{\|w\|_2}{w_i}\right)\le L_w\delta.
\]
For the weighted sum norm, choose a sign vector \(s\in\{-1,1\}^n\) attaining \(\|u\|_{1,w}=\sum_i s_iw_i u_i\). The same Euclidean ball inequality implies
\[
\|u\|_{1,w}\le\frac12\left(\sum_i s_iw_iv_i+\|w\|_2\|v\|_2\right)
\le\frac12\left(1+\frac{\|w\|_2}{\min_iw_i}\right)\|v\|_{1,w},
\]
using \(\|v\|_2\le\|v\|_{1,w}/\min_iw_i\). Thus both upper bounds hold for arbitrary nonempty closed convex \(C\).

**2. Exact norm of tangent-hyperplane projection.** For a unit vector \(\nu\), let \(J_\nu=I-\nu\nu^{\mathsf T}\). As \(J_\nu\) is symmetric, its operator norms under the dual weighted sum/maximum norms coincide. The weighted maximum-norm row sums are
\[
\|J_\nu\|_{\infty,w\to\infty,w}
=\max_i\left(1-\nu_i^2+\frac{|\nu_i|}{w_i}\sum_{j\ne i}w_j|\nu_j|\right).
\]
For a fixed row \(i\), Cauchy--Schwarz makes this at most
\[
1-t+\frac{W_i}{w_i}\sqrt{t(1-t)},\qquad
W_i=\left(\sum_{j\ne i}w_j^2\right)^{1/2},\quad t=\nu_i^2.
\]
Equality is realized by \(|\nu_j|=w_j\sqrt{1-t}/W_i\) for \(j\ne i\). For \(n\ge2\), the strict scalar maximum is attained at \(t=(1-w_i/\|w\|_2)/2\), with value \((1+\|w\|_2/w_i)/2\). Choosing a minimal-weight row therefore gives
\[
\sup_{\|\nu\|_2=1}\|J_\nu\|_{\infty,w\to\infty,w}
=\sup_{\|\nu\|_2=1}\|J_\nu\|_{1,w\to1,w}=L_w.
\]
The maximizing normal has no zero coordinates and is specified explicitly above. For \(n=1\), the interior identity map already yields one.

**3. Every tangent hyperplane is seen infinitesimally by a smooth body's projector.** Let \(C\) be a compact \(C^1\) convex body. For each unit vector \(\nu\), compactness supplies a supporting point \(z\in\partial C\) with outward normal \(\nu\). At \(z\), the tangent cone is the closed halfspace \(H_\nu=\{h:\langle h,\nu\rangle\le0\}\). In coordinates normal and tangent to the \(C^1\) boundary, the boundary is a graph with zero first derivative at \(z\). Therefore the scaled sets \(\varepsilon^{-1}(C-z)\) converge locally to \(H_\nu\): every limit point lies in the halfspace by the support inequality, while every point with strictly negative normal coordinate lies in these scaled sets for all sufficiently small \(\varepsilon\). Approximating points on the limiting boundary from within gives inner approximation of every point of \(H_\nu\). Since \(0\) belongs to each scaled set, projections of fixed \(h\) are uniformly bounded. Every convergent subsequence of these projections minimizes Euclidean distance to \(h\) over \(H_\nu\), by the variational inequality against approximants, and hence has the same unique limit \(P_{H_\nu}(h)\). Consequently, for each fixed \(h\)
\[
\lim_{\varepsilon\downarrow0}\frac{P_C(z+\varepsilon h)-z}{\varepsilon}
=P_{H_\nu}(h).
\]
Take arbitrary \(h\) and two vectors \(a,b\) with \(a-b=h\) and \(\langle a,\nu\rangle,\langle b,\nu\rangle>0\); a sufficiently large common positive multiple of \(\nu\) makes this possible. On that outer halfspace, \(P_{H_\nu}(a)-P_{H_\nu}(b)=J_\nu h\). Consequently the global Lipschitz coefficient of \(P_C\) in either norm is at least the operator norm of \(J_\nu\). Optimizing \(\nu\) by Step 2 matches the upper bound in Step 1.

**4. Attainment and shape discontinuity.** If \(C\) is strictly convex, every nonzero normal vector at a point \(p\in\partial C\) supports \(C\) only at \(p\). Hence when \(p\ne q\), and at least one of \(x-p\) or \(y-q\) is nonzero, the projection normal-cone inequalities from Step 1 are strict: \(\langle u,v-u\rangle>0\). The two norm bounds then become strict. If both inputs belong to \(C\), their quotient is one; if the projections coincide, it is zero. For \(n\ge2\), \(L_w>1\), so no distinct finite pair attains the sharp coefficient. On a box \(B=\prod_i[a_i,b_i]\), projection acts by independent scalar clamping and has Lipschitz modulus one in either norm (attained by two interior inputs). For \(\varepsilon>0\), the parallel body \(B+\varepsilon B_2\) has \(C^{1,1}\) boundary, being a positive level set of the Euclidean distance to \(B\), and converges to \(B\) in Hausdorff distance exactly \(\varepsilon\). Step 3 gives each parallel body's modulus \(L_w\), proving discontinuity.

## Verification
The analytic argument proves the statement in every finite dimension and for all admissible convex bodies and weights. The optional standalone `verify.py` program, run using `python3 verify.py`, numerically projects onto several unequal-axis ellipsoids, confirms the limiting tangent-plane coefficient, checks random two-input inequalities in both weighted norms, and compares box clamping. These finite checks corroborate but do not establish the universal result.

## Relationship to prior work
Balestro--Martini--Teixeira (arXiv:1908.08742, first released 23 August 2019) investigate general metric projections and normal geometry of convex bodies, including the classical Euclidean nonexpansivity statement. The published work *Sharp weighted coordinate sensitivity of Euclidean-ball clipping* (published-finding corpus, October 2026) establishes exactly the displayed weighted formula for a **Euclidean ball**, and explicitly excludes arbitrary convex bodies. Its sharp normal calculation is reused as an elementary ingredient; the new statement is the body-independent equality for every smooth convex body, strict-convexity nonattainment, and the sharp Hausdorff-discontinuity example. Leobacher--Steinicke (2021) study regularity of projections onto differentiable manifolds, rather than the global cross-norm coefficient of projection onto an arbitrary convex region. All these comparisons concern the full mathematical implications, not merely terminology.

## Limitations
No claim is made that every nonsmooth convex body's coefficient equals the universal bound (boxes show otherwise), nor that all optimal directions or finite attaining pairs are classified for smooth bodies with flat faces. Historical prior art under different norm or generalized projection terminology remains possible. The numerical checks are supplementary only; the exact coefficients depend on Euclidean nearest-point projection, rather than projection measured in the weighted norms themselves.

## References
1. V. Balestro, H. Martini, R. Teixeira, *Convex analysis in normed spaces and metric projections onto convex bodies*, arXiv:1908.08742, first posted 23 August 2019, https://arxiv.org/abs/1908.08742.
2. *Sharp weighted coordinate sensitivity of Euclidean-ball clipping*, published published-finding corpus record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-coordinate-sensitivity-of-euclidean-ball-clipping--78696bf157c3.
3. G. Leobacher, A. Steinicke, *Existence, uniqueness and regularity of the projection onto differentiable manifolds*, Annals of Global Analysis and Geometry 60 (2021), 559--587, https://doi.org/10.1007/s10455-021-09788-z.
4. E. M. Bednarczuk and K. E. Rutkowski, *On Lipschitz Continuity of Projections onto Polyhedral Moving Sets*, Applied Mathematics & Optimization 84 (2021), 2147--2175, https://doi.org/10.1007/s00245-020-09706-y.
