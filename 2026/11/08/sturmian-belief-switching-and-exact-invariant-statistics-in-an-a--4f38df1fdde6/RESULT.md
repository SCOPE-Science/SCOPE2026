# Sturmian belief switching and exact invariant statistics in an anti-confirmation update

## Finding

Consider the scalar biased Bayesian update from Dong and Marzen [1], with no sender-dependent in-group bias:
\[
F(b)=\begin{cases}
\displaystyle\frac{b}{b+\gamma_\ell(1-b)},&0<b<\frac12,\\[4pt]
\displaystyle\frac{b}{b+\gamma_h(1-b)},&\frac12\le b<1,
\end{cases}
\qquad 0<\gamma_\ell<1<\gamma_h.
\]
Put \(a=\log(1/\gamma_\ell)>0\), \(c=\log\gamma_h>0\), \(L=a+c\), and \(\alpha=a/L\). Every interior orbit enters the invariant log-odds interval \([-c,a)\) in finitely many updates. On that interval the dynamics is exactly the rigid circle rotation by \(\alpha\), via the coordinate \(\theta=(\log(b/(1-b))+c)/L\pmod1\). Consequently:

1. If \(\alpha=p/q\) in lowest terms, every interior trajectory becomes exactly periodic with least period \(q\). If \(\alpha\) is irrational, no interior trajectory is eventually periodic: all have the same dense recurrent belief interval, the unique invariant probability on this interval has density \(\rho(b)=1/[L b(1-b)]\), and every interior orbit is equidistributed for that law. In either case the recurrent dynamics has no attracting isolated cycle; every differentiable interior orbit has asymptotic Lyapunov exponent zero.
2. For any orbit after its finite entrance, let \(H_k=\mathbf1_{\{b_k\ge1/2\}}\) and \(\theta_0\in[0,1)\) denote the entrance phase. For every \(k\ge0\),
\[
H_k=\lfloor\theta_0+(k+1)\alpha\rfloor-\lfloor\theta_0+k\alpha\rfloor.
\]
Therefore, for every consecutive block of \(n\ge1\) updates, \(\left|\sum H_k-n\alpha\right|<1\). If \(\alpha\) is irrational this binary threshold itinerary is Sturmian: it is aperiodic and every two equally long blocks differ in their number of high-belief observations by at most one.
3. In the irrational case the exact time-averaged belief, independently of initial interior belief, is
\[
\overline b=\frac{\log(1+e^a)-\log(1+e^{-c})}{a+c},
\qquad
\lim_{n\to\infty}\frac1n\sum_{k<n}H_k=\alpha.
\]

For the exact likelihood ratios associated with the cycling parameters displayed in [1], \(\gamma_\ell=3/17\) and \(\gamma_h=13/7\) (reported to three significant digits as \(0.176\) and \(1.86\)), the rotation is irrational. In particular, the recurrent interval of beliefs is \([7/20,17/20]\) in the sense of orbit closure, the high-belief fraction is
\[
\frac{\log(17/3)}{\log(221/21)}\approx0.73698648093,
\]
and the exact time-averaged belief is
\[
\frac{\log(13/3)}{\log(221/21)}\approx0.62300815097.
\]
These predictions are deterministic and do not depend on the initial interior belief or on the network's ordering of the agent's update times.

## Assumptions and scope

The original scalar update is performed once per *local update count*, with \(b\in(0,1)\), the strict lower branch \(b<1/2\), and the upper branch including the tie \(b=1/2\). There is no coupling through sender beliefs; this is exactly the independent-agent case called confirmation-bias-only in [1, Section III.2]. Statements about times and averages are in the number of updates *of the specified agent*, not elapsed global network time. For multiple agents, the theorem applies componentwise whenever each has the same two multipliers and is updated infinitely often; it makes no claim about joint synchronized observables or state-dependent schedule weights.

For rational \(\alpha\), no uniqueness of invariant probability is claimed: the invariant interval is foliated by neutral periodic orbits. For irrational \(\alpha\), the uniqueness statement concerns the recurrent **interior** interval; the excluded endpoint beliefs \(b=0\) and \(b=1\) are fixed by the full Bayesian formula. The density is on the half-open invariant interval \([1/(1+e^c),1/(1+e^{-a}))\), with the two endpoints identified for the circle representation.

