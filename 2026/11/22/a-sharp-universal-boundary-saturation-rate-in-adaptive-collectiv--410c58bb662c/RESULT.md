# A sharp universal boundary-saturation rate in adaptive collective-risk games

## Finding
For the three-variable collective-risk feedback system of Wang et al. [1], there is a parameter regime in which every strictly interior trajectory must approach the union of the minimum-cost face and the maximum-risk face, regardless of the initial cooperation fraction or the payoff scale. The saturation has a universal explicit exponential rate, and this rate is optimal over the admissible model class: a rational example has strictly interior trajectories realizing precisely that slowest exponent. At the critical feedback ratio the same boundary-union attraction still holds, though the exponential bound is not asserted. Two rigorously stable boundary attractors show that the union cannot in general be replaced by either face alone.

Write
\[
 m=\mu_1+\mu_2,\quad s=\theta_3+\theta_4,\quad
 \kappa=\frac{(\alpha-\beta)(\theta_1+\theta_2)}m,\quad
 \rho=\frac{(\theta_1+\theta_2)\mu_1/m-\theta_1+\theta_4}{s}.
\]
For \(\rho>1\), define \(\lambda=(\alpha-\beta)s(\rho-1)>0\). Then for all \(t\ge0\) and every strictly interior initial state,
\[
 \boxed{\min\!\left\{\frac{c(t)-\beta}{\alpha-\beta},1-r(t)\right\}
 \le Q(0)^{1/(1+\kappa)}\exp\left(-\frac{\lambda}{1+\kappa}t\right),}
\]
where
\[
 Q(0)=\frac{c(0)-\beta}{\alpha-c(0)}
 \left(\frac{1-r(0)}{r(0)}\right)^{\kappa}>0.
\]
For \(\rho=1\), the expression inside the minimum tends to zero as \(t\to\infty\). In particular, throughout \(\rho\ge1\) there is no compact forward-invariant set entirely within the open state box.

The rate \(\lambda/(1+\kappa)\) cannot be improved as a theorem uniform over this class: for the rational parameters specified below, \(\lambda/(1+\kappa)=22/31\) and on an open set of strictly interior initial conditions the displayed minimum is asymptotic to a strictly positive constant times \(e^{-22t/31}\).

## Assumptions and scope
Fix integers \(N\ge3\) and \(2\le M\le N-1\), coefficients \(b,\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4>0\), and \(0<\beta<\alpha\). The deterministic, well-mixed population obeys the source's unit-timescale equations [1, Eq. (10)]:
\[
\begin{aligned}
\dot x&=x(1-x)\left[b\binom{N-1}{M-1}x^{M-1}(1-x)^{N-M}r-c\right],\\
\dot r&=r(1-r)[\mu_1-(\mu_1+\mu_2)x],\\
\dot c&=(\alpha-c)(c-\beta)[\theta_1-\theta_4-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r].
\end{aligned}
\]
The initial data satisfy \(x(0),r(0)\in(0,1)\) and \(c(0)\in(\beta,\alpha)\). A polynomial vector field is bounded on the invariant closed box, hence solutions exist globally; logistic factors and bounded logit derivatives prevent finite-time departure from the open box. The parameter \(\rho\) is a feedback-ratio threshold, not a probability when it exceeds one. The estimate's initial-state-dependent multiplicative constant is explicit; only its exponential *rate* is uniform.

## Proof
**Exact feedback identity.** Define risk and cost logits \(v=\log[r/(1-r)]\) and \(w=\log[(c-\beta)/(\alpha-c)]\). Direct differentiation, using the above equations, yields
\[
\dot v=\mu_1-mx,\qquad
\dot w=(\alpha-\beta)[\theta_1-\theta_4-(\theta_1+\theta_2)x+sr].
\]
With \(\kappa=(\alpha-\beta)(\theta_1+\theta_2)/m\), the cooperation terms cancel:
\[
\boxed{\frac{d}{dt}(w-\kappa v)=(\alpha-\beta)s(r-\rho).}
\]
Consequently \(Q=e^{w-\kappa v}\) is the positive expression stated above. The log-odds cancellation itself is an existing tool of the related published analysis [2], which treated a disjoint feedback-sign region; the global optimal boundary-union rate proved here is the contribution.

