# Strict isotropic-constant hierarchy across coordinate-flat cross-polytope sections

## Finding
For every integer \(n\ge3\) and every \(2\le m\le n\), let
\[
K_{n,m}=\{x\in\mathbb R^n: \sum_{i=1}^n|x_i|\le1,\quad\sum_{i=1}^m x_i=0\},
\]
with intrinsic Euclidean dimension \(d=n-1\). These hyperplanes represent the entire family of equal-positive-coordinate normals supported on exactly \(m\) coordinates, up to permutation and scaling. Let \(U_{n,m}\) be intrinsic-volume uniform on \(K_{n,m}\), and put
\[
B_m=\{y\in\mathbb R^m:\sum_i y_i=0,\ \sum_i|y_i|\le1\},\quad
v_m=\frac{\sqrt m}{2^{m-1}(m-1)!}\binom{2m-2}{m-1}.
\]
The exact volume and covariance eigenvalues, with multiplicities, are
\[
V_{n,m}=\operatorname{Vol}_d(K_{n,m})
=\frac{2^{n-m}(m-1)!}{(n-1)!}\,v_m,
\]
\[
\lambda_{n,m}^{\parallel}=\frac{2m-1}{(m+1)n(n+1)}\ \ (m-1\text{ times}),\qquad
\lambda_{n,m}^{\perp}=\frac{2}{n(n+1)}\ \ (n-m\text{ times}).
\]
Here \(\parallel\) means the subspace of the first \(m\) coordinates with zero sum, and \(\perp\) the remaining coordinate axes. In particular, with the affine-invariant isotropic constant
\[
L(K)=\frac{(\det\operatorname{Cov}(U_K))^{1/(2d)}}{\operatorname{Vol}_d(K)^{1/d}},
\]
**every** intermediate rank is strictly ordered, not merely the two endpoints:
\[
\boxed{L(K_{n,2})>L(K_{n,3})>\cdots>L(K_{n,n}).}
\]
Moreover, the Euclidean volumes are strictly decreasing in the same rank ordering:
\[
\boxed{V_{n,2}>V_{n,3}>\cdots>V_{n,n}.}
\]
For each adjacent pair, an exact dimension-separated ratio is available. Writing \(f_m=(2m-1)/(2(m+1))\),
\[
 r_m^2=\frac{(m+1)(2m-1)^2}{4m^3},\quad
 \delta_m=\frac{3}{(2m-1)(m+2)},
\]
we have
\[
\left(\frac{V_{n,m+1}}{V_{n,m}}\right)^2=r_m^2,\qquad
\left(\frac{L(K_{n,m+1})}{L(K_{n,m})}\right)^{2(n-1)}
=\frac{f_m(1+\delta_m)^m}{r_m^2}<1.
\]

## Assumptions and scope
All volumes and covariance determinants refer to the intrinsic Euclidean metric of the hyperplane, not to a nonorthonormal coordinate chart; the center is the origin. The parameter \(m\) is an **integer support rank** between two and \(n\), not a continuously varying normal. For \(m=n\), the second covariance eigenspace is absent. For \(m=2\), the body is an affine cross-polytope, while for \(m=n\) it is a scaled full type-A root polytope. These two endpoint geometries, and the unscaled root-polytope covariance, have been studied before; the asserted contribution is the strict ordering of *every intermediate rank* and the exact neighboring-rank certificate.

## Proof
**Base root section.** The body \(B_m\) is half the full type-A root polytope \(\operatorname{conv}\{e_i-e_j:i\ne j\}\). For self-containment, fix a sign orthant with \(j\) positive coordinates and \(m-j\) negative coordinates. The positive and negative masses are each \(s\in[0,1/2]\), with independent normalized simplex coordinates of sizes \(j\) and \(m-j\). The coarea density on this orthant is proportional to \(s^{m-2}\), and the multiplicity is \(\binom mj\). Summing its Euclidean volumes over \(j=1,\ldots,m-1\) and using Vandermonde's identity yields the displayed \(v_m\). Normalized simplex coordinates have the standard Dirichlet second moment \(\mathbb E\sum_i p_i^2=2/(j+1)\). Together with \(\mathbb E(s^2)=(m-1)/(4(m+1))\), this gives
\[
\mathbb E\|U_{B_m}\|_2^2
=\frac{(m-1)(2m-1)}{m(m+1)^2}.
\]
By permutation symmetry and the zero-sum constraint, \(\operatorname{Cov}(U_{B_m})=(2m-1)/(m(m+1)^2)\) times the identity of the \((m-1)\)-dimensional zero-sum subspace. These endpoint formulas agree with the previously published complete-graph root-polytope calculation, but here they are used only as inputs.

