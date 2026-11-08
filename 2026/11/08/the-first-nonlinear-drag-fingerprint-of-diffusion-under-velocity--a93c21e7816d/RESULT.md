# The first nonlinear-drag fingerprint of diffusion under velocity resetting

## Finding

Consider the one-dimensional inertial run-and-tumble model whose velocity is reset but whose active-force sign is **not** reset. The active force has values \(\pm\Sigma\), flips at rate \(\lambda\), and velocity resets to zero at an independent Poisson rate \(r\). A smooth odd drag law has local expansion \(g(v)=av+bv^3+O(v^5)\), with \(a>0\).

Writing \(D_g(r)=\lim_{t\to\infty}\operatorname{Var}(\int_0^t v_s\,ds)/(2t)\) for its effective spatial diffusion coefficient, and \(D_a(r)\) for the corresponding model with exactly linear drag \(g_a(v)=av\), the precise high-reset correction is

\[
D_g(r)=D_a(r)-\frac{6b\Sigma^4}{\lambda r^5}+O(r^{-6}),\qquad r\longrightarrow\infty,
\]

with the explicit linear benchmark

\[
D_a(r)=\frac{\Sigma^2}{(r+a)(r+a+2\lambda)}\left(\frac{2}{r+2a}+\frac{1}{2\lambda}\right).
\]

In particular, for the two drag laws examined in the motivating physical study, \(g_+(v)=\tan v\) and \(g_-(v)=\tanh v\), with common \(0<\Sigma<1\) and \(a=1\),

\[
D_{\tanh}(r)-D_{\tan}(r)=\frac{4\Sigma^4}{\lambda r^5}+O(r^{-6})>0
\]

for all sufficiently large \(r\). Thus both media have the same leading \(\Sigma^2/(2\lambda r^2)\) diffusivity, but the first term distinguishing these two drags with the same linear slope is exactly of fifth inverse-reset order and separates shear-thinning from shear-thickening by a universal signed coefficient.

## Assumptions and scope

Fix \(\lambda,\Sigma,a>0\). Let \(\sigma_t\in\{-1,+1\}\) be a stationary symmetric telegraph process flipping at rate \(\lambda\). Its Poisson clock is independent of a second clock of rate \(r>0\). Between velocity resets, \(\dot v_t=-g(v_t)+\Sigma\sigma_t\); at each second-clock event, only \(v_t\) is set to zero, while \(\sigma_t\) is unchanged. Position obeys \(\dot x_t=v_t\).

Assume \(g\) is odd and \(C^5\) in a neighborhood of the compact dynamically invariant velocity interval \([-V,V]\), with \(g'(v)\ge\kappa>0\) there, \(g(V)\ge\Sigma\), and \(g(-V)\le-\Sigma\). It has the Taylor expansion above near zero, where \(b=g'''(0)/6\). The comparison linear system uses the same telegraph and reset clocks. The interval can depend on the fixed parameters but not on \(r\). The tangent law is considered only on its accessible interval \([-\arctan\Sigma,\arctan\Sigma]\), and the hyperbolic-tangent law on \([-\operatorname{artanh}\Sigma,\operatorname{artanh}\Sigma]\), the latter requiring \(0<\Sigma<1\).

The asymptotics concern \(r\to\infty\) with \(\lambda,\Sigma,g\) fixed. No uniformity is asserted when the flipping rate, active-force amplitude, or drag parameters also vary with \(r\). The stationary process is uniquely obtained from the two-sided driving clocks: after a reset its velocity forgets the previous velocity, and the independent two-state sign chain is ergodic. The joint process mixes exponentially, so the Green–Kubo covariance integral and standard bounded-additive-functional central limit theorem apply.

## Proof

**1. Exact velocity-resolvent identity.** For the dynamics *without velocity resets* but with the same telegraph sign, define

\[
A_g(v,\sigma)=\int_0^\infty e^{-rt}\,\mathbb E^{(0)}_{v,\sigma}[v_t]dt,
\qquad A_0=A_g(0,+1).
\]

Let \(h_g(v,\sigma)=\int_0^\infty\mathbb E_{v,\sigma}[v_t]dt\), where the latter expectation includes resets. The first reset time is independent exponential of rate \(r\). By odd symmetry, \(h_g(0,\sigma)=\sigma h_g(0,+1)\), while the telegraph identity gives \(\mathbb E[\sigma_T\mid\sigma_0=\sigma]=r\sigma/(r+2\lambda)\). First-reset conditioning yields