The exact-fraction parameter specialization follows the likelihood ratios underlying the rounded numbers in [1]. If those printed decimals are instead treated as *exact*, \(\gamma_\ell=22/125\) and \(\gamma_h=93/50\), the same irrational-rotation, Sturmian, no-cycle and zero-Lyapunov conclusions hold, with endpoints \(50/143\) and \(125/147\) and the general formulas above. They are not exactly the fraction-based endpoints \(7/20\) and \(17/20\).

## Proof

**1. Odds conjugacy and entrance.** With \(u=\log(b/(1-b))\), direct algebra gives
\[
\frac{F(b)}{1-F(b)}=\frac{b}{\gamma(1-b)},
\qquad
u_{k+1}=\begin{cases}u_k+a,&u_k<0,\\u_k-c,&u_k\ge0.\end{cases}
\]
If \(u<-c\), each update adds \(a>0\) until \(u\ge-c\); the crossing update leaves \(u<a\), since its predecessor was below \(-c\). If \(u\ge a\), each update subtracts \(c>0\) until \(u<a\), with the crossing update still above \(-c\). Thus every finite interior \(u\) enters \(I=[-c,a)\) in finitely many steps. The branch formulas map \(I\) into itself. The bijection \(\theta=(u+c)/L\in[0,1)\) satisfies \(\theta_{k+1}=\{\theta_k+\alpha\}\), where \(\{\cdot\}\) is fractional part: for \(u<0\), \(\theta<1-\alpha\) and the addition does not wrap; for \(u\ge0\), it wraps exactly once.

**2. Orbit and coding.** Rotation by rational \(p/q\) has least period \(q\) everywhere; rotation by irrational \(\alpha\) has no periodic points and every orbit is dense and equidistributed on the circle. In the latter case normalized length is the unique invariant Borel probability for the circle rotation. Its inverse logit push-forward yields \(db/\{L b(1-b)\}\), because \(du/db=1/[b(1-b)]\). The high branch is \(u\ge0\), equivalent to \(\theta\ge c/L=1-\alpha\). For \(\theta_k=\{\theta_0+k\alpha\}\), the branch indicator is therefore the difference of consecutive floors written above. The differences telescope. For any initial phase and any starting index \(j\), the count in \(n\) consecutive updates is \(\lfloor\theta_j+n\alpha\rfloor\), which differs from \(n\alpha\) by less than one. Every two blocks of length \(n\) have counts in the two consecutive integers bracketing \(n\alpha\), so they are balanced. If \(\alpha\) is irrational their frequency is irrational, precluding periodicity; thus the word is Sturmian by the balanced-and-aperiodic characterization [3].

