# Sharp moment thresholds and multilevel variance at a random avoided eigenvalue crossing

## Finding
Let \(T\) have a bounded probability density \(f\) supported on \([-1,1]\), continuous at zero, with \(f(0)>0\). For \(\varepsilon>0\) set
\[
A_\varepsilon(t)=\begin{pmatrix}t&\varepsilon\\\varepsilon&-t\end{pmatrix},\qquad
\lambda_\varepsilon(t)=\lambda_{\max}(A_\varepsilon(t))=\sqrt{t^2+\varepsilon^2},
\]
and let \(P_\varepsilon(t)\) be its rank-one top-eigenvalue orthogonal projector; at \(\varepsilon=0\), define \(P_0(t)\) for \(t\ne0\). Set \(D_\varepsilon=\|P_\varepsilon(T)-P_0(T)\|_F^2\) and \(L_\varepsilon=\lambda_\varepsilon(T)-\lambda_0(T)\).

**Sharp crossing moment spectrum.** For every fixed real \(p>0\), as \(\varepsilon\downarrow0\),
\[
\mathbb E L_\varepsilon^p\sim
\begin{cases}
2^{-p}\varepsilon^{2p}\mathbb E|T|^{-p},&0<p<1,\\
f(0)\varepsilon^2\log(1/\varepsilon),&p=1,\\
\displaystyle 2f(0)\frac{p}{p^2-1}\varepsilon^{p+1},&p>1.
\end{cases}
\]
For every fixed \(q>0\),
\[
\mathbb E D_\varepsilon^q\sim
\begin{cases}
2^{-q}\varepsilon^{2q}\mathbb E|T|^{-2q},&0<q<\tfrac12,\\
\sqrt2 f(0)\varepsilon\log(1/\varepsilon),&q=\tfrac12,\\
2f(0)J_q\varepsilon,&q>\tfrac12,
\end{cases}
\quad J_q=\int_0^\infty\left(1-\frac{u}{\sqrt{1+u^2}}\right)^qdu.
\]
In particular \(J_1=1\), so the mean squared projector error is asymptotic to \(2f(0)\varepsilon\), whereas the mean squared eigenvalue error is asymptotic to \(4f(0)\varepsilon^3/3\).

**True coupled level corrections.** For each fixed \(\theta\in[0,1)\), couple both levels with the same random \(T\), and define
\[
C_P(\theta)=\int_0^\infty\left[1-\frac{u^2+\theta}{\sqrt{u^2+1}\sqrt{u^2+\theta^2}}\right]du,\quad
C_\lambda(\theta)=\int_0^\infty\left[\sqrt{u^2+1}-\sqrt{u^2+\theta^2}\right]^2du.
\]
Both integrals are strictly positive and finite. The exact leading constants for the squared correction norms are
\[
\lim_{\varepsilon\downarrow0}\frac{\mathbb E\|P_\varepsilon-P_{\theta\varepsilon}\|_F^2}{\varepsilon}=2f(0)C_P(\theta),\qquad
\lim_{\varepsilon\downarrow0}\frac{\mathbb E|\lambda_\varepsilon-\lambda_{\theta\varepsilon}|^2}{\varepsilon^3}=2f(0)C_\lambda(\theta).
\]
The same constants hold when the squared correction norms are replaced by their Hilbert-space and scalar **centered variances**, respectively. Hence this random-crossing model has distinct multilevel correction-variance exponents \(1\) and \(3\) for the top eigenspace and top eigenvalue. At \(\theta=0\), \(C_P(0)=1\) and \(C_\lambda(0)=2/3\).

For the uniform law on \([-1,1]\), the following identities are exact for every \(\varepsilon>0\):
\[
\mathbb E D_\varepsilon=1+\varepsilon-\sqrt{1+\varepsilon^2},\qquad
\mathbb E L_\varepsilon^2=\frac23+\varepsilon^2-\frac23(1+\varepsilon^2)^{3/2}+\frac23\varepsilon^3.
\]

