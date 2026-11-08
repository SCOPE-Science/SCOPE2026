# A universal optimal reset rate for diffusion anisotropy in a rotationally coupled colloid

## Finding
Consider the overdamped planar colloid with a constant body-frame mobility matrix
\[
\mu=\begin{pmatrix}aI_2&c\\c^{\mathsf T}&b\end{pmatrix},\qquad
D>0,\quad a,b>0,\quad 0<\gamma=\|c\|<\sqrt{ab},
\]
where \(D=k_{\mathrm B}T\). Free angular diffusion has coefficient \(\alpha=Db\). Independently, a Poisson process of rate \(r>0\) instantaneously restores the orientation to a fixed angle \(\phi_0\), without moving the colloid's position. Between events, position and angle follow the Stratonovich overdamped Brownian equation with laboratory-frame mobility \(\operatorname{diag}(R(\phi),1)\mu\operatorname{diag}(R(\phi)^{\mathsf T},1)\), as defined below.

Write \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) and define the orthonormal unit vectors \(e_{\parallel}=R(\phi_0)Jc/\gamma\) and \(e_{\perp}=R(\phi_0)c/\gamma\). For every initial position and initial orientation, the long-time velocity and covariance growth matrix are
\[
\lim_{t\to\infty}\frac{\mathbb E(X_t-X_0)}t
=v_r=\frac{Dr}{r+\alpha}R(\phi_0)Jc,
\qquad
\Sigma_r=\lim_{t\to\infty}\frac{\operatorname{Cov}(X_t)}t.
\]
In the ordered basis \((e_{\perp},e_{\parallel})\), the covariance growth matrix is diagonal, with
\[
\boxed{\Sigma_{\perp}(r)=2Da-\frac{4D^2\gamma^2}{r+4\alpha}},
\]
\[
\boxed{\Sigma_{\parallel}(r)=2Da-
\frac{2\alpha D^2\gamma^2(2\alpha^2+3\alpha r+4r^2)}{(r+\alpha)^3(r+4\alpha)}}.
\]
Both components are strictly increasing functions of \(r\), but their difference is strictly positive and uniquely maximized at a *finite* reset rate:
\[
\boxed{\Sigma_{\parallel}(r)-\Sigma_{\perp}(r)=
\frac{2D^2\gamma^2r(3\alpha^2+2\alpha r+2r^2)}{(r+\alpha)^3(r+4\alpha)}},
\]
\[
\boxed{r_{\mathrm{max}}=2\alpha,
\qquad \max_{r>0}(\Sigma_{\parallel}-\Sigma_{\perp})
=\frac{10D^2\gamma^2}{27\alpha}=\frac{10D\gamma^2}{27b}}.
\]
The normalized positions obey a planar Gaussian central limit theorem,
\[
\frac{X_t-v_rt}{\sqrt t}\ \Longrightarrow\ \mathcal N(0,\Sigma_r).
\]
In particular, anisotropy is produced solely by nonzero thermal translation–rotation coupling even though the intrinsic translational mobility \(aI_2\) is isotropic. At both the zero-rate and infinite-rate limits the covariance growth is isotropic, with respective scalar limits \(2Da-D\gamma^2/b\) and \(2Da\).

## Assumptions and scope
The body-frame mobility \(\mu\) is constant, real symmetric and strictly positive definite. Its translational block is isotropic and its translation–rotation cross block \(c\) is nonzero. The process is planar, free of external potential and active propulsion, and has no hydrodynamic interactions with other particles. The bath temperature is constant. The driving Brownian motion and the independent Poisson reset clock are defined on a common filtered probability space; position is continuous across resets while angle is assigned \(\phi_0\). There are no restrictions on the positive values of \(r\) or \(\alpha\) besides finiteness. All statements are asymptotic in observation time with parameters fixed; they do not concern position-reset protocols or transient finite-time covariances. The long-time spatial covariance is about the actual mean, not the uncentered second moment.

For clarity, define \(R(\phi)=\begin{psmallmatrix}\cos\phi&-\sin\phi\\\sin\phi&\cos\phi\end{psmallmatrix}\), and let \(\mathsf R(\phi)=\operatorname{diag}(R(\phi),1)\). Between resets the three-vector \(q=(X_1,X_2,\phi)\) satisfies
\[
\mathrm dq=\sqrt{2D}\,\mathsf R(\phi)\mu^{1/2}\circ\mathrm dW,
\]
with the Stratonovich interpretation, where \(W\) is a standard three-dimensional Brownian motion. Angles may be read modulo \(2\pi\); using an unwrapped angle during each reset interval gives the same spatial law. The physical diffusion tensor is \(\Sigma_r/2\) rather than \(\Sigma_r\).

