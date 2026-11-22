# Sharp weak-selection threshold for hybrid imitation–introspection public-goods learning

## Finding

Consider a finite heterogeneous linear public-goods game with at least one Fermi imitator and at least one counterfactual introspector. With the stochastic updating rule specified below, the stationary mean cooperator share has a **sharp first-order crossing** at an explicit return multiplier \(r_*\), strictly above the all-introspector threshold \(N\). This formula is valid for every population size, every positive contribution profile, and symmetric mutation down to zero:

\[
\begin{aligned}
\kappa&=\frac{1-2\mu}{2N(N-1)},&d&=\frac{2\mu}{N},\\
c&=\frac{\kappa}{h\kappa+d+1/N},&
b&=\frac{\kappa(1+hc)}{(h+1)\kappa+d},\\
Q&=(1-c)(hA_E+eA_H)+2(e-1)(1-b)A_E,\\
r_*&=N\left(1+\frac{\kappa Q}{2(1-2\mu)(N\kappa+d)A_H}\right).
\end{aligned}
\]

Here \(e\) and \(h\) count imitators and introspectors, \(A_E\) and \(A_H\) are their respective total contributions, and \(e+h=N\). For \(e=1\), the term involving \(b\) is zero, so \(b\) is only an algebraic auxiliary, not an observable pair correlation.

For fixed parameters and return multiplier \(r>0\), as the common choice sensitivity \(\beta\downarrow0\),

\[
\boxed{\displaystyle
p_C(\beta,r)=\frac12+
\beta\frac{(1-2\mu)(N\kappa+d)A_H}{4N^2(h\kappa+d)}(r-r_*)
+O(\beta^2).}
\]

Consequently, for every fixed \(r\ne r_*\), all sufficiently small positive \(\beta\) give stationary cooperation strictly above one half precisely when \(r>r_*\). Equality at \(r=r_*\) is a vanishing **linear-response coefficient**, not a claim that the finite-sensitivity abundance is exactly one half.

The threshold depends on the heterogeneity of contributions **only through the total contributions of the two learning types**. In the mutation-free, equal-contribution case with exactly one introspector, its particularly simple exact form is

\[
\boxed{r_*=\frac{N^3}{2N-1},\qquad N\ge2.}
\]

Thus a fixed single introspector must face a return of quadratic rather than linear order in population size to overcome Fermi imitation's cooperation deficit in weak selection. More generally, with zero mutation, equal contributions, and \(1\le h<N\),

\[
\frac{r_*}{N}=1+\frac{N-h}{h+1}\,\frac{2N+h-3}{2N+h-2}.
\]

## Assumptions and scope

Fix an integer \(N\ge2\). Partition the individuals into a nonempty set \(E\) of \(e\) Fermi imitators and a nonempty set \(H\) of \(h=N-e\) introspectors. Each has a fixed positive contribution \(\alpha_i>0\). A state is a vector \(x\in\{0,1\}^N\), where \(1\) means cooperation. At state \(x\), individual \(i\) receives

\[
\pi_i(x)=\frac rN\sum_{j=1}^{N}\alpha_jx_j-\alpha_i x_i,
\]

where \(r>0\) is the common public-goods return multiplier.

At each discrete time step, independently select a uniformly random focal individual \(i\). With probability \(2\mu\), replace that player's action by a uniformly random action (possibly the same action); with complementary probability \(1-2\mu\), use the player's fixed update rule. Assume \(0\le\mu<1/2\). An imitator samples \(j\ne i\) uniformly and copies \(j\)'s current action with probability \(\phi_\beta(\pi_i(x)-\pi_j(x))\), where \(\phi_\beta(u)=1/(1+\exp(\beta u))\). An introspector instead switches to the opposite action with probability \(\phi_\beta(\pi_i(x)-\pi_i(x^{(i)}))\), where \(x^{(i)}\) flips coordinate \(i\). Otherwise the state remains unchanged. Only one focal action may change at a time.

For every finite \(\beta\ge0\), this chain is irreducible and aperiodic, even when \(\mu=0\): an introspector can produce either action and an imitator can copy a suitable role model with strictly positive probability. Hence the stationary law and its mean share \(p_C(\beta,r)\) are uniquely defined and analytic near \(\beta=0\). The error term is for fixed \(N,e,h,\mu,\alpha,r\); it is not uniform as \(r\) or \(N\) grows with inverse sensitivity.