**Join integration.** Put \(k=n-m\). In mutually orthogonal coordinate blocks, \(K_{n,m}=\{(y,z):\|y\|_1+\|z\|_1\le1,\ \sum_{i=1}^my_i=0\}\). For \(k>0\), integrating first in the base block gives
\[
\operatorname{Vol}_d(K_{n,m})=
 v_m\int_{\|z\|_1\le1}(1-\|z\|_1)^{m-1}\,dz
= v_m\frac{2^k(m-1)!}{(n-1)!}.
\]
The radial variable \(R=\|z\|_1\) under the uniform measure has the \(\mathrm{Beta}(k,m)\) law. Conditionally on \(R\), the base block is uniform on \((1-R)B_m\), while the free block has independent equiprobable signs and uniform Dirichlet \((1,\ldots,1)\) absolute proportions. Consequently
\[
\mathbb E(1-R)^2=\frac{m(m+1)}{n(n+1)},\qquad
\mathbb E R^2=\frac{k(k+1)}{n(n+1)},
\]
\[
\operatorname{Var}(y\cdot u)=\frac{2m-1}{(m+1)n(n+1)}\|u\|^2
\quad (\sum_i u_i=0),\qquad
\mathbb E z_i^2=\frac{2}{n(n+1)}.
\]
All cross-covariances vanish by symmetries. For \(k=0\), the base result applies directly and agrees with these formulas.

**Strict rank ordering.** Since \(V_{n,m}\) is explicit,
\[
\left(\frac{V_{n,m+1}}{V_{n,m}}\right)^2=
\frac{(m+1)(2m-1)^2}{4m^3},\qquad
1-\left(\frac{V_{n,m+1}}{V_{n,m}}\right)^2=\frac{3m-1}{4m^3}>0.
\]
For the isotropic constant put \(f_m=(2m-1)/(2(m+1))\), so \(\lambda_{n,m}^{\parallel}=f_m\lambda_{n,m}^{\perp}\), and hence
\[
L(K_{n,m})^{2(n-1)}=
\frac{\bigl(2/[n(n+1)]\bigr)^{n-1}f_m^{m-1}}{V_{n,m}^2}.
\]
The dimension-independent adjacent ratio therefore equals \(Q_m=f_m(1+\delta_m)^m/r_m^2\), with \(\delta_m=3/((2m-1)(m+2))\). For every integer \(m\ge2\), \((m-1)\delta_m<1\), and the binomial bounds \(\binom mj\le m(m-1)^{j-1}\) imply
\[
(1+\delta_m)^m\le1+\frac{m\delta_m}{1-(m-1)\delta_m}.
\]
A direct exact factorization gives the *strict* remaining margin:
\[
\frac{r_m^2}{f_m}-1-\frac{m\delta_m}{1-(m-1)\delta_m}
=\frac{(m-1)(m+1)}{2m^3(2m^2+1)}>0.
\]
Thus \(Q_m<1\), proving all adjacent inequalities and hence both global chains. The proof covers every integer \(n\ge3\) and \(2\le m<n\), not just a finite checked range.

## Verification
Run `python CHECKER.py` using Python 3, NumPy, SciPy, and SymPy. The checker independently integrates sectors using exact rational Dirichlet moments, symbolically factors the sharp positivity certificate, constructs and triangulates actual hyperplane section polytopes in orthonormal coordinates through ambient dimension six, integrates quadratic polynomials over the resulting simplices, and tests rational comparisons through rank 500. The reproduced run passed 1,058 assertions. These finite computations supplement, but do not replace, the all-rank analytic proof above.

## Relationship to prior work
Nayar and Tkocz (2018) establish a strong log-concavity property for volumes of arbitrary subspace sections of the cross-polytope, not this uniform-interior covariance or the adjacent isotropic-constant ranking. Brandenburg, De Loera, and Meroni (2023) describe hyperplane-section combinatorial types and algorithmic polytope-moment optimization; the inspected results do not impose a strict chain in the support rank of equal-coordinate normals. Kipp (2024) studies isotropic constants of regular polytopes, including the cross-polytope endpoint, without covering the nonregular intermediate sections. The published exact inertia result for complete-graph root polytopes supplies the \(m=n\) endpoint and an endpoint comparison with the regular cross-polytope; that endpoint result alone does not imply the strict ordering of all \(m\) intermediate bodies. The base covariance and volume formulas are credited as previously known; the new statement tested for priority is the universal **intermediate-rank isotropic monotonicity** with its explicit strict algebraic certificate.

## Limitations
The claim is limited to coordinate-flat normals of equal nonzero magnitude, not all hyperplane normals or all convex bodies. An indexed-search absence is not proof of novelty; older literature on \(\ell_1\) sections, unconditional bodies, or root polytopes may contain an equivalent monotonicity inequality. The argument has not received independent mathematical review or formal proof verification. Numeric checks are not evidence of infinite-domain correctness or priority.

## References
1. P. Nayar and T. Tkocz, *On a convexity property of sections of the cross-polytope*, arXiv:1810.02038, first public 2018-10-04. https://arxiv.org/abs/1810.02038
2. M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first public 2023-04-27. https://arxiv.org/abs/2304.14239
3. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353, first public 2024-07-01. https://arxiv.org/abs/2407.01353
4. A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public 2019-10-11. https://arxiv.org/abs/1910.05193
5. *Exact inertia of complete-graph root polytopes and a sharp isotropic deficit*, published mathematical finding, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-inertia-of-complete-graph-root-polytopes-and-a-sharp-isotr--cfc3c48a6fc4