**3. Time averages and Lyapunov exponent.** In the irrational case the logistic function \(\sigma(u)=e^u/(1+e^u)\) is a Riemann-integrable observable of the circle phase (allowing the single endpoint discontinuity). Equidistribution implies
\[
\lim_{n\to\infty}\frac1n\sum_{k<n}b_k
=\frac1L\int_{-c}^{a}\frac{e^u}{1+e^u}\,du
=\frac{\log(1+e^a)-\log(1+e^{-c})}{L}.
\]
At every point whose forward itinerary avoids the switching boundary \(b=1/2\), the derivative of the \(n\)-fold scalar map telescopes:
\[
(F^n)'(b_0)=\frac{b_n(1-b_n)}{b_0(1-b_0)}.
\]
Indeed, each branch is logistic conjugate to a log-odds translation of derivative one. After entrance, the numerators are uniformly bounded above and below by positive constants on the compact recurrent belief interval; hence \(\lim_{n\to\infty}n^{-1}\log|(F^n)'(b_0)|=0\). The countable set of preimages of the switching point is excluded from this differentiability assertion. Irrational rotation also has zero topological/metric entropy on its circle representation; no assertion about the sender-coupled model follows.

**4. Arithmetic of the reported cycling parameters.** The likelihood fractions in [1] give \(e^a=17/3\) and \(e^c=13/7\). If \(a/c=p/q\) for positive integers \(p,q\), then \((17/3)^q=(13/7)^p\), contradicting unique prime factorization because the left side has prime factor \(17\) and the right does not. Hence \(a/c\), and therefore \(\alpha\), is irrational. The logistic image of \([-\log(13/7),\log(17/3))\) is \([7/20,17/20)\). Moreover \(L=\log(221/21)\) and \(\log(1+17/3)-\log(1+7/13)=\log(13/3)\), giving the claimed statistics. For the literal printed decimal pair, irrationality follows similarly since the prime factor \(11\) occurs in \(125/22\) but not in \(93/50\).

## Verification

Run `python3 verify.py` in this directory using Python's standard library. It verifies exact-rational odds identities and trajectories, checks finite mechanical-word identities including switching ties and initial conditions outside the invariant interval, and tests exact rational-rotation comparator cases. It prints `VERIFY_OK` with its check counts and numerical statistics. These finite tests are independent checks of algebra and implementation, not proofs of infinite equidistribution or irrationality; those follow from the preceding arguments.

## Relationship to prior work

Dong and Marzen [1, Section III.2, Eq. (15), Figure 2, Algorithm 2] introduced this exact piecewise Bayesian map and demonstrated numerically that one parameter regime cycles, while the opposite-sign regime polarizes. Their discussion does not specify rotation conjugacy, rational/irrational period classification, bounded finite-window visit discrepancy, the unique invariant belief density, or the exact arithmetic of their featured parameter ratios. The result above supplies these for the uncoupled cycling regime; it does not re-derive or contradict their network-level experiments with sender-dependent in-group bias.

Alvim and coauthors [2, Section 2.2, Definition of the confirmation-bias update] study a distinct neighbor-weighted averaging rule, rather than a piecewise multiplicative likelihood-ratio update. Classical facts about rotations, symbolic balanced words and equidistribution [3] are essential prior mathematical ingredients. The application-specific conjugacy, explicit statistics and exact arithmetic specialization are the result here; no novelty is asserted for rotation theory itself.

## Limitations

The sharp orbit classification applies only to fixed positive multipliers with \(\gamma_\ell<1<\gamma_h\), not to sender-dependent in-group bias, adaptive multipliers, agents updated only finitely many times, or stochastically fluctuating likelihood ratios. Network time-weighted empirical distributions may depend on scheduling. The uniqueness of the recurrent measure is for irrational rotation, not the rational case and not the full interval including absorbing endpoints. The reported decimals are rounded; separate arithmetic statements are provided for the literal decimal interpretation. The general rotation and Sturmian theorems are classical; publication priority for this precise application and its parameter corollary has not been independently established.

## References

[1] E. Dong and S. Marzen, *Cognitive biases can move opinion dynamics from consensus to signatures of transient chaos*, arXiv:2405.19128v1, first formal preprint 2024-05-29, https://arxiv.org/html/2405.19128 ; *American Journal of Physics* 92 (2024), 801–808, https://doi.org/10.1119/5.0220792.

[2] M. S. Alvim, B. Amorim, S. Knight, S. Quintero and F. Valencia, *A Formal Model for Polarization under Confirmation Bias in Social Networks*, *Logical Methods in Computer Science* 19 (2023), https://arxiv.org/html/2112.09542.

[3] M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press, 2002; standard results on irrational circle rotations and balanced Sturmian words. See also https://en.wikipedia.org/wiki/Sturmian_word for a summary of the classical characterization.

[4] K. Wright, *How Opinions Become Chaotic*, *Physics* 16, 181 (2023-10-26), https://physics.aps.org/articles/v16/181. A public description of the research program, without the scalar update equation.

[5] E. Dong and S. Marzen, *Cognitive biases can move opinion dynamics from consensus to chaos*, APS March Meeting oral abstract and presentation 2024-03-05, https://meetings-archive.aps.org/mar/2024/g31/3/. The abstract does not state the scalar map or the results claimed here.