**Supercritical uniform saturation.** If \(\rho>1\), the identity implies \(Q(t)\le Q(0)e^{-\lambda t}\), because \(r(t)<1\). Put \(a=(c-\beta)/(\alpha-\beta)\in(0,1)\) and \(u=1-r\in(0,1)\). The exact algebraic formula for \(Q\) gives
\[
 a u^\kappa=Q(1-a)r^\kappa\le Q.
\]
Since \(\min\{a,u\}^{1+\kappa}\le a u^\kappa\), taking the \((1+\kappa)\)-th root proves the claimed inequality. The distance to the union of the two specified closed boundary faces therefore tends to zero. A compact invariant set strictly inside the open box would have its minimum bounded below and is impossible.

**Critical feedback.** At \(\rho=1\), integration gives
\[
 Q(t)=Q(0)\exp\left(-(\alpha-\beta)s\int_0^t(1-r(q))\,dq\right).
\]
If \(\int_0^\infty(1-r(q))\,dq=\infty\), then \(Q(t)\to0\) and the preceding product inequality still implies \(\min\{a,u\}\to0\). Otherwise \(u(t)=1-r(t)\to0\): indeed \(u\ge0\) is uniformly continuous because the bounded vector field makes \(\dot u\) uniformly bounded, and any nonnegative uniformly continuous integrable function tends to zero. Again the minimum tends to zero. Any compact interior forward-invariant trajectory would force \(1-r\ge\varepsilon>0\), hence \(Q\to0\), contradicting boundedness of its logarithm on that compact set.

**A stable rational example attaining the optimal exponent.** Let
\[
 (N,M)=(3,2),\quad(\mu_1,\mu_2)=(4,1),\quad
 (\theta_1,\theta_2,\theta_3,\theta_4)=(1,4,1,1),
 \quad(\beta,\alpha)=(1/5,3/4),\quad b=4805/10812.
\]
Then \(\rho=2\), \(\kappa=11/20\), \(\lambda=11/10\), and the equilibrium
\[
 E_*=\left(\frac{102}{155},1,\frac15\right)
\]
is asymptotically stable: its Jacobian is upper triangular with diagonal eigenvalues \(-49/775,-22/31,-22/31\). In particular, its attracting neighborhood contains strictly interior points. Along every such strictly interior trajectory converging to \(E_*\), local hyperbolic stability gives \(x(t)-102/155=O(e^{-\eta t})\), \(1-r(t)=O(e^{-\eta t})\), and \(c(t)-1/5=O(e^{-\eta t})\) for some \(\eta>0\). The scalar logarithmic derivatives satisfy
\[
 \frac{d}{dt}\log(1-r(t))=-\frac{22}{31}+O(e^{-\eta t}),\quad
 \frac{d}{dt}\log(c(t)-1/5)=-\frac{22}{31}+O(e^{-\eta t}).
\]
Their error terms are integrable. Integration proves the existence of strictly positive, finite constants \(C_r,C_c\) such that
\[
 1-r(t)\sim C_r e^{-22t/31},\qquad
 c(t)-1/5\sim C_c e^{-22t/31}.
\]
Thus the minimum in the theorem is asymptotic to \(\min\{C_c/(11/20),C_r\}e^{-22t/31}\); no larger universal exponent is possible even on this fixed rational instance.

