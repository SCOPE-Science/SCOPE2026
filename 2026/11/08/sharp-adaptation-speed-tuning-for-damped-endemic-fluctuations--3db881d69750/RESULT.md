# Sharp adaptation-speed tuning for damped endemic fluctuations

## Finding

Consider the prevalence-driven adaptive SIS equations
\[
\dot y=-y+\tau y(1-y)z,\qquad
\dot z=\xi(1-z-\omega yz).
\]
At fixed transmission ratio \(\tau>1\) and fixed link-breaking/creation ratio \(\omega>0\), let the common network-response speed \(\xi\) vary through all positive values. The unique endemic equilibrium is independent of \(\xi\):
\[
(y_*,z_*)=\left(\frac{\tau-1}{\tau+\omega},\frac{\tau+\omega}{\tau(1+\omega)}\right).
\]
Define
\[
K=\tau-1,\quad A=\frac{K}{1+\omega},\quad
B=\frac{\tau(1+\omega)}{\tau+\omega},\quad
\eta=\sqrt{\frac{\omega}{\tau+\omega}},\quad
\xi_{\pm}=\frac{K}{B^2}(1\pm\eta)^2.
\]
Then \(0<\xi_-<\xi_+\), and the linearization at the endemic equilibrium is a stable focus **exactly** for \(\xi_-<\xi<\xi_+\). For \(0<\xi<\xi_-\) and \(\xi>\xi_+\), it is a stable node with two distinct real eigenvalues; at either endpoint it is a defective stable repeated-eigenvalue node.

The local spectral decay exponent
\[
\gamma(\xi)=-\max\{\operatorname{Re}\lambda:\lambda\in\sigma(J_*)\}
\]
has the **unique global maximum** at the upper critical speed \(\xi_+\), with
\[
\boxed{\gamma(\xi_+)=\frac{K}{B}(1+\eta)},\qquad
\lim_{\xi\to\infty}\gamma(\xi)=\frac{K}{B}.
\]
Thus optimal finite-speed adjustment beats arbitrarily fast network adjustment by the exact multiplicative factor \(1+\eta\), which lies strictly between one and two and can approach two. Every sufficiently small nonstationary perturbation in the focus interval has infinitely many, decaying crossings of the endemic prevalence level \(y_*\), although there are no nonconstant periodic solutions.

## Assumptions and scope

The state variables are the prevalence \(y\in[0,1]\) and normalized link density \(z\in[0,1]\). Time is scaled by the recovery rate. The link-breaking response is \(f_{\mathrm{br}}(y)=y\), the creation response is \(f_{\mathrm{cr}}(y)=1\), and the physical breaking rate is \(\zeta=\omega\xi\). The comparison varies both positive response rates in fixed proportion, **not** creation rate with breaking rate fixed. The parameters \(\tau>1\), \(\omega>0\), and \(\xi>0\) are arbitrary real numbers. Claims on convergence speed refer precisely to the real parts of the **endemic Jacobian eigenvalues**, not a nonlinear finite-time hitting-time optimum or the mixing of an underlying finite stochastic process.

## Proof

The endemic equilibrium equations give \(z=1/[\tau(1-y)]\) and \(1-z=\omega yz\), hence the unique positive solution \((y_*,z_*)\) above. Direct differentiation yields
\[
J_*=
\begin{pmatrix}
-\dfrac{\tau-1}{1+\omega}&\dfrac{\tau(\tau-1)(1+\omega)}{(\tau+\omega)^2}\\
-\dfrac{\omega\xi(\tau+\omega)}{\tau(1+\omega)}&-\dfrac{\tau\xi(1+\omega)}{\tau+\omega}
\end{pmatrix}.
\]
Its trace equals \(-A-B\xi\), and a cancellation gives \(\det J_*=K\xi\). Therefore its characteristic polynomial is
\[
p_{\xi}(\lambda)=\lambda^2+(A+B\xi)\lambda+K\xi.
\]
In particular all eigenvalues have negative real parts. Since
\[
AB=\frac{K\tau}{\tau+\omega}=K(1-\eta^2),
\]
the discriminant factors as
\[
\begin{aligned}
\Delta(\xi)&=(A+B\xi)^2-4K\xi\\
&=B^2(\xi-\xi_-)(\xi-\xi_+).
\end{aligned}
\]
This proves the sharp focus interval. At the endpoints the off-diagonal Jacobian entries remain nonzero, so the repeated eigenvalue has a nontrivial Jordan block (it is not a scalar matrix).

