# An entropy Lyapunov certificate for globally stable adaptive institutional rewards

## Finding

**Theorem (global attraction for every feedback speed).** In the adaptive institutional-reward public-goods replicator system of Hua and Liu [1], assume the unique interior cooperation--reward equilibrium exists strictly inside the admissible rectangle. Then that equilibrium attracts **every** interior initial condition for **every** feedback timescale \(\varepsilon>0\), including arbitrarily fast or slow reward adaptation. The following explicit weighted binary relative entropy is a proper Lyapunov function, with an exact nonpositive dissipation identity. In particular, the model has no nonconstant periodic solution or nontrivial compact recurrent trajectory in the interior under these assumptions. The theorem proves a global, all-speed statement; local stability and representative trajectories were considered in [1].

## Assumptions and scope

Fix an integer \(N\ge2\), a group multiplier \(0<r<N\), a contribution cost \(c>0\), incentive scale \(\delta>0\), feedback parameter \(u>0\), bounds \(0<\alpha<\beta\), and timescale \(\varepsilon>0\). Define

\[
D=c\left(1-\frac rN\right)>0,\qquad
S_N(x)=\sum_{j=0}^{N-1}(1-x)^j.
\]

The continuous-time system is

\[
\begin{aligned}
\varepsilon\dot x&=x(1-x)\bigl[-D+\delta aS_N(x)\bigr],\\
\dot a&=(a-\alpha)(\beta-a)\bigl[u-(u+1)x\bigr].
\end{aligned}
\]

Here \(x\in(0,1)\) is the fraction cooperating and \(a\in(\alpha,\beta)\) is institutional reward intensity. Put

\[
x_*:=\frac{u}{1+u},\qquad a_*:=\frac{D}{\delta S_N(x_*)}.
\]

**The indispensable coexistence hypothesis is \(\alpha<a_*<\beta\).** It is not replaced by merely \(0<a_*<1\), and the theorem does not claim convergence to an interior point when this condition fails. On a boundary, an initial condition need not converge to the interior equilibrium because all four sides are invariant.

Define \(t=(a-\alpha)/(\beta-\alpha)\), \(t_*=(a_*-\alpha)/(\beta-\alpha)\), and binary relative entropy

\[
K(p\Vert q)=p\log\frac pq+(1-p)\log\frac{1-p}{1-q},\qquad 0<p,q<1.
\]

Then \(0<t_*<1\), and the certificate is

\[
V(x,a):=K(x_*\Vert x)+\frac{\delta S_N(x_*)}{\varepsilon(1+u)}K(t_*\Vert t).
\]

## Proof

1. **Uniqueness of the interior equilibrium.** Inside the open rectangle, \(\dot a=0\) implies \(x=x_*\); then \(\dot x=0\) implies \(a=a_*\). The system is polynomial, and the closed rectangle is forward invariant because the vector field is tangent to its sides. Thus solutions starting inside remain well defined for all positive time.

2. **Positive and proper entropy.** The elementary strict Gibbs inequality gives \(K(p\Vert q)\ge0\), with equality exactly at \(p=q\). For each fixed \(p\in(0,1)\), \(K(p\Vert q)\to+\infty\) as \(q\downarrow0\) or \(q\uparrow1\). Since both coefficients are strictly positive, \(V\) vanishes exactly at \((x_*,a_*)\) and diverges on approach to any part of the boundary of the open rectangle. Hence its finite sublevel sets are compact inside the rectangle.

3. **Exact dissipation and cancellation.** Direct differentiation yields

\[
\frac{\partial V}{\partial x}=\frac{x-x_*}{x(1-x)},\qquad
\frac{\partial V}{\partial a}=\frac{\delta S_N(x_*)}{\varepsilon(1+u)}\frac{a-a_*}{(a-\alpha)(\beta-a)}.
\]

Substitute the vector field, use \(D=\delta a_*S_N(x_*)\) and \(u-(u+1)x=(u+1)(x_*-x)\), and cancel the terms containing \((a-a_*)S_N(x_*)\):

\[
\boxed{\frac{dV}{dt}=\frac{\delta a}{\varepsilon}(x-x_*)[S_N(x)-S_N(x_*)].}
\]

For \(N\ge2\),

\[
S_N'(x)=-\sum_{j=1}^{N-1}j(1-x)^{j-1}<0\quad(0<x<1).
\]