## Proof

**1. Neutral dynamics and spin covariances.** Set \(S_i=2x_i-1\) and \(t=1-2\mu\). At \(\beta=0\), every introspector flips with probability \(1/(2N)\) per step, while an imitator has a neutral copying coefficient \(\kappa=t/[2N(N-1)]\) and an unbiased mutation drift \(-dS_i\), where \(d=2\mu/N\). The conditional one-step spin drifts are

\[
\begin{aligned}
\mathbb E[\Delta S_i\mid x]&=\kappa\sum_{j\ne i}(S_j-S_i)-dS_i &&(i\in E),\\
\mathbb E[\Delta S_i\mid x]&=-S_i/N &&(i\in H).
\end{aligned}
\]

The neutral chain is invariant under the simultaneous swap of the two actions. Its unique stationary law therefore gives \(\mathbb E S_i=0\). Two distinct introspectors have zero stationary spin correlation: each flips at a constant rate independently of the others' actions, and the equation for their product has a strictly negative coefficient.

For an imitator \(i\) and introspector \(j\), stationarity of \(S_iS_j\) yields, using that only one spin changes in a step,

\[
0=\kappa-(h\kappa+d+1/N)\,\mathbb E(S_iS_j).
\]

Thus every imitator–introspector correlation equals \(c\). For distinct imitators \(i,j\), stationarity of their product similarly yields

\[
0=\kappa(1+hc)-((h+1)\kappa+d)\,\mathbb E(S_iS_j),
\]

so their correlation equals \(b\). These identities are **exact finite-population identities**, not mean-field factorization. The formulas imply \(0\le c<1\) and, whenever an imitator pair exists, \(0\le b<1\).

**2. First-order selection forces.** Let \(m_i=\left.\frac{d}{d\beta}\mathbb E_{\beta}S_i\right|_{\beta=0}\), with the expectation under the stationary law. Differentiating the introspector switching probabilities at neutrality gives

\[
 m_i=\frac{t\alpha_i}{2}\left(\frac rN-1\right),\qquad i\in H.
\]

Therefore the sum over introspectors is \(M_H=\frac t2 A_H(r/N-1)\). For an imitator \(i\), the first-order selection forcing in the stationary spin-drift equation is

\[
F_i=-\frac{\kappa}{4}\sum_{j\ne i}(\alpha_i+\alpha_j)\bigl(1-\mathbb E_0[S_iS_j]\bigr).
\]

Indeed, when a defector copies a cooperator the derivative of the Fermi probability is \(-\alpha_j/4\); when a cooperator copies a defector it is \(+\alpha_i/4\). Multiplying by spin increments \(\pm2\), and using \(\mathbb E_0[(1-x_i)x_j]=\mathbb E_0[x_i(1-x_j)]=(1-\mathbb E_0[S_iS_j])/4\), proves this force formula. Summing over imitators and using the neutral correlations gives \(F_E=\sum_{i\in E}F_i=-\kappa Q/4\).

**3. Exact first-moment closure for the derivative.** Summing the stationary imitator drift equations eliminates all imitator–imitator copying terms. Writing \(M_E=\sum_{i\in E}m_i\), the remaining identity is

\[
0=\kappa(eM_H-hM_E)-dM_E-\frac{\kappa Q}{4}.
\]

Consequently,

\[
M_E+M_H=
\frac{(N\kappa+d)M_H-\kappa Q/4}{h\kappa+d}.
\]

Since \(p_C=1/2+(1/(2N))\sum_i\mathbb E S_i\), division by \(2N\) and the definition of \(r_*\) prove the displayed expansion. All denominators are positive. The strictly positive summand \((1-c)(hA_E+eA_H)\) gives \(Q>0\); thus \(r_*>N\) and the crossing has strictly positive slope.

