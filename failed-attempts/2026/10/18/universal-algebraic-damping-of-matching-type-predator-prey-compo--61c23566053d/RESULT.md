# Universal algebraic damping of matching-type predator–prey composition cycles

## Finding

For the deterministic four-population matching-type predator–prey model of Costa, Czuppon and Forien, the positive equal-type coexistence equilibrium attracts not only globally but with a sharp, parameter-explicit **algebraic composition envelope**. Whenever the initial two prey abundances are unequal or the initial two predator abundances are unequal, the squared, naturally weighted type imbalance is asymptotic to a universal constant divided by time. In contrast, an exactly type-balanced trajectory approaches equilibrium exponentially.

Define the equilibrium prey and predator densities per type by \(n>0\) and \(h>0\), and write \(c,\gamma,p,\rho>0\) for the prey competition, predator competition, predation and predator reproduction coefficients. Put

\[
\begin{aligned}
\mathcal E(t)&=\rho n\left(\frac{n_0(t)-n_1(t)}{n_0(t)+n_1(t)}\right)^2
+p h\left(\frac{h_0(t)-h_1(t)}{h_0(t)+h_1(t)}\right)^2,\\
\kappa&=\frac{(4c\gamma+p\rho)(c\rho n^2+\gamma p h^2)+4p\rho nh(cp+\gamma\rho)}{2\left[nh(4c\gamma-3p\rho)^2+16p\rho(cn+\gamma h)^2\right]}.
\end{aligned}
\]

Every strictly positive initial state with \((n_0-n_1,h_0-h_1)\ne(0,0)\) satisfies

\[
\boxed{\lim_{t\to\infty} t\,\mathcal E(t)=\kappa^{-1}.}
\]

The coefficient \(\kappa\) is strictly positive for every allowed parameter set. Thus the amplitude of phenotypic mismatch decays as \(t^{-1/2}\), rather than exponentially. The phase rotates with asymptotic angular speed \(\omega=\sqrt{p\rho nh}\); in polar coordinates for the two weighted imbalances, \(\theta(t)=\omega t+O(\log t)\).

For the admissible benchmark \(n=h=c=\gamma=p=\rho=1\) (equivalently, intrinsic prey and predator net growth rates \(3\) and \(1\)), the exact quantitative law is

\[
\lim_{t\to\infty}t\left[\left(\frac{n_0-n_1}{n_0+n_1}\right)^2+\left(\frac{h_0-h_1}{h_0+h_1}\right)^2\right]=\frac{65}{9}.
\]

## Assumptions and scope

The four abundances \(n_i(t),h_i(t)\), indexed by \(i\in\{0,1\}\), obey the deterministic, well-mixed ordinary differential equations

\[
\dot n_i=n_i\bigl(a-c(n_0+n_1)-ph_i\bigr),\qquad
\dot h_i=h_i\bigl(B-\gamma(h_0+h_1)+\rho n_i\bigr).
\]

All four initial abundances are strictly positive. Here \(a=b-d>0\) is the prey net intrinsic growth, and \(B=\beta-\delta\) is the predator net intrinsic growth (which need not be positive). Assume \(c,\gamma,p,\rho>0\) and that the unique equal-type coexistence equilibrium is strictly positive:

\[
n=\frac{2\gamma a-pB}{4c\gamma+p\rho}>0,
\qquad
h=\frac{\rho a+2cB}{4c\gamma+p\rho}>0.
\]

No stochastic finite-population approximation, mutation during the deterministic flow, delay or spatial heterogeneity is asserted. All asymptotic limits are at fixed positive model parameters as physical time \(t\to\infty\).

## Proof

**1. Global convergence and the stable-versus-neutral splitting.** Set \(N=n_0+n_1\), \(H=h_0+h_1\), \(x=(n_0-n_1)/N\), and \(y=(h_0-h_1)/H\). Direct quotient differentiation gives exactly

\[
\begin{aligned}
\dot N&=N\left(a-cN-\frac{pH}{2}(1+xy)\right),\\
\dot H&=H\left(B-\gamma H+\frac{\rho N}{2}(1+xy)\right),\\
\dot x&=-\frac{pH}{2}y(1-x^2),\\
\dot y&=\frac{\rho N}{2}x(1-y^2).
\end{aligned}
\]

