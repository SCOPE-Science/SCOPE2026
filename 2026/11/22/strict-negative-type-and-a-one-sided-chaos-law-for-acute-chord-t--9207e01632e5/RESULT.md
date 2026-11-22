# Strict negative type and a one-sided chaos law for acute chord triangles on the sphere

## Finding

Write \(\sigma\) for normalized surface area on the unit sphere \(S^2\subset\mathbb R^3\), and define the continuous zonal kernel
\[
K(x,y)=\sqrt{\frac{1-x\cdot y}{2}}+\frac12\sqrt{\frac{1+x\cdot y}{2}}-\frac12,
\qquad h(x,y)=K(x,y)-\frac12.
\]
For distinct nonantipodal points \(x,y\), \(K(x,y)\) is the probability that \(x,y,Z\) form a **strictly acute Euclidean chord triangle** when \(Z\sim\sigma\). For antipodal endpoints that probability is zero, rather than \(K(x,-x)=1/2\).

The integral operator with kernel \(h\) on \(L^2(\sigma)\) has eigenvalue zero on constants and, on the degree-\(\ell\) real spherical harmonics, the **strictly negative** eigenvalue
\[
\boxed{\lambda_\ell=-\frac{2+(-1)^\ell}{8(\ell-\frac12)(\ell+\frac12)(\ell+\frac32)}<0,\quad \ell=1,2,\ldots,}
\]
with multiplicity \(2\ell+1\). The nonconstant expansion is absolutely and uniformly convergent. Consequently, for any Borel probability measure \(\mu\) on \(S^2\), independent \(A,B\sim\mu\) and \(Z\sim\sigma\), and any real orthonormal harmonic basis \(Y_{\ell m}\) for \(L^2(\sigma)\),
\[
\boxed{\frac12-\Pr(ABZ\text{ strictly acute})=
 \sum_{\ell\ge1}|\lambda_\ell|\sum_{m=1}^{2\ell+1}
 \left(\int Y_{\ell m}\,d\mu\right)^2
 +\frac12\Pr(A=-B).}
\]
The right side vanishes **if and only if** \(\mu=\sigma\); the uniform surface law is the unique optimizer of this mixed-sampling acuteness problem.

For independent \(X_1,\ldots,X_n\sim\sigma\), let \(T_n\) count strictly acute Euclidean chord triangles over all unordered triples of indices. Then
\[
\boxed{\frac{T_n-\frac12\binom n3}{n^2}\ \Longrightarrow\ W
=\frac14-\frac12\sum_{\ell=1}^{\infty}|\lambda_\ell|Q_{2\ell+1},}
\]
where the \(Q_{2\ell+1}\) are mutually independent chi-square variables with the indicated integer degrees of freedom. The sum is almost surely finite, \(W\) has mean zero, variance \((\pi-3)/16\), a **sharp upper support endpoint** \(1/4\), and an unbounded lower tail. In particular the limit is not Gaussian. This is one coherent spectral statement: the same negative harmonic eigenvalues govern the deterministic extremal identity and the random counting fluctuations.

## Assumptions and scope

Every triangle is the ordinary flat triangle with three chords in \(\mathbb R^3\), **not** an intrinsic spherical geodesic triangle. Strict acuteness excludes right and degenerate triangles. The extremal identity allows arbitrary Borel measures \(\mu\), including atoms. The limiting theorem assumes independent **normalized surface-uniform** vertices and fixed sphere dimension two; \(n\to\infty\). All harmonics are real and orthonormal against probability measure \(\sigma\), not unnormalized surface area. The chi-square variables on different harmonic degrees are independent. Their degrees of freedom are \(2\ell+1\), and no unspecified centering is hidden in the displayed representation.

## Proof

**1. Conditional acute-region geometry.** Take noncoincident, nonantipodal \(x,y\), with central separation \(\theta\in(0,\pi)\), \(s=\sin(\theta/2)\), \(c=\cos(\theta/2)\). For perpendicular unit vectors \(u,v\) choose \(x=cv-su\), \(y=cv+su\). The three dot-product inequalities expressing strict acuteness at \(x,y,z\), respectively, are
\[
-s<u\cdot z<s,\qquad v\cdot z<c.
\]
Uniform projection onto any axis of \(S^2\) is uniform on \([-1,1]\). Hence the spherical belt \(|u\cdot z|<s\) has probability \(s\). The cap \(v\cdot z\ge c\), of probability \((1-c)/2\), lies in this belt because \(u\perp v\) and \(|u\cdot z|\le\sqrt{1-c^2}=s\). Subtraction gives \(K(x,y)=s-(1-c)/2\). Coincident endpoints have zero acute probability, agreeing with \(K(x,x)=0\). Antipodal endpoints always produce a right angle at \(z\), giving probability zero, whereas the continuous extension has \(K(x,-x)=1/2\). Thus the exact difference between the actual conditional probability and \(K\) is \(1/2\) times the indicator of antipodality.

