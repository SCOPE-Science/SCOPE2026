# Cubic spherical harmonics on coordinate-axis caps: a unique dimension-three spectral transition

## Finding
Let \(d\ge3\), and equip the unit sphere \(\mathbb S^{d-1}\subset\mathbb R^d\) with probability-normalized surface measure \(\sigma_d\). Let \(\mathcal H_3\) be the complexification of the space of restrictions of homogeneous, Euclidean-harmonic real cubic polynomials. For \(1/2\le t<1\), define the union of \(2d\) equal coordinate-axis caps
\[
\Omega_{d,t}=\{x\in\mathbb S^{d-1}:\max_{1\le j\le d}x_j^2\ge t\}.
\]
These caps have disjoint interiors (and touch only on a null set at \(t=1/2\)). Let \(T_{d,t}=P_3\mathbf1_{\Omega_{d,t}}P_3\) act on \(\mathcal H_3\), where \(P_3\) is the global orthogonal projection. Its eigenvalues are the fractions of global squared \(L^2\) energy captured in the region.

**Complete spectrum.** The operator has three symmetry-sector eigenvalue branches \(\lambda_A,\lambda_B,\lambda_C\), with multiplicities
\[
\dim A=d,\qquad \dim B=d(d-2),\qquad \dim C=\binom d3.
\]
All three eigenvalues are given by the explicit incomplete-Beta formulas in the next section. The \(C\)-branch is strictly smallest for every allowed \(d,t\). For \(d\ge4\), the complete strict order is
\[
\boxed{\lambda_A(d,t)>\lambda_B(d,t)>\lambda_C(d,t).}
\]
Only dimension three has an internal concentration-mode transition. Put
\[
\boxed{t_*=\frac{3+2\sqrt6}{15}.}
\]
For \(d=3\), the order is \(\lambda_B>\lambda_A>\lambda_C\) when \(1/2\le t<t_*\), \(\lambda_A=\lambda_B>\lambda_C\) at \(t=t_*\), and \(\lambda_A>\lambda_B>\lambda_C\) when \(t_*<t<1\). The maximal eigenspace is three-dimensional on either side and six-dimensional at the unique crossing. All branches lie strictly between zero and one; no allowed cap union produces a tight restriction operator.

**Sharp observability asymptotic.** For the squared condition number \(\kappa_d(t)=\lambda_{\max}(T_{d,t})/\lambda_{\min}(T_{d,t})\), at every fixed integer \(d\ge3\),
\[
\boxed{\lim_{t\uparrow1}(1-t)^2\kappa_d(t)
=\frac{(d-1)(d+1)(d+3)}{18(d+2)}.}
\]
Equivalently, the condition number of the continuous restriction map itself is the square root of \(\kappa_d(t)\). This is a sharp quadratic loss in the squared cap-aperture variable.

## Assumptions and scope
The integer \(d\) is fixed and at least three. The parameter \(t\) is the **squared coordinate cutoff**, not an angular cutoff or the cap's surface-area fraction. The cap angular half-width is \(\arccos\sqrt t\). At \(t=1/2\), pairwise intersections are null, so the union indicator agrees almost everywhere with the sum of the \(d\) two-sided coordinate-cap indicators. The endpoint \(t=1\), where all eigenvalues vanish, is excluded; overlapping interiors at \(t<1/2\) are not covered. The complex and real harmonic spectra are identical.

