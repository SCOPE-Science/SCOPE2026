# Positive-semidefinite Kerr interactions forbid internal Hopf crossings, with a sharp two-mode converse

## Finding

For a network of parametrically driven, damped Kerr modes with identical positive loss rate, a positive-semidefinite nonlinear interaction matrix makes a finite-frequency *internal* equilibrium instability impossible on every physical stationary support. This holds even when stationary phase-branch signs disagree and individual pumps and detunings differ. The condition is sharp in the symmetric two-mode family: positive self-coupling \(a\) and positive cross-coupling \(b\) admit a transverse imaginary-eigenvalue crossing for some parameters **if and only if** \(b>a\). In particular, every stronger-than-onsite coupling ratio admits an explicit one-parameter family with exactly one linear-stability switch.

## Assumptions and scope

Let \(N\ge1\), \(\kappa>0\), \(V=V^{\mathsf T}\in\mathbb R^{N\times N}\), real detunings \(\Delta_j\), and positive drives \(G_j\). Consider the deterministic mean-field equations
\[
i\dot\alpha_j=\left(-\Delta_j-\frac{i\kappa}{2}+\sum_{k=1}^{N}V_{jk}|\alpha_k|^2\right)\alpha_j+G_j\overline\alpha_j,\qquad j=1,\ldots,N.
\]
On a stationary active support \(S\), assume \(I_j=|\alpha_j|^2>0\) for every \(j\in S\); then \(G_j\ge\kappa/2\). Write \(\chi_j=\sqrt{G_j^2-\kappa^2/4}\) and the stationary phase sign \(\sigma_j\in\{-1,+1\}\), where at the endpoint \(\chi_j=0\) the sign is immaterial. Internal means perturbations within the active-support invariant subspace, not dormant-mode excitations. In the first assertion \(V_S\) is positive semidefinite, possibly singular. The two-mode converse assumes \(a>0\), \(b\ge0\), symmetric onsite and mutual couplings, two positive active intensities, equal drive, and constant detunings while pump and loss are varied together.

## Proof

**1. Exact internal linearization.** In amplitude-phase coordinates \(\alpha_j=\sqrt{I_j}e^{i\phi_j}\),
\[
\dot I_j=I_j[-\kappa-2G_j\sin(2\phi_j)],\qquad
\dot\phi_j=\Delta_j-\sum_{k\in S}V_{jk}I_k-G_j\cos(2\phi_j).
\]
At a stationary positive-intensity point, \(G_j\sin(2\phi_j)=-\kappa/2\), \(G_j\cos(2\phi_j)=\sigma_j\chi_j\), and \(\sum_kV_{jk}I_k=\Delta_j-\sigma_j\chi_j\). Let \(D=\operatorname{diag}(\sigma_j\chi_jI_j)_{j\in S}\). In the order \((\delta I,\delta\phi)\), the exact real Jacobian is
\[
J_S=\begin{pmatrix}0&-4D\\-V_S&-\kappa\mathbf 1\end{pmatrix},\qquad
\det(\lambda\mathbf1-J_S)=\det\!\left(\lambda(\lambda+\kappa)\mathbf1-4DV_S\right).
\]
The coordinate change is nonsingular because every active intensity is positive. This identity also applies when some \(\chi_j\) vanish.

**2. Positive-semidefinite obstruction for any support size.** When \(V_S\succeq0\), write \(R=V_S^{1/2}\), which exists even if \(V_S\) is singular. Sylvester's determinant identity shows that \(4DR^2\) and \(4RDR\) have identical characteristic polynomials. The latter is real symmetric, so every eigenvalue \(\mu\) of \(4DV_S\) is real. At a hypothetical nonzero imaginary Jacobian eigenvalue \(\lambda=i\omega\), \(\omega\in\mathbb R\setminus\{0\}\), the spectral equation would give
\[
\mu=\lambda(\lambda+\kappa)=-\omega^2+i\kappa\omega\notin\mathbb R,
\]
a contradiction. Therefore no *internal* finite-frequency imaginary crossing is possible, for any drive/phase signs. Every principal submatrix of a positive-semidefinite \(V\) is itself positive semidefinite, yielding the simultaneous all-support assertion.

**3. Necessity in the symmetric dimer.** For \(V=\left(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\right)\) with \(a>0\), \(b\ge0\), the eigenvalues of \(V\) are \(a+b\) and \(a-b\). Hence \(b\le a\) gives the obstruction in step 2. Thus \(b>a\) is necessary for a two-active-mode spectral Hopf crossing.

**4. Constructive sufficiency for every \(b>a\).** Fix arbitrary \(I,\chi>0\) and set
\[
\epsilon=\frac{b-a}{2b},\quad I_e=I(1-\epsilon),\quad I_o=I(1+\epsilon),\quad
\Delta_e=aI_e+bI_o+\chi,\quad \Delta_o=bI_e+aI_o-\chi.
\]
Since \(0<\epsilon<1/2\), both intensities are positive. For every \(\kappa>0\), set \(G(\kappa)=\sqrt{\chi^2+\kappa^2/4}\), and choose phases satisfying \(G\sin(2\phi_e)=G\sin(2\phi_o)=-\kappa/2\), \(G\cos(2\phi_e)=+\chi\), and \(G\cos(2\phi_o)=-\chi\). Both trigonometric pairs have unit norm, so these phases exist and the intensity equations of step 1 hold exactly. Consequently the same positive-intensity mixed stationary branch persists through all \(\kappa>0\), with its detunings fixed.