The function

\[
V=\sum_{i=0}^{1}\bigl(n_i-n\log n_i\bigr)
+\frac{p}{\rho}\sum_{i=0}^{1}\bigl(h_i-h\log h_i\bigr)
\]

has derivative \(\dot V=-c(N-2n)^2-(p\gamma/\rho)(H-2h)^2\). Its positive-orthant sublevel sets are compact. On the derivative-zero set \(N=2n\), \(H=2h\), invariance forces \(xy=0\) at all times; the last two equations then force \(x=y=0\). LaSalle's principle therefore yields convergence of every positive solution to \((n,n,h,h)\). This global-convergence result is also Proposition 2.4 of the motivating paper, and is used here as a known premise. The exact symmetric plane \(x=y=0\) is invariant.

Write \(u=N-2n\), \(v=H-2h\), and rescale composition to

\[
X=\sqrt{\rho n}\,x,\qquad Y=\sqrt{ph}\,y,
\qquad \omega=\sqrt{p\rho nh}.
\]

The linearization in \((u,v,X,Y)\) is the direct sum of

\[
A=\begin{pmatrix}-2cn&-pn\\ \rho h&-2\gamma h\end{pmatrix},
\qquad
\begin{pmatrix}0&-\omega\\ \omega&0\end{pmatrix}.
\]

Because \(\operatorname{tr}A=-2(cn+\gamma h)<0\) and \(\det A=nh(4c\gamma+p\rho)>0\), the total-population directions are exponentially stable, while the composition directions have eigenvalues \(\pm i\omega\). Ordinary linear stability cannot determine the rate in the latter directions.

**2. Quadratic slaving of the total populations.** Near coexistence, the total-population equations have stable forcing

\[
\binom{\dot u}{\dot v}=A\binom uv+qXY+O\bigl((|u|+|v|)^2+(|u|+|v|)(X^2+Y^2)\bigr),
\quad q=\frac{2nh}{\omega}\binom{-p}{\rho}.
\]

The composition equations are

\[
\dot X=-\omega\left(1+\frac{v}{2h}\right)Y\left(1-\frac{X^2}{\rho n}\right),\qquad
\dot Y=\omega\left(1+\frac{u}{2n}\right)X\left(1-\frac{Y^2}{ph}\right).
\]

A smooth local center manifold is a graph \((u,v)=P_2(X,Y)+O((X^2+Y^2)^{3/2})\). Put \(\psi=(X^2-Y^2)/2\), \(\chi=XY\), and \(P_2=\alpha\psi+\eta\chi\) with column vectors \(\alpha,\eta\in\mathbb R^2\). At the linear rotation \(\dot X=-\omega Y\), \(\dot Y=\omega X\), one has \(\dot\psi=-2\omega\chi\), \(\dot\chi=2\omega\psi\). The center-manifold invariance equation, coefficient by coefficient, is

\[
2\omega\eta=A\alpha,\qquad -2\omega\alpha=A\eta+q.
\]

It has a unique solution, since \(A\) is Hurwitz:

\[
\alpha=-2\omega(A^2+4\omega^2I)^{-1}q,
\qquad \eta=-A(A^2+4\omega^2I)^{-1}q.
\]

**3. Angular averaging and strict damping.** Set \(E=X^2+Y^2\). Substituting the exact composition equations gives, on the center manifold,

\[
\dot E=\omega XY\left[\frac{(P_2)_1}{n}-\frac{(P_2)_2}{h}
+\frac{2X^2}{\rho n}-\frac{2Y^2}{ph}\right]+O(E^{5/2}).
\]

With \(X=\sqrt E\cos\theta\), \(Y=\sqrt E\sin\theta\), this is \(\dot E=E^2F(\theta)+O(E^{5/2})\), and \(\dot\theta=\omega+O(E)\). The two pure-composition quartics average to zero over one rotation, as does the \(\psi\chi\) term. Since \(\langle X^2Y^2\rangle=E^2/8\), the cycle-averaged radial coefficient is

\[
\langle F\rangle=\frac{\omega}{8}\left(\frac{\eta_1}{n}-\frac{\eta_2}{h}\right)=-\kappa.
\]

