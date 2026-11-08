# Finite reactivity restores a unique optimal reset rate on the one-dimensional lattice

## Finding

**Theorem (unique reactive optimum and singular nearest-neighbor limit).** Fix an integer \(m\ge 1\), a trap killing rate \(\kappa>0\), and a Poisson resetting rate \(r>0\). In the continuous-time, nearest-neighbor, one-dimensional lattice walk specified below, the mean time \(T_m(r,\kappa)\) to reaction has **exactly one global minimizer** \(r_*(m,\kappa)\in(0,\infty)\). For every \(m\), this optimizer is a strictly increasing function of \(\kappa\). For \(m=1\) it has the explicit formula

\[
r_*(1,\kappa)=\frac{\kappa+2}{1+\sqrt{\kappa+2}}\sim\sqrt\kappa\qquad(\kappa\to\infty),
\]

and the minimum mean is

\[
T_1(r_*,\kappa)=\frac{(1+\sqrt{\kappa+2})^2}{\kappa}\longrightarrow1.
\]

For each integer \(m\ge2\), the increasing optimizer instead approaches a **finite** perfect-absorption optimum. Its limit is \(r_\infty(m)=(1-q_\infty)^2/q_\infty\), where \(q_\infty\) is the unique root in \((0,1)\) of

\[
-(m-1)+2\sum_{j=1}^{m-1}q^j+q^m=0.
\]

Thus a perfectly absorbing nearest-neighbor trap has an infinite optimal reset rate, whereas **every finite positive reaction rate has a finite unique optimal reset rate**, with the sharp square-root crossover above.

## Assumptions and scope

Let \(X_t\) be the continuous-time simple symmetric nearest-neighbor random walk on \(\mathbb Z\), jumping at rate one to each of its two neighboring sites. Its initial position is the positive integer \(m\); independently, events of a rate-\(r\) Poisson clock instantaneously return it to \(m\). At site zero an independent killing clock acts at rate \(\kappa\) **only during time spent at zero** (equivalently, killing with intensity \(\kappa\mathbf1_{\{X_t=0\}}\)). The walk can leave zero before being killed. The absorption time \(\tau\) is the first killing event and \(T_m(r,\kappa)=\mathbb E_m\tau\). All statements quantify over every integer \(m\ge1\) and finite \(\kappa>0\), without assumptions of small or large rates. The perfectly absorbing limit means \(\kappa\to\infty\) *after* the finite-rate optimization.

Define \(q=q(r)=(r+2-\sqrt{r(r+4)})/2\in(0,1)\). Then \(r=(1-q)^2/q\), and increasing \(r\) corresponds to strictly decreasing \(q\). The full exact mean is

\[
T_m(r,\kappa)=\frac{1+q+\kappa\sum_{j=1}^{m}q^j}{\kappa q^m(1-q)}.
\]

## Proof

**1. Resolvent and renewal.** Put \(\Delta=\sqrt{r(r+4)}=(1-q^2)/q\). The free-walk resolvent \(G_r(i,j)=\int_0^\infty e^{-rt}\Pr_i(X_t=j)\,dt\) solves \((r+2)G_r(i,j)-G_r(i-1,j)-G_r(i+1,j)=\mathbf1_{\{i=j\}}\), yielding \(G_r(m,0)=q^m/\Delta\) and \(G_r(0,0)=1/\Delta\). Rank-one killing at zero gives the Laplace transform of the killing time without resetting:

\[
f_\kappa(r)=\mathbb E_m(e^{-r\tau_\kappa})=\frac{\kappa G_r(m,0)}{1+\kappa G_r(0,0)}=\frac{\kappa q^m}{\kappa+\Delta}.
\]

The first-reset decomposition gives \(T_m=(1-f_\kappa(r))/(r f_\kappa(r))\). Substitute \(r=(1-q)^2/q\) and \(\Delta=(1-q^2)/q\), then use \(1-q^m=(1-q)\sum_{j=0}^{m-1}q^j\), to obtain the stated exact mean. In particular it separates as

\[
T_m(q,\kappa)=U_m(q)+\frac{V_m(q)}\kappa,\quad U_m(q)=\frac{q^{1-m}(1-q^m)}{(1-q)^2},\quad V_m(q)=\frac{1+q}{q^m(1-q)}.
\]

This formula and the renewal-resolvent method are **not** asserted to be new; comparable earlier lattice and partial-absorption formulas are identified below.

**2. One stationary point for all parameters.** Direct differentiation gives

\[
\frac{dT_m}{dq}=\frac{P_m(q;\kappa)}{\kappa q^{m+1}(1-q)^2},\quad
P_m=P_{m,0}+\kappa P_{m,1},
\]

where

\[
P_{m,0}(q)=-m+2q+mq^2,\qquad
P_{m,1}(q)=-(m-1)q+2\sum_{j=2}^m q^j+q^{m+1}.
\]

For \(m=1\) the sum is empty and \(P_{1,1}=q^2\). In increasing powers of \(q\), the constant coefficient is \(-m<0\), the linear coefficient is \(2-\kappa(m-1)\) (of either sign), and **every coefficient from quadratic degree onward is positive** (with the expected combination at coincident degrees when \(m=1\)). Hence the sequence of nonzero coefficients has exactly one sign change. Descartes' rule gives at most one positive root, counting multiplicity. Since \(P_m(0;\kappa)=-m<0\) and \(P_m(1;\kappa)=2+\kappa m>0\), exactly one root \(q_*(m,\kappa)\) lies in \((0,1)\), it is simple, and \(P_m\) changes from negative to positive there. Moreover the exact mean diverges both as \(q\downarrow0\) and as \(q\uparrow1\) for finite \(\kappa>0\). Thus \(q_*\) is the unique global minimum, and \(r_*=(1-q_*)^2/q_*\) the unique finite optimal reset rate.

