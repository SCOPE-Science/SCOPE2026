# Critical-return recurrence dichotomy in nonlinear environmental public-goods games

## Finding

At the **critical multiplication factor** \(r=N\), a two-strategy nonlinear public-goods game with an adaptive environment has an exact group-size-dependent recurrence dichotomy. For group size \(N=2\), every non-equilibrium interior trajectory is a periodic orbit surrounding the unique coexistence equilibrium. For every integer \(N\ge3\), that equilibrium is a hyperbolic source, there is no nonconstant periodic orbit in the open state square, and every other interior solution comes arbitrarily close to the boundary at arbitrarily late times:

\[
\liminf_{t\to\infty}\min\{x(t),1-x(t),p(t),1-p(t)\}=0.
\]

Thus keeping the same *critical return-to-group-size ratio* does not preserve recurrent coexistence when changing the interaction size from pairwise to higher order. The result describes behavior relative to the full state square, **not** convergence to a particular corner or a specified boundary cycle.

## Assumptions and scope

Fix an integer \(N\ge2\), \(\varepsilon>0\), \(\theta>0\), \(0<\delta_s,\delta_d<1\), and \(r=N\). The mean-field model is

\[
\begin{aligned}
\dot x&=x(1-x)G(x,p),\\
\dot p&=\varepsilon p(1-p)[(\theta+1)x-1],\\
G(x,p)&=(1-p)(1+\delta_s x)^{N-1}+p(1-\delta_d x)^{N-1}-1.
\end{aligned}
\]

The state space is the open square \(\Omega=(0,1)^2\), with \(x\) the fraction of cooperators and \(p\) the probability of a discounting public-goods regime. The endpoints and coefficients follow the asymmetric version of Jiang et al.'s environmental-feedback geometric-payoff model [1]. All statements concern the deterministic continuous-time replicator closure, not discrete stochastic participation. For all interior initial conditions the flow stays interior at finite times by the multiplicative boundary factors and bounded smooth vector field.

Define \(a=(1+\theta)^{-1}\), \(A=(1+\delta_s a)^{N-1}\), \(D=(1-\delta_d a)^{N-1}\). Since \(D<1<A\), the unique interior equilibrium is

\[
(x_*,p_*)=\left(a,\frac{A-1}{A-D}\right).
\]

## Proof

**1. Equilibrium and local type.** The equation \(\dot p=0\) in \(\Omega\) forces \(x=a\). The function \(p\mapsto G(a,p)\) is strictly decreasing and switches sign between \(p=0\) and \(p=1\), giving the displayed unique equilibrium. Put \(f(x,p)=G(x,p)+1\); then \(f(0,p)=1\). For \(N\ge3\),

\[
 f_{xx}(x,p)=(N-1)(N-2)\left[(1-p)\delta_s^2(1+\delta_s x)^{N-3}+p\delta_d^2(1-\delta_d x)^{N-3}\right]>0.
\]

Because \(f(a,p_*)=f(0,p_*)=1\), strict convexity implies \(G_x(a,p_*)=f_x(a,p_*)>0\). At the equilibrium the Jacobian is

\[
J_*=
\begin{pmatrix}
a(1-a)G_x(a,p_*)&a(1-a)(D-A)\\
\varepsilon p_*(1-p_*)(\theta+1)&0
\end{pmatrix}.
\]

Its trace is positive, while its determinant equals \(a(1-a)(A-D)\varepsilon p_*(1-p_*)(\theta+1)>0\). Both eigenvalues have strictly positive real parts (positive real roots or a conjugate pair with positive real part). Hence it is a hyperbolic source.

**2. Global absence of closed orbits for larger groups.** On \(\Omega\) choose the positive \(C^1\) Dulac multiplier

\[
B(x,p)=\frac{1}{x^2(1-x)p(1-p)}.
\]

The second component of \(B(\dot x,\dot p)\) is independent of \(p\), so

\[
\operatorname{div}(B\dot x,B\dot p)
=\frac{xG_x-G}{x^2p(1-p)}
=\frac{\int_0^x t f_{xx}(t,p)\,dt}{x^2p(1-p)}>0.
\]

The identity follows from differentiation of \(x f_x-f\), using \(f(0,p)=1\). The open square is simply connected; the Bendixson–Dulac theorem excludes every nonconstant periodic orbit lying in \(\Omega\).

**3. Arbitrarily late boundary excursions.** A forward orbit whose distance from the boundary is eventually uniformly positive has a nonempty compact omega-limit set lying entirely in \(\Omega\). Since there is exactly one equilibrium, and it is a hyperbolic source, a planar Poincaré–Bendixson omega-limit set without a periodic orbit would have to be this equilibrium or contain connecting orbits terminating there. Neither is possible for a nonstationary forward trajectory: the equilibrium has trivial local forward stable manifold and cannot be the forward endpoint of a connecting orbit. Therefore no non-equilibrium interior trajectory can remain eventually in a compact subset of \(\Omega\); equivalently, the asserted liminf is zero. This is weaker than convergence to the boundary and does not prescribe where excursions occur.