For \(\Delta(\xi)>0\), the slower positive decay rate \(\gamma\) solves
\[
\gamma^2-(A+B\xi)\gamma+K\xi=0.
\]
Implicit differentiation, using that the slower root is the smaller root, gives
\[
\gamma'(\xi)=\frac{K-B\gamma(\xi)}{\sqrt{\Delta(\xi)}}.
\]
The quantity \(K/B\) is never a real decay root because substituting it into the last quadratic yields \(K(K-AB)/B^2>0\). Below \(\xi_-\) the slower root is less than \(K/B\), as follows by continuity from \(\gamma(\xi)\to0\) when \(\xi\to0^+\). Above \(\xi_+\) it is greater than \(K/B\), as is seen at \(\xi_+\), where \(\gamma=(K/B)(1+\eta)\). Thus the spectral exponent increases strictly below \(\xi_-\), decreases strictly above \(\xi_+\), and on the focus interval equals \((A+B\xi)/2\), which increases strictly. Continuity at the two endpoints proves unique global optimality at \(\xi_+\). Dividing the characteristic polynomial by \(\xi\) and taking \(\xi\to\infty\) gives the finite slow decay root \(K/B\), proving the ratio formula.

In the focus interval, a real nonsingular linear change of coordinates transforms the linear part into \(-\gamma I+\nu R\), where \(\nu>0\) and \(R\) is planar quarter-turn rotation. In polar coordinates for the transformed nonlinear vector field, \(\dot r=-\gamma r+O(r^2)\) and \(\dot\theta=\nu+O(r)\). For any sufficiently small nonzero initial displacement, \(r(t)\to0\) while \(\theta(t)\) winds without bound. Each revolution crosses the line corresponding to \(y=y_*\); hence the exact nonlinear prevalence crosses its endemic level infinitely often, with amplitude tending to zero. This does not assert periodic solutions.

## Verification

The accompanying `verify.py` uses symbolic differentiation of the original vector field and checks the fixed point, characteristic polynomial, determinant cancellation, and boundary formulas. It also executes 180 independent exact-rational Jacobian comparisons on a rectangular parameter grid. For the exact example \(\tau=3\), \(\omega=1\), one has
\[
\xi_-=\frac29,\quad\xi_+=2,\quad\gamma(2)=2,
\quad \lim_{\xi\to\infty}\gamma(\xi)=\frac43.
\]
At \(\xi=2\) the Jacobian is \(\begin{psmallmatrix}-1&3/4\\-4/3&-3\end{psmallmatrix}\), with a single eigenvalue \(-2\) and a nontrivial Jordan block. At this exact optimum, generic linear perturbations carry a \(t e^{-2t}\) factor; the statement optimizes the spectral exponent rather than a uniform constant-times-\(e^{-2t}\) bound.

## Relationship to prior work

Achterberg and Sensi introduced and analyzed this single-population adaptive SIS model in a preprint publicly released on 2022-09-02 (arXiv:2209.01224; journal 2023). Their Section 4.2 gives the endemic equilibrium and stability for the prevalence-proportional breaking example, with an illustration of spiral behavior, while their Sections 3 and 5 establish stability and slow/fast network-dynamics facts. Their accessible complete article does not state the exact two-boundary node/focus interval, the uniquely rate-optimal finite response speed, or the explicit ratio to infinitely fast adjustment. The multigroup extension by Achterberg, Sensi, and Sottile (arXiv:2407.17639, 2024) analyzes heterogeneous communities, existence/stability and periodic behaviors, not this single-population spectral-speed optimization. Earlier G-ASIS work (2020) studies link-update mechanisms and epidemic thresholds, rather than this exact local-rate optimum. Standard planar spectral calculus underlies the derivation, but the uniform all-parameter sharp tuning law and its epidemiological interpretation are specific to this model.

## Limitations

The result concerns deterministic mean-field dynamics, not the exact finite-population Markov SIS chain. It does not optimize outbreak peak size, total cases, nonlinear convergence-time prefactors, or intervention cost. The upper critical point is defective, so polynomial transient factors may matter at finite times. Oscillations are damped crossings, not persistent periodic epidemic waves. Literature searches and inspected materials did not identify a covering result, but non-indexed or inaccessible treatments may exist. Independent external validation has not been performed.

## References

1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224, first posted 2022-09-02, https://arxiv.org/abs/2209.01224; *Nonlinear Dynamics* 111 (2023), https://doi.org/10.1007/s11071-023-08498-4.
2. M. A. Achterberg, M. Sensi, and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639, first posted 2024-07-24, https://arxiv.org/abs/2407.17639.
3. M. A. Achterberg, J. L. A. Dubbeldam, C. J. Stam, and P. Van Mieghem, *Classification of link-breaking and link-creation updating rules in susceptible-infected-susceptible epidemics on adaptive networks*, *Physical Review E* 101 (2020), 052302, https://doi.org/10.1103/PhysRevE.101.052302.