**3. Strict response to reactivity.** The function \(V_m\) has a unique minimum \(q_0=(\sqrt{m^2+1}-1)/m\), because \(V_m'\) has numerator \(P_{m,0}\). For \(m\ge2\), \(U_m'\) has numerator \(P_{m,1}\), whose nonzero root \(q_\infty\in(0,1)\) is unique: after division by \(q\), its defining expression has strictly positive derivative, is negative at zero and positive at one. When \(m=1\), \(U_1(q)=1/(1-q)\) is strictly increasing and we set the boundary value \(q_\infty=0\).

The ratio \(R_m(q)=U_m(q)/V_m(q)=\sum_{j=1}^m q^j/(1+q)\) is strictly increasing since

\[
(1+q)^2R_m'(q)=\sum_{j=1}^m\left(jq^{j-1}+(j-1)q^j\right)>0.
\]

At the minimum \(q_0\) of \(V_m\), therefore \(U_m'(q_0)=V_m(q_0)R_m'(q_0)>0\), proving \(q_\infty<q_0\) (including \(m=1\)). At \(q_\infty\), \(P_{m,1}\) vanishes and \(P_{m,0}<0\); at \(q_0\), \(P_{m,0}\) vanishes and \(P_{m,1}>0\). Consequently \(q_*\in(q_\infty,q_0)\) for every finite \(\kappa>0\). The unique simple crossing gives \(\partial_qP_m(q_*;\kappa)>0\). Implicit differentiation now yields

\[
\frac{dq_*}{d\kappa}=-\frac{P_{m,1}(q_*)}{\partial_qP_m(q_*;\kappa)}<0,
\quad \frac{dr}{dq}=1-q^{-2}<0,
\quad \frac{dr_*}{d\kappa}>0.
\]

Taking \(\kappa\downarrow0\) and \(\kappa\to\infty\) in the stationary equation and using the established unique roots gives \(q_*\to q_0\) and \(q_*\to q_\infty\), respectively. For \(m\ge2\) this yields the stated finite perfect-target limit.

**4. Nearest-neighbor singular law.** When \(m=1\), the stationary equation reduces to \(-1+2q+(1+\kappa)q^2=0\) with root \(q_*=(1+\sqrt{\kappa+2})^{-1}\). Substitute this into \(r=(1-q)^2/q\) and the exact mean to obtain the formulas in the Finding. In particular \(r_*\sim\sqrt\kappa\), while the perfect-trap mean is \(T_1(q,\infty)=1/(1-q)\), whose infimum \(1\) is attained only as \(q\downarrow0\) (that is, \(r\to\infty\)). The two limiting regimes are therefore nonuniform.

## Verification

The supplied standalone `checker.py` uses standard-library exact rational arithmetic to compare the resolvent-renewal formula with the closed form and independently differentiated derivatives for a grid of integer distances and positive reaction rates, and uses numerical bisection for root and endpoint checks. Run `python3 checker.py`; the expected output is `PASS 1949 exact/numerical assertions`. These finite tests are **not** the universal proof; the proof is the resolvent identity, the one-sign-change polynomial argument, and the implicit derivative inequalities above. Additional independent finite-interval Markov-generator solves at five test parameters agreed with the corresponding infinite-line means to numerical precision where boundary effects were negligible.

## Relationship to prior work

Hartmann and Majumdar (2025), arXiv:2505.19903, derive the perfectly absorbing lattice mean first-passage time and establish that a lattice nearest neighbor has optimum at infinite resetting rate; their discussion motivated the question of what finite reactivity does to this singular case. Das and Giuggioli (2022) derive discrete-time lattice resetting laws with partially absorbing targets, including the one-dimensional mean formula. Their general formula, under the continuous-time scaling limit, **already determines the mean formula above**, so deriving it alone is not an originality claim. Whitehouse, Evans and Majumdar (2013) treat partially reactive resetting in the continuum; Schumm and Bressloff (2021) provide general renewal equations and optimize continuum partially absorbing targets. The claimed contribution is specifically the all-integer-distance **global uniqueness and strict monotonicity in reactivity**, plus the **sharp singular square-root nearest-neighbor asymptotic**. The examined source sections did not state this joint lattice classification, although future discovery of a stronger result could supersede it.

## Limitations

The model assumes symmetric nearest-neighbor jumps at unit rate, resetting to the fixed starting site, a *single* locally reactive site, and memoryless resetting and killing. No claims are made for several targets, finite spatial domains, drift, or non-Poisson reset clocks. The perfect-target infinite optimum is a limiting comparison, not a finite-rate solution at any positive finite \(\kappa\). Independent external validation and publication-priority assessment remain outstanding. Numerical checks do not prove infinite-dimensional claims. Broad discrete-time first-passage formulas remain potential equivalent sources of the underlying mean expression.

## References

1. A. K. Hartmann and S. N. Majumdar, *Diffusion with stochastic resetting on a lattice*, arXiv:2505.19903 (first submitted May 26, 2025), https://arxiv.org/abs/2505.19903.
2. D. Das and L. Giuggioli, *Discrete space-time resetting model: application to first-passage and transmission statistics*, Journal of Physics A 55 (2022), 424004, https://doi.org/10.1088/1751-8121/ac9765.
3. J. Whitehouse, M. R. Evans and S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489 (2013), https://arxiv.org/abs/1301.2489.
4. R. D. Schumm and P. C. Bressloff, *Search processes with stochastic resetting and partially absorbing targets*, arXiv:2104.09372 (2021), https://arxiv.org/abs/2104.09372.