**4. Equal-contribution zero-mutation simplification.** For \(\mu=0\) and all \(\alpha_i=1\), direct substitution gives \(c=1/(2N+h-2)\), \(1-b=h(1-c)/(h+1)\) and \(Q=2ehN(1-c)/(h+1)\). Substitution into \(r_*\) gives the stated general expression. At \(h=1\), it simplifies exactly to \(N^3/(2N-1)\). This is a rational algebraic identity for all integers \(N\ge2\).

## Verification

The included Python-standard-library program `verify_hybrid.py` constructs the full transition matrix independently from the defining update rules. It verifies the exact eight-state first-order stationary perturbation coefficient

\[
\left.\frac{\partial p_C}{\partial\beta}\right|_{\beta=0}
=\frac{56r-323}{1260}
\]

for the three-individual example with two imitators, one introspector, unit contributions and \(\mu=1/10\). Its exact crossing is \(r_*=323/56\). The program also tests 90 finite-chain numerical derivatives across population sizes \(2\)–\(5\), different type mixes, return multipliers, and mutation levels including zero, plus 19 exact rational single-introspector identities. Run `python3 verify_hybrid.py` in the directory containing this document and the program. These tests check arithmetic and conventions; the all-size conclusion follows from the proof above, not from enumerating small populations.

## Relationship to prior work

Foster, Knight and Krapohl (arXiv:2606.31740, June 30, 2026) establish the extrinsic cooperation ceiling for purely imitative dynamics and explicitly discuss rule mixing as a future direction. Their exploratory mixed-rule figure uses Moran and introspection; it does not present this finite-population Fermi–introspection stationary linear-response formula. Their earlier introspection result (arXiv:2605.23513) proves a product stationary law for *pure* introspection: it cannot be substituted into the hybrid model because imitation generates nonzero neutral cross-agent correlations. Couto and Pal (2023) similarly analyze pure introspection in asymmetric games.

Amaral and Javarone (Physical Review E 97, 042305, 2018) explicitly combine Fermi imitation with counterfactual Logit innovation and solve a mean-field equation for two-person matrix games, with further simulations on networks. That publication is essential prior art for the **hybrid mechanism**, but its infinite-population mean-field game and its displayed thresholds do not give the exact finite, heterogeneous, mutation-regularized stationary derivative or the quadratic one-introspector threshold obtained here. Takesue (arXiv:1903.09570, 2019) combines imitation with aspiration-based updating in spatial prisoner's dilemmas, an importantly different intrinsic rule. These comparisons concern the specific proved formula, not a novelty claim for mixing update types itself.

## Limitations

This is an exact **weak-choice-sensitivity first-order** theorem. At \(r=r_*\) the first derivative vanishes; the sign at small nonzero sensitivity is not established by the stated expansion. For a fixed positive sensitivity, the global crossover may be different or may not occur. The approximation is not uniform over growing return multipliers or growing populations. Mean stationary cooperation is not an absorption probability, and no experimental behavioral assertion is made. The all-size proof is analytic; the accompanying finite computations are diagnostics. Literature priority is bounded by the explicitly inspected sources and search coverage, and has not been independently validated.

## References

1. H. Foster, V. Knight, S. Krapohl, *The Cooperation Ceiling: Extrinsic Population Dynamics and the Intrinsic Escape*, arXiv:2606.31740 (first public version June 30, 2026). https://arxiv.org/abs/2606.31740
2. H. Foster, V. A. Knight, S. Krapohl, *An Exact Cooperation Formula for Introspection Dynamics in the Heterogeneous Public Goods Game*, arXiv:2605.23513 (first public version May 22, 2026). https://arxiv.org/abs/2605.23513
3. M. A. Amaral, M. A. Javarone, *Heterogeneous update mechanisms in evolutionary games: Mixing innovative and imitative dynamics*, Physical Review E **97**, 042305 (2018). https://doi.org/10.1103/PhysRevE.97.042305
4. H. Takesue, *Roles of mutation rate and co-existence of multiple strategy updating rules in evolutionary prisoner's dilemma games*, arXiv:1903.09570 (2019). https://arxiv.org/abs/1903.09570
5. M. Couto, S. Pal, *Introspection Dynamics in Asymmetric Multiplayer Games*, Dynamic Games and Applications **13** (2023). https://doi.org/10.1007/s13235-023-00525-8