**Why both boundary faces are essential.** Keep the same coefficients except set \(b=1\). The corner \(E_0=(0,1,3/4)\) has Jacobian eigenvalues \(-3/4,-4,-11/10\), whereas the different boundary equilibrium \(E_1=(4/5,5/8,1/5)\) has eigenvalues \(-121/80\) and \(-3/50\pm i\sqrt{141}/50\). Both are asymptotically stable, and each has an open set of strictly interior initial states in its basin. Trajectories tending to \(E_0\) do not have \(c\to\beta\), and those tending to \(E_1\) do not have \(r\to1\). Hence the disjunction is structurally unavoidable. The existence and possible stability of boundary equilibria were already discussed by [1]; their role here is to establish that the new *global union* theorem cannot be strengthened to either individual face.

**Outside the feedback regime.** For example, \((N,M)=(3,2)\), \(b=2\), \(\mu_1=\mu_2=1\), all \(\theta_j=1\), and \((\beta,\alpha)=(1/5,4/5)\) give \(\rho=1/2\) and a fully interior equilibrium \((x,r,c)=(1/2,1/2,1/2)\). Thus an unrestricted extension of the boundary-union conclusion into \(\rho<1\) is false.

## Verification
The standalone script `verification/check.py` (Python and SymPy) independently verifies the symbolic feedback-logit identity, rational equilibria, Jacobian characteristic polynomials and rate values by exact arithmetic. Additionally, the sharpness witness has Jacobian eigenvalues \(-49/775,-22/31,-22/31\), obtained directly by symbolic differentiation. The global time-asymptotic claims depend on the analytical proof, not the finite calculation.

## Relationship to prior work
Wang et al. [1] introduce exactly this feedback system and classify boundary and interior equilibria, including coexistence and bistability. This result does not claim those models, equilibria, or local stability concepts as new. Published analysis [2] already derives the risk–cost logit cancellation for its condition \(\Delta>0\), equivalent to \(\rho<0\), and proves upper-cost selection and global collapse under additional assumptions. The present feedback region \(\rho\ge1\) is disjoint. In contrast to a merely sign-reversed logit inequality, the result supplies a quantitative, globally valid union-of-boundaries law, handles critical equality, and proves the exponential rate optimal using a matched-eigenvalue stable rational equilibrium. The related five-dimensional environmental model [3] also has logit cancellations, but its governing variables and equations differ and it provides no statement on the three-variable system's optimal attraction rate. The two-variable collective-risk model [4] omits adaptive cost.

## Limitations
The exponent \(\lambda/(1+\kappa)\) is optimal as a *universal* exponent; particular parameters or initial states may converge more rapidly. The theorem neither selects which face eventually attracts a given state nor proves convergence to a single equilibrium. At \(\rho=1\) it asserts attraction without a rate. It is not a result for the paper's modified model with cost-to-risk feedback, stochastic finite populations, arbitrary update speeds, or different environmental response laws. Published S1 supporting material of [1] was not fully inspected; it and unindexed articles are a residual historical-priority risk. No independent scientific audit is claimed.

## References
[1] L. Wang, S. Hua, Y. Liu, L. Zhang, L. Liu and A. Szolnoki, “Coevolutionary dynamics of cooperation, risk, and cost in collective risk games,” *PLOS Computational Biology* **22**, e1013512 (2026), first publicly released 2026-02-20. DOI: https://doi.org/10.1371/journal.pcbi.1013512; complete open main text: https://pmc.ncbi.nlm.nih.gov/articles/PMC12923141/.

[2] “Global collapse despite positive coexistence equilibria under risk–cost feedback,” publicly available mathematical analysis, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-global-collapse-despite-positive-coexistence-equilibria-under-ri--238b78f6c336.

[3] K. Betz, F. Fu and N. Masuda, “Evolutionary game dynamics with environmental feedback in a network with two communities,” arXiv:2404.17082, first public 2024-04-25, https://arxiv.org/html/2404.17082v2; see also “A feedback-resonance boundary forbids interior recurrence in two-community eco-evolutionary games,” https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-feedback-resonance-boundary-forbids-interior-recurrence-in-two--55fe6065bbf9.

[4] L. Liu, X. Chen and A. Szolnoki, “Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game,” *eLife* **12**, e82954 (2023), https://doi.org/10.7554/eLife.82954.