**2. Harmonic coefficients and their signs.** By rotation invariance and the Funk--Hecke formula, the eigenvalue in harmonic degree \(\ell\) is
\[
\frac12\int_{-1}^1h(t)P_\ell(t)\,dt,
\quad h(t)=\sqrt{\frac{1-t}{2}}+\frac12\sqrt{\frac{1+t}{2}}-1,
\]
where \(P_\ell\) is the Legendre polynomial and \(P_\ell(1)=1\). The average of \(K\) is \(1/2\), since the averages of both square-root terms individually equal \(2/3\); therefore the degree-zero coefficient of \(h\) is zero. For \(\ell\ge1\), Rodrigues' formula and \(\ell\) integrations by parts (or an equivalent beta integral) yield
\[
a_\ell:=\frac12\int_{-1}^1\sqrt{\frac{1+t}{2}}P_\ell(t)\,dt
=\frac{\Gamma(3/2)^2}{\Gamma(3/2-\ell)\Gamma(\ell+5/2)}
=\frac{(-1)^{\ell+1}}{4(\ell-\frac12)(\ell+\frac12)(\ell+\frac32)}.
\]
Parity gives the other square-root coefficient \((-1)^\ell a_\ell\), hence \(\lambda_\ell=((-1)^\ell+1/2)a_\ell\), exactly the negative formula in the finding. It decays as \(O(\ell^{-3})\), and \(\sum_{\ell\ge1}(2\ell+1)|\lambda_\ell|<\infty\). The addition theorem gives the absolutely uniformly convergent expansion
\[
h(x,y)=\sum_{\ell\ge1}\lambda_\ell\sum_{m=1}^{2\ell+1}Y_{\ell m}(x)Y_{\ell m}(y)
=\sum_{\ell\ge1}(2\ell+1)\lambda_\ell P_\ell(x\cdot y).
\]
Its trace identity, obtained by setting \(x=y\), is
\[
\sum_{\ell\ge1}(2\ell+1)|\lambda_\ell|=-h(x,x)=\frac12.
\]

**3. An exact extremal deficit for all sampling measures.** Integrate the uniformly convergent expansion against \(\mu\otimes\mu\). The constant part of \(K\) contributes \(1/2\). Correcting the exceptional antipodal pairs by step 1 gives the displayed identity. All spectral terms are nonnegative. If the sum is zero, every nonconstant spherical harmonic has zero \(\mu\)-integral. Constants have the same integral under \(\mu\) and \(\sigma\), and finite spherical-harmonic sums are uniformly dense in continuous functions on the sphere (polynomial approximation). Hence \(\mu=\sigma\). Conversely \(\mu=\sigma\) kills all nonconstant harmonic means and has no antipodal atoms, attaining probability \(1/2\).

**4. Exact second projection and the counting limit.** Let \(H(x,y,z)\) be the zero-one strictly acute indicator for three points. Under \(\sigma^{\otimes3}\), \(p=\mathbb EH=1/2\). Rotational invariance makes the first Hoeffding projection identically zero, while the second is \(h_2(x,y)=\mathbb E[H(x,y,Z)]-p=h(x,y)\) almost everywhere. Define the completely canonical third projection
\[
h_3(x,y,z)=H(x,y,z)-p-h(x,y)-h(x,z)-h(y,z).
\]
Conditional expectation given any two arguments is zero. Thus the exact unnormalized Hoeffding decomposition is
\[
T_n-\frac12\binom n3=(n-2)\sum_{i<j}h(X_i,X_j)+\sum_{i<j<k}h_3(X_i,X_j,X_k).
\]
The canonical triple terms for distinct triples are pairwise uncorrelated, so the last sum has variance \(\binom n3\mathbb E[h_3^2]=O(n^3)\) and, divided by \(n^2\), vanishes in \(L^2\).

For a finite harmonic cutoff \(L\), the addition theorem rewrites the leading pair term as
\[
\frac1n\sum_{i<j}h^{(L)}(X_i,X_j)
=\frac12\sum_{\ell=1}^L\lambda_\ell\sum_{m=1}^{2\ell+1}
\left[\left(\frac1{\sqrt n}\sum_iY_{\ell m}(X_i)\right)^2
-\frac1n\sum_iY_{\ell m}(X_i)^2\right].
\]
The multivariate central limit theorem and law of large numbers give independent standard-Gaussian coordinates in the brackets' limits. The squared \(L^2\) tail of the normalized canonical pair sum is at most \(\tfrac12\sum_{\ell>L}(2\ell+1)\lambda_\ell^2\), uniformly in \(n\). First take \(n\to\infty\), then \(L\to\infty\). The factor \((n-2)/n\to1\) gives
\[
\frac{T_n-\frac12\binom n3}{n^2}
\Longrightarrow\frac12\sum_{\ell\ge1}\lambda_\ell\bigl(Q_{2\ell+1}-(2\ell+1)\bigr).
\]
The trace identity turns this centered series into the claimed \(1/4-\frac12\sum|\lambda_\ell|Q_{2\ell+1}\), with almost sure and \(L^1\) convergence of the nonnegative sum. Its upper bound is \(1/4\). This endpoint is sharp: keep finitely many chi-squares arbitrarily small (an event of positive probability), then control the remaining nonnegative weighted tail by its arbitrarily small expectation. Its lower support is unbounded because the degree-one chi-square is unbounded and independent of the other degrees.