**4. Pairwise recurrence is the exact exception.** For \(N=2\), set \(c=\delta_s+\delta_d\), \(b=\delta_s/c\), \(a=(1+\theta)^{-1}\), and \(\kappa=\varepsilon(1+\theta)\). The same system reduces to

\[
\dot x=c x^2(1-x)(b-p),\qquad \dot p=\kappa p(1-p)(x-a).
\]

A first integral on the open square is

\[
H(x,p)=\kappa\left[\frac{a}{x}+(1-a)\log\frac{x}{1-x}\right]
-c\left[b\log p+(1-b)\log(1-p)\right].
\]

Indeed \(H_x=\kappa(x-a)/[x^2(1-x)]\), \(H_p=c(p-b)/[p(1-p)]\), and the two contributions to \(dH/dt\) cancel. The function \(H\) tends to \(+\infty\) at every approach to the square boundary, has exactly one critical point \((a,b)\), and this point is its strict minimum. All other energy levels are compact regular simple closed curves: the separated component functions decrease toward their unique minimizers and increase away from them, so a regular level bounds the connected convex-in-coordinate sublevel region. The vector field never vanishes on these curves, making each a periodic orbit. Thus every nonstationary pairwise trajectory remains in a compact interior orbit.

**5. Exact witness.** Let \(N=3\), \(r=3\), \(\delta_s=\delta_d=1/2\), and \(\varepsilon=\theta=1\). Then \(a=1/2\), \(A=25/16\), \(D=9/16\), and \(p_*=9/16\). Direct differentiation yields

\[
J_* = \begin{pmatrix}1/32&-1/4\\63/128&0\end{pmatrix},
\quad \operatorname{spec}(J_*)=\left\{\frac{1+i\sqrt{503}}{64},\frac{1-i\sqrt{503}}{64}\right\}.
\]

At \(N=2\), with the remaining parameters unchanged, \((a,b)=(1/2,1/2)\) is a center with eigenvalues \(\pm i/4\), and the global integral above proves all non-equilibrium interior orbits are closed.

## Verification

The self-contained `check.py` uses symbolic differentiation and exact rational arithmetic to reconstruct both small-group Jacobians, the divergence for sizes two through five, and the derivative of the conserved pairwise energy. It checks finite algebraic identities only; the all-group strict-convexity and global omega-limit arguments are analytic, as proved above. Execute with `python check.py` using Python 3 and SymPy.

## Relationship to prior work

Jiang et al. [1] introduced the model, its interior equilibrium, and stability/oscillation regimes mainly under strict inequalities \(r<N\) and \(r>N\), calling \(r=N\) a phase demarcation. Its Appendix B/C supplies Jacobian formulas, and its figures discuss behavior on either side. Their equilibrium formulas imply part of the local source observation when specialized, so that local fact alone is **not** asserted to be novel. The present result instead proves a global **equality-line** dichotomy: complete recurrent coexistence for \(N=2\), but no compact non-equilibrium interior recurrence and mandatory arbitrarily late boundary excursions for any \(N\ge3\), including asymmetric nonlinear strengths.

Ito and Yamamichi [2] classify neutral cycles of pairwise environmental-feedback games. The pairwise center is therefore presented as the familiar comparison case, not as a novel general theorem. Their classification treats payoff mixtures linear in the frequency of two player strategies, not the nonlinear higher-order geometric factors for arbitrary \(N\ge3\). Standard Bendixson–Dulac and Poincaré–Bendixson results are used as proof methods, without a claim of novelty for those theorems.

## Limitations

The model is deterministic, well mixed and smooth, with the particular logistic feedback used in [1], positive asymmetric nonlinear strengths below one, and exactly the critical multiplication factor. The theorem establishes a boundary *liminf*, not convergence to a specific boundary equilibrium, a boundary heteroclinic cycle, a rate of escape, or robustness to stochasticity, arbitrary feedback laws, spatial structure, or other payoff functions. Originality has only been compared with available records and primary sources; the possibility of unindexed equivalents remains. Independent scientific validation has not been performed.

## References

1. Y. Jiang, X. Wang, W. Zhu, M. Wei, L. Liu, S. Tang, H. Zheng, *Nonlinear Public Goods Game in Dynamical Environments*, first public arXiv version October 11, 2025, arXiv:2510.10259; model and appendices of accessible v2 (February 20, 2026), https://arxiv.org/html/2510.10259v2 and https://arxiv.org/abs/2510.10259.
2. H. Ito and M. Yamamichi, *A complete classification of evolutionary games with environmental feedback*, PNAS Nexus **3** (2024), pgae455, https://academic.oup.com/pnasnexus/article/3/11/pgae455/7817389.
