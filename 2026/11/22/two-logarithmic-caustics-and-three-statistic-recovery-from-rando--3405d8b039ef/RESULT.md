# Two logarithmic caustics and three-statistic recovery from random ellipsoid shadows

## Finding
Let \(a>b>c>0\) be the semiaxes of a solid triaxial Euclidean ellipsoid. For a Haar-uniform orthogonal projection onto a plane, let \(S\ge T>0\) denote the squared major and minor semiaxes of the projected ellipse, and let \(R=S/T\). Put \(A=a^2\), \(B=b^2\), and \(C=c^2\).

The density \(f_R\) has precisely two interior logarithmic saddle contributions, at \(r_A=B/C\) and \(r_C=A/B\). If these are different, they are the only interior divergences, and
\[
 f_R(r)=\kappa_A\log\frac1{|r-B/C|}+O_{A,B,C}(1),\quad
 \kappa_A=\frac{C^{3/2}}{2\pi\sqrt{B(A-B)(A-C)}}
\]
near \(r=B/C\), while
\[
 f_R(r)=\kappa_C\log\frac1{|r-A/B|}+O_{A,B,C}(1),\quad
 \kappa_C=\frac{B^{3/2}}{2\pi\sqrt{A(A-C)(B-C)}}
\]
near \(r=A/B\). If \(B^2=AC\), the two locations coincide and the logarithmic coefficient is \(\kappa_A+\kappa_C\).

More importantly, the *two singularity positions and the coefficient of the higher-position singularity* determine both intrinsic axis ratios \(b/a\) and \(c/a\) uniquely. Write the ordered singularity positions as \(1<p\le q\). When \(p<q\), the squared-axis ratios \((B/A,C/A)\) are exactly one of
\[
 \left(\frac1p,\frac1{pq}\right),\qquad
 \left(\frac1q,\frac1{pq}\right).
\]
The coefficient \(k_q=\lim_{r\to q} f_R(r)/\log(1/|r-q|)\) equals, respectively,
\[
 K_1=\frac{1}{2\pi q\sqrt{(p-1)(pq-1)}}\quad\text{or}\quad
 K_2=\frac{p}{2\pi\sqrt{q(p-1)(pq-1)}}.
\]
Because \(K_2/K_1=p\sqrt q>1\), the two candidates are strictly distinguishable. If \(p=q\), then \((B/A,C/A)=(1/p,1/p^2)\) already. Thus the stated three statistics recover the ellipsoid up to homothety and rigid motion (not absolute scale).

The same law has sharp endpoint probabilities:
\[
 \Pr(R<1+\varepsilon)\sim \frac{B^2}{4(A-B)(B-C)}\varepsilon^2,
 \qquad
 \Pr(R>A/C-\varepsilon)\sim
 \frac{C^{3/2}}{2\sqrt{A(A-B)(B-C)}}\varepsilon.
\]

## Assumptions and scope
The ellipsoid is \(\{x\in\mathbb R^3:x_1^2/A+x_2^2/B+x_3^2/C\le1\}\) with strictly distinct semiaxes. The viewing normal is Haar-uniform on \(S^2\), and the shadow is the *orthographic* Euclidean projection, not a central section. All densities are with respect to the squared visible aspect ratio \(r=R\), not \(\sqrt R\) or the conventional minor/major ratio. Logarithms use dimensionless ratios. The asymptotics hold at fixed \(A>B>C>0\) with \(\varepsilon\downarrow0\), not uniformly as eigenvalue gaps collapse.

