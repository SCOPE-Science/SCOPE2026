# The first reentrant azimuthal phase diagram for antipodal spherical caps

## Finding
Let \(E_c=\{\omega\in S^2:|\omega_3|\ge c\}\), with \(0<c<1\), and let \(\mathcal H_\ell\) be the complex spherical harmonics of pure degree \(\ell\). The sharp spatial concentration constant is
\[
\Lambda_\ell(c)=\sup_{0\ne F\in\mathcal H_\ell}\frac{\int_{E_c}|F|^2\,d\sigma}{\int_{S^2}|F|^2\,d\sigma}.
\]
For \(\ell=4\), the maximizing absolute azimuthal orders, as \(c\) increases, are **exactly** \(3,0,2,1,0\), separated by four sharp transition points \(a<b<g<d\) defined by
\[
\begin{aligned}
a&=\sqrt{u_*},\quad 455u_*^3-625u_*^2+293u_*-27=0,\quad u_*\in(0,1/7),\\
b&=\sqrt{(5+2\sqrt{15})/35},\\
g&=\sqrt{3/7},\\
d&=\sqrt{(15+2\sqrt{30})/35}.
\end{aligned}
\]
On the five open intervals \((0,a),(a,b),(b,g),(g,d),(d,1)\), the maximizers belong precisely to the azimuthal sectors \(|m|=3,0,2,1,0\), respectively. At \(c=a,b,g,d\), the maximizing sector sets are \(\{0,3\},\{0,2\},\{0,1,2\},\{0,1\}\), respectively. All these statements hold for arbitrary complex coefficient combinations within a maximizing eigenspace.

For every \(\ell\in\{0,1,2,3\}\), the maximizing absolute azimuthal order is nonincreasing with \(c\): degree zero is constantly \(0\); degree one is constantly \(0\); degree two has orders \(1,0\), transitioning at \(1/\sqrt3\); degree three has orders \(2,1,0\), transitioning at \(1/\sqrt5\) and \(\sqrt{3/5}\). At the first degree-three transition \(m=0,1,2\) tie. Therefore degree four is the **first pure spherical-harmonic degree** at which the dominant azimuthal order reenters a larger value as the antipodal caps shrink.

## Assumptions and scope
The sphere has its usual rotation-invariant surface measure; normalization cancels in every quotient. \(Y_{\ell m}\) are the usual complex orthonormal spherical harmonics, \(-\ell\le m\le\ell\), and \(P_\ell^m\) are associated Legendre functions. The results apply only to a single pure degree and to two equal caps centered at antipodal poles, not to a low-pass collection of degrees or nonsymmetric regions. The angles and intervals refer to \(c=\cos\Theta\), so increasing \(c\) means decreasing the angular cap radius \(\Theta\).

## Proof
Azimuthal integration in \(\varphi\) makes the restriction operator diagonal in the \(Y_{\ell m}\) basis. Its normalized eigenvalues are
\[
L_{\ell,m}(c)=\frac{2\int_c^1(P_\ell^m(x))^2\,dx}{\int_{-1}^1(P_\ell^m(x))^2\,dx},\qquad 0\le m\le\ell.
\]
The eigenvalues for \(m\ne0\) have multiplicity two, from \(m\) and \(-m\). Hence the sharp constant is \(\max_{0\le m\le\ell}L_{\ell,m}(c)\), and equality holds exactly in the direct sum of the maximizing azimuthal eigenspaces.

For \(\ell=4\), put \(t=c^2\) and \(L_{4,m}(c)=1-cD_m(t)\), where direct exact integration gives
\[
\begin{aligned}
D_0(t)&=(1225t^4-2700t^3+1998t^2-540t+81)/64,\\
D_1(t)&=t(135-459t+585t^2-245t^3)/16,\\
D_2(t)&=(245t^4-720t^3+702t^2-240t+45)/32,\\
D_3(t)&=t(105-189t+135t^2-35t^3)/16,\\
D_4(t)&=(35t^4-180t^3+378t^2-420t+315)/128.
\end{aligned}
\]
The decisive pairwise differences, computed by subtracting these exact expressions, are
\[
\begin{aligned}
L_{4,0}-L_{4,3}&=3c(1-t)Q(t)/64,\quad Q(t)=455t^3-625t^2+293t-27,\\
L_{4,0}-L_{4,2}&=3c(1-t)(7t-3)(35t^2-10t-1)/64,\\
L_{4,0}-L_{4,1}&=9c(1-t)(7t-3)(35t^2-30t+3)/64,\\
L_{4,1}-L_{4,2}&=15c(1-t)^2(7t-3)(7t-1)/32,\\
L_{4,1}-L_{4,3}&=15c^3(1-t)^2(7t-1)/8,\\
L_{4,2}-L_{4,3}&=45c(1-t)^3(7t-1)/32.
\end{aligned}
\]
Also \(L_{4,3}>L_{4,4}\) for all \(0<c<1\), since their difference is \(315c(1-t)^4/128\); and \(L_{4,2}>L_{4,4}\) because their difference is \(135c(1-t)^3(7t+1)/128\). The remaining comparison \(L_{4,1}-L_{4,4}=15c(1-t)^2(133t^2-58t+21)/128\) is positive because the displayed quadratic has negative discriminant and positive leading coefficient.

