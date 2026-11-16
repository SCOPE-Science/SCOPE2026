# A smooth positive annular weight with a boundary zero of its Szegő kernel

## Finding
Let \(A=\{z\in\mathbb C:1/4<|z|<1\}\), and give its boundary the strictly positive, real-analytic weight
\[
\varphi(\zeta)=|\zeta-2/3|^2,\qquad \zeta\in\partial A.
\]
Let \(S_\varphi\) be the weighted Szegő reproducing kernel of the holomorphic Hardy space on \(A\), with squared norm \((2\pi)^{-1}\int_{\partial A}|f|^2\varphi\,ds\). **There exists a real number \(w_*\in(-3/4,-3/8)\subset A\) for which \(S_\varphi(1,w_*)=0\).** The first argument \(1\) lies on the **outer boundary**, whereas the second argument lies strictly in the domain. In particular, smooth strict positivity of the boundary weight does not guarantee boundary-to-interior zero-freeness of the weighted Szegő kernel on a doubly connected domain.

The statement answers the existential boundary-zero question explicitly raised in Remark 5.7(1) of Jain–Verma (2025) and Problem 2.1 of Jain (2026), for this annular example. No assertion about weights lacking a holomorphic modulus factor or about arbitrary multiply connected domains is made.

## Assumptions and scope
The boundary of \(A\) is the union of the circles of radii \(1\) and \(\rho=1/4\); \(ds\) denotes ordinary Euclidean arclength on each circle. The Hardy space is the closure in \(L^2(\partial A,ds/(2\pi))\) of Laurent polynomials, equivalently the usual space of analytic functions with square-integrable boundary traces. The weighted Hardy space is the analogous closure in the positive weight \(\varphi\,ds/(2\pi)\). The parameter \(p=2/3\) lies in \(A\), and \(q(z)=z-p\) has no zeros on \(\partial A\), so \(\varphi=|q|^2\) is smooth and strictly positive there. All kernel formulas use an inner product linear in the first argument. Multiplying the measure by a positive constant rescales the kernel but does not change its zeros.

The point \(1\) is the boundary limit of the first variable of the kernel; the displayed series converges absolutely there for every second variable in a compact subset of \(A\).

## Proof
**1. The unweighted annulus kernel.** Distinct Laurent monomials are orthogonal with
\[
\|z^n\|_0^2=1+\rho^{2n+1}\quad (n\in\mathbb Z).
\]
Consequently the unweighted Szegő kernel is \(S_0(z,w)=H(z\overline w)\), where
\[
H(s)=\sum_{n\in\mathbb Z}\frac{s^n}{1+\rho^{2n+1}},\qquad \rho^2<|s|<1.
\]
Both positive- and negative-index portions converge absolutely in this annulus. In particular, \(H(s)\) is real for real \(s\) in \((-1,-\rho^2)\cup(\rho^2,1)\). The normalization is compatible with the standard Euclidean arclength formula for annular Szegő kernels.

**2. Removing one interior evaluation.** Multiplication by \(q(z)=z-p\) is an isometry from the weighted Hardy space onto the closed codimension-one subspace \(H_0^p=\{g\in H_0:g(p)=0\}\). Indeed, \(qf\) vanishes at \(p\), and conversely \(g/q\) has a removable singularity at \(p\), while \(q\) and \(1/q\) are bounded near both boundary circles. The reproducing kernel of \(H_0^p\) is the rank-one compression
\[
S_0^p(z,w)=H(z\overline w)-\frac{H(zp)H(p\overline w)}{H(p^2)}.
\]
It follows from the isometry, for \(z,w\ne p\), that
\[
S_\varphi(z,w)=\frac{H(z\overline w)H(p^2)-H(zp)H(p\overline w)}{H(p^2)(z-p)(\overline w-p)}.
\]
Since \(H(p^2)>0\), \(1-p\ne0\), and \(w-p\ne0\) for negative real \(w\), zeros of \(S_\varphi(1,w)\) there are exactly zeros of the real continuous function
\[
D(w)=H(w)H(p^2)-H(p)H(pw),\qquad -1<w<-\rho.
\]