## Proof
**1. Exact spectral law.** The projected ellipse has support function \(h(v)=\sqrt{v^TQv}\) for in-plane unit vectors, where \(Q=\operatorname{diag}(A,B,C)\). Its squared semiaxes \(S\ge T\) are the eigenvalues of the restriction of \(Q\) to the normal plane. Interlacing gives \(A\ge S\ge B\ge T\ge C\). For viewing normal \(n\), put \(w_i=n_i^2\). The secular numerator identity is
\[
 \sum_{i=1}^3w_i\prod_{j\ne i}(z-q_j)=(z-S)(z-T),
 \quad(q_1,q_2,q_3)=(A,B,C).
\]
Evaluation at the three \(q_i\) gives
\[
 w_1=\frac{(A-S)(A-T)}{(A-B)(A-C)},\quad
 w_2=\frac{(S-B)(B-T)}{(A-B)(B-C)},\quad
 w_3=\frac{(S-C)(T-C)}{(A-C)(B-C)}.
\]
The weights have the \(\operatorname{Dirichlet}(1/2,1/2,1/2)\) density \((2\pi\sqrt{w_1w_2w_3})^{-1}\). The Jacobian of \((S,T)\mapsto(w_1,w_3)\) is \((S-T)/[(A-B)(A-C)(B-C)]\). Hence the exact joint density on \(B<S<A\), \(C<T<B\) is
\[
 f_{S,T}(s,t)=\frac{s-t}{2\pi\sqrt{(A-s)(A-t)(s-B)(B-t)(s-C)(t-C)}}.
\]
Consequently the *complete* marginal density of \(R=S/T\) is the self-contained quadrature
\[
 f_R(r)=\frac{r-1}{2\pi}\int_{\max\{C,B/r\}}^{\min\{B,A/r\}}
 \frac{t^2\,dt}{\sqrt{(A-rt)(A-t)(rt-B)(B-t)(rt-C)(t-C)}},
 \quad 1<r<A/C,
\]
with the integral taken as zero if its lower endpoint exceeds its upper endpoint. This classical forward-projection distribution is included as a *starting identity*, not claimed as a new forward kernel.

**2. Exhaustive singularity locations and coefficients.** The integration endpoints switch formulas only at \(r=B/C\) and \(r=A/B\). Elsewhere in \((1,A/C)\) the integral can be regularized by a smooth square-root endpoint substitution, so its density has no divergent singularities. Near a normal \(n=e_1\), introduce orthonormal local coordinates \((u,v)=(n_2,n_3)\). The eigenvalues have second-order expansions
\[
 S=B+(A-B)u^2+O(\|(u,v)\|^3),\quad
 T=C+(A-C)v^2+O(\|(u,v)\|^3),
\]
so
\[
 R-\frac BC=\frac{A-B}{C}u^2-\frac{B(A-C)}{C^2}v^2+O(\|(u,v)\|^3).
\]
For a smooth probability density equal to \(1/(4\pi)\) at each of the two antipodal poles, a nondegenerate saddle \(F=F_0+\alpha u^2-\beta v^2+O(\|(u,v)\|^3)\) contributes \((2\pi\sqrt{\alpha\beta})^{-1}\log(1/|F-F_0|)+O(1)\) to the pushed-forward density. Indeed the linear change \((x,y)=(\sqrt\alpha u+\sqrt\beta v,\sqrt\alpha u-\sqrt\beta v)\) reduces the quadratic form to \(xy\), with Jacobian \((2\sqrt{\alpha\beta})^{-1}\), and integrating \(\delta(z-xy)\) over a fixed small square yields \(2\log(1/|z|)+O(1)\); the Morse lemma controls higher-order errors. This gives \(\kappa_A\).

At \(n=e_3\), local coordinates \((u,v)=(n_1,n_2)\) instead give
\[
 R-\frac AB=-\frac{A-C}{B}u^2+\frac{A(B-C)}{B^2}v^2+O(\|(u,v)\|^3),
\]
which gives \(\kappa_C\). A normal \(\pm e_2\) maximizes \(R=A/C\), and the only nonsmooth interior directions of the eigenvalue map are those giving a circular shadow \(R=1\). Thus there are no other saddle contributions. Coincident levels add their coefficients.

