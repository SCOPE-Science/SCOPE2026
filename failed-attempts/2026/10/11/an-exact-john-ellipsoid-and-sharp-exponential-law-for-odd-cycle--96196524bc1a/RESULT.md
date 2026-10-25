# An exact John ellipsoid and sharp exponential law for odd-cycle fractional stable-set polytopes

## Finding
For every odd integer \(n\ge5\), let \(A_n\) be the adjacency matrix of the cycle \(C_n\), with indices in \(\mathbb Z/n\mathbb Z\), and consider its fractional stable-set polytope
\[
 Q_n=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_{i+1}\le1\ \text{for every }i\}.
\]
Set \(r=\sqrt5-2\). Let \(q_n\in(0,r)\) be the unique solution of
\[
1-4q-q^2=q^n(1+4q-q^2),
\]
and define
\[
 t_n=\frac{2q_n}{1+q_n^2},\qquad
 a_n=\frac{t_n}{1+t_n},\qquad
 \eta_n=\frac{t_n(1-t_n)}{2(1+t_n)}.
\]
Then the **unique maximum-volume inscribed Euclidean ellipsoid** of \(Q_n\), in the standard coordinate metric, is
\[
 E_n=\{a_n\mathbf1+\Sigma_n^{1/2}u:\|u\|_2\le1\},\qquad
 \Sigma_n=\eta_n\bigl(I+\tfrac{t_n}{2}A_n\bigr)^{-1}.
\]
All \(2n\) facets of \(Q_n\) support \(E_n\) at pairwise distinct contact points. Its squared principal semiaxes, counted with multiplicity, are
\[
 \lambda_j=\frac{\eta_n}{1+t_n\cos(2\pi j/n)},\qquad j=0,\ldots,n-1.
\]
Writing \(\kappa_n=\pi^{n/2}/\Gamma(1+n/2)\), its exact volume is
\[
\operatorname{vol}_n(E_n)=\kappa_n\,\frac{q_n^{n/2}}{1+q_n^n}
 \left(\frac{1-q_n}{1+q_n}\right)^n.
\]
Moreover the parameter approaches its limiting value with a sharp, nonzero exponential correction:
\[
\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}
 \frac{1/\sqrt5-t_n}{(\sqrt5-2)^n}=\frac{8\sqrt5}{25}.
\]

## Assumptions and scope
All assertions concern the full-dimensional *fractional* stable-set polytope defined by the nonnegativity and adjacent-pair inequalities, not the integral stable-set polytope obtained by adding an odd-cycle inequality. The dimension is odd and at least five. The ellipsoid's shape matrix \(\Sigma_n\) is the positive-definite covariance-form matrix: an ellipsoid centered at \(c\) is \(\{c+\Sigma^{1/2}u:\|u\|_2\le1\}\). Its \(n\)-volume is \(\kappa_n\sqrt{\det\Sigma}\). The standard inner product, rather than an affine-invariant semiaxis normalization, fixes the displayed spectrum and volume.

## Proof
**1. The unique scalar parameter.** For \(0<t<1\), define
\[
 F_n(t)=\frac1n\sum_{j=0}^{n-1}\frac1{1+t\cos(2\pi j/n)},\qquad
 H_n(t)=\frac{1-t^2}{2t}F_n(t).
\]
Every summand \((1-t^2)/(2t(1+ct))\), with \(-1\le c\le1\), has derivative
\[
 -\frac{1+2ct+t^2}{2t^2(1+ct)^2}<0
\]
for \(0<t<1\); the numerator is \((t+c)^2+1-c^2>0\) in this interval. Thus \(H_n\) strictly decreases from infinity as \(t\downarrow0\). Because \(n\) is odd, none of the cosine values equals \(-1\); hence \(H_n(t)\to0\) as \(t\uparrow1\). There is exactly one \(t_n\in(0,1)\) for which
\[
 F_n(t_n)=\frac{2t_n}{1-t_n^2}. \tag{1}
\]
Set \(t=2q/(1+q^2)\), equivalently \(q=t/(1+\sqrt{1-t^2})\). The elementary Poisson-kernel expansion followed by the root-of-unity filter gives
\[
 F_n(t)=\frac{1+q^2}{1-q^2}
 \frac{1+(-q)^n}{1-(-q)^n}.
\]
For odd \(n\), substitution into (1) gives exactly
\[
1-4q-q^2=q^n(1+4q-q^2). \tag{2}
\]
The left side is strictly positive at the solution. Since its positive zero is \(r=\sqrt5-2\), it follows that \(q_n\in(0,r)\). This also proves uniqueness of the required root; in particular \(t_n<1/\sqrt5\).

