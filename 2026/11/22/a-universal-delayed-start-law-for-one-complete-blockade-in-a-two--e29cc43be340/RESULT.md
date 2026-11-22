# A universal delayed-start law for one complete blockade in a two-stage transmission chain

## Finding

Consider the single-source, single-target continuous-time transmission chain specified below. For every choice of positive progression rate \(\alpha\), transmission rate \(\beta\), recovery rate \(\gamma\), and prescribed complete-blockade duration \(L\), there is **exactly one** start time \(s_*(L)\geq0\) minimizing the eventual chance that the target is infected. It is strictly positive for every finite \(L>0\), is strictly decreasing as \(L\) grows, and converges to zero only as \(L\to\infty\).

Write \(r=\beta+\gamma\), \(d=r-\alpha\), and
\[
 m_L=\frac{\gamma}{e^{\gamma L}-1}\int_0^L e^{(\gamma-\alpha)u}\,du.
\]
Then \(0<m_L<1\), and the unique global optimum over every \(s\in[0,\infty)\) is
\[
 s_*(L)=\begin{cases}
 -\dfrac{\log(1-dm_L/r)}{d},&d\ne0,\\[6pt]
 \dfrac{m_L}{r},&d=0.
 \end{cases}
\]
In addition,
\[
 \lim_{L\downarrow0}s_*(L)=
 \begin{cases}\dfrac{\log(r/\alpha)}{r-\alpha},&r\ne\alpha,\\[5pt]
 1/r,&r=\alpha,\end{cases}
 \qquad\lim_{L\to\infty}s_*(L)=0.
\]
The short-blockade limit is the mode of the uncontrolled infectious-but-not-yet-transmitted probability. Thus for every strictly positive finite duration, the best block starts before that peak but **not** immediately.

## Assumptions and scope

At time zero one source is in a latent, nontransmitting stage \(E\). Its independent exponential progression clock has rate \(\alpha>0\). After progression, the source is infectious, denoted \(I\). While \(I\), the source transmits to exactly one initially susceptible target at rate \(\beta>0\), or recovers irreversibly without transmitting at rate \(\gamma>0\). The two competing clocks are independent while active; at most one transmission event is relevant. Recovery also operates during a blockade, and no reinfection, replenishment, secondary chains, or feedback occurs.

A precommitted intervention switches **only the transmission transition** off, completely, on the single interval \([s,s+L]\), with start \(s\geq0\) and fixed length \(L>0\). Progression and recovery retain their original rates. Normal transmission resumes after \(s+L\), if the source is still infectious and the target susceptible. There are no costs other than fixed duration, no observations or adaptivity, and no terminal deadline. The quantity minimized is the probability of target transmission at any finite time, equivalently by time infinity. It is not a population-level epidemic final-size or peak-prevalence objective.

## Proof

**1. No-intervention law.** Put \(r=\beta+\gamma\). Without blocking, the competing-event probability of eventual target transmission, starting from either the latent stage or the infectious stage, is \(\beta/r\). The probability of being infectious *without earlier transmission or recovery* at a prospective start time \(s\) is
\[
 p_I(s)=\alpha\int_0^s e^{-\alpha t}e^{-r(s-t)}\,dt
 =\begin{cases}
 \dfrac{\alpha(e^{-\alpha s}-e^{-rs})}{r-\alpha},&r\ne\alpha,\\[6pt]
 \alpha s e^{-\alpha s},&r=\alpha.
 \end{cases}
\]
The latent-stage probability at that time is \(e^{-\alpha s}\).

