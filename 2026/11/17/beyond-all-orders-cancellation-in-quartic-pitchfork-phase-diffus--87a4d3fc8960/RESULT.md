# Beyond-all-orders cancellation in quartic pitchfork phase diffusion

## Finding

For the stationary noisy pitchfork and its integrated phase,
\[
 dW_t=(RW_t-gW_t^3)\,dt+\sqrt{2T}\,dB_t,\qquad
 \Phi_t-\Phi_0=c\int_0^tW_s\,ds,
\]
with \(g,T>0\), \(R\in\mathbb R\), and real \(c\), write \(\rho=R/\sqrt{gT}\). There is a finite, positive dimensionless phase-variance function \(\mathcal F(\rho)\) satisfying
\[
 \lim_{t\to\infty}\frac{\operatorname{Var}(\Phi_t-\Phi_0)}{t}
 =\frac{c^2}{g}\mathcal F(\rho).
\]
Our main result is the **all-orders cancellation theorem**: for each integer \(N\ge1\), as \(\rho\to+\infty\),
\[
 \boxed{\mathcal F(\rho)=\sqrt2\,\pi\,e^{\rho^2/4}\bigl(1+O_N(\rho^{-2N})\bigr).}
\]
In particular, *every algebraic correction coefficient* to the normalized Kramers-scale phase diffusivity vanishes, despite the nonzero algebraic corrections to the well partition function and to the saddle integral separately. The implicit constants may depend on \(N\); no exponentially small uniform error bound is asserted.

The underlying integral-relaxation-time representation for this quartic diffusion is classical and is **not** claimed as new. The new conclusion is the matching of the complete two formal Laplace series, and thus the cancellation at every algebraic order for this specific *unnormalized integrated position covariance* (the phase-variance rate).

## Assumptions and scope

All stochastic integrals are Itô. The two-sided driving Brownian motion is standard, and \(W_0\) has the unique stationary probability distribution; \(\Phi_0\) is any fixed angle lift or constant. The phase \(\Phi\) is unwrapped. If \(c=0\), its additional variance vanishes trivially. No independent intrinsic phase noise is included. The asymptotic regime fixes \(g,T,c\) and sends \(R/\sqrt{gT}\to+\infty\), equivalently it can be realized with other positive parameter scalings having that same ratio.

In dimensionless variables \(X=(g/T)^{1/4}W\) and \(s=\sqrt{gT}\,t\), the stationary diffusion is
\[
 dX_s=(\rho X_s-X_s^3)\,ds+\sqrt2\,d\widetilde B_s,
 \quad V_\rho(x)=x^4/4-\rho x^2/2,
 \quad \pi_\rho(dx)=Z_\rho^{-1}e^{-V_\rho(x)}dx,
\]
where \(Z_\rho=\int_{\mathbb R}e^{-V_\rho(x)}dx\).

## Proof

