# A reactivity-neutral drift in optimal resetting to a partially absorbing point trap

## Finding

For a Brownian particle reset at Poisson times to a fixed positive distance from a partially absorbing point trap, there is a **unique inward drift** at which the globally optimal resetting frequency is exactly **independent of the trap reactivity**, for every finite positive reactivity. On the two sides of this drift, increasing reactivity moves the unique optimum in opposite, strict directions.

For diffusivity \(D>0\), reset distance \(L>0\), signed physical drift \(\mu\in\mathbb R\) (positive means *away* from the trap), and trap strength \(k>0\), let \(r_*(\mu,k)\) minimize the mean absorption time. Define \(u_c>1\) as the unique root of

\[
u-u\sqrt{\frac{u-1}{u+1}}=\log(1+u),
\]

and set

\[
m_c=u_c\sqrt{\frac{u_c-1}{u_c+1}},\quad
\mu_c=-\frac{2D}{L}m_c,\quad
s_c=\frac{2u_c^2}{u_c+1}.
\]

Then the following *global, all-reactivities* classification holds:

\[
\frac{\partial r_*(\mu,k)}{\partial k}
\begin{cases}
>0,&\mu>\mu_c,\\
=0,&\mu=\mu_c,\\
<0,&\mu<\mu_c.
\end{cases}
\]

At the transition the complete optimizer curve collapses to one rate:

\[
r_*(\mu_c,k)=\frac{D}{L^2}s_c\qquad\text{for every }k>0.
\]

Numerically, \(u_c=1.294952188188740\ldots\), \(m_c=0.464240177926471\ldots\), and \(s_c=1.461382226893605\ldots\). Thus \(\mu_c\simeq-0.928480355853\,D/L\). The threshold and critical rate are independent of \(k\), but the *optimal mean absorption time* still depends on \(k\).

## Assumptions and scope

Fix \(D,L,k>0\) and \(\mu\in\mathbb R\). A particle begins at \(X_0=L\) and evolves between resets as \(dX_t=\mu\,dt+\sqrt{2D}\,dW_t\) on the full line. Independent Poisson events of rate \(r>0\) return the still-surviving particle instantaneously to \(L\). Killing at the origin has finite strength \(k\), represented in the forward equation by the sink \(-k\,p(0,t)\delta_0\). Crossing the origin does not necessarily kill. The target quantity is mean time *until reaction*, rather than the first time the origin is visited.

Use the dimensionless parameters

\[
a=\frac{\mu L}{2D},\quad m=|a|,\quad
\eta=\frac{2D}{kL},\quad s=\frac{rL^2}{D},\quad
u=\sqrt{m^2+s}.
\]

The known exact mean-reaction-time formula, derived in the initiating work [1], is

\[
T_\mu(r)=\frac{L^2}{D}\,
\frac{(1+\eta u)e^{u+a}-1}{s}.
\tag{1}
\]

In particular, no finite \(k\) is replaced by a perfectly absorbing boundary. The claim is a **parameter-sensitivity theorem for the unique optimum**, not a claim to have first derived formula (1), or the previously established global uniqueness of the optimal rate.

## Proof

**1. Uniqueness and transversality of the stationary optimum.** Let \(\Phi_\eta(s)=e^{u+a}(1+\eta u)\), \(u=\sqrt{m^2+s}\), and

\[
B_\eta(s)=\Phi_\eta(s)-1-s\Phi'_\eta(s).
\]

Direct differentiation of (1) shows \(\partial_s T_\mu=-(L^2/D)B_\eta(s)/s^2\). A second differentiation gives

\[
\Phi''_\eta(s)=\frac{e^{u+a}}{4u^3}
\left[(u-1)+\eta(u^2+u-1)\right],
\quad B'_\eta(s)=-s\Phi''_\eta(s).
\tag{2}
\]

