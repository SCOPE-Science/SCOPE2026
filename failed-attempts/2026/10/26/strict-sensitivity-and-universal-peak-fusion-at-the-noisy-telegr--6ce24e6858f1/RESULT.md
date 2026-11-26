# Strict sensitivity and universal peak fusion at the noisy telegraph-trap transition

## Finding

For the established two-to-one-mode transition of a thermally diffusing, harmonically confined run-and-tumble particle, the critical **dimensionless thermal variance is a strictly decreasing smooth function of the tumbling-to-trap rate**, and its derivative has an exact, strictly negative covariance formula. The two off-center density peaks approach zero with a **parameter-independent square-root coefficient**: for each fixed \(0<q<1\), their positive location obeys
\[
 m_q(\delta)=\sqrt{3(\delta_c(q)-\delta)}+o\!\left(\sqrt{\delta_c(q)-\delta}\right),\qquad \delta\uparrow\delta_c(q).
\]
The existence and implicit equation of the phase boundary, its endpoint asymptotics, and the Gaussian-convolution stationary density are published results, not claimed as new. The contributions assessed here are the exact strict sensitivity law, a global proof of nondegeneracy at every transition point, and the universal leading peak-fusion coefficient.

## Assumptions and scope

Let \(h,v,D,\rho>0\). Consider the stationary solution of \(dX_t=(-hX_t+v\sigma_t)dt+\sqrt{2D}\,dW_t\), where \(\sigma_t\in\{-1,1\}\) flips at rate \(\rho\), independently of Brownian motion. Use the normalized coordinate \(Y=hX/v\), normalized switching rate \(q=\rho/h\), and normalized thermal variance \(\delta=Dh/v^2\). Write \(p_{q,\delta}\) for its stationary density. The known representation is
\[
 Y\overset{d}{=}U_q+\sqrt\delta Z,\quad Z\sim N(0,1),\quad \Pr(U_q\in du)=\frac{(1-u^2)^{q-1}}{B(1/2,q)}\mathbf1_{(-1,1)}(u)du,
\]
with independent terms. Here \(B\) is Euler's beta function. For \(0<q<1\), define \(z_q>0\) by the unique root
\[
 2z_q\,\mathbb E_{\pi_{q,z_q}}[T]=1,\qquad
 \pi_{q,z}(dt)=\frac{t^{-1/2}(1-t)^{q-1}e^{-zt}}{\int_0^1 s^{-1/2}(1-s)^{q-1}e^{-zs}ds}\,dt,\quad 0<t<1,
\]
and set \(\delta_c(q)=1/(2z_q)\). The implicit equation itself coincides with the known central-curvature criterion. For all \(q\in(0,1)\), the new exact identity is
\[
 \boxed{\frac{d\delta_c}{dq}=
 \frac{\operatorname{Cov}_{\pi_{q,z_q}}\!\left(T,\log(1-T)\right)}
 {1-2z_q^2\operatorname{Var}_{\pi_{q,z_q}}(T)}<0.}
\]
Both numerator and denominator are finite; numerator is strictly negative and denominator strictly positive. The asymptotic for \(m_q\) is for fixed \(q\) as \(\delta\) approaches the known critical value from below, not a uniform two-parameter limit.

## Proof

**Stationary convolution.** Solving the stable linear equation from an infinite stationary past splits it into an independent telegraph-driven convolution and a Gaussian Ornstein--Uhlenbeck convolution with variance \(D/h\) in the original units. The normalized telegraph convolution has the stated symmetric beta density, by the stationary current equations of the noiseless run-and-tumble model. This recovers the established formula and makes no claim of originality for it.

