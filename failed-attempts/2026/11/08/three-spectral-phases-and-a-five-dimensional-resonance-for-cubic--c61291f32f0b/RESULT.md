# Three spectral phases and a five-dimensional resonance for cubic spherical harmonics in antipodal caps

## Finding
Let \(\sigma\) be normalized surface measure on \(\mathbb S^2\), let \(\mathcal H_3\) be the real seven-dimensional space of degree-three spherical harmonics, and for every \(0<t<1\) put
\[
C_t=\{\omega\in\mathbb S^2:|\omega_3|\ge t\},\qquad K_t=P_{\mathcal H_3}\,\mathbf1_{C_t}|_{\mathcal H_3}.
\]
The self-adjoint concentration operator \(K_t\) has four eigenvalue sectors \(E_m\), \(m=0,1,2,3\), corresponding to azimuthal order \(m\). Their dimensions are respectively \(1,2,2,2\), and the eigenvalues are exactly
\[
\begin{aligned}
\lambda_0(t)&=1-\frac{21}{4}t^3+\frac{21}{2}t^5-\frac{25}{4}t^7,\\
\lambda_1(t)&=1-\frac{21}{16}t+\frac{77}{16}t^3-\frac{147}{16}t^5+\frac{75}{16}t^7,\\
\lambda_2(t)&=1-\frac{35}{8}t^3+\frac{21}{4}t^5-\frac{15}{8}t^7,\\
\lambda_3(t)&=1-\frac{35}{16}t+\frac{35}{16}t^3-\frac{21}{16}t^5+\frac{5}{16}t^7.
\end{aligned}
\]
Define \(t_1=1/\sqrt5\) and \(t_2=\sqrt{3/5}\). The **complete strict ordering and crossing classification** on the nondegenerate range is:

- For \(0<t<t_1\): \(\lambda_2>\lambda_0>\lambda_1>\lambda_3\).
- At \(t=t_1\): \(\lambda_0=\lambda_1=\lambda_2>\lambda_3\).
- For \(t_1<t<t_2\): \(\lambda_1>\lambda_0>\lambda_2>\lambda_3\).
- At \(t=t_2\): \(\lambda_0=\lambda_1>\lambda_2>\lambda_3\).
- For \(t_2<t<1\): \(\lambda_0>\lambda_1>\lambda_2>\lambda_3\).

There are no other distinct-sector crossings in \(0<t<1\). At the first threshold the top eigenspace has dimension five, and
\[
\left.K_{t_1}\right|_{E_0\oplus E_1\oplus E_2}
=\left(1-\frac{17\sqrt5}{125}\right)I,
\qquad\left.K_{t_1}\right|_{E_3}=\left(1-\frac{9\sqrt5}{25}\right)I.
\]
At the second threshold the top eigenspace has dimension three, with eigenvalue \(1-18\sqrt{15}/125\). In particular the optimal concentration mode passes through \(m=2\), then \(m=1\), then \(m=0\) as the caps shrink, while \(m=3\) is the **unique least-concentrated order** at every interior radius.

For every nonzero \(h\in\mathcal H_3\), the sharp energy bounds are
\[
\lambda_3(t)\int_{\mathbb S^2}h^2\,d\sigma\le
\int_{C_t}h^2\,d\sigma\le
\max\{\lambda_0(t),\lambda_1(t),\lambda_2(t)\}\int_{\mathbb S^2}h^2\,d\sigma.
\]
The lower equality holds exactly for nonzero \(h\in E_3\). Upper equality holds exactly in the top sector or the indicated direct sum at either crossing. Thus the restriction map to the two caps has exact \(L^2\) condition number \(\sqrt{\lambda_{\max}(t)/\lambda_3(t)}\) on \(\mathcal H_3\).

## Assumptions and scope
The sphere is the unit sphere in \(\mathbb R^3\); surface mass is normalized to one. The two caps have the same colatitudinal cutoff \(0<t<1\), hence are disjoint except at the excluded equatorial endpoint. All functions and coefficients are real. \(P_{\mathcal H_3}\) is the ambient \(L^2(\mathbb S^2,\sigma)\)-orthogonal projector. The operator \(K_t\) is a compression of multiplication by the cap indicator and is not a projector. Eigenvalues measure the fraction of the full-sphere energy contained in the two caps.

## Proof
Let \(z=\omega_3=\cos\theta\) and \(\phi\) be longitude. An orthogonal real basis for azimuthal order \(m\) consists, up to nonzero constants, of
\[
(1-z^2)^{m/2}P_3^{(m)}(z)\cos(m\phi),\qquad
(1-z^2)^{m/2}P_3^{(m)}(z)\sin(m\phi),
\]
with the sine term omitted when \(m=0\), and \(P_3(z)=(5z^3-3z)/2\). Since the cap indicator depends only on \(z\), longitude integration makes different orders orthogonal under both the full-sphere and cap inner products. Rotation symmetry within each nonzero order also makes its two real basis vectors share one eigenvalue. Because each squared associated Legendre factor is even in \(z\), its cap-energy quotient is
\[
\lambda_m(t)=
\frac{\int_t^1(1-z^2)^m[P_3^{(m)}(z)]^2\,dz}
{\int_0^1(1-z^2)^m[P_3^{(m)}(z)]^2\,dz}.
\]
Direct polynomial integration yields the four exact expressions in the Finding. The denominators are strictly positive; every numerator lies strictly between zero and its denominator for \(0<t<1\). Summing according to sector dimensions gives the independent trace identity
\[
\lambda_0+2\lambda_1+2\lambda_2+2\lambda_3=7(1-t),
\]
in agreement with the spherical harmonic addition formula.

