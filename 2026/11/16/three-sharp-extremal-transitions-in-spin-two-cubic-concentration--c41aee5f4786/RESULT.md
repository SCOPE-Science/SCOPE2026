# Three sharp extremal transitions in spin-two cubic concentration on antipodal caps

## Finding
Let \({}_2\mathcal H_3=\operatorname{span}_{\mathbb C}\{{}_2Y_{3m}:-3\le m\le3\}\), the seven-dimensional space of spin-weight \(+2\), pure-degree-three spherical harmonics on the round two-sphere. Let \(0<c<1\), \(\Omega_c=\{\omega\in S^2:|\omega_3|\ge c\}\), and let \(K_c=P_{{}_2\mathcal H_3}\mathbf1_{\Omega_c}|_{{}_2\mathcal H_3}\), where the projection and inner products use full-sphere area measure. The concentration operator has precisely four eigenvalue branches \(\lambda_j(c)\), indexed by absolute azimuthal order \(j=|m|\), of respective multiplicities \(1,2,2,2\):
\[
\begin{aligned}
\lambda_0(c)&=1-\frac{35}{8}c^3+\frac{21}{4}c^5-\frac{15}{8}c^7,\\
\lambda_1(c)&=1-\frac{35}{32}c+\frac{35}{32}c^3-\frac{77}{32}c^5+\frac{45}{32}c^7,\\
\lambda_2(c)&=1-\frac74c+\frac{35}{16}c^3-\frac78c^5-\frac9{16}c^7,\\
\lambda_3(c)&=1-\frac{21}{32}c-\frac{35}{32}c^3+\frac{21}{32}c^5+\frac3{32}c^7.
\end{aligned}
\]
Every eigenvalue lies strictly between zero and one. Put
\[
a=\frac1{\sqrt3},\qquad b=\sqrt{\frac{2\sqrt7-1}{9}},\qquad d=\sqrt{\frac{11-\sqrt{73}}6},\qquad 0<a<d<b<1.
\]
The **maximal** eigenspace is \(m=0\) for \(0<c<a\); at \(a\), it is \(m=0,\pm1,\pm3\) (dimension five); for \(a<c<b\), it is \(m=\pm1\); at \(b\), it is \(m=\pm1,\pm2\) (dimension four); for \(b<c<1\), it is \(m=\pm2\). The **minimal** eigenspace is \(m=\pm2\) for \(0<c<d\), is \(m=0,\pm2\) at \(d\), and is \(m=0\) for \(d<c<1\). Thus three distinct sharp transition cutoffs govern the two extremal levels. The sharp squared-energy condition ratio is \(\kappa(c)=\lambda_{\max}(c)/\lambda_{\min}(c)\), with the above piecewise selection, and
\[
\lim_{c\uparrow1}(1-c)^2\kappa(c)=\frac15.
\]
The full-spectrum trace identity is \(\lambda_0+2\lambda_1+2\lambda_2+2\lambda_3=7(1-c)\). The theorem is for a *single pure harmonic degree and a symmetric two-cap mask*; it does not assert an all-degree or general-region spectrum.

## Assumptions and scope
Spin-weighted harmonics are complex sections of the spin-weight-two line bundle with standard Hermitian norm. In a standard spherical frame \({}_2Y_{3m}(\theta,\phi)\) is a unit-modulus multiple of \(\sqrt{7/(4\pi)}\,d^3_{m,-2}(\theta)e^{im\phi}\), where \(d^3\) is the Wigner small-\(d\) matrix, and \(\cos\theta=x\). Squared magnitudes and hence the stated eigenvalues do not depend on the phase convention or choice of local frame. The cap set \(\Omega_c\) consists of the closed northern and southern polar caps with colatitude \(\theta\le\arccos c\) or \(\theta\ge\pi-\arccos c\). Boundary circles have zero measure. The ratio \(\kappa\) measures the sharp ratio of **squared \(L^2\)-norms**; the singular-value condition number of restriction is \(\sqrt\kappa\). The endpoints \(c=0,1\) are excluded from strict claims because the concentration operator then degenerates to identity or zero.

## Proof
Azimuthal integration makes \(K_c\) diagonal in \({}_2Y_{3m}\), since the cap mask depends only on \(x=\cos\theta\). Spin parity gives equal cap integrals for \(m\) and \(-m\). To compute the diagonal, set \(p=(1+x)/2\), \(q=(1-x)/2\). For nonnegative \(m\), the squared Wigner entries \(v_m(x)=|d^3_{m,-2}(\arccos x)|^2\) are the following *exact polynomials*:
\[
\begin{aligned}
v_0(x)&=\frac{15}{8}(1-x^2)^2x^2,\\
v_1(x)&=10(2p-q)^2q^3p,\\
v_2(x)&=(5p-q)^2q^4,\\
v_3(x)&=6q^5p.
\end{aligned}
\]
For negative \(m\), \(v_{-m}(x)=v_m(-x)\). Wigner orthogonality yields \(\int_{-1}^1v_m(x)\,dx=2/7\). Consequently the cap-energy fraction is exactly
\[
\lambda_{|m|}(c)=\frac72\left(\int_c^1v_m(x)\,dx+\int_{-1}^{-c}v_m(x)\,dx\right).
\]
Integrating these polynomials gives the four stated eigenvalues, which lie strictly in \((0,1)\) since each density is nonzero on sets of positive measure inside and outside the cap for \(0<c<1\). Adding with multiplicities yields the trace identity, also implied by the spin-harmonic addition theorem.

