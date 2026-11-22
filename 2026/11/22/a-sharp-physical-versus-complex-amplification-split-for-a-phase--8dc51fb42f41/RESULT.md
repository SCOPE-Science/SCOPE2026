# A sharp physical-versus-complex amplification split for a phase-optimized Maxwell integrator

## Finding

The phase-optimized five-subflow Maxwell discretization with coefficient \(a=\tfrac14+\tfrac{i}{4\sqrt3}\) has an exact **positive modified Hermitian energy** for every scalar transverse Fourier mode in its strict spectral CFL interval \(0<q^2<12\). If \(M(q)\) is the complex modal one-step map, \(P_n(q)=\operatorname{Re}(M(q)^n)\) denotes the real physical-output map on real initial data, and \(\delta=12-q^2\), then their sharp all-time Euclidean amplification has different near-endpoint constants:

\[
\lim_{\delta\downarrow0}\sqrt\delta\sup_{n\in\mathbb N_0}\|M(\sqrt{12-\delta})^n\|_{\mathbb C^2\to\mathbb C^2}=2\sqrt3,
\qquad
\lim_{\delta\downarrow0}\sqrt\delta\sup_{n\in\mathbb N_0}\|P_n(\sqrt{12-\delta})\|_{\mathbb R^2\to\mathbb R^2}=\sqrt3.
\]

Both constants are attainable asymptotically on the **same real unit input** \((0,1)^{\mathsf T}\), at an integer observation index of order \(\delta^{-1/2}\). A companion exact output-energy identity describes how projecting the full complex trajectory suppresses the modified energy, even though the complex trajectory preserves it. This is about nonuniform all-time near-CFL stability, not physical electromagnetic-energy conservation.

## Assumptions and scope

Take the homogeneous, lossless, constant-coefficient periodic Maxwell semidiscretization and one nonzero energy-scaled transverse Fourier polarization as in Duan, Li and Guo [1]. Let \(q=\nu\Delta t K_h>0\) be its dimensionless Fourier frequency. Use the original five-subflow palindromic composition, with the *complete complex recurrence* performed for \(n\) steps before taking its real part for physical output; do **not** project after each subflow or each time step. The amplitude norms above are induced Euclidean operator norms in this two-component modal coordinate. The output map acts on real initial modal vectors; the complex map's supremum is over complex vectors, although real vectors already realize the limiting lower bound. The complementary conjugate coefficient yields the same real map and norm statements.

The one-step complex amplification matrix [1, Eqs. (12)--(15)] is

\[
M(q)=\begin{pmatrix}A(q)&B(q)\\C(q)&A(q)\end{pmatrix},\quad
A(q)=1-\frac{q^2}{2}+\frac{q^4}{24},\quad
B(q)=q\left(\frac{q^2-8}{8}-\frac{i q^2}{8\sqrt3}\right).
\]

The lower left polynomial is given in [1, Eq. (15)]; for this coefficient it simplifies to the identity \(C(q)=-\rho(q)\overline{B(q)}\), where \(\rho(q)=1-q^2/12\). The claim does not extend unchanged to other composition coefficients, spatially inhomogeneous Maxwell systems, dissipative media, or boundary closures without the relevant modal reduction.

## Proof

**1. Exact positive modified energy.** Set \(y=q^2\), \(\rho=1-y/12\) and \(W=\operatorname{diag}(\rho,1)\). Direct substitution into the five-subflow polynomials gives

\[
C=-\rho\overline B,\qquad
|B|^2=\frac{y(y^2-12y+48)}{48},\qquad
A^2+\rho|B|^2=1.
\]

For \(0<y<12\), the weight \(W\) is positive definite. Conjugation by \(S=\operatorname{diag}(\sqrt\rho,1)\) gives

\[
S M S^{-1}=
\begin{pmatrix}A&\sqrt\rho B\\-\sqrt\rho\overline B&A\end{pmatrix}\in SU(2),
\quad M^* W M=W.
\]

Hence every complex solution \(u_n=M^n u_0\) obeys \(\rho|h_n|^2+|e_n|^2=\rho|h_0|^2+|e_0|^2\), and \(\|M^n\|_2\le\rho^{-1/2}\) for all nonnegative integers \(n\). The weighted energy is a Fourier-mode-dependent *modified* quantity and must not be identified with the original Maxwell energy.

**2. Exact formula for physical projected energy.** Throughout the open CFL interval \(A=\cos\theta\) has \(0<\theta<\pi\) and \(\sin\theta=\sqrt\rho|B|\). Cayley--Hamilton gives [1, Eq. (29)]

\[
M^n=\begin{pmatrix}
\cos(n\theta)&\frac{B}{\sqrt\rho|B|}\sin(n\theta)\\
-\frac{\sqrt\rho\overline B}{|B|}\sin(n\theta)&\cos(n\theta)
\end{pmatrix}.
\]

For real initial data let \(P_n=\operatorname{Re}(M^n)\) and \(r=\operatorname{Re}B/|B|\). Then

\[
S P_n S^{-1}=
\begin{pmatrix}\cos(n\theta)&r\sin(n\theta)\\-r\sin(n\theta)&\cos(n\theta)\end{pmatrix}.
\]

Consequently the physical output obeys, for **every** real initial vector \(u\),