Here is a self-contained finite special-function prescription for all eigenvalues. For \(0\le u\le1\), put
\[
\begin{aligned}
L_2(u)&=u^2+\frac{3(1-u)^2}{d+1},\\
L_3(u)&=u^3+\frac{15(1-u)^3}{(d+1)(d+3)},\\
M_A&=\frac{6(d-1)}{(d+2)^2(d+4)},\\
M_B&=\frac{2(d-2)}{(d+2)(d+4)},\\
M_C&=\frac{(d-1)(d-2)}{6(d+2)(d+4)}.
\end{aligned}
\]
Define the degree-at-most-three polynomials
\[
\begin{aligned}
R_A(u)&=\frac{L_3(u)-6L_2(u)/(d+2)+9/(d+2)^2}{M_A},\\
R_B(u)&=\frac{(d+1)L_2(u)-dL_3(u)-1}{(d-1)M_B},\\
R_C(u)&=\frac{1-3L_2(u)+2L_3(u)}{6M_C}.
\end{aligned}
\]
Then, for \(J\in\{A,B,C\}\),
\[
\boxed{\lambda_J(d,t)=\frac{d}{B(1/2,(d-1)/2)}
\int_t^1R_J(u)\,u^{-1/2}(1-u)^{(d-3)/2}\,du.}
\]
These are finite sums of standard incomplete Beta functions, not unspecified spectral integrals. Explicitly, if \(R_J(u)=\sum_{m=0}^3r_{J,m}u^m\), then
\[
\lambda_J(d,t)=\frac{d}{B(1/2,(d-1)/2)}
\sum_{m=0}^3r_{J,m}\,B_{1-t}\bigl((d-1)/2,m+1/2\bigr),
\]
where \(B_x(a,b)=\int_0^xv^{a-1}(1-v)^{b-1}\,dv\). Thus the formulas are exact at every real allowed cutoff.

## Proof
**Harmonic sectors.** Write \(r^2=\sum_i x_i^2\). The pure cubic harmonics split into three invariant orthogonal subspaces under the full signed-permutation symmetry group:
\[
\begin{aligned}
A&=\operatorname{span}\{x_i^3-\tfrac3{d+2}x_i r^2:1\le i\le d\},\\
B&=\bigoplus_{i=1}^d\{x_i\sum_{j\ne i}a_jx_j^2:\sum_{j\ne i}a_j=0\},\\
C&=\operatorname{span}\{x_ix_jx_k:1\le i<j<k\le d\}.
\end{aligned}
\]
The displayed polynomials are harmonic: applying the ambient Laplacian to \(x_i^3\) gives \(6x_i\), to \(x_ir^2\) gives \(2(d+2)x_i\), and to a \(B\)-polynomial gives \(2x_i\sum_{j\ne i}a_j=0\); squarefree cubics are also harmonic. Their dimensions sum to
\[
d+d(d-2)+\binom d3=\binom{d+2}3-d=\dim\mathcal H_3.
\]
Coordinate sign flips distinguish the odd-coordinate characters. For each fixed such character, permutations of the remaining coordinates split the coefficient space into a constant line (the \(A\) piece) and the standard sum-zero representation (the \(B\) piece). The squarefree characters form the \(C\) piece. Invariant quadratic forms are therefore scalar on each indicated sector, with no off-diagonal coupling. This applies equally to the full inner product and to the cap-restricted one, proving that the three sectors give the entire concentration spectrum.

**Exact kernel moments.** Put \(X_i=x_i^2\) and \(S_j=\sum_i X_i^j\). Up to positive sectorwise constants, the sums of squared functions in orthonormal bases of the three sectors are
\[
\begin{aligned}
K_A&=S_3-\frac6{d+2}S_2+\frac9{(d+2)^2},\\
K_B&=\frac{(d+1)S_2-dS_3-1}{d-1},\\
K_C&=\frac{1-3S_2+2S_3}{6}.
\end{aligned}
\]
For \(K_B\), this follows from the identity \(\sum_iX_i[\sum_{j\ne i}X_j^2-(1-X_i)^2/(d-1)]\); for \(K_C\), it is Newton's identity for \(\sum_{i<j<k}X_iX_jX_k\). Positivity follows from these sums-of-squares representations. Because \(X=(X_1,\ldots,X_d)\) has Dirichlet parameters \((1/2,\ldots,1/2)\),
\[
\mathbb ES_2=\frac3{d+2},\qquad
\mathbb ES_3=\frac{15}{(d+2)(d+4)},
\]
whence \(\mathbb EK_J=M_J\) for the three constants above. Conditional on \(X_1=u\), the remaining normalized squared coordinates have Dirichlet parameters \((1/2,\ldots,1/2)\) on \(d-1\) coordinates. Therefore \(\mathbb E(S_2\mid X_1=u)=L_2(u)\) and \(\mathbb E(S_3\mid X_1=u)=L_3(u)\), giving exactly the polynomials \(R_J\).