**3. Rigorous opposite signs.** Put \(H_N(s)=\sum_{n=-N}^{N}s^n/(1+\rho^{2n+1})\) with \(N=32\), and \(D_N(w)=H_N(w)H_N(p^2)-H_N(p)H_N(pw)\). Each value of \(D_N\) at the two rational test points is an *exact rational number*. Direct integer arithmetic gives
\[
D_{32}(-3/8)>19/100,\qquad D_{32}(-3/4)<-9/100.
\]
Here is a fully explicit truncation error bound, so those finite inequalities imply strict signs for the infinite kernel. For every real \(s\) in the six arguments \(w,p^2,p,pw\) used at the two test points, \(1/4\le |s|\le3/4\). For such \(s\), the positive-index tail is bounded by \(4(3/4)^{N+1}\), and the negative-index tail by \((16/3)(1/4)^{N+1}\), since for \(k\ge1\), \(1/(1+\rho^{1-2k})\le4/16^k\). Thus
\[
|H(s)-H_N(s)|\le E_N:=4(3/4)^{N+1}+(16/3)(1/4)^{N+1},\qquad E_{32}<1/3000.
\]
The geometric bounds on both index ranges also give \(|H(s)|,|H_N(s)|\le16/3<6\). Estimating the errors in the four products therefore yields
\[
|D(w)-D_{32}(w)|\le24E_{32}<1/125.
\]
Hence \(D(-3/8)>19/100-1/125>0\), whereas \(D(-3/4)<-9/100+1/125<0\). Continuity and the intermediate value theorem furnish a zero \(w_*\in(-3/4,-3/8)\), and the denominator in the formula for \(S_\varphi(1,w_*)\) is nonzero. This completes the proof.

## Verification
The standalone `CHECK.py` uses only Python's standard library and exact `fractions.Fraction` arithmetic. It independently reconstructs the finite Laurent sum with \(N=32\), checks the two strict rational inequalities, verifies \(E_{32}<1/3000\), checks all six argument magnitudes, and validates the resulting error-separated signs. The finite rational calculation is a fully described, reproducible step of the proof. Floating-point root searches are neither required nor used for acceptance.

Run with `python CHECK.py` from the directory containing this document. The printed decimal illustrations are optional; exact comparisons determine success.

## Relationship to prior work
Jain and Verma, *Weighted Kernel Functions on Planar Domains* (initial public arXiv version 19 August 2025), explicitly report in Remark 5.7(1) that they do not know a smooth positive weight producing a weighted Szegő/Garabedian kernel zero with one variable on the boundary and the other in the interior. Their Example 5.3 assumes a **nowhere-zero** holomorphic factor; the present factor \(q=z-p\) has an interior zero, so the corresponding rank-one compression is essential. Their Theorem 3.4 concerns weights approaching the constant weight and does not exclude the present example. Jain, *On the weighted Szegő kernel* (online 28 April 2026), repeats the boundary-zero question in Problem 2.1.

The known annular Szegő-kernel bilateral series, unique unweighted zero, and theta-product formulas are background (Gafai–Murid–Wahid 2022; Gafai–Murid–Naqos–Wahid 2023). The 2022 article also studies **rotation-invariant** boundary-component weights, not the nonradial weight used here. The novelty claim concerns the explicit smooth-positive **nonradial weight and boundary-to-interior zero**, not the classical annular kernel or the standard rank-one projection formula.

## Limitations
The result is existential, with a certified rational interval for the second argument; it does not establish its uniqueness or an exact closed form. The weight admits a holomorphic modulus factor with one interior zero, so it does not resolve the *separate* question of whether every positive boundary weight admits such a holomorphic factor. Its conclusion is specific to the given annulus and weight; no classification of all weights or annuli is asserted. The present review is not independent verification of mathematical priority.

## References
1. A. Jain and K. Verma, *Weighted Kernel Functions on Planar Domains*, arXiv:2508.14016, first submitted 19 August 2025, especially Theorem 3.4, Example 5.3, and Remark 5.7. https://arxiv.org/abs/2508.14016
2. A. Jain, *On the weighted Szegő kernel*, Concrete Operators 13 (2026), article 20260016, published online 28 April 2026, Problem 2.1. https://doi.org/10.1515/conop-2025-0016
3. N. S. Gafai, A. H. M. Murid, N. H. A. A. Wahid, *Infinite Product Representation for the Szegö Kernel for an Annulus*, Journal of Function Spaces (2022), article 3763450, Sections 4–5. https://doi.org/10.1155/2022/3763450
4. N. S. Gafai, A. H. M. Murid, S. Naqos, N. H. A. A. Wahid, *Computing the zeros of the Szegö kernel for doubly connected regions using conformal mapping*, AIMS Mathematics 8 (2023), 12040–12061, Theorem 1. https://doi.org/10.3934/math.2023607