\[
h_g(v,\sigma)=A_g(v,\sigma)+\frac{r}{r+2\lambda}\sigma h_g(0,+1).
\]

Evaluating at \((0,+1)\) and solving, one obtains the exact non-renewal identity

\[
h_g(v,\sigma)=A_g(v,\sigma)+\frac{rA_0}{2\lambda}\sigma.
\]

In the stationary joint law \(\pi_g\), symmetry gives \(\mathbb E_{\pi_g}v=0\). The Green–Kubo formula therefore becomes

\[
D_g(r)=\mathbb E_{\pi_g}[v A_g(v,\sigma)]+\frac{rA_0}{2\lambda}\,m_g,
\qquad m_g=\mathbb E_{\pi_g}[v\sigma].\tag{1}
\]

The sign-preserving nature of resetting is essential in this identity; resetting the telegraph force itself would lead to a different renewal law.

**2. Exact linear comparator.** If \(g_a(v)=av\), the no-reset resolvent is

\[
A_a(v,\sigma)=\frac{v}{r+a}+\frac{\Sigma\sigma}{(r+a)(r+2\lambda)},\qquad A_a(0,+1)=\frac{\Sigma}{(r+a)(r+2\lambda)}.
\]

The stationary generator applied to \(v\sigma\) and \(v^2\) gives

\[
m_a=\frac{\Sigma}{r+a+2\lambda},\qquad
q_a:=\mathbb E_{\pi_a}[v^2]=\frac{2\Sigma m_a}{r+2a}.
\]

Substitution into (1) simplifies to the stated closed formula for \(D_a(r)\). It has leading behavior \(\Sigma^2/(2\lambda r^2)\).

**3. Two independent local corrections.** Couple the nonlinear and linear velocities using the same stationary sign history and exactly the same velocity reset times. Write \(T\) for the backward age since the last reset at observation time zero. Then \(T\sim\mathrm{Exp}(r)\), independently of the sign trajectory. Both velocities start from zero at the previous reset. Since each drag opposes the velocity, \(|v_g|,|v_a|\le\Sigma T\). On the compact reachable interval, \(|g(v)-av|\le C|v|^3\). Variation of constants consequently gives, for every finite \(p\ge1\),

\[
\|v_g-v_a\|_{L^p}=O(r^{-4}),\qquad
\|v_g\|_{L^p}+\|v_a\|_{L^p}=O(r^{-1}).\tag{2}
\]

On the event of no sign flip during the backward age \(T\), the two velocities obey the same sign throughout the most recent cycle. The local ODE expansion gives \(\sigma_0(v_g-v_a)=-b\Sigma^3T^4/4+O(T^5)\). The probability of a sign flip conditional on \(T\) is at most \(\lambda T\), and the difference is bounded by \(CT^4\), so the flip-containing histories contribute only \(O(\mathbb ET^5)\). Exponentially rare large ages do not alter these estimates. Because \(\mathbb ET^4=24/r^4\),

\[
m_g-m_a=-\frac{6b\Sigma^3}{r^4}+O(r^{-5}).\tag{3}
\]

Similarly, starting the *no-reset* dynamics from \((0,+1)\), absence of a flip up to a short time \(t\) gives \(v_g(t)-v_a(t)=-b\Sigma^3t^4/4+O(t^5)\). Flipped histories have probability \(O(\lambda t)\) and contribute \(O(t^5)\) to the expectation. Integrating against \(e^{-rt}\) therefore yields

\[
A_g(0,+1)-A_a(0,+1)=-\frac{6b\Sigma^3}{r^5}+O(r^{-6}).\tag{4}
\]

Both factors of six come from the factorial moment of the exponential waiting time, not from a Gaussian approximation.

**4. The remaining resolvent term is one order smaller.** For a no-reset trajectory starting at \((v,\sigma)\) in the invariant interval, variation of constants and \(|v_t|\le|v|+\Sigma t\) give the resolvent comparison

\[
|A_g(v,\sigma)-A_a(v,\sigma)|
\le C\int_0^\infty e^{-rt}\int_0^t(|v|+\Sigma s)^3ds\,dt.
\]

