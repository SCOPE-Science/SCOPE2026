# False controllability under upwind transport: sharp exponential energy and a Gaussian arrival layer

## Finding

**Theorem (quantitative false controllability and its arrival crossover).** Fix an advection speed \(v>0\), a common actuator/observation interval length \(a>0\), and an intervening gap \(g>0\). For a sequence of positive mesh widths \(h\downarrow0\) satisfying \(A=a/h\in\mathbb N\) and \(n=g/h\in\mathbb N\), use the first-order *semidiscrete upwind* scheme and the fixed indicator actuator and target defined below. Write \(G_h(T)\) for its scalar terminal target controllability Gramian and \(G(T)\) for the continuum Gramian. Put \(T_*=g/v\).

1. The continuum is **not target controllable** for \(0<T\le T_*\), since \(G(T)=0\). Nevertheless \(G_h(T)>0\) for every \(h>0\) and \(T>0\): every discretized system is target controllable.
2. For every fixed \(0<T<T_*\), writing \(\theta=vT/g\in(0,1)\) and \(I(T)=g(\theta-1-\log\theta)>0\),
   \[
   G_h(T)\sim
   \frac{T\theta^2}{4\pi g^2(1-\theta)^5}\,
   h^4\exp\!\left(-\frac{2I(T)}h\right).
   \]
   Thus the minimum input energy to attain a unit terminal target output equals \(G_h(T)^{-1}\) and has the corresponding sharp, exponentially diverging reciprocal asymptotic.
3. Define the standard normal density \(\varphi(s)=e^{-s^2/2}/\sqrt{2\pi}\), distribution function \(\Phi(s)=\int_{-\infty}^s\varphi(z)\,dz\), and \(H(s)=\varphi(s)+s\Phi(s)\). For any fixed real \(s\), and \(T_h(s)=T_*+s\sqrt{gh}/v>0\),
   \[
   \lim_{h\downarrow0}\frac{G_h(T_h(s))}{h^{3/2}}
   =\frac{g^{3/2}}v\int_{-\infty}^{s}H(z)^2\,dz.
   \]
   In particular, at the exact physical arrival horizon,
   \[
   G_h(T_*)\sim
   \frac{g^{3/2}}v\frac{1-1/\sqrt2}{3\sqrt\pi}\,h^{3/2}.
   \]
4. For fixed \(T_*<T\le(g+a)/v\), the discrete Gramian converges to the strictly positive continuum value
   \[
   G_h(T)\longrightarrow G(T)=\frac{(vT-g)^3}{3v}.
   \]

The *subcritical exponential rate, its explicit prefactor, and the critical Gaussian layer* quantify the artificial target reachability caused solely by spatial upwinding. The leading subcritical and critical constants are independent of the fixed interval length \(a\); \(a\) only needs to remain positive as the mesh is refined.

## Assumptions and scope

On \((0,L)\), where \(L=2a+g\), consider rightward pure transport with zero inflow at the left boundary. On \(\mathcal H=L^2(0,L)\), the right-shift semigroup is
\[
(S(t)u)(x)=\begin{cases}u(x-vt),&x>vt,\\0,&x\le vt.\end{cases}
\]
The scalar actuator is \(b=\mathbf1_{(0,a)}\) and the scalar output is \(Cz=\langle z,c\rangle_{L^2}\) with \(c=\mathbf1_{(a+g,2a+g)}\). The continuum state equation is \(\dot z=\mathcal Az+b\,u(t)\), the measured output is \(Cz\), and both initial state and target-output displacement are interpreted in the usual terminal reachability sense. The continuum impulse response is \(q(t)=CS(t)b\) and \(G(T)=\int_0^Tq(t)^2\,dt\). Only the controllability of this **one scalar target output**, not full-state controllability, is asserted.

There are \(M=2A+n\) equal-width cells. Index coordinates by \(j=0,\ldots,M-1\), and set \(S_he_j=e_{j+1}\) for \(j<M-1\), \(S_he_{M-1}=0\). The upwind generator is \(A_h=(v/h)(S_h-I)\). The actuator column \(b_h\) equals one on cells \(0,\ldots,A-1\), zero elsewhere; the observer is \(C_hz=h\sum_{j=A+n}^{2A+n-1}z_j\). Thus both are **cell-average discretizations of fixed continuum indicator functions**, with the observation using the correct mass matrix \(hI\). Define \(q_h(t)=C_he^{tA_h}b_h\) and \(G_h(T)=\int_0^Tq_h(t)^2dt\). There is no time discretization, physical diffusion, damping, nonzero initial state, or added regularization.