For each \(\eta>0\), the bracket in (2) is strictly increasing in \(u>0\), negative near zero and positive for large \(u\). Thus \(B_\eta\) is initially increasing, if that negative interval is encountered, and then strictly decreasing. For \(m>0\), \(B_\eta(0)=e^{m+a}(1+\eta m)-1>0\); when \(m=0\), the Puiseux expansion yields \(B_\eta(s)=(1+\eta)\sqrt{s}/2+O(s^{3/2})>0\) near zero. Finally \(B_\eta(s)<0\) for sufficiently large \(s\) by (2) and the exponentially growing negative term of its explicit expression. Therefore it has exactly one positive zero \(s_*\), which lies on its strictly decreasing branch. The unique mean-time minimizer is \(r_*=Ds_*/L^2\), and \(B'_\eta(s_*)<0\), so implicit differentiation is valid for every \(\mu\) and \(k>0\).

**2. A zero reactivity response is rigid.** From the definition,

\[
B_\eta(s)=e^{u+a}\left[
1-\frac{s}{2u}
+\eta\left(u-\frac{s(u+1)}{2u}\right)
\right]-1.
\]

Since \(\partial_\eta B_\eta(s_*)=e^{u+a}G(u,m)\) where

\[
G(u,m)=u-\frac{(u^2-m^2)(u+1)}{2u},
\tag{3}
\]

implicit differentiation, together with \(B'_\eta(s_*)<0\) and \(d\eta/dk<0\), implies

\[
\operatorname{sgn}\!\left(\frac{\partial r_*}{\partial k}\right)
=-\operatorname{sgn} G(u_*,m).
\tag{4}
\]

Suppose the derivative vanishes. The equation \(G=0\) forces

\[
s=\frac{2u^2}{u+1},\qquad
m^2=\frac{u^2(u-1)}{u+1},\qquad u>1.
\tag{5}
\]

On this locus, \(B_\eta=0\) simplifies, **independently of \(\eta\)**, to \(e^{u+a}=u+1\). Because \(\log(1+u)<u\) for \(u>0\), the drift must point inward, \(a=-m\). Substitution of (5) yields the single scalar equation

\[
F(u)=u-u\sqrt{\frac{u-1}{u+1}}-\log(1+u)=0,
\qquad u>1.
\tag{6}
\]

**3. Exactly one neutral drift.** Define \(h(u)=u\sqrt{(u-1)/(u+1)}\) for \(u>1\). Then

\[
h'(u)=\frac{u^2+u-1}{(u+1)\sqrt{u^2-1}}
>\frac{u}{u+1},
\]

since the difference of the positive squared numerators is \(2u^3-2u+1>0\) for \(u>1\). Thus \(F'(u)=u/(u+1)-h'(u)<0\). Moreover \(F(1)=1-\log 2>0\), while \(F(u)\to-\infty\). Hence equation (6) has exactly one solution \(u_c>1\). Equations (5) produce the unique \(m_c\) and \(s_c\) in the claim. Conversely, at \(a=-m_c\), \(s=s_c\), both the constant and the coefficient of \(\eta\) in \(B_\eta(s)\) vanish. This is a stationary optimum for **every** \(\eta>0\); the uniqueness proved above makes it the global optimum for every \(k>0\).

**4. The sign on both sides.** The implicit optimizer \(s_*(a,\eta)\) and the quantity \(G(u_*,|a|)\) vary continuously in their parameters. By steps 2–3, \(G\) can vanish *only* at inward drift magnitude \(m_c\). At zero drift, \(B_\eta(1)=e/2-1>0\), hence \(s_*(0,\eta)>1\) and \(G(u_*,0)=u_*(1-u_*)/2<0\). Thus \(G<0\) and \(\partial_k r_*>0\) for all outward drifts and all inward drifts with magnitude below \(m_c\).

To identify the remaining sign without relying on a numerical test, fix inward magnitude \(m=1\) and let \(\eta\downarrow0\). At \(\eta=0\), \(\Phi_0(s)=e^{\sqrt{1+s}-1}\) satisfies \(\Phi''_0(s)>0\) for every \(s>0\), while \(B_0(0)=0\). Therefore \(B_0(s)<0\) for every fixed \(s>0\), so the unique positive zero \(s_*(\eta)\) for \(\eta>0\) tends to zero. In (3) this gives \(G(u_*,1)\to1>0\). No zero of \(G\) can occur at \(m=1\) for any \(\eta>0\), and none can occur as \(m\) varies within \((m_c,\infty)\). Hence \(G>0\) throughout that region. Equation (4) now gives \(\partial_k r_*<0\) for every stronger inward drift. This completes the global classification.

## Verification

The standard-library Python program `verify.py` calculates the unique scalar root, solves the stationary equation for multiple inward and outward drifts and reactivities by sign bracketing, checks the parameter-independent critical optimum, and compares mean times away from each computed minimum. Execute `python verify.py` with Python 3.9 or newer. The packaged program produced **534 passing finite consistency assertions** and numerically returned \(u_c\simeq1.294952188188740\), \(m_c\simeq0.464240177926471\), \(s_c\simeq1.461382226893605\). These tests are not proofs of the all-parameter signs; the proof is in the preceding section.

## Relationship to prior work

Mazzolo [1, especially Appendix A.1–A.5 and equation (185)] already supplies the exact partially reactive point-sink mean formula (1); proves uniqueness and increasing optimal rate with trap reactivity when the drift vanishes; and numerically documents a *different* nonmonotonic effect when varying inward drift at fixed reactivity. The new contribution is the sharp, **all-reactivities** classification of \(\partial_k r_*\), including the unique negative-drift value for which the optimum is identical for every reactivity. These statements are not among the results of the inspected source sections.

Whitehouse, Evans and Majumdar [2, Section 4.1] analyze the partly reactive target under *zero* drift. Ray, Mondal and Reuveni [3, Section IV] study restart optimization with drift toward a *perfectly absorbing* boundary, including a zero-reset phase, so their theorem does not imply the finite-point-sink reactivity-neutral parameter. Published mathematical notes [4–6] already give finite-reactivity all-drift uniqueness, the strict opposite-drift optimal-rate ordering, and singular strong-reactivity or large-drift asymptotics. Those stronger existing results are expressly not claimed as new. Their documented statements do not include the fixed-drift, all-positive-reactivity neutral point or its strict global sensitivity reversal. Absence of a covering statement in inspected literature and database searches does not prove absolute priority.

## Limitations

The result assumes one fixed reset location, one finite-strength point trap on the full line, constant drift and diffusivity, and independent Poisson resetting. The threshold concerns optimal mean *reaction* time, not survival probabilities at each time, global optimization over arbitrary reset clocks, multiple traps, or spatially varying drifts. The optimum's *rate* is neutral only at the threshold; its optimized *mean time* still changes with reactivity. The all-reactivities conclusion is for finite \(k>0\), without claiming uniformity of approximations at \(k=0\) or \(k=\infty\). Independent mathematical validation and literature-wide priority certification remain outstanding.

## References

1. A. Mazzolo, “Diffusion with stochastic resetting in the presence of a delta killing trap: Drift-controlled survival regimes,” arXiv:2609.22527v1, first publicly posted 18 September 2026; https://arxiv.org/abs/2609.22527 . Especially Section III.3.2 and Appendix A.1–A.5.
2. J. Whitehouse, M. R. Evans, and S. N. Majumdar, “Effect of Partial Absorption on Diffusion with Resetting,” *Physical Review E* **87**, 022118 (2013), arXiv:1301.2489; https://arxiv.org/abs/1301.2489 . Especially Section 4.1.
3. S. Ray, D. Mondal, and S. Reuveni, “Péclet number governs transition to acceleratory restart in drift-diffusion,” *Journal of Physics A* **52**, 255002 (2019), arXiv:1811.08239; https://arxiv.org/abs/1811.08239 . Especially Section IV.
4. “Unique optimal resetting and a finite-reactivity drift-orientation gap,” published mathematical result (2026), scientific comparison of the drifted one-point-reactive-sink model.
5. “A persistent reactivity gap between optimal opposite-drift resetting rates,” published mathematical result (2026), scientific comparison of same-object strong-drift limits.
6. “Cubic-root rounding of the drift-controlled optimal-resetting transition at a partially reactive point trap,” published mathematical result (2026), scientific comparison of the singular large-reactivity limit.