**2. Exact tangencies.** Write \(t=t_n\), \(a=t/(1+t)\), \(\eta=t(1-t)/(2(1+t))\), and
\[
 D=\bigl(I+\tfrac t2 A_n\bigr)^{-1},\qquad \Sigma=\eta D.
\]
The Fourier eigenvalues of \(I+(t/2)A_n\) are \(1+t\cos(2\pi j/n)>0\), so \(\Sigma\) is positive definite. Cyclic symmetry implies \(D_{ii}=F_n(t)\) and \(D_{i,i+1}=G_n(t)\), where the diagonal equation of \((I+tA_n/2)D=I\) yields \(F_n+tG_n=1\). By (1),
\[
 \Sigma_{ii}=\eta F_n=a^2,\qquad
 (e_i+e_{i+1})^T\Sigma(e_i+e_{i+1})
 =2\eta(F_n+G_n)=(1-2a)^2.
\]
Here \(0<a<1/2\). For any ellipsoid \(E=\{c+\Sigma^{1/2}u:\|u\|_2\le1\}\), the support function is \(h_E(v)=v^Tc+\sqrt{v^T\Sigma v}\). With \(c=a\mathbf1\), the negative coordinate normals \(-e_i\) have support value \(-a+a=0\), and the edge normals \(e_i+e_{i+1}\) have support value \(2a+(1-2a)=1\). Thus \(E\subseteq Q_n\), and every defining facet is tangent to \(E\). Distinct facets have nonproportional normals; strict convexity of the ellipsoid ensures that their contact points are distinct.

**3. Global John optimality.** Use positive facet weights \(w_i^-=2a\) for the normals \(-e_i\) with margin \(a\), and \(w_i^+=1-2a\) for the normals \(e_i+e_{i+1}\) with margin \(1-2a\). The normalized contact normals \(p_i^-/a=-e_i/a\) and \(p_i^+/(1-2a)=(e_i+e_{i+1})/(1-2a)\) satisfy both John conditions:
\[
 \sum_i\left[w_i^-\frac{-e_i}{a}
 +w_i^+\frac{e_i+e_{i+1}}{1-2a}\right]=0,
\]
\[
\begin{aligned}
&\sum_i\left[w_i^-\frac{e_ie_i^T}{a^2}
 +w_i^+\frac{(e_i+e_{i+1})(e_i+e_{i+1})^T}{(1-2a)^2}\right]\\
&=\frac2a I+\frac1{1-2a}(2I+A_n)
=\frac1\eta\bigl(I+\tfrac t2 A_n\bigr)=\Sigma^{-1}.
\end{aligned}
\]
The last equalities follow on substituting \(a=t/(1+t)\) and \(\eta=t(1-t)/(2(1+t))\). Under the affine normalization \(u=\Sigma^{-1/2}(x-c)\), these are exactly the first-moment zero and second-moment identity conditions for contact points on the unit sphere. John's characterization therefore proves that \(E\) is the maximal-volume inscribed ellipsoid, uniquely.