## Proof

**Continuum travel time.** The transported actuator occupies \((vt,vt+a)\), whereas the target occupies \((a+g,2a+g)\). Their overlap is zero through \(t=T_*\). For \(T_*<t\le (g+a)/v\), its length equals \(vt-g\). Hence \(q(t)=(vt-g)_+\) through that time, giving the asserted continuum Gramians.

**Exact discrete response.** Matrix nilpotence gives
\[
e^{tA_h}=e^{-z}\sum_{k=0}^{M-1}\frac{z^k}{k!}S_h^k,
\qquad z=vt/h.
\]
For a Poisson random variable \(N_z\) of mean \(z\), let \(\psi_A(r)=r\) for integers \(1\le r\le A\), \(\psi_A(r)=2A-r\) for \(A<r<2A\), and \(\psi_A(r)=0\) otherwise. Counting source/target cell pairs separated by \(k\) shows
\[
q_h(t)=h\,\mathbb E\,\psi_A(N_z-n)
=h e^{-z}\sum_{r=1}^{2A-1}\min(r,2A-r)\frac{z^{n+r}}{(n+r)!}.
\]
The term \(r=1\) is strictly positive whenever \(t>0\), hence \(G_h(T)>0\) for all \(T>0\). The minimum-norm control for a scalar terminal displacement \(y=1\) is \(u_*(t)=q_h(T-t)/G_h(T)\), with squared \(L^2(0,T)\)-norm \(1/G_h(T)\) by Cauchy--Schwarz.