The variable \(X_1\) has Beta density \(u^{-1/2}(1-u)^{(d-3)/2}/B(1/2,(d-1)/2)\). For \(t\ge1/2\), almost every point lies in at most one coordinate-axis cap pair. The symmetry of each \(K_J\) under coordinate permutations thus gives
\[
\frac{\int_{\Omega_{d,t}}K_J\,d\sigma_d}{\int K_J\,d\sigma_d}
=\frac{d}{B(1/2,(d-1)/2)}\int_t^1R_J(u)u^{-1/2}(1-u)^{(d-3)/2}\,du,
\]
proving all three eigenvalue formulas and their multiplicities. As a normalization cross-check, the three branches obey
\[
d\lambda_A+d(d-2)\lambda_B+\binom d3\lambda_C
=\frac{d(d-1)(d+4)}6\,\sigma_d(\Omega_{d,t}).
\]

**Sharp ordering and isolated crossing.** Define the positive function
\[
W_d(t)=\frac{d\sqrt t\,(1-t)^{(d-1)/2}}{B(1/2,(d-1)/2)}.
\]
The differences factor exactly as
\[
\begin{aligned}
\lambda_A-\lambda_B&=W_d(t)\frac{(d+4)\bigl((d+2)(d+6)t^2-(4d+6)t-3\bigr)}{3(d+1)(d+3)},\\
\lambda_B-\lambda_C&=W_d(t)\frac{(d+2)(d+4)(1-t)((d+6)t-3)}{(d-1)(d+1)(d+3)}.
\end{aligned}
\]
These equalities follow from a direct polynomial differentiation check, not a numerical root search: for either displayed quotient \(Q\) multiplying \(W_d\), the identity
\[
\frac12(1-dt)Q(t)+t(1-t)Q'(t)=-(R_J(t)-R_K(t))
\]
implies equality of derivatives of the two sides; both sides vanish at \(t=1\). The second difference is positive for all allowed parameters. For the first, the quadratic in parentheses is negative at \(t=0\), has exactly one positive root, and its value at \(t=1/2\) is \((d^2-12)/4\). Hence it is positive throughout \([1/2,1)\) when \(d\ge4\). When \(d=3\), the unique positive root is \(t_*=(3+2\sqrt6)/15\); its sign changes from negative to positive there.

For completeness, when \(d=3\), direct addition of the two difference formulas yields
\[
\lambda_A-\lambda_C=W_3(t)\left[-\frac7{48}(15t^2-48t+17)\right]>0
\]
throughout \([1/2,1)\), since the polynomial inside the parentheses is negative at \(1/2\) and strictly decreasing up to \(1\). This confirms \(C\) is strictly smallest even before the \(A/B\) transition. These comparisons establish every claimed ordering and the six-dimensional top eigenspace at equality. Strict \(0<\lambda_J<1\) follows because a nonzero harmonic polynomial cannot vanish throughout either nonempty open cap region or its nonempty open complement.

**Thin-cap constant.** As \(t\uparrow1\), \(\lambda_A\) is the largest and \(\lambda_C\) the smallest. Their normalized conditional kernels satisfy
\[
R_A(1)=\frac{(d-1)(d+4)}6,\qquad
R_C(u)=\frac{3(d+2)(d+4)}{(d-1)(d+1)}(1-u)^2+O((1-u)^3).
\]
Integrating these against the Beta density at \(u=1\) gives
\[
\lambda_A\sim\frac{2dR_A(1)}{(d-1)B(1/2,(d-1)/2)}(1-t)^{(d-1)/2},
\]
\[
\lambda_C\sim\frac{2d}{(d+3)B(1/2,(d-1)/2)}
\frac{3(d+2)(d+4)}{(d-1)(d+1)}(1-t)^{(d+3)/2}.
\]
Their ratio yields exactly the boxed sharp coefficient above.

