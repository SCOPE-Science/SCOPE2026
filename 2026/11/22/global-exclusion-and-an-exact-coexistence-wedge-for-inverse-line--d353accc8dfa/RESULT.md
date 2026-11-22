# Global exclusion and an exact coexistence wedge for inverse-linear stage-specific predation

## Finding

For a discrete-generation prey population attacked successively by adult-stage and juvenile-stage specialist predators, inverse-linear (geometric/negative-binomial shape-one) escape probabilities imply an exact *competitive exclusion identity*. With no adult-prey carryover, **every** initially positive orbit loses the adult-stage predator when its basic replacement parameter is no larger than that of the juvenile-stage predator. This is a global conclusion, even when the prey and surviving predator oscillate, and it holds for the full admissible class of bounded monotone density-dependent prey recruitment laws.

For Beverton–Holt recruitment, an additional exact conclusion is available: a unique strictly positive three-species equilibrium exists **if and only if**

\[
R_J>1,\qquad R_J<R_A<1+r(R_J-1).
\]

Within this nonempty wedge its coordinates are

\[
(h_*,x_*,y_*)=\left(\frac1{R_J},\,\frac{rR_J}{R_A+r-1}-1,\,\frac{R_A}{R_J}-1\right).
\]

Here \(R_J\) and \(R_A\) are the juvenile-specific and adult-specific predators' respective basic replacement parameters and \(r>1\) is prey recruitment at zero density. No dynamical stability of this coexistence equilibrium is asserted.

## Assumptions and scope

Use the stage-specific three-population model in Seno–Goyal (2026), their equation (13), with adult prey survival \(\sigma=0\). Let \(H\) be adult-prey density and \(P^J,P^A\) predator densities. Set the juvenile and adult prey-escape functions to the admissible negative-binomial shape-one laws

\[
\Pi_J(P^J)=\frac{1}{1+a_JP^J},\qquad
\Pi_A(P^A)=\frac{1}{1+a_AP^A},\qquad a_J,a_A>0.
\]

Let \(\rho_J,\rho_A>0\) be predator-conversion constants and let \(K>0\) be the carrying capacity of the predator-free prey process, normalized by \(F(K)=1\). Assume \(F(z)>0\) for \(0\le z\le K\) and \(0<F(z)z\le K\) for \(0<z\le K\). These properties follow from the source's monotonicity assumptions for prey recruitment on the capacity interval. Take \(0<H_0\le K\) and \(P^J_0,P^A_0>0\).

Write \(h=H/K\), \(x=a_JP^J\), \(y=a_AP^A\), \(R_J=\rho_Ja_JK\), \(R_A=\rho_Aa_AK\), and \(G(h,y)=F(Kh/(1+y))\,h/(1+y)\). The exact positive recurrence is

\[
\begin{aligned}
h_{t+1}&=\frac{G(h_t,y_t)}{1+x_t},\\
x_{t+1}&=\frac{R_Jx_tG(h_t,y_t)}{1+x_t},\\
y_{t+1}&=\frac{R_Ay_th_t}{1+y_t}.
\end{aligned}
\tag{1}
\]

For the exact equilibrium classification, specialize to \(F(H)=r/[1+(r-1)H/K]\) with \(r>1\). Equation (1) then becomes

\[
(h',x',y')=\left(\frac{rh}{(1+x)(1+y+(r-1)h)},\;R_Jx h',\;\frac{R_Ayh}{1+y}\right).
\tag{2}
\]

All assertions concern deterministic infinite-precision difference equations, not demographic stochasticity.

## Proof

**1. Invariance and uniform bounds.** Since \(0<h_t\le1\), the assumption \(G(h_t,y_t)\le1\) gives \(0<h_{t+1}\le1\), with strict positivity of all components preserved. Likewise \(x_{t+1}\le R_J\), for all \(t\ge0\), regardless of initial predator density.

**2. Exact multiplicative exclusion identity.** The first two components of (1) yield

\[
x_{t+1}=R_Jx_th_{t+1}.
\]

For strictly positive data define \(q_t=h_ty_t/x_t\). The adult-predator equation and the preceding identity give

\[
\boxed{q_{t+1}=\frac{R_A}{R_J}\frac{q_t}{1+y_t}.}\tag{3}
\]

If \(R_A<R_J\), then \(0<q_t\le q_0(R_A/R_J)^t\). Moreover, \(y_t=R_Jx_{t-1}q_t\le R_J^2q_t\) for \(t\ge2\). Hence \(y_t\to0\) exponentially and, more explicitly, \(y_t\le R_J^2q_0(R_A/R_J)^t\) for \(t\ge2\).