**A unique simple curvature crossing.** Let
\[
 F_q(z)=\int_{-1}^{1}(1-u^2)^{q-1}e^{-zu^2}du
 =B(1/2,q)\,{}_1F_1\!\left(\tfrac12;q+\tfrac12;-z\right),\qquad G_q(z)=\sqrt z F_q(z).
\]
Here \({}_1F_1\) is the confluent hypergeometric function. The Kummer equation gives the *exact* ordinary differential equation
\[
 zG_q''+(z+q-\tfrac12)G_q'+\frac{1-q}{2z}G_q=0.
\]
For every \(0<q<1\), \(G_q>0\), and at every zero of \(G_q'\),
\[
 G_q''(z)=-\frac{1-q}{2z^2}G_q(z)<0.
\]
Thus every stationary point of \(G_q\) is a strict local maximum. At small positive \(z\), \(G_q'(z)>0\). Watson's expansion at infinity gives \(G_q(z)=\sqrt\pi\,[1+(1-q)/(2z)+O(z^{-2})]\), with differentiable remainder, and therefore \(G_q'(z)<0\) for large \(z\). Hence there exists exactly one critical point \(z_q\), and it is a simple strict maximum. The central curvature of \(p_{q,\delta}\) has sign opposite to \(G_q'(z)\) for \(z=(2\delta)^{-1}\), so this is the unique, transverse central-curvature transition. At \(q\ge1\), the noiseless beta density is unimodal (uniform when \(q=1\)); its Gaussian convolution has no off-center modal transition.

**Strict sensitivity.** Under \(\pi_{q,z}\), denote \(\mu=\mathbb E[T]\) and \(V=\operatorname{Var}(T)\). The central-curvature equation becomes \(H(q,z)=2z\mu-1=0\). The exact exponential-family derivatives are
\[
 \partial_q\mu=\operatorname{Cov}(T,\log(1-T))<0,
 \qquad \partial_z\mu=-V.
\]
The strict inequality follows because \(T\) increases while \(\log(1-T)\) strictly decreases, and \(\pi_{q,z}\) is nondegenerate. At the root,
\[
 \partial_z H=2\mu-2z_qV=\frac{1-2z_q^2V}{z_q}>0.
\]
To prove the last inequality independently, observe the algebraic relation \(G_q'(z)=-G_q(z)H(q,z)/(2z)\); at its simple strict maximum \(G_q''(z_q)<0\), hence \(\partial_z H(q,z_q)>0\). The implicit-function theorem now gives a smooth \(z_q\), strictly increasing with \(q\), and differentiation of \(\delta_c(q)=(2z_q)^{-1}\) gives exactly the boxed covariance sensitivity formula.

**Universal peak merger.** Define \(p_\delta=p_{q,\delta}\) at a fixed \(q\in(0,1)\). As a Gaussian convolution it solves the heat equation \(\partial_\delta p_\delta=\tfrac12\partial_y^2 p_\delta\). Nondegeneracy of the curvature crossing and the orientation of its sign imply
\[
 p_{\delta_c}''(0)=0,\qquad p_{\delta_c}^{(4)}(0)=2\partial_\delta p_\delta''(0)|_{\delta_c}<0.
\]
All derivatives are analytic for positive \(\delta\). Symmetry and Taylor expansion give
\[
 \frac{p_\delta'(y)}{y}=\frac{\delta-\delta_c}{2}p_{\delta_c}^{(4)}(0)+\frac{y^2}{6}p_{\delta_c}^{(4)}(0)
 +O\!\left((\delta-\delta_c)^2+|\delta-\delta_c|y^2+y^4\right).
\]
The analytic implicit-function theorem in \(y^2\) yields a unique small positive noncentral stationary point for \(\delta<\delta_c\), at \(y^2=3(\delta_c-\delta)+O((\delta_c-\delta)^2)\). It is a strict local maximum (the center is then a local minimum). Taking square roots proves the stated coefficient. The already published global phase diagram identifies these local peaks as the symmetric noncentral modes; that global classification is not claimed here as a new discovery.

## Verification

The supplied standalone `check.py` computes the hypergeometric curvature root using a bracketed scalar solver. Independent Gauss--Jacobi quadrature computes second and fourth position-density derivatives. For six representative rates \(q\), it verifies the curvature sign change, zero critical curvature, and negative quartic curvature. At \(q=1/2\), four successively smaller critical offsets test convergence of the mode location to \(\sqrt{3(\delta_c-\delta)}\); the observed ratios approach one. A separate endpoint-aware quadrature evaluates the exact derivative formula for five \(q\) values and compares it against finite differences, with maximal absolute discrepancy less than \(6\times10^{-8}\). The analytic proof, not these finite tests, establishes the quantified conclusion.

For reproduction with Python, NumPy and SciPy installed, run `python check.py`. The code has no external data dependency.

## Relationship to prior work

Sabhapandit--Majumdar (arXiv:2404.02480, first public 2024-04-03), Section 4.1, already gives the beta--Gaussian stationary law, its hypergeometric curvature criterion, and a phase diagram. Frydel (arXiv:2207.08695), Section III, studies related Gaussian-smoothed confined active-particle distributions and illustrates thermal flattening. Guéneau--Majumdar--Schehr (arXiv:2602.08436, 2026), Section V.A.1, explicitly determines the same critical curve and its *logarithmic near-endpoint asymptotic*, which is prior coverage rather than a new conclusion here. Paoluzzi--Puglisi--Angelani (arXiv:2404.16955) analyzes closely related harmonic run-and-tumble thermodynamics. The new statements here concern a strict global derivative with its positive-denominator certificate and a nondegenerate universal peak-fusion amplitude. Neither is explicitly given in the inspected primary sections. A general heat-equation pitchfork theorem could imply the coefficient in hindsight; the model-specific nondegeneracy and sensitivity are therefore essential to the single combined result.

## Limitations

Only the one-dimensional symmetric telegraph model with positive Gaussian thermal diffusion is covered. The result is stationary and one-point, not a trajectory-level irreversibility statement. There is no claim of a new critical curve, new zero-noise transition, or new logarithmic endpoint asymptotic. The universal fusion coefficient applies at fixed interior switching rate, and neither uniformity as \(q\to0,1\) nor behavior under asymmetric switching is proved. Strict monotonicity is established for this beta-family thermal convolution, not arbitrary active-force laws. Publication-priority searches cannot exclude an implicit treatment of the sensitivity/merger formula in less directly indexed literature; independent validation has not been performed.

## References

- S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480 (first posted 2024-04-03), Section 4.1.
- D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, arXiv:2207.08695 (2022), particularly Sec. III.
- M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026), Section V.A.1.
- D. Paoluzzi, A. Puglisi, and L. Angelani, *Entropy production of run-and-tumble particles*, arXiv:2404.16955 (2024).