Inserting the explicit \(A,q\) and simplifying yields precisely the stated rational expression for \(\kappa\). An independent dissipative calculation follows from the Lyapunov function in Step 1: its center-manifold expansion is \(V=V_*+E/\rho+O(E^2)\), while its exact derivative is \(\dot V=-c u^2-(p\gamma/\rho)v^2\). Averaging those squares yields the identical positive coefficient

\[
\kappa=\frac{\rho c(\alpha_1^2+\eta_1^2)+p\gamma(\alpha_2^2+\eta_2^2)}{8}>0.
\]

The strict inequality follows because the forcing vector \(q\) is nonzero, so \(\alpha,\eta\) cannot both vanish. The rational formula also has strictly positive numerator and denominator.

Take a smooth periodic \(G\) satisfying \(\omega G'(\theta)=-\kappa-F(\theta)\), which is possible because the right side has zero mean. The corrected energy \(\widetilde E=E+E^2G(\theta)\) then obeys

\[
\dot{\widetilde E}=-\kappa\widetilde E^2+o(\widetilde E^2).
\]

Therefore \((1/\widetilde E)'\to\kappa\), giving \(tE(t)\to\kappa^{-1}\). The usual exponentially attracting center-manifold foliation transfers this asymptotic from the reduced flow to all positive solutions that are not exactly type-balanced. Indeed, along any such solution \(E>0\), and the exact equations imply \(|(\log E)'|\le C(|u|+|v|+E)\to0\). Thus the nonzero composition cannot converge exponentially and cannot lie in the strong-stable fiber of the equilibrium; exponentially small transverse tracking errors are negligible compared with \(E\). Finally \(\dot\theta=\omega+O(E)+O(e^{-\eta_0t})\) for some \(\eta_0>0\), which integrates to \(\theta(t)=\omega t+O(\log t)\). For exactly balanced data \(E\equiv0\), and exponential convergence follows from the stable matrix \(A\).

## Verification

The standalone `verify.py` expands the original four equations into the exact \((N,H,x,y)\) equations, verifies both quadratic center-manifold invariance identities symbolically, derives and simplifies the damping coefficient, and checks the benchmark \(\kappa=9/65\) with exact arithmetic. Its finite-time diagnostics integrate the original four equations under two positive parameter sets and compare growing values of \(tE(t)\) with the corresponding analytic limits. Use `python verify.py` after installing `requirements.txt`. These numerical trajectories support the calculation only; the asymptotic theorem is proved above.

## Relationship to prior work

Costa, Czuppon and Forien (arXiv:2609.04834, initially public September 4, 2026) establish the four-type deterministic model and global convergence in the strictly positive coexistence regime, including Proposition 2.4 and its Lyapunov proof in Appendix A.2. Their proof does not specify the composition relaxation exponent, the strictly positive cubic damping coefficient, or its exact dependence on all ecological parameters. Those quantitative conclusions are the new claim; global convergence and the model itself are not. Different classical predator–prey and coevolutionary models study persistent or stochastic oscillations, but their premises do not directly establish this deterministic four-type coefficient.

## Limitations

This result concerns deterministic dynamics with all four components initially positive, and with strictly positive equal-type coexistence densities. It does not quantify finite-population noise, diffusion approximations, time to stochastic fixation, mutation, spatial coupling, or parameter limits approaching a coexistence boundary. The \(t^{-1/2}\) rate describes the weighted type-composition amplitude, not necessarily each total population or every coordinate. It is derived using standard smooth center-manifold and periodic averaging arguments; independently established scientific priority is not asserted.

## References

1. M. Costa, P. Czuppon and R. Forien, *Eco-evolutionary cycles in a matching type predator-prey interaction* (2026), arXiv:2609.04834v1, Sections 2.2 and Appendix A.2, https://arxiv.org/abs/2609.04834.
2. *Evolutionary Diversification of Prey and Predator Species Facilitated by Asymmetric Interactions*, PLOS ONE (2016), full text PMCID:PMC5042472, https://pmc.ncbi.nlm.nih.gov/articles/PMC5042472/.
3. J. Carr, *Applications of Centre Manifold Theory* (1981), Springer, standard center-manifold reduction and tracking results.
4. J. A. Sanders, F. Verhulst and J. Murdock, *Averaging Methods in Nonlinear Dynamical Systems*, 2nd ed. (2007), Springer, standard periodic averaging methods.