## Assumptions and scope
All matrices are real symmetric \(2\times2\); eigenvalues are ordered by numerical value, and all quantities use exact arithmetic. A tie at \(T=0\) for the unperturbed top eigenvalue is a null event. Density boundedness and continuity at zero, together with strictly positive \(f(0)\), are essential for the universal leading coefficients as stated. The coupling uses the **same** random parameter at both levels. The theorem concerns the top *individual* eigenspace, not the projector onto the two-dimensional cluster, which is the identity and hence has zero error.

## Proof
**1. Exact spectral identities.** Write \(r_a(t)=\sqrt{t^2+a^2}\). For \(a>0\), \(A_a^2=r_a^2I\), so \(P_a=(I+A_a/r_a)/2\). For \(t\ne0\), \(P_0=(I+\operatorname{sgn}(t)\operatorname{diag}(1,-1))/2\). The Pauli-matrix trace identities give
\[
L_\varepsilon(t)=\frac{\varepsilon^2}{r_\varepsilon(t)+|t|},\qquad
D_\varepsilon(t)=1-\frac{|t|}{r_\varepsilon(t)}.
\]
Similarly, for \(0\le\theta<1\),
\[
\|P_\varepsilon-P_{\theta\varepsilon}\|_F^2
=1-\frac{t^2+\theta\varepsilon^2}{r_\varepsilon(t)r_{\theta\varepsilon}(t)},\quad
\lambda_\varepsilon-\lambda_{\theta\varepsilon}
=\frac{(1-\theta^2)\varepsilon^2}{r_\varepsilon(t)+r_{\theta\varepsilon}(t)}.
\]
These formulas include \(\theta=0\) away from the null set \(t=0\).

**2. Eigenvalue moment threshold.** At each fixed nonzero \(t\), \(L_\varepsilon(t)/\varepsilon^2\to1/(2|t|)\), and \(L_\varepsilon/\varepsilon^2\le1/(2|t|)\). Bounded density makes \(|T|^{-p}\) integrable for \(p<1\), yielding the first regime by dominated convergence. For \(p>1\), substitute \(t=\varepsilon u\) and dominate by an integrable function, since \((\sqrt{1+u^2}-|u|)^p=O(|u|^{-p})\). The coefficient is
\[
\int_0^\infty(\sqrt{1+u^2}-u)^pdu
=\int_0^\infty e^{-pv}\cosh(v)\,dv=\frac{p}{p^2-1},
\]
by \(u=\sinh v\). The positive and negative sides each contribute \(f(0)\). For \(p=1\), split at a fixed small \(\delta>0\), replace \(f(t)\) by \(f(0)+o_\delta(1)\) in the inner interval, and use \(L_\varepsilon(t)\sim\varepsilon^2/(2|t|)\) uniformly on \(\varepsilon\ll|t|\le\delta\). Both sides yield \(f(0)\varepsilon^2\log(1/\varepsilon)\). The outer interval is \(O_\delta(\varepsilon^2)\); then send \(\delta\downarrow0\).

**3. Projector moment threshold.** For nonzero fixed \(t\), \(D_\varepsilon(t)/\varepsilon^2\to 1/(2t^2)\) and \(D_\varepsilon/\varepsilon^2\le1/(2t^2)\); dominated convergence proves the \(q<1/2\) regime. For \(q>1/2\), set \(t=\varepsilon u\); the rescaled integrand \((1-|u|/\sqrt{1+u^2})^q\) is \(O(|u|^{-2q})\), integrable at infinity, and converges under bounded-density domination. At the boundary \(q=1/2\), the intermediate-zone integrand is asymptotic to \(\varepsilon/(\sqrt2|t|)\); both sides contribute \(\sqrt2 f(0)\varepsilon\log(1/\varepsilon)\). The integral \(J_1=\int_0^\infty(1-u/\sqrt{1+u^2})du=1\) by an elementary antiderivative.