For a stationary initial velocity this has \(L^p\)-order \(r^{-5}\). Changing the initial velocity from \(v_g\) to \(v_a\) changes the linear resolvent by \((v_g-v_a)/(r+a)\), also of \(L^p\)-order \(r^{-5}\). Since each velocity has \(L^p\)-order \(r^{-1}\) and each resolvent \(L^p\)-order \(r^{-2}\), Hölder's inequality and (2) prove

\[
\mathbb E_{\pi_g}[vA_g(v,\sigma)]-
\mathbb E_{\pi_a}[vA_a(v,\sigma)]=O(r^{-6}).\tag{5}
\]

**5. Assemble the coefficient.** By (1), (3), (4), and (5), together with \(m_a=\Sigma r^{-1}+O(r^{-2})\) and \(A_a(0,+1)=\Sigma r^{-2}+O(r^{-3})\),

\[
\begin{aligned}
D_g-D_a&=O(r^{-6})+\frac{r}{2\lambda}\{(A_g-A_a)m_a+A_a(m_g-m_a)+(A_g-A_a)(m_g-m_a)\}\\
&=-\frac{3b\Sigma^4}{\lambda r^5}-\frac{3b\Sigma^4}{\lambda r^5}+O(r^{-6})\\
&=-\frac{6b\Sigma^4}{\lambda r^5}+O(r^{-6}).
\end{aligned}
\]

Here \(A_g\) and \(A_a\) inside the braces are evaluated at \((0,+1)\). For tangent drag \(b=+1/3\); for hyperbolic-tangent drag \(b=-1/3\). Their difference therefore has the claimed positive coefficient \(4\Sigma^4/\lambda\).

## Verification

The companion `VERIFY.py` works solely with exact rational arithmetic and the Python standard library. It checks the linear Green–Kubo formula in two independent forms and computes the **exact first derivative at cubic-drag strength zero**, using stationary polynomial-moment equations and a distinct cubic Poisson-resolvent calculation. For several positive rational physical parameters and increasing reset rates, the rational scaled derivative approaches \(-6\Sigma^4/\lambda\), independently corroborating the fifth-order coefficient. The verifier also checks the two independent local factorial contributions to the coefficient and the shear-thinning versus shear-thickening sign. The infinite-rate result is established by the proof above; finite checks are not substituted for the asymptotic estimates.

Reproduce with `python3 VERIFY.py`. No simulation data or inaccessible datasets are required.

## Relationship to prior work

Howlader, Mondal and Das (2026) study the same velocity-only resetting model, including \(\tan\) and \(\tanh\) drags, and report the common \(r^{-2}\) diffusion scaling from numerical experiments. The present result adds an explicit **first drag-dependent coefficient** and proves that the two rheologies separate at inverse fifth order. Their original model, large-rate exponent, and numerically observed transport properties are not claimed as new here.

Olsen and Löwen (2024) derive a general renewal representation for partial resetting when the full non-position environment is renewed; their Section 2 explicitly requires resetting environmental evolution for that convolution structure. The telegraph sign in this theorem survives velocity resets. Hence the old renewal formula does not directly give (1), (3), or the nonlinear-drag coefficient. The present derivation respects the persistent hidden sign.

## Limitations

This is an asymptotic theorem, not an explicit stationary density for nonlinear drag. The constants in the error term can depend on the fixed drag, forcing amplitude, and flipping rate; no joint \(r,\lambda\) limit is asserted. The result does not establish finite-rate diffusion ordering for all rates, nor an optimal rate. Smoothness, oddness, and a compact strongly dissipative accessible velocity region are used essentially in the displayed error bounds. Independent publication-priority assessment has not been performed; a more general unlocated perturbation theorem could potentially entail the coefficient.

## References

1. S. Howlader, S. Mondal and P. Das, *Velocity Resetting of Inertial Run-and-Tumble Particles in Non-Newtonian Media: Velocity Distribution, Diffusion and First-Passage Time*, arXiv:2606.00560v1 (first public May 30, 2026), https://arxiv.org/abs/2606.00560 . Especially model equations and Sections 2–4.
2. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (2024), https://arxiv.org/abs/2401.12685 . Especially Sections 2 and 3.1 and the environmental-renewal hypothesis.