**5. Variance and non-Gaussianity.** Since \(x\cdot y\) is uniform on \([-1,1]\) for independent \(\sigma\)-points, write \(s=\sqrt{(1-t)/2}\), \(c=\sqrt{(1+t)/2}\). We have \(\mathbb Es=\mathbb Ec=2/3\), \(\mathbb Es^2=\mathbb Ec^2=1/2\), \(\mathbb Esc=\pi/8\), and \(K=s+(c-1)/2\). Thus
\[
\mathbb E K^2=\frac{\pi-1}{8},\qquad \int h^2\,d\sigma^{\otimes2}=\frac{\pi-3}{8}
=\sum_{\ell\ge1}(2\ell+1)\lambda_\ell^2.
\]
Independent chi-square variances then yield \(\operatorname{Var}(W)=\frac12\sum(2\ell+1)\lambda_\ell^2=(\pi-3)/16\). The finite upper endpoint together with positive variance rules out a Gaussian law. The exact finite-sample variance of \(T_n\) was established in earlier work and is not asserted to be new.

## Verification

Run `python3 verify.py` using the standalone standard-library checker included with this result. It independently integrates the conditional acuteness kernel, numerically recomputes the first twelve Funk--Hecke eigenvalues from Legendre polynomials, checks positivity of their negatives, sums the trace and Hilbert--Schmidt masses, checks the Hoeffding variance identity at several sample sizes, and simulates the three-point acute event at fixed chord separations using direct Cartesian dot products. The executed check returned `ALL_CHECKS_PASSED`, with trace sum through degree 50,000 equal to \(0.499990000250\) and the squared-eigenvalue sum through degree 1,000 equal to \(0.017699081699\), versus \((\pi-3)/8\). Such computations corroborate but do not replace the infinite arguments in the proof.

## Relationship to prior work

Edelman--Strang (2015) gives a foundational random-triangle shape treatment; its Gaussian/shape-space sampling model is not surface-uniform sampling of a fixed sphere. Brauchart and collaborators (2015) study large random spherical point sets and extremal angular separation, not acuteness counts or their harmonic fluctuation law. Akopyan--Edelsbrunner--Nikitenko (2020), Section 3 and Lemma 4, proves the single-triangle Euclidean acuteness probability \(1/2\) and studies acute facets; it does not establish the present strict harmonic spectrum, arbitrary-measure extremizer or full count limit.

The separately published *Exact variance of acute Euclidean chord triangles on a sphere* explicitly establishes the pairwise conditional kernel \(K\), joint probability and exact finite-sample variance. Those are **used and credited as established inputs**, not renewed novelty claims. Its complete accessible result does not evaluate the infinitely many Legendre eigenvalues, prove the mixed-sampling optimality/deficit identity, or identify the one-sided non-Gaussian limiting distribution of the complete count. A related published result on strongly obtuse inscribed-triangle counts concerns arclength-uniform points on the **circle**, an angle threshold strictly above a right angle, and Fourier coefficients of both signs; its circle geometry does not imply the sphere result. General Funk--Hecke and canonical U-statistic theory supplies methodology, but not the explicit signed spectrum or geometric rigidity conclusion.

## Limitations

The count-limit statement is for surface-uniform samples on exactly \(S^2\), with no dimension-uniform claim or finite-\(n\) distribution formula. The extremal theorem fixes the **third** vertex to be surface-uniform; it does not maximize the probability for three independent vertices all drawn from an arbitrary common measure. The spectral deficit contains an exceptional antipodal-atom correction, without which the arbitrary-measure statement would be false. Historical priority is provisional, not independently certified; the generic degenerate U-statistic machinery and the previously published conditional kernel substantially reduce the independent novelty to the explicit harmonic signs, strict optimization identity and specified limiting law.

## References

1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053v1, first public 9 January 2015. https://arxiv.org/html/1501.03053v1
2. J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang and R. S. Womersley, *Random Point Sets on the Sphere—Hole Radii, Covering, and Separation*, arXiv:1512.07470v1, first public 23 December 2015. https://arxiv.org/abs/1512.07470
3. A. Akopyan, H. Edelsbrunner and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783v1, first public 15 July 2020. https://arxiv.org/html/2007.07783v1
4. *Exact variance of acute Euclidean chord triangles on a sphere*, published mathematical research record, 1 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-variance-of-acute-euclidean-chord-triangles-on-a-sphere--662e8b72619a
5. *Strongly obtuse inscribed-triangle counts: exact variance and a two-sided spectral limit*, published mathematical research record, 25 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-strongly-obtuse-inscribed-triangle-counts-exact-variance-and-a-t--8db816b9ed60
6. R. J. Serfling, *Approximation Theorems of Mathematical Statistics*, Wiley, 1980, Section 5.5 (general U-statistics tools).