All six pairwise gaps factor without approximation:
\[
\begin{aligned}
\lambda_0-\lambda_1&=\frac7{16}t(1-t^2)(5t^2-1)(5t^2-3),\\
\lambda_0-\lambda_2&=\frac78t^3(1-t^2)(5t^2-1),\\
\lambda_0-\lambda_3&=\frac7{16}t(1-t^2)(15t^4-12t^2+5),\\
\lambda_1-\lambda_2&=\frac{21}{16}t(1-t^2)^2(5t^2-1),\\
\lambda_1-\lambda_3&=\frac78t(1-t^2)^2(5t^2+1),\\
\lambda_2-\lambda_3&=\frac{35}{16}t(1-t^2)^3.
\end{aligned}
\]
The seemingly indefinite quartic is actually
\[
15t^4-12t^2+5=15(t^2-2/5)^2+13/5>0.
\]
Thus each gap has a fully determined sign, and the only interior zeros of any gap occur at \(t_1\) or \(t_2\). Reading the signs yields the five-case ordering. At \(t_1\) direct substitution gives the fivefold top eigenvalue \(1-17\sqrt5/125\), versus \(1-9\sqrt5/25\) on \(E_3\). At \(t_2\) the eigenvalues on \(E_0\oplus E_1\) equal \(1-18\sqrt{15}/125\), strictly above the other two. The Rayleigh quotient of \(K_t\) is exactly \(\int_{C_t}h^2/\int_{\mathbb S^2}h^2\), so the spectral theorem proves the sharp inequalities, all equality cases, and the restriction condition number.

## Verification
Run `python checks/verify.py` with Python 3 (standard library only). The program independently reconstructs all four eigenvalue polynomials from squared associated Legendre polynomials using exact rational coefficients; checks all six factorizations and the seven-dimensional trace; reduces polynomial identities modulo the exact crossing relations \(t^2=1/5\) and \(t^2=3/5\); checks the three ordering phases using rational probes; and performs twelve independent numerical integration consistency checks. Its terminal success marker is `ALL_CUBIC_TWO_CAP_SPECTRAL_CHECKS_OK`. The proof above, not finite tests, establishes the continuum of cutoff values.

## Relationship to prior work
The foundational spherical Slepian framework and one-cap concentration matrices are developed by Simons, Dahlen and Wieczorek (2004/2006, cited below). Simons and Dahlen (2006) give the general double-cap localization matrix and parity decomposition. In particular, their formula for matrix entries supplies the known general analytic framework, **not** the new algebraic ordering comparison. The present finding concerns the degree-three *single harmonic level*, gives all four exact mode branches, proves a three-regime maximizing order and a persistent minimizing order, and identifies the exceptional five-dimensional equal-concentration eigenspace. Those precise global ordering and degeneracy statements are not asserted in the inspected primary sections. This is a specialization with an additional sharp ordering result; the general construction itself is not claimed as new. Numerical spherical Slepian software also computes concentration factors for user-selected degree masks but does not by itself certify these exact inequalities or unique crossing locations.

## Limitations
Only a single real degree-three harmonic level and a symmetric pair of equal antipodal caps are treated. This is not the usual full low-pass space of all degrees through three. The endpoints \(t=0,1\), where all eigenvalues coincide, are excluded from the strict ordering claims. No analogous phase classification is proved for unequal caps, arbitrary regions, other harmonic degrees, or mixed-degree bands. The independent review of the result remains outstanding; an equivalent historical closed-form mode-ordering result in unindexed literature cannot be excluded. The 1977 paper by Gilbert and Slepian on two-interval polynomial concentration was located, but its full text could not be accessed; its abstract treats polynomial intervals rather than the four azimuthal-order comparisons here.

## References
1. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (first public August 31, 2004), subsequently SIAM Review 48 (2006), 504–536. https://arxiv.org/abs/math/0408424 ; https://doi.org/10.1137/S0036144504445765 . Relevant full-text material: Section 5.1, equations (5.2)–(5.7).
2. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061. https://geoweb.princeton.edu/people/simons/PDF/reprints/GJI-2006.pdf ; https://doi.org/10.1111/j.1365-246X.2006.03065.x . Relevant full-text material: Section 4.2, equations (64)–(72), and Section 6.
3. SHTOOLS, *SHReturnTapersM*, https://shtools.github.io/SHTOOLS/pyshreturntapersm.html . A numerical general-concentration implementation rather than an exact analytic ordering theorem.

4. E. N. Gilbert and D. Slepian, *Doubly Orthogonal Concentrated Polynomials*, SIAM Journal on Mathematical Analysis 8 (1977), 290–319. https://doi.org/10.1137/0508022 . Full text not accessed; the abstract describes interval polynomial concentration and asymptotics.