## Proof
**1. Angular and translational decomposition.** The Stratonovich-to-Itô correction gives the mean spatial drift \(D R(\phi)Jc\) and angular diffusivity \(\alpha=Db\). Since \(aI_2-cc^{\mathsf T}/b\) is strictly positive definite, split the thermal noises into a rotational Brownian driver and an independent planar Brownian driver. Between jumps,
\[
\mathrm d\phi=\sqrt{2\alpha}\,\mathrm dB^{(0)},\qquad
\mathrm dX=DR(\phi)Jc\,\mathrm dt+
\frac{R(\phi)c}{b}\,\mathrm d\phi+
\sqrt{2D}\,R(\phi)Q^{1/2}\mathrm dB^{(2)},
\quad Q=aI_2-\frac{cc^{\mathsf T}}b.
\]
Here \(B^{(0)}\) and \(B^{(2)}\) are independent. The Itô identity
\[
\mathrm d\{R(\phi)Jc\}=-R(\phi)c\,\mathrm d\phi
-\alpha R(\phi)Jc\,\mathrm dt
\]
therefore yields the exact *between-reset* displacement identity
\[
\mathrm dX=-\frac1b\,\mathrm d\{R(\phi)Jc\}
+\sqrt{2D}\,R(\phi)Q^{1/2}\mathrm dB^{(2)}.
\]
The identity must not be integrated across a reset jump: the angle jumps but the position does not. This distinction is essential for the covariance.

**2. Independent cycles and their means.** Successive complete intervals between Poisson resets have independent durations \(T\sim\operatorname{Exp}(r)\) and independent spatial increments \(Y\). Because \(aI_2\) is isotropic, rotate the body and laboratory frames so that \(\phi_0=0\) and \(c=(\gamma,0)^{\mathsf T}\), with the resulting coordinates ordered as \((e_{\perp},e_{\parallel})\). If \(\Theta\mid T=t\sim\mathcal N(0,2\alpha t)\), integration over one cycle gives
\[
Y=\frac\gamma b\begin{pmatrix}\sin\Theta\\1-\cos\Theta\end{pmatrix}+Z,
\qquad
\mathbb E(Z\mid\phi_s:0\le s\le T,T)=0,
\]
where
\[
\operatorname{Cov}(Z\mid\phi_s:0\le s\le T,T)
=2D\int_0^T R(\phi_s)Q R(\phi_s)^{\mathsf T}\,\mathrm ds.
\]
For integer \(n\), the explicit Laplace formulas are
\[
\mathbb E(e^{in\Theta})=\frac r{r+n^2\alpha},\quad
\mathbb E(Te^{in\Theta})=\frac r{(r+n^2\alpha)^2},\quad
\mathbb E\!\left[\int_0^T e^{in\phi_s}\mathrm ds\right]
=\frac1{r+n^2\alpha}.
\]
In particular \(\mathbb EY=(\gamma/b)(0,\alpha/(r+\alpha))^{\mathsf T}\) and \(\mathbb ET=1/r\), proving the velocity formula by the renewal-reward law.

**3. The centered covariance and Gaussian limit.** All moments of \((T,Y)\) are finite: the geometric part is bounded and the independent noise has conditional covariance bounded by a constant times \(T\). The regenerative renewal-reward central limit theorem, including the negligible terminal incomplete interval, therefore yields
\[
\Sigma_r=\frac{\mathbb E[(Y-v_rT)(Y-v_rT)^{\mathsf T}]}{\mathbb ET}
=r\,\mathbb E[(Y-v_rT)(Y-v_rT)^{\mathsf T}].
\]
This gives both the Gaussian limit and covariance growth. The two coordinates have zero off-diagonal covariance by the symmetry \(\Theta\mapsto-\Theta\) and the corresponding symmetry of the integrated noise covariance. Put \(q_j=r/(r+j^2\alpha)\) for \(j=1,2\). The independent-noise parts of the two covariance rates are
\[
N_{\perp}=2Da-\frac{D\gamma^2}b(1+q_2),\qquad
N_{\parallel}=2Da-\frac{D\gamma^2}b(1-q_2).
\]
The geometric contribution in the transverse direction is
\[
G_{\perp}=\frac{r\gamma^2}{2b^2}(1-q_2).
\]
For the parallel direction define \(\kappa=\alpha r/(r+\alpha)\). Then
\[
G_{\parallel}=\frac{r\gamma^2}{b^2}
\left\{\frac32-2q_1+\frac12q_2
-2\kappa\left(\frac1r-\frac r{(r+\alpha)^2}\right)
+\frac{2\kappa^2}{r^2}\right\}.
\]
The expression in braces comes from the exact mean of \((1-\cos\Theta-\kappa T)^2\), using \(\mathbb ET^2=2/r^2\). Substitution of \(b=\alpha/D\) in \(\Sigma_{\perp}=N_{\perp}+G_{\perp}\) and \(\Sigma_{\parallel}=N_{\parallel}+G_{\parallel}\) produces the two displayed rational formulas.

