# One collective circulation plane with unbounded dissipation in a fully connected multibath Brownian network

## Finding

An overdamped, fully connected harmonic network may be driven by arbitrarily many independent, unequal-temperature baths yet has a stationary **probability-current field confined to one two-dimensional plane**. Its integrated current matrix has exactly one nonzero conjugate eigenvalue pair. All stationary bath heat rates and the total entropy-production rate are explicit:

\[
 A_{ij}=\frac{b(T_j-T_i)}{n(2a+b)},\qquad
 h_i=\frac{b^2(\overline T-T_i)}{n(2a+b)},\qquad
 \sigma=\frac{b^2}{n(2a+b)}\left(\overline T\sum_{i=1}^n\frac1{T_i}-n\right).
\]

Here \(A_{ij}=\int x_j j_i(x)\,dx\) is the integrated stationary probability-current tensor, \(h_i\) is the mean energy rate deposited into bath \(i\), and \(\sigma\) is steady reservoir entropy production, in units with mobility and Boltzmann's constant equal to one. If the temperatures are not all equal, \(A\) has rank two and its nonzero eigenvalues are

\[
 \pm i\Omega,\qquad \Omega=\frac{b}{2a+b}\sqrt{\frac1n\sum_{i=1}^n(T_i-\overline T)^2}.
\]

**Dissipation is not controlled by this circulation spectrum, even with fixed mean bath temperature and fixed temperature variance.** For every fixed \(a,b>0\), the three-bath family

\[
 T_1=\varepsilon,\qquad
 T_{2,3}=\frac{3-\varepsilon\mp\sqrt{3+6\varepsilon-3\varepsilon^2}}2,
 \quad 0<\varepsilon<\tfrac14,
\]

has \(\overline T=1\), population temperature variance exactly \(1\), and therefore the same nonzero current eigenvalues \(\pm ib/(2a+b)\) at every \(\varepsilon\). Nevertheless

\[
 \sigma_\varepsilon\sim\frac{b^2}{3(2a+b)\varepsilon}
 \quad\text{as }\varepsilon\downarrow0.
\]

Thus a fixed collective rotation spectrum and even two fixed bath-temperature moments can coexist with arbitrarily high irreversible thermal dissipation. This statement concerns the spectrum of the **integrated current**, not its full matrix entries, which vary with the temperature vector.

## Assumptions and scope

For every integer \(n\ge2\), choose real \(a,b>0\) and temperatures \(T_1,\ldots,T_n>0\). Let \(X\in\mathbb R^n\) obey the Itô stochastic differential equation

\[
 dX_t=-KX_t\,dt+\sqrt{2D}\,dW_t,\qquad
 K=aI+b(I-P),\quad P=\frac{\mathbf1\mathbf1^\top}{n},\quad
 D=\operatorname{diag}(T_1,\ldots,T_n),
\]

where \(W\) has independent standard Brownian coordinates. The potential is \(U(x)=x^\top Kx/2\); equivalently, every pair interacts by a spring of stiffness \(b/n\), with individual pinning \(a\). Write \(Q=I-P\) and \(\overline T=n^{-1}\sum_iT_i\). All assertions are finite-dimensional and exact; no thermodynamic limit or linear-response assumption is used. Heat is defined with the standard Stratonovich force-work convention. The cold-bath limit in the last claim is approached **only through positive temperatures**.

The stationary density \(\rho\) is a centered Gaussian with covariance \(C\). Its probability-current vector is

\[
 j(x)=(-Kx-D\nabla\log\rho(x))\rho(x)
 =(-K+DC^{-1})x\rho(x).
\]

For each bath, heat received from the system per unit time is \(h_i=\mathbb E[(KX)_i^2]-T_iK_{ii}\). The stationary reservoir entropy production is \(\sigma=\sum_i h_i/T_i\), equal to the usual positive Fokker–Planck quadratic current expression.

## Proof

**1. Invariant Gaussian and covariance.** Because \(K=aP+(a+b)Q\) is symmetric positive definite, the process has a unique centered nondegenerate Gaussian invariant distribution. Its covariance solves \(KC+CK=2D\), hence

\[
 C=\frac{PDP}{a}
 +\frac{2(PDQ+QDP)}{2a+b}
 +\frac{QDQ}{a+b}.
\]

This is verified by projecting the Lyapunov equation onto the four \(P,Q\) blocks: the corresponding relaxation-rate sums are \(2a\), \(2a+b\), \(2a+b\), and \(2(a+b)\). Positivity also follows directly from \(C=2\int_0^\infty e^{-Kt}De^{-Kt}\,dt\).

**2. Rank-two stationary current.** Set \(A=\int j(x)x^\top\,dx=D-KC\). The Lyapunov equation gives \(A=(CK-KC)/2\), so the projector formula implies

\[
 A=\frac{b}{2a+b}(PD-DP)
   =\frac{b}{n(2a+b)}(\mathbf1T^\top-T\mathbf1^\top),
\]

where \(T=(T_1,\ldots,T_n)^\top\). Thus \(j(x)=AC^{-1}x\rho(x)\) lies in \(\operatorname{span}\{\mathbf1,T\}\) at every position; this proves a pointwise flux-plane statement, not merely a bound on matrix rank. For unequal temperatures, \(T\) and \(\mathbf1\) are independent and this skew-symmetric matrix has rank exactly two. Put \(v=T-\overline T\mathbf1\) and \(s^2=n^{-1}\|v\|^2\). In the orthonormal plane spanned by \(\mathbf1/\sqrt n\) and \(v/(s\sqrt n)\), \(A\) has matrix \(\bigl(\begin{smallmatrix}0&\Omega\\-\Omega&0\end{smallmatrix}\bigr)\), with \(\Omega=bs/(2a+b)\), and is zero on its orthogonal complement. If all baths agree, \(A=0\) and detailed balance holds.

