# Sharp double-exponential elimination in strictly dominant two-action log-evidence games

## Finding
For the coupled two-player, two-action log-linear replicator dynamics, suppose each player has a strictly dominant first action. For every initial state in the open square, the probabilities \(x(t)\) and \(y(t)\) of those dominant actions tend to zero **doubly exponentially**. If \(\alpha=A_{11}-A_{21}>0\) and \(\beta=B_{11}-B_{21}>0\) denote the payoff gaps against the opponent's first (dominant) action, set \(\lambda=\sqrt{\alpha\beta}\). There exists a trajectory-dependent \(L>0\) such that
\[
 x(t)\exp\!\left(\frac{L}{2\sqrt{\beta}}e^{\lambda t}\right)\longrightarrow1,\qquad
 y(t)\exp\!\left(\frac{L}{2\sqrt{\alpha}}e^{\lambda t}\right)\longrightarrow1.
\]
In particular \(\lim_{t\to\infty}\log(1/y(t))/\log(1/x(t))=\sqrt{\beta/\alpha}\). The exponent \(\lambda\) depends only on the two payoff gaps against the strategies eventually eliminated, not on the other two strictly positive gaps.

## Assumptions and scope
Let \(A=(A_{ij})\) be player A's payoff matrix, indexed by A's action \(i\) and B's action \(j\). Let \(B=(B_{ij})\) be player B's payoff matrix, indexed by B's action \(i\) and A's action \(j\). Assume
\[
 \alpha=A_{11}-A_{21}>0,\quad \alpha_0=A_{12}-A_{22}>0,\quad
 \beta=B_{11}-B_{21}>0,\quad\beta_0=B_{12}-B_{22}>0.
\]
Let \(x,y\in(0,1)\) be each player's probability of action 1 and use *logarithmic* fitness \(f^A=A(\log y,\log(1-y))^\top\), \(f^B=B(\log x,\log(1-x))^\top\). Their continuous-time replicator equations are
\[
 \dot x=x(1-x)[\alpha\log y+\alpha_0\log(1-y)],\quad
 \dot y=y(1-y)[\beta\log x+\beta_0\log(1-x)].
\]
All assertions hold in physical ODE time without time reparametrization, for arbitrary finite interior initial conditions. The first actions are dominant in the *ordinary payoff* sense, but are eliminated under this particular log-fitness rule.

## Proof
Define log-odds against the first actions,
\[
 u=\log\frac{1-x}{x},\qquad v=\log\frac{1-y}{y}.
\]
Exact differentiation gives
\[
 \dot u=\alpha\log(1+e^v)+\alpha_0\log(1+e^{-v}),\quad
 \dot v=\beta\log(1+e^u)+\beta_0\log(1+e^{-u}).
\]
Each right-hand side is positive for every real argument, has a strictly positive global minimum (it is continuous and grows at both infinities), and is at most linear in its argument. Therefore the solution is globally defined, \(u,v\to+\infty\), and both coordinates eventually become nonnegative.

For such times use \(\log(1+e^z)=z+\log(1+e^{-z})\) to write
\[
 \dot u=\alpha v+r_A(v),\qquad \dot v=\beta u+r_B(u),
\]
where \(r_A(v)=(\alpha+\alpha_0)\log(1+e^{-v})>0\), \(r_B(u)=(\beta+\beta_0)\log(1+e^{-u})>0\), and both errors tend to zero. Define
\[
 W=\sqrt\beta\,u+\sqrt\alpha\,v,\qquad Z=\sqrt\beta\,u-\sqrt\alpha\,v.
\]
For \(\lambda=\sqrt{\alpha\beta}\), direct substitution gives
\[
 \dot W=\lambda W+F(t),\quad\dot Z=-\lambda Z+G(t),
\]
where \(F=\sqrt\beta\,r_A(v)+\sqrt\alpha\,r_B(u)>0\) and \(G=\sqrt\beta\,r_A(v)-\sqrt\alpha\,r_B(u)\). Both are bounded and vanish at infinity. Choose \(t_0\) with \(u(t_0),v(t_0)>0\). Variation of constants yields the finite, strictly positive number
\[
 L=e^{-\lambda t_0}W(t_0)+\int_{t_0}^{\infty}e^{-\lambda s}F(s)\,ds>0.
\]
The tail-integral formula shows \(W(t)-Le^{\lambda t}\to0\), because \(F(s)\to0\) and the exponential convolution has vanishing tail. The stable equation gives \(Z(t)\to0\). Thus
\[
 u(t)=\frac{L}{2\sqrt\beta}e^{\lambda t}+o(1),\qquad
 v(t)=\frac{L}{2\sqrt\alpha}e^{\lambda t}+o(1).
\]
Since \(x=(1+e^u)^{-1}\) and \(y=(1+e^v)^{-1}\), the multiplicative limits follow. Every quantifier and coefficient is thereby established without assuming a local linearization at a boundary where logarithmic fitness is singular.

## Verification
Run `python check.py` with Python, SciPy, and its standard library. It solves the exact log-odds ODE for five diverse positive payoff-gap sets, tests convergence of \(e^{-\lambda t}W(t)\), and checks the positive-eigenvector asymptotic. All five tests passed on the stored script. These finite integrations corroborate but do not replace the analytic proof. Direct substitution checks the exact transformed ODE and the two scalar equations for \(W,Z\).

## Relationship to prior work
Ruiz-Serra, Ay, and Harré (2026), Sections II and III, define precisely this logarithmic fitness and prove qualitative elimination/inversion in dominance games; their treatment does not state the sharp double-exponential time profile and its universal cross-player logarithmic ratio derived here. Ay and Erb (2005) introduced this log-linear replicator class; the underlying dynamics and ordinary linearization machinery are not claimed as new. This theorem concerns the **asymptotic decay scale and full amplitude**, not a new elimination or inversion criterion. Berker and Conitzer (2024) study a different restart game and do not imply the present law.

## Limitations
The result uses strict dominance for **both** players and exactly two actions each. If only one player has a dominant strategy or dominance is weak, the positive-coupling argument does not apply. It describes an ideal continuous-time log-evidence dynamics at infinite numerical precision, not the convergence speed of noisy behavioral learning. The coefficient \(L\) depends on the initial condition and all four payoff gaps; only the growth exponent and ratio are universal. Independent audit has not been performed.

## References
1. J. Ruiz-Serra, N. Ay, M. Harré, *Bayesian Replicator Dynamics and the Inversion of Strict Dominance in Bimatrix Games*, arXiv:2610.36345v2, https://arxiv.org/html/2610.36345v2 (initial version October 26, 2026).
2. N. Ay and J. Erb, *On a Notion of Linear Replicator Equations*, Journal of Dynamics and Differential Equations 17 (2005), 427–451, DOI: 10.1007/s10884-005-4574-3, cited as the source of log-linear fitness in reference 1.