## Verification
The companion `check_cubic_coordinate_caps.py` (Python 3, SymPy, mpmath) verifies the sector dimension and trace identities algebraically for formal \(d\); reconstructs each normalized cap integrand independently from a representative harmonic cubic and Dirichlet moments; verifies both Beta-derivative difference identities as exact rational-function identities; and checks the crossing polynomial and thin-cap coefficient. It then performs 25 independent high-precision Beta quadrature cases for dimensions \(3,4,5,8,13\) at squared cutoffs \(0.505,0.53,0.65,0.85,0.97\), comparing the representative-polynomial integrals with the factored differences. Running `python check_cubic_coordinate_caps.py` produces `CUBIC_COORDINATE_CAPS_EXACT_PASS symbolic=all_d independent_cases=25`. The general proof is analytical; the numerical cases are corroborative, not a proof by sampling.

## Relationship to prior work
Simons, Dahlen and Wieczorek (arXiv:math/0408424) formulate spherical spatio-spectral concentration for general regions and provide the finite-dimensional eigenproblem, especially for the ordinary two-sphere. Jaming and Speckbacher (arXiv:2004.02474v1, first public 2020-04-06) prove large-sieve concentration inequalities on compact two-point homogeneous spaces. Both foundational theories apply in principle but neither gives the three all-dimensional signed-coordinate-cap eigenbranches or identifies the exceptional dimension-three crossover. Existing explicit studies of **two antipodal caps** at cubic degree use a different mask; they cannot be added as eigenvalue formulas because their eigenvectors for different axes do not generally agree. An exact **six-axis-cap** calculation at *quartic*, not cubic, degree has four symmetry sectors on the two-sphere; the present cubic result concerns a different harmonic degree, provides an all-dimensional classification, and has a different sharp threshold. A six-cap fifth-order cubature result treats weighted polynomial integration and quadratic harmonic stability, not this cubic energy spectrum. A separate all-dimensional same-mask classification for pure degrees one and two establishes linear isotropy and a quadratic two-sector split; neither applies to degree-three harmonic coefficients, whose distinct sign-character decomposition has three branches. The present theorem provides their complete formulas and a unique exceptional-dimensional crossing rather than extrapolating a degree-two eigenvalue. No inspected statement implies the exact unique-dimensional-anomaly theorem by direct parameter substitution.

## Limitations
The theorem is restricted to pure degree-three spherical harmonics, equal cap widths, and the nonoverlapping regime \(t\ge1/2\). It does not classify low-pass combinations of harmonic degrees, unequal masks, or overlapping caps. Its thin-cap limit holds at each fixed dimension and is not claimed uniformly in \(d\). While the calculations and accessible comparisons support the result, historical priority cannot be certified exhaustively; earlier octahedral or hyperoctahedral representation computations might contain equivalent formulas. There has been no independent mathematical audit.

## References
1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1 (2020-04-06), https://arxiv.org/abs/2004.02474.
2. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (2004-08-31), https://arxiv.org/abs/math/0408424.
3. *Cubic spherical harmonics on antipodal caps: two exact symmetry switches*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-cubic-spherical-harmonics-on-antipodal-caps-two-exact-symmetry-s--c0fecc278359.
4. *Exact fourth-degree octahedral-cap concentration and a triple-to-simple optimal-mode transition*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-fourth-degree-octahedral-cap-concentration-and-a-triple-to--56baf4ae0d4c.
5. *A unique fifth-degree spherical cubature radius for six octahedral cap windows*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-unique-fifth-degree-spherical-cubature-radius-for-six-octahedr--d07bf59bb1e6.
6. *Perfect linear isotropy and sharp quadratic instability on disjoint coordinate caps*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perfect-linear-isotropy-and-sharp-quadratic-instability-on-disjo--4ed7c0178b0e.