**4. Spectrum and volume.** The discrete Fourier vectors diagonalize \(A_n\), giving the asserted semiaxes. By \(t=2q/(1+q^2)\),
\[
1+t\cos\theta=\frac{(1+qe^{i\theta})(1+qe^{-i\theta})}{1+q^2}.
\]
For odd \(n\), the roots-of-unity product implies
\[
 \prod_{j=0}^{n-1}(1+t\cos(2\pi j/n))
 =\frac{(1+q^n)^2}{(1+q^2)^n}.
\]
Also \(\eta(1+q^2)=q((1-q)/(1+q))^2\). Taking \(\kappa_n\sqrt{\det\Sigma}\) yields the displayed volume exactly.

**5. Sharp asymptotic.** The unique roots \(q_n\in(0,r)\) converge to \(r\): equation (2) forces the gap to vanish, since the right side is bounded by a fixed multiple of \(r^n\). Because \(1-4r-r^2=0\), factorization of (2) yields
\[
 (r-q_n)(4+r+q_n)=q_n^n(1+4q_n-q_n^2).
\]
Consequently \(r-q_n=O(r^n)\), and so \((q_n/r)^n\to1\). Taking the scaled limit gives
\[
 \frac{r-q_n}{r^n}\longrightarrow
 \frac{1+4r-r^2}{4+2r}=\frac{4r}{\sqrt5}.
\]
Finally the derivative of \(t(q)=2q/(1+q^2)\) at \(r\) is \(2(1-r^2)/(1+r^2)^2\). Multiplication and simplification give \(8\sqrt5/25\), proving the stated limit.

## Verification
The standalone standard-library script `verify.py` evaluates the unique defining scalar root by bisection for odd dimensions \(5\le n\le31\), constructs and inverts the actual candidate shape matrix, independently checks both classes of facet tangencies, checks the positive John inverse-shape identity and weight total, and checks the determinant product and finite-size asymptotic samples. This finite test does not certify the infinitely many dimensions or the asymptotic limit; those follow from the preceding analytic argument. Reproduce with `python3 verify.py`.

## Relationship to prior work
The fractional stable-set polytope and its facet formulation are standard. Kafer, Pashkovich and Sanità study circuit diameter of this same polytope, including its defining inequalities and circuit structure, not maximum-volume Euclidean inscribed ellipsoids. Hamano, Hibi and Ohsugi study Ehrhart and Gorenstein properties of fractional stable-set polytopes; those are different invariants. Giandomenico, Letchford, Rossi and Smriglio study outer ellipsoidal relaxations of the *integral* stable-set problem via the theta construction; an enclosing ellipsoid of a different body does not imply this inscribed-ellipsoid theorem. The standard John contact characterization and Fourier/root-of-unity methods are established tools, not claimed as discoveries. The present mathematical claim is the joint closed-form ellipsoid, complete contact system, and sharp exponential finite-size correction for odd cycles.

## Limitations
The theorem does not address even cycles, graph classes beyond odd cycles, integral stable-set polytopes, arbitrary affine metrics, or previously unknown global approximations for stable-set optimization. Numerical checks are finite, and no human or independent audit has been performed. Exhaustive historical priority cannot be guaranteed from the inspected sources; an equivalent formulation using cyclic packing, statistical D-optimal design, or other nomenclature remains a residual literature risk.

## References
1. S. Kafer, K. Pashkovich, L. Sanità, *On the Circuit Diameter of some Combinatorial Polytopes*, arXiv:1709.09642v1, first publicly posted 2017-09-27, Section 5, https://arxiv.org/html/1709.09642v1 ; SIAM J. Discrete Math. 33 (2019), 1–25, https://doi.org/10.1137/17M1152115 (journal listing: primary MSC 52B05).
2. G. Hamano, T. Hibi, H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613, https://arxiv.org/html/1603.09613v2 .
3. A. Giandomenico, A. N. Letchford, F. Rossi, S. Smriglio, *A New Approach to the Stable Set Problem Based on Ellipsoids* (2011), https://www.researchgate.net/publication/221316994_A_New_Approach_to_the_Stable_Set_Problem_Based_on_Ellipsoids .
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant on his 60th Birthday (1948), 187–204, standard ellipsoid contact characterization.