As \(\delta,a,\varepsilon>0\), the exact derivative is negative whenever \(x\ne x_*\), and is zero precisely on the line \(x=x_*\).

4. **Largest invariant zero-dissipation set.** On \(x=x_*\),

\[
\dot x=\frac{\delta x_*(1-x_*)S_N(x_*)}{\varepsilon}(a-a_*).
\]

Thus a point on that line with \(a\ne a_*\) instantly leaves it. The largest invariant subset of the zero-dissipation line is the single equilibrium. Every interior trajectory stays in its initial compact entropy sublevel set, so LaSalle's invariance principle applies and forces convergence to \((x_*,a_*)\). Positive definiteness and strict sublevel trapping also prove Lyapunov stability. The argument does not impose any upper or lower restriction on \(\varepsilon>0\) beyond positivity.

5. **No interior recurrence.** Along any nonstationary interior trajectory \(V\) cannot be constant on any nonzero time interval, because the only trajectory contained in \(x=x_*\) is stationary. Periodic or nontrivially recurrent trajectories would force repeated values of the nonincreasing proper \(V\), contradicting the strict entropy decrease. This is a consequence of the same theorem, not a separate finding.

## Verification

The attached `verify.py` checks the exact dissipation identity, including the normalized-reward derivative and its sign, for 2,400 randomly generated **exact-rational** test instances over \(2\le N\le17\). It checks the rational sample \(N=5\), \(r=3\), \(c=1\), \(\delta=1/5\), \(u=2\), \(\alpha=1/2\), \(\beta=3\), for which \(x_*=2/3\) and \(a_*=162/121\). Additionally, it integrates 20 trajectories over five positive timescales, with logistic-coordinate integration preserving the open state bounds. Execute from a directory containing `verify.py` with `python verify.py` (Python 3; SciPy optional for the trajectory checks).

These experiments confirm specified cases and the implemented algebra, but **do not** prove the arbitrary-parameter theorem. The proof above is the certificate. In particular, finite integrations do not certify global attraction by themselves.

## Relationship to prior work

Hua and Liu [1, Section 3.3 and Appendix] specify this exact adaptive public-goods feedback system, identify its equilibria, and establish local Jacobian stability. They explicitly assume a small timescale in the model and numerically vary it in a finite range; descriptions of global-looking phase portraits do not supply the all-parameter compact-entropic certificate proved here. Their equilibrium formula is fully credited. The new assertion is the **proper explicit entropy Lyapunov function and complete interior global-attraction guarantee for all positive timescales**, under the correct interior-reward condition.

Liu, Cao and Wu [2] analyze a distinct eco-evolutionary payoff/feedback system and show nonlinear imitation can produce limit cycles; those conditions do not establish this reward model's global attractor. Gong and coauthors [3] study replicator-mutator environmental feedback and limit-cycle bifurcations for a different vector field. General classical Lyapunov/LaSalle theory is used as a proof method, not claimed as new.

## Limitations

The result concerns deterministic, well-mixed, two-strategy replicator dynamics without mutation or noise. It requires strictly interior initial conditions and strictly interior incentive equilibrium, \(N\ge2\), positive bounded reward, and all parameters as stated. It provides no uniform numerical convergence-rate bound, no result for stochastic finite-population games, no global claim for boundary initial conditions, and no classification outside the coexistence regime. Primary-source global-looking phase diagrams and broad dynamical stability ideas create a residual literature-priority risk; absence of matching searches does not prove publication priority. The mathematical proof is an ordinary direct argument, not independent external validation.

## References

[1] Shijia Hua and Linjie Liu, *Coevolutionary dynamics of population and institutional rewards in public goods games*, arXiv:2308.09530, first posted 2023-08-18, https://arxiv.org/abs/2308.09530 .

[2] Yuan Liu, Lixuan Cao and Bin Wu, *General non-linear imitation leads to limit cycles in eco-evolutionary dynamics*, arXiv:2210.10552, 2022, https://arxiv.org/abs/2210.10552 .

[3] Lulu Gong, Weijia Yao, Jian Gao and Ming Cao, *Limit Cycles Analysis and Control of Evolutionary Game Dynamics with Environmental Feedback*, arXiv:2205.10734, 2022, https://arxiv.org/abs/2205.10734 .