**4. Coupled level corrections and centering.** Substituting \(t=\varepsilon u\) into the two formulas of Step 1 gives the exact limiting integrands defining \(C_P,C_\lambda\). For large \(|u|\), both are \(O(u^{-2})\); bounded convergence after splitting off a finite interval and domination establishes the two limits. They are strictly positive for every \(\theta<1\), because the two matrices have distinct top projectors and distinct positive eigenvalues for \(t\) near zero; they are finite by the tail bound. The mean correction in Frobenius norm is \(O(\varepsilon\log(1/\varepsilon))\), since the pointwise norm is bounded by \(C_\theta\min\{1,\varepsilon/|t|\}\). The scalar mean correction is \(O(\varepsilon^2\log(1/\varepsilon))\), since its absolute value is bounded by \(C_\theta\min\{\varepsilon,\varepsilon^2/|t|\}\). Their squared means are respectively \(o(\varepsilon)\) and \(o(\varepsilon^3)\). Subtracting squared means therefore leaves the same variance limits. Setting \(\theta=0\) and integrating gives \(C_P(0)=1\) and \(C_\lambda(0)=2/3\) (also Step 2 at \(p=2\)).

**5. Uniform-density exact formulas.** For \(f(t)=1/2\) on \([-1,1]\), integrate over \(t\in[0,1]\). The identity \(\int_0^1 t/\sqrt{t^2+\varepsilon^2}\,dt=\sqrt{1+\varepsilon^2}-\varepsilon\) gives the first result. Expand \((\sqrt{t^2+\varepsilon^2}-t)^2=2t^2+\varepsilon^2-2t\sqrt{t^2+\varepsilon^2}\), then integrate to obtain the second.

## Verification
Run the standalone standard-library checker as `python3 check.py`. It reproduces the exact finite-parameter formulas by independent quadrature, checks positive coupled level corrections and tests several moment asymptotic regimes. Its finite tests do not substitute for Steps 1–5, which prove the universal statements for arbitrary eligible densities and every fixed positive moment order.

## Relationship to prior work
Dölz and Lozano-Simón (arXiv:2610.36955v1, 2026) define multilevel Monte Carlo estimators for random nonlinear eigenvalue problems and emphasize the difficulty of individual eigenpair tracking near crossings. Their algorithm instead uses parameter-to-solution maps associated with eigenvalue clusters; their general formulas do not identify the sharp individual-mode moment transitions or the explicit distinct exponents for a random avoided crossing. Grubišić, Saarikangas and Hakula (2023) establish analytic dependence for **spectrally isolated clusters**; their framework is not a uniform-gap result for the individual top eigenspace at a crossing. Dölz and Ebert (arXiv:2210.09089) analyze multiple-eigenvalue perturbations and eigenspace uncertainty, but the inspected abstract/accessible article record does not itself establish the exact two-level random-crossing moment spectrum. The matrix diagonalization and elementary integration here are classical tools; the claim is the complete sharp statistical rate and coefficient classification for the specified numerical benchmark, not a new spectral-perturbation identity.

## Limitations
This is a deliberately small real-symmetric crossing normal form, not a general perturbation theorem for nonlinear operators, a finite-element implementation theorem, or an MLMC work-complexity bound. It does not claim that a **cluster projector** suffers the same loss: the complete two-eigenvalue cluster projector is exactly stable. The density must be bounded and positive/continuous at the crossing; different vanishing or singular density behavior can change the exponents. Published results outside the inspected set could contain an equivalent sharp normal-form calculation. No independent audit has been performed.

## References
1. J. Dölz and J. Lozano-Simón, *Multilevel Monte Carlo methods for random nonlinear eigenvalue problems*, arXiv:2610.36955v1 (first public 27 October 2026), https://arxiv.org/html/2610.36955v1.
2. L. Grubišić, M. Saarikangas and H. Hakula, *Stochastic collocation method for computing eigenspaces of parameter-dependent operators*, Numerische Mathematik 153 (2023), 85–110, https://doi.org/10.1007/s00211-022-01339-3.
3. J. Dölz and D. Ebert, *On uncertainty quantification of eigenvalues and eigenspaces with higher multiplicity*, arXiv:2210.09089 (2022), https://arxiv.org/abs/2210.09089.
4. M. Giles, *Multilevel Monte Carlo methods*, Acta Numerica 24 (2015), 259–328, https://doi.org/10.1017/S096249291500001X.