**Sharp prearrival asymptotics.** Fix \(0<t<T_*\) and write \(\rho=vt/g<1\) and \(n=g/h\). Then \(z=n\rho\) and, for every fixed \(r\ge1\),
\[
\frac{\Pr(N_z=n+r)}{\Pr(N_z=n)}\longrightarrow\rho^r.
\]
On each compact time interval below \(T_*\), the probability ratio is bounded by \(\rho_0^r\) for some \(\rho_0<1\); the triangular coefficient is at most \(r\). Dominated convergence in the finite sum, uniformly on these intervals, yields
\[
q_h(t)\sim h\Pr(N_{n\rho}=n)\sum_{r\ge1}r\rho^r
=\frac{h\rho}{(1-\rho)^2}\Pr(N_{n\rho}=n).
\]
Stirling's formula gives \(\Pr(N_{n\rho}=n)\sim(2\pi n)^{-1/2}\exp[-n(\rho-1-\log\rho)]\), so
\[
q_h(t)\sim\frac{h^{3/2}\rho}{\sqrt{2\pi g}(1-\rho)^2}
\exp[-I(t)/h],\quad I(t)=vt-g-g\log(vt/g).
\]
Here \(I'(t)=v-g/t<0\) for \(t<T_*\). Splitting \(\int_0^Tq_h^2\) at any \(T-\delta>0\), the earlier part is exponentially negligible compared with the endpoint contribution (use the Poisson Chernoff bound). The one-sided Laplace formula gives
\[
\int_0^Tq_h(t)^2dt\sim
\frac{h}{2(g/T-v)}\frac{h^3\theta^2}{2\pi g(1-\theta)^4}e^{-2I(T)/h},
\]
which simplifies to the coefficient stated in item 2. This is a full asymptotic equivalence, not merely a logarithmic large-deviation estimate.

**Central-limit arrival layer.** For \(t_h(s)=T_*+s\sqrt{gh}/v\), the Poisson mean is \(n+s\sqrt n\). For fixed \(s\), the centered/normalized Poisson law converges to \(Z+s\), with \(Z\) standard normal; its uniformly bounded second moments ensure convergence of the positive-part expectation. Since \(A=a/h\) grows faster than \(\sqrt n\), the difference between \(\psi_A(N_z-n)\) and \((N_z-n)_+\) has exponentially small expectation in this window. Consequently,
\[
\frac{q_h(t_h(s))}{\sqrt{gh}}\longrightarrow
\mathbb E(Z+s)_+=\varphi(s)+s\Phi(s)=H(s).
\]
The convergence is locally uniform in \(s\). On the negative half-line, the Poisson Chernoff bound and a moment bound for the positive excess give a uniform, integrable Gaussian-type domination after the same rescaling, with the distant region \(t\le(1-\epsilon)T_*\) exponentially negligible. Using \(dt=\sqrt{gh}\,ds/v\) therefore gives the asserted integral crossover, with lower limit extending to \(-\infty\).

For the explicit critical constant, reflect the integration variable to get
\[
\int_{-\infty}^0H(s)^2ds
=\int_0^\infty[\varphi(w)-w\Phi(-w)]^2dw
=\frac{1-1/\sqrt2}{3\sqrt\pi}.
\]
The last identity follows by expanding the square, integrating the two cross terms by parts using \(\varphi'(w)=-w\varphi(w)\), and evaluating the resulting elementary Gaussian integrals.

**After arrival.** The upwind shift converges strongly in \(L^2\) to the transport shift for fixed time (alternatively, apply the law of large numbers to the exact Poisson formula). Thus \(q_h(t)\to q(t)\) pointwise. The contractive discrete semigroup and fixed input/output norms bound \(|q_h(t)|\le\|b\|_2\|c\|_2=a\). Dominated convergence on \([0,T]\) yields \(G_h(T)\to G(T)\) and item 4.

## Verification

The companion `checks/upwind_gramian_check.py` independently evaluates the exact Poisson sum and compares it with a direct matrix exponential on small grids. It checks the stated subcritical, critical, and moving-horizon asymptotic constants numerically and the Gaussian integral identity; the checks are finite diagnostics, not the proof of an infinite-mesh limit. Reproduce using `python checks/upwind_gramian_check.py` with Python, NumPy, and SciPy. All formulas and limit arguments above are self-contained.

## Relationship to prior work

Inoue and Sato (2026), Remark 2.3, explicitly exhibit the same separated-indicator right-shift configuration and its finite physical travel time. Their Sections 5.2 and 5.4 show qualitative false controllability caused by coarse-grid first-order upwinding in a two-dimensional flow; they do **not** state a sharp subcritical Gramian exponential/prefactor or a critical arrival-layer limit for this one-dimensional example. The present theorem quantifies exactly that mechanism for fixed physical actuator and observation intervals, including the resulting minimal-energy blowup.

Delarue and Lagoutière (2007/2011) provide a Markov-chain representation of upwinding and analyze its diffusive errors, including central-limit behavior. The Poisson representation here is a constant-velocity specialization of that established probabilistic viewpoint; it is **not** claimed as new. The new statement is the exact input-output controllability Gramian asymptotics, the sharp exponential prefactor, and the \(h^{3/2}\) arrival crossover. Standard Stirling, Poisson deviations, and Gaussian limits are proof ingredients rather than claimed discoveries.

## Limitations

The result concerns one spatial dimension, uniform first-order **semidiscrete** upwinding, one fixed indicator actuator/target pair of equal positive widths, constant positive advection speed, scalar terminal target controllability, and mesh sequences exactly aligned with the interval endpoints. The result does not assert analogous constants for arbitrary smooth/overlapping profiles, nonuniform grids, full-state controllability, physical diffusion, or fully discrete time integration. The convergence of \(G_h\) above arrival does not give a finite-mesh monotonicity guarantee. No independent mathematical validation is represented.

## References

1. D. Inoue and K. Sato, *Controllability Allocation Scores for Linear Infinite-Dimensional Systems*, arXiv:2610.28205 (first public version 2026-10-20), https://arxiv.org/abs/2610.28205 . In particular Remark 2.3 and Sections 5.2, 5.4.
2. F. Delarue and F. Lagoutière, *Probabilistic analysis of the upwind scheme for transport*, arXiv:0712.3217 (first public version 2007-12-19), https://arxiv.org/abs/0712.3217 . In particular Section 3, probabilistic representation and Gaussian fluctuations; published in *Archive for Rational Mechanics and Analysis* 199 (2011), 229--268.