\[
(P_nu)^{\mathsf T}W(P_nu)
=\left[\cos^2(n\theta)+r^2\sin^2(n\theta)\right]u^{\mathsf T}Wu
=\left[1-\frac{(\operatorname{Im}B)^2}{|B|^2}\sin^2(n\theta)\right]u^{\mathsf T}Wu.
\]

This is an identity at the observed time, **not** a claim that the output maps \(P_n\) form an iteration semigroup or decrease energy monotonically in \(n\). At the interior frequency \(q^2=8\), \(\operatorname{Re}B=0\), and the entire physical output becomes \(P_n=\cos(n\arccos(-1/3))I\), although the complex internal field is not a scalar update.

**3. Sharp boundary layer.** Write \(q=\sqrt{12-\delta}\) with \(\delta\downarrow0\). Exact algebra gives \(A=1-\delta/2+\delta^2/24\), \(\theta/\sqrt\delta\to1\), \(B\to\sqrt3-3i\), \(C=-\delta\overline B/12\to0\), and \(\sqrt\delta/\sin\theta\to1\). Thus, **uniformly over every integer** \(n\ge0\),

\[
\sqrt\delta\,M^n-\sin(n\theta)
\begin{pmatrix}0&\sqrt3-3i\\0&0\end{pmatrix}\longrightarrow0,
\qquad
\sqrt\delta\,P_n-\sin(n\theta)
\begin{pmatrix}0&\sqrt3\\0&0\end{pmatrix}\longrightarrow0
\]

in the corresponding operator norms. Uniformity holds because the coefficient differences are independent of \(n\), while \(|\sin(n\theta)|,|\cos(n\theta)|\le1\). These relations prove the claimed upper limits \(|\sqrt3-3i|=2\sqrt3\) and \(\sqrt3\).

For lower limits choose \(n_\delta\) as an integer nearest to \(\pi/(2\theta)\); then \(|n_\delta\theta-\pi/2|\le\theta/2\), whence \(\sin(n_\delta\theta)\to1\). Applying each matrix to \((0,1)^{\mathsf T}\) proves attainment of both constants and \(n_\delta\sim\pi/(2\sqrt\delta)\). The endpoint \(q^2=12\) itself has \(M=\bigl(\begin{smallmatrix}1&\sqrt3-3i\\0&1\end{smallmatrix}\bigr)\), so the physical projected powers already grow linearly there; strict CFL is essential. This completes the proof.

## Verification

The accompanying `verify.py` uses exact rational-polynomial arithmetic to check \(C=-\rho\overline B\), \(A^2+\rho|B|^2=1\), and the interior zero-real-coupling identity. It also checks the complex and projected weighted-energy identities on representative rational parameters and performs numerical regressions near the CFL edge. Run `python3 verify.py` and require the terminal line beginning `VERIFY_OK`. The analytic proof above, not the sampled computations, establishes the quantified infinite-time and boundary limits.

## Relationship to prior work

Duan, Li and Guo [1] introduced the precise palindromic family, computed its complex phase-optimized coefficient and modal amplification matrix, proved spectral stability for \(0<q^2<12\), and gave the exact Cayley--Hamilton representation together with the correct real-output interpretation. Their results are prerequisites; none of those constructions or spectral thresholds is presented here as new. The additional statements here are the **explicit positive Hermitian invariant**, the **exact scalar physical-output energy law**, the **interior physical-output cancellation**, and the **sharp pair of distinct uniform all-time near-CFL gain constants** with a common real extremizing input. These quantitatively refine their strict-CFL power-boundedness statement; the finite-time and asymptotic sharp coefficients do not appear as its asserted conclusions.

General complex splitting methods, including Bernier, Blanes, Casas and Escorihuela-Tomàs [2], establish conjugacy-to-unitary or related preservation properties under other hypotheses. Such results motivate the modified-energy viewpoint but do not provide the parameter-exact Hermitian weight or the projected-output half-gain limit for the present Maxwell map.

## Limitations

The result is an exact two-component Fourier-mode statement for the specified coefficient and strict mode-wise CFL interval. It does not give a new convergence order, an error estimate for the continuum PDE, or physical electromagnetic-energy conservation. It does not establish a mesh-independent transient bound arbitrarily near the CFL edge: the exact result instead shows its sharp \(\delta^{-1/2}\) deterioration. At each fixed noncritical step the true supremum over **integer** powers may depend on rationality of the numerical phase; only the near-edge limiting suprema are evaluated here. The formulas follow from the explicit source matrix plus new algebraic and uniform asymptotic analysis; independent priority review beyond the examined literature is not claimed.

## References

[1] H. Duan, H. Li and L. Guo, *Sharp CFL stability and temporal-dispersion optimization of symmetric splitting schemes for time-domain Maxwell equations*, arXiv:2608.22315 (first public release 2026-08-23), https://arxiv.org/abs/2608.22315, particularly Eqs. (12)--(15), (23), (29), and Corollary 3.7.

[2] J. Bernier, S. Blanes, F. Casas and A. Escorihuela-Tomàs, *Symmetric-conjugate splitting methods for linear unitary problems*, arXiv:2303.10950 (2023), https://arxiv.org/abs/2303.10950.