To prove the *global* extremal classification, the six independent pairwise differences factor exactly:
\[
\begin{aligned}
\lambda_0-\lambda_1&=\frac{35}{32}c(1-c^2)^2(1-3c^2),\\
\lambda_0-\lambda_3&=\frac{21}{32}c(1-c^2)^2(1-3c^2),\\
\lambda_1-\lambda_3&=-\frac7{16}c(1-c^2)^2(1-3c^2),\\
\lambda_0-\lambda_2&=\frac7{16}c(1-c^2)(3c^4-11c^2+4),\\
\lambda_1-\lambda_2&=-\frac7{32}c(1-c^2)(9c^4+2c^2-3),\\
\lambda_2-\lambda_3&=\frac7{32}c(1-c^2)(3c^4+10c^2-5).
\end{aligned}
\]
The only possible interior crossings occur at \(a\), \(d\), \(b\), or \(e=\sqrt{(2\sqrt{10}-5)/3}\). They satisfy \(a<d<e<b\). The first three factor signs show \(\lambda_0>\lambda_1,\lambda_3\) below \(a\), while \(\lambda_1>\lambda_0,\lambda_3\) above \(a\). The remaining three signs show that \(\lambda_0>\lambda_2\) below \(d\) and reverses above it, \(\lambda_1>\lambda_2\) below \(b\) and reverses above it, and \(\lambda_2<\lambda_3\) below \(e\) and reverses above it. These implications, with \(a<d<e<b\), establish every maximal and minimal sector claimed, with no numerical assumptions. The fourth threshold \(e\) changes the ordering of two *intermediate* levels only. At \(a\) the three top branches \(0,1,3\) coincide, giving dimension five; at \(b\) the top branches \(1,2\) coincide, giving dimension four; at \(d\) the two bottom branches \(0,2\) coincide, giving dimension three. There are no further extremal ties.

Finally, Taylor expansion of the exact polynomials at \(c=1\) gives \(\lambda_0(c)=\tfrac{35}{2}(1-c)^3+O((1-c)^4)\), and \(\lambda_2(c)=\tfrac72(1-c)+O((1-c)^2)\). The sharp top and bottom sectors near \(c=1\) are respectively \(2\) and \(0\), so the limit of \((1-c)^2\kappa(c)\) is \((7/2)/(35/2)=1/5\). The Rayleigh quotient of \(K_c\) is the measured-to-full \(L^2\) energy fraction. This proves the sharp energy inequalities and all equality spaces by the spectral theorem.

## Verification
The standalone standard-library script `checks/verify_spin2_caps.py` reconstructs the Wigner-square polynomials using exact rational arithmetic and a second finite-factorial Wigner formula, verifies all seven normalized densities, the four integrated spectra, the trace identity, all six pairwise polynomial factorizations, exact rational ordering witnesses in each phase, and the endpoint expansion. Execute `python3 checks/verify_spin2_caps.py`; success is signaled by `SPIN2_DEGREE3_EXACT_CAP_SPECTRUM_AND_GAPS_PASS`. The sign proof above, not finite rational tests, proves all continuum claims.

## Relationship to prior work
Michel, Plattner and Seibert (2021) establish the general spin-weighted Slepian matrix and its decomposition for arbitrary regions, and a commuting operator for a *single* spherical cap. Those foundational results yield the finite matrix to be studied but do not assert the displayed two-antipodal-cap degree-three spin-two eigenvalue polynomials, the sharp five- and four-dimensional optimal resonances, or the changes in the least-observable sector. Seibert (2018) develops tensor and spin-weighted Slepian localization on one cap; the doctoral thesis metadata and abstract were inspected, but its full text was unavailable for comparison. Simons and Dahlen (2006) treat the scalar polar-gap concentration problem. A published precise scalar cubic antipodal-cap ordering result likewise has different density polynomials, different mode transitions, and no immediate implication for spin weight two: although the spin-raising operator relates representations on the whole sphere, it does not commute with spatial multiplication by the cap indicator. All general spin-Slepian constructions, Wigner formulas, and scalar Slepian theory are acknowledged as established. Only the explicit spin-two, pure-degree-three two-cap extremal classification and its consequences are proposed as an additional result.

## Limitations
The analysis concerns the seven-dimensional spin \(+2\) level with \(\ell=3\), not spin \(0\), an all-degree band, arbitrary spin or unequal/nonantipodal caps. It is an exact low-degree classification and does not supply a theorem covering arbitrary harmonic degree. General integral formulas in earlier spin-Slepian work enable a priori computation of the matrix; novelty is limited to the global sharp comparisons and resonances, not the general framework. The complete 2018 dissertation was not accessible, so equivalent prior explicit calculations cannot be ruled out. Historical priority is provisional; independent audit has not been performed.

## References
1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, first public 2021-03-26. Sections 2.3, 3.1, 3.2 and 4.3. https://arxiv.org/abs/2103.14650
2. K. Seibert, *Spin-weighted spherical harmonics and their application for the construction of tensor Slepian functions on the spherical cap*, doctoral thesis, Universität Siegen, 2018. Metadata and abstract inspected; full thesis unavailable. https://dspace.ub.uni-siegen.de/entities/publication/87b140bd-e63e-434f-ba43-f98843cba1fd
3. F. J. Simons and F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International **166** (2006), 1039–1061. https://doi.org/10.1111/j.1365-246X.2006.03065.x
4. *Three spectral phases and a five-dimensional resonance for cubic spherical harmonics in antipodal caps*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-spectral-phases-and-a-five-dimensional-resonance-for-cubic--c61291f32f0b