**1. The phase variance as a reversible diffusion energy.** Define
\[
 J_\rho(x)=\int_x^\infty y e^{-V_\rho(y)}dy
 =\frac{\sqrt\pi}{2}e^{\rho^2/4}
 \operatorname{erfc}\!\left(\frac{x^2-\rho}{2}\right).
\]
The identity holds also for negative \(x\), by oddness of the integrand \(y e^{-V_\rho(y)}\). Let \(L_\rho=\partial_x^2-V_\rho'\partial_x\). The derivative
\[
 u_\rho'(x)=e^{V_\rho(x)}J_\rho(x)
\]
solves \(-(L_\rho u_\rho)(x)=x\); indeed \((e^{-V_\rho}u_\rho')'=-x e^{-V_\rho}\). Its stationary Dirichlet energy is finite: the complementary-error-function bound at large \(|x|\) gives \(u_\rho'(x)=O(|x|^{-2})\), while \(\pi_\rho\) has quartic tails. Itô's formula, stationary \(L^2\) integrability of \(u_\rho(X_s)\), and martingale orthogonality yield the asymptotic phase-variance rate
\[
 \mathcal F(\rho)=2\int (u_\rho')^2\,d\pi_\rho
 =\frac2{Z_\rho}\int_{\mathbb R}e^{V_\rho(x)}J_\rho(x)^2dx.
 \tag{1}
\]
A standard proof uses the decomposition \(\int_0^sX_rdr=u_\rho(X_0)-u_\rho(X_s)+\sqrt2\int_0^su_\rho'(X_r)d\widetilde B_r\), whose boundary term is bounded in \(L^2\) independently of \(s\). The error in variance divided by \(s\) then tends to zero by Cauchy–Schwarz. Finally, the physical time and amplitude scalings give \(c^2/g\) times (1).

**2. Same complete expansion at the barrier and in the wells.** Set \(\lambda=\rho>0\) and \(Q=\lambda^2/4\). Introduce the coefficients
\[
 a_k=\frac{(4k)!}{16^k(2k)!k!}\quad(k=0,1,\ldots),
 \qquad a_0=1,\ a_1=\frac34,\ a_2=\frac{105}{32}.
\]
Completing the square and substituting \(u=x^2\) yields the *exact* partition-function identity
\[
 Z_\lambda=e^Q\int_0^\infty u^{-1/2}e^{-(u-\lambda)^2/4}du.
\]
Expansion around the single Gaussian saddle \(u=\lambda\) and symmetric Gaussian moment integration give, for each fixed \(N\ge1\),
\[
 Z_\lambda=2\sqrt\pi\,e^Q\lambda^{-1/2}
 \left(\sum_{k=0}^{N-1}a_k\lambda^{-2k}+O_N(\lambda^{-2N})\right).\tag{2}
\]
For clarity, in the change \(u=\lambda+2z\), each even binomial coefficient of \((1+2z/\lambda)^{-1/2}\) integrates to
\[
 \binom{-1/2}{2k}2^{2k}
 \frac{\int z^{2k}e^{-z^2}dz}{\int e^{-z^2}dz}
 =\frac{(4k)!}{16^k(2k)!k!}=a_k.
\]
The apparent singular endpoint at \(u=0\) lies a Gaussian distance \(\lambda/2\) away and does not affect any algebraic order.

For the *barrier* integral with the fixed interior cutoff \(|x|\le\sqrt\lambda/2\), put
\[
 B_\lambda=\int_{-\sqrt\lambda/2}^{\sqrt\lambda/2}
   e^{-\lambda x^2/2+x^4/4}dx.
\]
Using \(x=\sqrt{2/\lambda}\,z\) and expanding \(e^{z^4/\lambda^2}\) under its Gaussian saddle gives
\[
 B_\lambda=\sqrt{2\pi}\,\lambda^{-1/2}
 \left(\sum_{k=0}^{N-1}\frac{1}{k!}
 \frac{\int z^{4k}e^{-z^2}dz}{\int e^{-z^2}dz}\lambda^{-2k}
 +O_N(\lambda^{-2N})\right)
 =\sqrt{2\pi}\,\lambda^{-1/2}
 \left(\sum_{k=0}^{N-1}a_k\lambda^{-2k}+O_N(\lambda^{-2N})\right).\tag{3}
\]
The expansions (2) and (3) thus agree coefficient-by-coefficient **to every order**, not merely at first order. Truncating at an arbitrary fixed order is justified by splitting into Gaussian saddle neighborhoods and their exponentially small tails. This also shows why the divergent formal series is only asymptotic, not a convergent identity.

**3. The numerator is the barrier integral to all algebraic orders.** For \(|x|\le\sqrt\lambda/2\), the exact error-function formula implies, uniformly,
\[
 J_\lambda(x)=\sqrt\pi e^Q
  \left(1+O(e^{-9\lambda^2/64}/\lambda)\right).
\]
On \(\sqrt\lambda/2<|x|\le\sqrt\lambda\), the potential is at most \(-7\lambda^2/64\), so this region contributes exponentially less to \(\int e^{V_\lambda}J_\lambda^2\) than the barrier saddle. On \(|x|\ge\sqrt\lambda\), the Gaussian complementary-error-function tail bound (Mills' bound) gives \(J_\lambda(x)\le C e^{-V_\lambda(x)}/(x^2-\lambda)\) away from the endpoint, with a bounded transition zone; consequently the remaining integral is at most \(e^Q\) times a polynomial in \(\lambda\), exponentially less than the leading \(e^{2Q}\lambda^{-1/2}\) barrier contribution. Thus for every fixed \(N\),
\[
 \int_{\mathbb R}e^{V_\lambda(x)}J_\lambda(x)^2dx
  =\pi e^{2Q}B_\lambda\bigl(1+O_N(\lambda^{-2N})\bigr).\tag{4}
\]
Insert (2)–(4) into (1). The two matching finite sums cancel in the quotient; because \(N\) was arbitrary,
\[
 \mathcal F(\lambda)=\frac{2\pi e^{2Q} B_\lambda}{Z_\lambda}
 \bigl(1+O_N(\lambda^{-2N})\bigr)
 =\sqrt2\pi e^Q\bigl(1+O_N(\lambda^{-2N})\bigr),
\]
as required.

## Verification

`verify_phase_diffusion.py` checks (i) six exact rational equalities between the two saddle series, (ii) numerical quadrature of the complete phase-diffusion formula at increasing positive barrier parameter, and (iii) the no-correction trend after division by \(\sqrt2\pi e^{\lambda^2/4}\). The checker is finite corroboration, **not** an infinite-order proof; all-orders validity is established by arbitrary-order Gaussian expansion and analytic tail bounds above. Run `python verify_phase_diffusion.py` in the extracted package directory. It requires Python 3, NumPy, and SciPy.

## Relationship to prior work

Shmakov and Littlewood (arXiv:2306.09524, first public 2023-06-15), equations (12) and (16), identify the integrated pitchfork covariance as a phase-diffusion contribution, establish universal scaling, and evaluate the crossover numerically. Weis and coauthors (arXiv:2207.11667) give the critical coefficient near \(0.97499\) and Kramers/telegraph interpretations. Kalmykov, Coffey, and Titov (Physica A 377 (2007), 412–420), especially equations (17), (21), and (23), already give a general exact integral formula for the same quartic position-correlation time and its *first* high-barrier asymptotic correction. Equation (1) is therefore classical under normalization and is cited as such.

The specific statement not identified in those inspected presentations is the **complete cancellation of every polynomial-order correction** for the *unnormalized* phase-diffusion rate, established here by an explicit match of the two full Laplace coefficient sequences. The first-order term in the previously published *normalized integral correlation time* need not vanish: dividing the unnormalized covariance integral by the stationary position variance creates a nonzero algebraic correction. In particular, a nonzero first-order correction to that normalized correlation time does not contradict the present theorem. The already known integral representation implies the result after additional asymptotic analysis; originality here is claimed only for that analysis and cancellation, not for the exact representation or the leading Kramers rate.

## Limitations

The error \(O_N(\lambda^{-2N})\) holds for each fixed \(N\) and does not claim a uniform constant in \(N\), an optimal exponentially small remainder, or an exact identity at finite parameter. Independent phase noise, phase-dependent amplitude coupling, nonlinear phase feedback, and nonsymmetric double wells are outside scope. Historical spectral/continued-fraction work supplies strong implicit coverage of the exact diffusion coefficient, and an unindexed derivation of the all-order cancellation remains a publication-priority risk. This finding has undergone self-review, not independent mathematical audit.

## References

1. S. Shmakov and P. B. Littlewood, *Coalescence of limit cycles in the presence of noise*, arXiv:2306.09524 (first submitted 2023-06-15), https://arxiv.org/abs/2306.09524.
2. C. Weis, M. Fruchart, R. Hanai, K. Kawagoe, P. B. Littlewood and V. Vitelli, *Exceptional points in nonlinear and stochastic dynamics*, arXiv:2207.11667 (2022), https://arxiv.org/abs/2207.11667.
3. Yu. P. Kalmykov, W. T. Coffey and S. V. Titov, *On the Brownian motion in a double-well potential in the overdamped limit*, Physica A 377 (2007), 412–420, https://doi.org/10.1016/j.physa.2006.11.067.