**4. Sharp rate optimization.** Differentiating the two covariance rates yields
\[
\Sigma_{\perp}'(r)=\frac{4D^2\gamma^2}{(r+4\alpha)^2}>0,
\]
\[
\Sigma_{\parallel}'(r)=
\frac{2\alpha D^2\gamma^2(14\alpha^3+21\alpha r^2+8r^3)}{(r+\alpha)^4(r+4\alpha)^2}>0.
\]
For the anisotropy \(A(r)=\Sigma_{\parallel}(r)-\Sigma_{\perp}(r)\), exact factorization gives
\[
A'(r)=\frac{2D^2\gamma^2(2\alpha-r)
(6\alpha^3-\alpha^2r+4\alpha r^2+2r^3)}
{(r+\alpha)^4(r+4\alpha)^2}.
\]
The second factor in the numerator is strictly positive because \(6\alpha^2-\alpha r+4r^2>0\) for all \(r\ge0\). Hence \(A\) strictly increases before \(2\alpha\) and strictly decreases after. Its value at \(2\alpha\) is \(10D^2\gamma^2/(27\alpha)\). Direct limits of the covariance formulas prove isotropy as \(r\downarrow0\) and \(r\to\infty\), completing the proof.

## Verification
The standalone `verify.py` uses SymPy to cross-check the independent cycle-moment expressions against the closed covariance formulas; it verifies both component derivatives, the exact anisotropy factorization, the extremal value, and both zero-gap endpoint limits. It also compares independently arranged numeric formulas for twelve positive parameter pairs. To replay: install Python 3 with `sympy`, then run `python verify.py` beside this file. The program reports `PASS: nine symbolic identities and 12 independently evaluated renewal-moment cases`. These are algebraic reproducibility checks; the infinite-time claims are proved by the regeneration argument, not by the finite tests.

## Relationship to prior work
Cleuren and Eichhorn, *Sorting by Resetting* (arXiv:2603.19430, first posted March 19, 2026), introduce the full body-frame mobility model with nonzero translation–rotation coupling, derive mean motion under **periodic** orientation resetting, and explicitly identify fluctuations and random resetting as further directions. The present result adopts their microscopic dynamics but computes the **centered long-time covariance under independent Poisson orientation resets** and finds a sharp, universal, finite-rate anisotropy maximum; neither follows from their first-moment formula alone.

Chaki, Olsen and Löwen, *Anisotropic Brownian particles under resetting* (arXiv:2406.17550, June 25, 2024), calculate effective diffusion for Poisson orientational resetting when translational and angular thermal noises are independent and the body-frame translational mobilities are unequal. In their model there is no off-diagonal thermal cross mobility \(c\): setting their translational mobilities equal removes the anisotropy. Here the translational block is *equal in both directions*, yet coupling \(c\ne0\) induces nonzero drift and the finite-rate anisotropy maximum.

Ghosh and Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting* (arXiv:2501.05149, January 9, 2025; later published in 2026), obtain orientation-reset-induced anisotropic diffusion from explicit self-propulsion and diagonal body-frame noises. Their drift and diffusion generator are different from the passive correlated thermal-mobility model treated here. Generic renewal-reward central limit theory is used as a known proof method, not claimed as new.

## Limitations
The sharp optimum applies to the **absolute difference of covariance growth rates**, not to arbitrary sorting-quality metrics such as separation-to-noise ratio. It assumes isotropic translational mobility, nonzero cross-mobility, a fixed reset orientation, zero positional displacement at resets and Poisson reset times. It does not classify nonscalar translational mobility, angle-dependent hydrodynamics, finite-speed reorientation or correlated reset clocks. The model need not describe every experimental colloid; for example, the strictly positive mobility \(\mu=\begin{psmallmatrix}1&0&1/2\\0&1&0\\1/2&0&1\end{psmallmatrix}\) demonstrates the admissible class. Publication priority beyond the inspected sources requires independent review; no assertion is made that broad renewal or homogenization results could not imply the formula after specialization.

## References
1. B. Cleuren and R. Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1 (publicly posted March 19, 2026), https://arxiv.org/abs/2603.19430 . Particularly the colloid equations (4)–(8), discussion and Appendix B.
2. S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550 (publicly posted June 25, 2024), https://arxiv.org/abs/2406.17550 . Particularly its independent-noise model and orientation-only resetting section.
3. A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149 (publicly posted January 9, 2025), https://arxiv.org/abs/2501.05149 . Its active propulsion and diagonal-noise model provides a distinct comparison.