On that branch put \(M=4\chi\operatorname{diag}(I_e,-I_o)V\), \(t=\operatorname{tr}M\) and \(d=\det M\). Direct multiplication gives
\[
t=4a\chi(I_e-I_o)=-8a\chi I\epsilon<0,\qquad
d=16\chi^2I_eI_o(b^2-a^2)>0.
\]
The internal characteristic polynomial is
\[
p_\kappa(\lambda)=(\lambda^2+\kappa\lambda)^2-t(\lambda^2+\kappa\lambda)+d.
\]
Its quartic coefficients in descending order are \(1,2\kappa,\kappa^2-t,-\kappa t,d\), all positive. The second Routh–Hurwitz determinant is \(\kappa(2\kappa^2-t)>0\), and the third is
\[
\mathfrak D_3=\kappa^2(t^2-2\kappa^2t-4d).
\]
Because \(t<0\), the only zero is at
\[
\kappa_c^2=\frac{4d-t^2}{-2t}=rac{2b\chi I(3b+5a)}{a}>0.
\]
Therefore every root has negative real part exactly for \(\kappa>\kappa_c\). For \(0<\kappa<\kappa_c\), the Routh array has precisely two right-half-plane roots (the other two remain left of the imaginary axis); no positive real root exists because the polynomial coefficients are positive, so the unstable pair is conjugate and nonreal. At the boundary put
\[
\omega^2=-\frac{t}{2}=\frac{2a\chi I(b-a)}{b}>0.
\]
The relation defining \(\kappa_c\) implies the *exact* factorization
\[
p_{\kappa_c}(\lambda)=(\lambda^2+\omega^2)[(\lambda+\kappa_c)^2+\omega^2].
\]
Thus the imaginary pair is simple and the other pair has strictly negative real part. Differentiation of \(p_\kappa(\lambda)=0\) along its simple eigenvalue branch gives
\[
\left.\frac{d}{d\kappa}\operatorname{Re}\lambda\right|_{\kappa_c}=-\frac{2\omega^2}{\kappa_c^2+4\omega^2}<0.
\]
The crossing is transverse. Combining steps 3–4 proves the sharp iff statement.

**5. Exact concrete witness.** With \(a=1\), \(b=3/2\), \(I=\chi=1\), the construction gives \(\epsilon=1/6\), \(I_e=5/6\), \(I_o=7/6\), \(\Delta_e=43/12\), \(\Delta_o=17/12\), \(\kappa_c^2=57/2\), \(G_c^2=65/8\), and \(\omega^2=2/3\). The result uses strict cross-coupling below \(2a\), not an endpoint saturation.

## Verification

Run \(\texttt{python3 verify.py}\) using the included standard-library-only checker. It recomputes the exact two-mode stationary constraints and the polynomial/Routh identities over multiple rational parameter examples, checks the exact witness and compares the predicted spectral branches on both sides of the critical damping. These tests supplement rather than establish the universal positive-semidefinite theorem, which is proved in step 2 by the real-symmetric spectral reduction.

## Relationship to prior work

Gómez and del Pino (2026), arXiv:2610.26573v1, derive the amplitude-phase linearization on an active support and analyze an oscillatory instability for one physically relevant dimer with cross-Kerr coupling twice its onsite Kerr coefficient. Their Appendix B.5 is the starting spectral equation. Appendix C.4 identifies the equal-phase-sign real-spectrum restriction and derives a parameter-dependent Hopf condition for their fixed dimer. Neither provides the all-support positive-semidefinite no-Hopf theorem for **arbitrary network size and mixed phase signs**, nor the sharp \(b>a\) realizability classification and adjustable-loss stability switch for **every** positive symmetric dimer coupling ratio. The present conclusion is not a restatement of their numerical Hopf threshold; it characterizes a structural boundary in the nonlinear interaction matrix. Ameye, Eichler and Zilberberg (2025) analyze parametrically driven networks with linear coupling and bifurcation landscapes, a different interaction mechanism. Trinchão et al. (2026) observe Hopf transitions in chip-scale Kerr parametric oscillators, not this matrix-signature theorem.

## Limitations

This is a theorem about *linear internal stability and spectral crossings* of deterministic mean-field fixed points, not a proof of a nonlinear Hopf normal form, birth of a stable limit cycle, basin of attraction, or quantum Lindbladian instability. The no-go requires a common positive loss rate on the active modes; unequal losses are not addressed. It does not exclude zero-frequency loss of stability or instability of dormant modes. Indefiniteness is not claimed sufficient for an arbitrary prescribed network or parameter set: the converse is an *existence* statement for the symmetric dimer with tunable detunings, loss and matched drive. The primary source's general Jacobian equation makes the spectral method available, so broader independently discovered matrix criteria remain a literature-priority risk; this document claims only the explicit no-go-and-sharpness theorem proved above.

## References

1. A. S. Gómez and J. del Pino, *Avalanches and Aging Driven by Parametric Amplification in Kerr Oscillator Networks*, arXiv:2610.26573v1 (first public 2026-10-19), especially Eq. (3), Appendix B.5 and Appendix C.4, https://arxiv.org/abs/2610.26573.
2. O. Ameye, A. Eichler and O. Zilberberg, *The parametric instability landscape of coupled Kerr parametric oscillators*, arXiv:2501.08793v1 (2025), https://arxiv.org/abs/2501.08793; Phys. Rev. Research 7, 033204.
3. L. O. Trinchão et al., *From order to chaos in a chip-scale Kerr parametric oscillator*, arXiv:2605.18690v1 (2026), https://arxiv.org/abs/2605.18690.