**3. Inversion.** Let \(p<q\) be the ordered observed logarithmic levels. Their product is \((B/C)(A/B)=A/C=pq\). The only choices for \(B/A\) are \(1/p\) and \(1/q\). In the first, the upper singularity is \(B/C=q\), and substitution into \(\kappa_A\) yields \(K_1\); in the second, it is \(A/B=q\), and substitution into \(\kappa_C\) yields \(K_2\). Their ratio is \(p\sqrt q>1\), excluding ambiguity. If \(p=q\), the middle squared semiaxis is the geometric mean of the other two, giving the stated unique ratios.

**4. Endpoint laws.** Near a circular shadow set \(s=B+u\), \(t=B-v\) with \(u,v>0\). The joint density is \((u+v)/[2\pi(A-B)(B-C)\sqrt{uv}]\,(1+o(1))\), and \(R-1=(u+v)/B+o(u+v)\). Integration over \(u+v<B\varepsilon\) gives the displayed quadratic law. Near the global maximum, set \(s=A-u\), \(t=C+v\); the joint density is \([2\pi\sqrt{(A-B)(B-C)uv}]^{-1}(1+o(1))\), and \(A/C-R=u/C+Av/C^2+o(u+v)\). Integration over this simplex gives the displayed linear law. All relative errors are uniform after rescaling over each compact limiting simplex, with integrable square-root boundary factors.

## Verification
Run `python triaxial_shadow_check.py` in a Python 3 environment containing NumPy and SciPy. The checker exercises the secular-coordinate inversion against independently diagonalized randomly oriented shadow matrices; both logarithmic density coefficients (including their coalescence), the small- and large-ratio endpoint laws, normalization of the exact integral, and the two-branch reconstruction. It reports 990 passed deterministic numerical/algebraic assertions. These tests are diagnostics; the infinite-dimensional assertions above follow from the analytic proof, not numerical enumeration.

## Relationship to prior work
Binney and de Vaucouleurs (1981, Section 2.2 and Appendix) already gave the apparent-axis-ratio projection kernel of triaxial models and explicitly identified two preferred principal-axis ratios. Binney (1985, Section 2) also derived the forward projected-ellipse geometry. Those forward formulas and peak *locations* are **not claimed novel here**. The contribution under examination is the explicit two-sided logarithmic coefficients, their exact coalescence, and especially the algebraic three-statistic *inverse classification*, including the strict factor \(p\sqrt q\) discriminating the two middle-axis candidates. The Dirichlet/interlacing joint density is a convenient rederivation of classical compression probability, not itself a priority claim. Published work on identifying population distributions of varying galaxy shapes concerns a distinct statistical mixture inverse problem.

## Limitations
The three-statistic inversion is exact only for a single strictly triaxial shape observed under an ideal Haar distribution of viewing directions, without sampling noise, selection bias, or mixtures of shapes. No finite-sample estimator, noise robustness, or uniqueness for distributions of different intrinsic ellipsoids is established. The forward projection kernel and the two peak positions have documented priority in 1981; the originality assessment concerns the sharp coefficients and inverse theorem, and independent historical verification remains necessary.

## References
1. J. Binney and G. de Vaucouleurs, *The apparent and true ellipticities of galaxies of different Hubble types in the Second Reference Catalogue*, Monthly Notices of the Royal Astronomical Society 194 (1981), 679–691, especially Section 2.2 and Appendix. DOI: https://doi.org/10.1093/mnras/194.3.679 (public date verified March 1, 1981).
2. J. Binney, *Testing for triaxiality with kinematic data*, Monthly Notices of the Royal Astronomical Society 212 (1985), 767–781, especially Section 2. DOI: https://doi.org/10.1093/mnras/212.4.767.
3. M. Cappellari et al., *The ATLAS3D project – XXIV. The intrinsic shape distribution of early-type galaxies*, Monthly Notices of the Royal Astronomical Society 444 (2014), 3340–3355, Section 3.1. DOI: https://doi.org/10.1093/mnras/stu1603 (population-level inverse context).