If \(R_A=R_J\), then \(q_{t+1}=q_t/(1+y_t)\), so \(q_t\downarrow q_\infty\ge0\). If \(q_\infty=0\), boundedness of \(x_{t-1}\) and the expression for \(y_t\) again yield \(y_t\to0\). If \(q_\infty>0\), then telescoping the logarithm of (3) shows

\[
\sum_{t=0}^{\infty}\log(1+y_t)=\log(q_0/q_\infty)<\infty.
\]

Since all summands are nonnegative, \(y_t\to0\) in this case as well. Thus the adult-specific predator always tends to extinction when \(R_A\le R_J\). In particular no forward-invariant compact subset of the strictly positive state space can exist for this parameter range. The result excludes positive periodic or other uniformly interior recurrent attractors, not just positive fixed points.

**3. Full strictly positive equilibrium census for Beverton–Holt recruitment.** At any strictly positive fixed point, \(x'=x\) together with \(x'=R_Jxh'\) forces \(h_*=1/R_J\). The adult-predator fixed-point equation forces \(1+y_*=R_A/R_J\). Substitution into the prey equation in (2) then yields \(1+x_*=rR_J/(R_A+r-1)\). These are the only possible coordinates. Strict positivity of \(h_*,x_*,y_*\) is equivalent to \(R_A>R_J\) and \(R_A<1+r(R_J-1)\). Since \(r>1\), the interval is nonempty exactly when \(R_J>1\). Conversely, whenever these strict inequalities hold, the displayed coordinates are strictly positive and direct substitution into all three components of (2) verifies the fixed point. This proves existence, uniqueness, and the sharp necessity of the entire wedge.

**4. Constructive witness.** For \((r,R_J,R_A)=(3,2,3)\), the unique positive equilibrium is exactly \((h_*,x_*,y_*)=(1/2,1/5,1/2)\). Substitution into (2) reproduces all three fractions exactly.

## Verification

The standalone \(\texttt{verify.py}\) checker implements (2) using exact rational arithmetic. It checked \(576\) rational Beverton–Holt transitions and \(54\) transitions for a non-Beverton–Holt admissible recruitment function \(F(z)=2/(1+z^2)\), each confirming (3), the bound on \(x\), and the identity \(x'=R_Jxh'\). It also checked the positive-equilibrium wedge over \(72\) parameter combinations and the rational witness. This computational testing supplements, but is not substituted for, the general algebraic proof above. Run \(\texttt{python verify.py}\) using Python 3 standard library.

## Relationship to prior work

Seno and Goyal (2026), equation (13), provide the common stage-specific recurrence, the negative-binomial escape family in their equation (8), and basic predator replacement parameters in their equations (18)–(19). Their Lemma 6 establishes a necessary replacement ordering for positive *equilibria*, without a global extinction theorem for oscillatory trajectories; their conclusion expressly leaves analytical coexistence dynamics for subsequent analysis. Their detailed example uses exponential escape, a different limit of their negative-binomial family. The present claim concerns the shape-one inverse-linear member and strengthens the equilibrium-only ordering to global predator extinction, while completely resolving equilibrium existence in the Beverton–Holt subcase.

Marcinko and Kot (2020) study a *single* parasitoid with alternative recruitment and escape functions; the system has only two populations and does not imply this two-predator comparison. May–Hassell (1981) and the sequential parasitoid model discussed in the Seno–Goyal introduction differ in the location of density dependence and/or host stages. No claim is made that these foundational model families are new. An unindexed treatment of the same three-species shape-one specialization could have historical priority.

## Limitations

The extinction theorem requires zero adult-prey carryover and shape-one inverse-linear escape for *both* predators. Changing either assumption can break (3). It does not prove the surviving juvenile-specific predator persists, nor that the prey approaches an equilibrium. The exact coexistence wedge applies to Beverton–Holt recruitment and concerns existence/uniqueness of a positive equilibrium, not its stability, global attraction, or permanence of all positive orbits. No extrapolation to finite, stochastic biological populations is asserted.

## References

1. H. Seno and A. Goyal, “Discrete-time exploitative competition model of different stage-specific predators,” *Journal of Mathematical Biology* **93**, article 11 (2026), published 2026-07-03, https://doi.org/10.1007/s00285-026-02427-w.
2. K. Marcinko and M. Kot, “A comparative analysis of host–parasitoid models with density dependence preceding parasitism,” *Journal of Biological Dynamics* **14** (2020), 479–514, https://doi.org/10.1080/17513758.2020.1783005.