The cubic \(Q\) has discriminant \(-2192701440<0\), hence a unique real root, which lies in \((0,1/7)\) because \(Q(0)<0<Q(1/7)\). The quadratic \(35t^2-10t-1\) has its only positive root \((5+2\sqrt{15})/35\), lying between \(1/7\) and \(3/7\). The roots of \(35t^2-30t+3\) lie on opposite sides of \(3/7\); the larger is \((15+2\sqrt{30})/35\). The listed difference factorizations therefore imply the following exhaustive ordering. On \((0,a)\), order \(3\) dominates all others; on \((a,1/\sqrt7)\), order \(0\) dominates order \(3\), which dominates \(1,2,4\); on \((1/\sqrt7,b)\), order \(0\) dominates order \(2\), which dominates \(1,3,4\); on \((b,g)\), order \(2\) dominates all; on \((g,d)\), order \(1\) dominates all; and on \((d,1)\), order \(0\) dominates order \(1\), which dominates the rest. Exact equalities at transition values follow from the same differences, including the three-way tie at \(g\).

For completeness, for degrees at most three the same normalized Legendre integrals give: at \(\ell=1\), \(L_{1,0}-L_{1,1}=3c(1-c^2)/2>0\); at \(\ell=2\), \(L_{2,1}-L_{2,2}=15c(1-c^2)^2/8>0\) and \(L_{2,0}-L_{2,1}=5c(1-c^2)(3c^2-1)/4\); at \(\ell=3\), \(L_{3,2}>L_{3,3}\), \(L_{3,1}>L_{3,3}\), and
\[
\begin{aligned}
L_{3,1}-L_{3,2}&=21c(1-c^2)^2(5c^2-1)/16,\\
L_{3,0}-L_{3,2}&=7c^3(1-c^2)(5c^2-1)/8,\\
L_{3,0}-L_{3,1}&=7c(1-c^2)(5c^2-3)(5c^2-1)/16.
\end{aligned}
\]
These signs establish the lower-degree maximizers and show that no degree below four has an increase of the winning absolute order as \(c\) grows.

## Verification
The accompanying standalone Python checker recomputes exact normalized associated-Legendre integrals for degrees one to four, all five fourth-degree defect polynomials and all ten pairwise fourth-degree differences. It also verifies algebraic root ordering, five strict phase-interval witnesses and the three-way maximal tie. The checker is supplementary: the proof consists of exact integration, polynomial factorization and exhaustive sign comparisons over the full continuous parameter domain.

## Relationship to prior work
The double-polar-cap spherical Slepian concentration problem and its block decomposition were established in the classical geodetic and harmonic-analysis literature. Modern treatments construct Slepian bases for scalar and spin-weighted spherical harmonics. These sources provide general concentration-matrix techniques, not the exact *upper spectral envelope* and first failure of monotone optimizing azimuthal order across all cap radii in the pure-degree-four case. The present contribution is the continuous-aperture, global mode-selection classification and the minimal-degree counterexample, not the already-known Legendre integral representation.

## Limitations
The result is restricted to degrees at most four for the minimality claim, and to \(S^2\) for the fourth-degree phase diagram. It does not yield an all-degree law or a uniform conditioning theorem. Historical priority for this precise elementary but previously unlocated counterexample cannot be excluded by database searches; the known general Slepian matrix formula makes its individual eigenvalue polynomials computable in principle. No independent audit has been performed.

## References
1. A. Plattner, K. Seibert, V. Michel, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first public version 2021-03-26).
2. F. J. Simons, F. A. Dahlen, *Spherical Slepian functions and the polar gap in geodesy*, Geophysical Journal International 166 (2006), 1039–1061, DOI:10.1111/j.1365-246X.2006.03065.x.
3. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review 48 (2006), 504–536, DOI:10.1137/S0036144504445765.
4. A. P. Bates, Z. Khalid, R. A. Kennedy, *Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere*, arXiv:1608.05479 (2016-08-19).