**2. Exact saved transmission probability.** Set
\[
 A_L=1-e^{-\gamma L},\quad
 K_L=\int_0^L e^{-\alpha u}e^{-\gamma(L-u)}\,du,\quad
 M_L=\int_0^L e^{-\alpha u}\bigl(1-e^{-\gamma(L-u)}\bigr)\,du.
\]
If already infectious at the start, blocking saves the baseline transmission probability \(\beta/r\) precisely when recovery takes place during the next \(L\) units of time, an event of probability \(A_L\). If still latent, progression at offset \(u\in[0,L]\) has probability density \(\alpha e^{-\alpha u}\), and protection succeeds precisely when recovery precedes the block's end, with probability \(1-e^{-\gamma(L-u)}\). Total probability gives the *exact* improvement
\[
 S_L(s)=\frac{\beta}{r}\bigl[A_Lp_I(s)+\alpha e^{-\alpha s}M_L\bigr],
 \qquad P_L(s)=\frac{\beta}{r}-S_L(s).
\]
If latent throughout the blockade or infectious but not recovered by its end, the normal competing risks resume and the eventual conditional transmission probability remains \(\beta/r\); thus no further terms are omitted.

**3. Derivative and unique global optimum.** Direct integration or integration by parts yields \(\alpha M_L+\gamma K_L=A_L\). With
\[
 m_L=\frac{\gamma K_L}{A_L}
 =\frac{\gamma}{e^{\gamma L}-1}\int_0^L e^{(\gamma-\alpha)u}\,du,
\]
and \(p_I'(s)=\alpha e^{-\alpha s}-rp_I(s)\), differentiation gives
\[
 S_L'(s)=\frac{\alpha\beta A_L}{r}e^{-\alpha s}
 \left[m_L-\Phi_d(s)\right],\qquad
 \Phi_d(s)=\begin{cases}
 \dfrac{r(1-e^{-ds})}{d},&d\ne0,\\[5pt]
 rs,&d=0.
 \end{cases}
\]
Every multiplier outside the brackets is strictly positive. The quantity \(m_L\) is an expectation of \(e^{-\alpha U}\) for \(U\) supported strictly on \((0,L)\), so \(0<m_L<1\). On \([0,\infty)\), \(\Phi_d\) is strictly increasing from zero, with derivative \(re^{-ds}>0\). If \(d\le0\) its limit is infinite; if \(d>0\), its limit is \(r/d>1\). Thus the equation \(\Phi_d(s)=m_L\) has exactly one strictly positive solution. At smaller \(s\), \(S_L'>0\); at larger \(s\), \(S_L'<0\). This proves unique *global* maximization of saved transmission, hence unique global minimization of eventual target infection, including the boundary \(s=0\) and the limit \(s\to\infty\). Solving the scalar equation gives the displayed formula, including its continuous \(d=0\) branch.

**4. Strict duration monotonicity and both limits.** Let \(U_L\) have density
\[
 f_L(u)=\frac{\gamma e^{\gamma u}}{e^{\gamma L}-1},\quad 0<u<L.
\]
Then \(m_L=\mathbb E[e^{-\alpha U_L}]\). For every \(L_2>L_1>0\), \(U_{L_2}\) strictly stochastically dominates \(U_{L_1}\): its distribution function on \((0,L_1)\) is \((e^{\gamma u}-1)/(e^{\gamma L_2}-1)\), strictly below the same expression with \(L_1\) in the denominator. Because \(e^{-\alpha u}\) is strictly decreasing, \(m_{L_2}<m_{L_1}\). The inverse of \(\Phi_d\) is strictly increasing, so \(s_*(L)\) is strictly decreasing. As \(L\downarrow0\), the support of \(U_L\) shrinks to zero and \(m_L\to1\); inversion gives the stated limiting mode. As \(L\to\infty\), \(U_L\to\infty\) in probability and hence \(m_L\to0\) by bounded convergence, yielding \(s_*(L)\to0\). All rate coincidences are covered by continuous limiting formulas.

**5. An exact strict example.** Take \(\alpha=2\), \(\beta=2\), \(\gamma=1\), and \(L=\log 2\). Then \(r=3\), \(d=1\), \(m_L=1/2\), and \(s_*=\log(6/5)\). The improvement and infection probabilities are
\[
 S_L(s)=\frac56e^{-2s}-\frac23e^{-3s},\qquad
 P_L(s)=\frac23-\frac56e^{-2s}+\frac23e^{-3s}.
\]
The uniquely optimal start produces \(S_L(s_*)=125/648\) and \(P_L(s_*)=307/648\). Immediate protection instead yields \(S_L(0)=1/6\) and \(P_L(0)=1/2\). The exact strictly positive infection-risk reduction from delaying the block is therefore \(17/648\).

## Verification

The adjacent standalone `checker.py` uses exact fractions for the strict-example probabilities and a separately implemented fourth-order Runge–Kutta integration of the three-state forward equations. The test suite passed 1,231 checks over 68 fixed-seed parameter configurations, including the repeated-rate case, multiple start choices and multiple blockade lengths. This computational work corroborates the formulas; the general quantified statements follow from the proof above. Reproduction: with Python 3.10 or newer, run `python checker.py` in the directory containing both files.

## Relationship to prior work

Hollingsworth et al. (2011) provide early analysis of delayed interventions for nonlinear epidemic dynamics and multiple competing population-level objectives. Shim (2013) analyzes optimally controlled vaccination and distancing in a stratified influenza model. Di Lauro, Kiss and Miller (2021) analyze one-shot reductions in transmission in nonlinear epidemic models for total case counts, peak prevalence and delay. Britton and Leskelä (2023) prove a general single-interval intervention law for nonlinear classical SIR final incidence under a linear control-cost budget. These studies motivate the scheduling question, but their nonlinear susceptible-depletion models and collective outcome measures do not directly imply the exact individual exposure–transmission–recovery competing-risk theorem here. In particular, the present result has neither susceptible depletion nor a rebound epidemic; delaying the finite blockade is optimal because the source is initially noninfectious and can recover while contacts are blocked.

## Limitations

Only one source and one target, exponential latent progression, independent exponential transmission and recovery, perfect single-interval blockade, precommitted timing, and an infinite horizon are treated. Imperfect controls, heterogeneous latent distributions, observation-based schedules, interacting transmission networks, variable effort and multiple blocks may change the conclusion. The result does not claim a better clinical or public-health policy. A broader equivalence in old queueing, stochastic control or competing-risk literature has not been excluded definitively; the claimed novelty is this exact fully specified theorem under the cited mathematical literature comparisons, not first discovery of delayed interventions generally. No independent scientific audit has been performed.

## References

1. Hollingsworth, T. D., Klinkenberg, D., Heesterbeek, H., and Anderson, R. M. (2011). *Mitigation strategies for pandemic influenza A: balancing conflicting policy objectives*. PLOS Computational Biology 7(2): e1001076. https://doi.org/10.1371/journal.pcbi.1001076 (published February 10, 2011).
2. Shim, E. (2013). *Optimal strategies of social distancing and vaccination against seasonal influenza*. Mathematical Biosciences and Engineering 10(5–6): 1615–1634. https://doi.org/10.3934/mbe.2013.10.1615.
3. Di Lauro, F., Kiss, I. Z., and Miller, J. C. (2021). *Optimal timing of one-shot interventions for epidemic control*. PLOS Computational Biology 17(3): e1008763. https://doi.org/10.1371/journal.pcbi.1008763.
4. Britton, T., and Leskelä, L. (2023). *Optimal intervention strategies for minimizing total incidence during an epidemic*. SIAM Journal on Applied Mathematics. https://doi.org/10.1137/22M1504433.
5. Feng, Y., Iyer, G., and Li, L. (2021). *Scheduling fixed length quarantines to minimize the total number of fatalities during an epidemic*. Journal of Mathematical Biology 82: 69. https://doi.org/10.1007/s00285-021-01615-0 (complete mathematical model and Theorem 1.1 inspected via an open-author PDF).