**3. Bath heat and entropy production.** The Stratonovich heat rate follows from \(dU=(KX)^\top\circ dX\) and Itô's correction:

\[
 h_i=\mathbb E[(KX)_i^2]-T_iK_{ii}=(KCK-DK)_{ii}.
\]

Since \(KC=D-A\), we have \(KCK-DK=-AK\). Off-diagonal elements of \(K\) are \(-b/n\), while \(A_{ii}=0\), so

\[
 h_i=-\sum_j A_{ij}K_{ji}=\frac b n\sum_jA_{ij}
 =\frac{b^2}{n(2a+b)}(\overline T-T_i).
\]

In particular \(\sum_i h_i=0\), as required by stationarity. Summing \(h_i/T_i\) yields the stated entropy-production formula. The strict arithmetic–harmonic mean inequality gives \(\overline T\sum_i1/T_i>n\) whenever the temperatures differ. Alternatively, substitution of \(j=AC^{-1}x\rho\) proves

\[
 \sigma=\int_{\mathbb R^n}\frac{j(x)^\top D^{-1}j(x)}{\rho(x)}\,dx
 =\operatorname{tr}(C^{-1}A^\top D^{-1}A),
\]

confirming that the quantity is genuine nonnegative stationary entropy production, not an ad hoc heat contrast. A mathematical pairwise heat-routing representation, not a unique physical bond-current decomposition, is \(J_{i\to j}=b^2(T_i-T_j)/[n^2(2a+b)]\), whose sum over \(j\) equals \(-h_i\).

**4. Fixed-spectrum, unbounded-cost family.** In the three-temperature family stated above, the latter two temperatures are positive for all \(0<\varepsilon<1/4\), because \((3-\varepsilon)^2-(3+6\varepsilon-3\varepsilon^2)>0\) there. Directly,

\[
 T_1+T_2+T_3=3,\qquad
 T_1^2+T_2^2+T_3^2=6.
\]

Hence the population variance is \(6/3-(3/3)^2=1\). The current matrix has the same conjugate eigenvalues \(\pm ib/(2a+b)\) for every \(\varepsilon\), though its eigenvectors and entries need not be the same. As \(\varepsilon\downarrow0\), the other two temperatures approach the strictly positive numbers \((3\mp\sqrt3)/2\). Thus only \(1/T_1=1/\varepsilon\) diverges in \(\sigma\), proving the sharp leading equivalent above. No zero-temperature dynamics is asserted.

## Verification

Run `python3 verify.py` in a standard Python 3 environment; no external packages or external files are required. The verifier independently solves the complete \(n^2\)-unknown Lyapunov system over exact rational numbers, without using the projector covariance formula, and checks the stationary current, skew symmetry, rank-polynomial identity, heat balance, entropy production, and positive current quadratic expression. Its 36 cases use dimensions \(2\) through \(5\), multiple positive pinning/coupling pairs, and both equal- and unequal-temperature vectors. These finite checks support the algebra but do not prove the quantified infinite family; the analytic argument above supplies that proof. The three-bath fixed-moment calculation is proved exactly in section 4, not inferred from numerical sampling.

## Relationship to prior work

Filliger and Reimann [1] introduce the two-bath planar Brownian gyrator and its systematic torque. Zia and collaborators [2] provide a general stationary Gaussian probability-angular-momentum framework, including the commutator identity; that identity is **prior work**, not presented here as a new discovery. Bonetto, Lebowitz and Lukkarinen [3] study a different, underdamped, nearest-neighbor crystal with a bath at every site, using self-consistently chosen interior temperatures. Defaveri, Olivares and Anteneodo [4] study mean-field harmonic couplings with inertial dynamics and two endpoint reservoirs. Neither inspected model determines the arbitrary independent-temperature, all-site overdamped rank-two flux plane together with the exact heat and entropy formulas or the fixed-temperature-moment dissipation divergence. The distinguishing contribution is the specialized global-coupling classification and its thermodynamic consequence, not Gaussian solvability itself.

## Limitations

The conclusions require equal mobilities, identical pairwise harmonic couplings, positive pinning and strictly positive bath temperatures. Arbitrary nonuniform graph couplings or inertial oscillators may have higher-rank current fields. The nonzero eigenvalues describe the integrated probability-current tensor \(A\), not the eigenvalues of the full stochastic generator or a physical angular velocity. Heat is defined at the independent reservoir interfaces; a decomposition into putative pairwise mechanical bond currents is not unique. The result gives a divergence as a cold bath approaches zero, not a finite-temperature singularity. Published-source and research-record searches are bounded and cannot certify historical novelty; independent scientific validation has not been carried out.

## References

[1] R. Filliger and P. Reimann, *The Brownian gyrator: a minimal heat engine on the nano-scale*, arXiv:0710.3735v1, public 19 October 2007. https://arxiv.org/abs/0710.3735

[2] R. K. P. Zia, J. B. Weiss, D. Mandal and B. Fox-Kemper, *Manifest and Subtle Cyclic Behavior in Nonequilibrium Steady States*, arXiv:1610.02976, public October 2016. https://arxiv.org/abs/1610.02976

[3] F. Bonetto, J. L. Lebowitz and J. Lukkarinen, *Fourier's Law for a Harmonic Crystal with Self-consistent Stochastic Reservoirs*, arXiv:math-ph/0307035v1, public 17 July 2003. https://arxiv.org/abs/math-ph/0307035

[4] L. Defaveri, C. Olivares and C. Anteneodo, *Heat conduction in chains of non-locally coupled harmonic oscillators: mean-field limit*, arXiv:2111.01332, public 2 November 2021. https://arxiv.org/abs/2111.01332
