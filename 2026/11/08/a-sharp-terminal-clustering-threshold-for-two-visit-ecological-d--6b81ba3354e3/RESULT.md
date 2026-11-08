# A sharp terminal-clustering threshold for two-visit ecological detection

## Finding

**Theorem (two-snapshot detection design).** Consider a habitat site initially unoccupied and subject to continuous-time colonization and local extinction, with respective rates \(c>0\) and \(e>0\). Choose exactly two instantaneous detection attempts at times \(0\le t_1\le t_2\le H\), with a fixed horizon \(H>0\). Each attempt independently detects the species with probability \(0<d\le1\) conditional on presence and never reports a detection when the site is empty. Define
\[
 g=c+e,\qquad a=\frac c{c+e},\qquad
 r=\frac{d(1-a)}{1-da},\qquad
 H_c=\frac1g\log\frac1r.
\]
Then the unique globally optimal survey times for maximizing the probability of at least one detection by time \(H\) are
\[
 (t_1^*,t_2^*)=\begin{cases}
 (H,H),&0<H\le H_c,\\[2pt]
 ((H+H_c)/2,H),&H>H_c.
 \end{cases}
\]
In particular, short deadlines favor two independent attempts at the deadline; once \(H\) exceeds the explicit threshold, the earlier attempt separates continuously from the terminal one. Writing \(P^*\) for the optimal detection probability and \(P_{\mathrm{term}}=P(H,H)\), the exact value of the improvement is
\[
 P^*-P_{\mathrm{term}}
 =da(1-da)\left(\max\left\{0,\sqrt r-e^{-gH/2}\right\}\right)^2.
\]
For \(H>H_c\) this gain is strictly positive, while for \(H\le H_c\) it is zero. Both the threshold and the unique schedule apply for every positive pair of transition rates and every allowed imperfect-detection probability.

## Assumptions and scope

Let \(X(t)\in\{0,1\}\) be a time-homogeneous continuous-time Markov chain, with \(0\) denoting empty and \(1\) denoting occupied, generator
\[
 Q=\begin{pmatrix}-c&c\\e&-e\end{pmatrix},\qquad X(0)=0.
\]
Each survey is an instantaneous binary observation with conditional success probability \(d\) when \(X(t)=1\) and zero success probability when \(X(t)=0\). The two observation errors are conditionally independent given the occupancy states, even when the two observation times coincide (then the visits represent independent simultaneous observers or repeated independent tests). Neither survey changes the occupancy process. The initial state and parameters are assumed known for the design. The objective is the *unconditional* probability of at least one successful observation, not expected survey cost, information about model parameters, or the probability of occupancy at the deadline.

The range \(c,e>0\) ensures \(a\in(0,1)\); \(0<d\le1\) ensures \(0<r\le1\), and thus \(H_c\ge0\). At \(d=1\) the threshold is zero and the unique optimum is to sample at \(H/2\) and \(H\) for every \(H>0\). When \(d\downarrow0\), the probability objective itself tends to zero, so the zero-detection boundary is deliberately not included.

## Proof

**Step 1: exact one- and two-time occupancy laws.** With \(g=c+e\), the chain transition probabilities are
\[
 \Pr\{X(t)=1\mid X(0)=0\}=a(1-e^{-gt}),\quad
 \Pr\{X(t+s)=1\mid X(t)=1\}=a+(1-a)e^{-gs}.
\]
For any admissible \(t_1,t_2\), put \(x=e^{-gt_1}\) and \(y=e^{-g(t_2-t_1)}\). Since \(X(0)=0\),
\[
 \Pr\{X(t_1)=1\}=a(1-x),\qquad
 \Pr\{X(t_2)=1\}=a(1-xy),
\]
\[
 \Pr\{X(t_1)=X(t_2)=1\}
 =a(1-x)\bigl[a+(1-a)y\bigr].
\]
Inclusion-exclusion for the conditionally independent survey successes therefore gives the *exact* success probability
\[
 P(t_1,t_2)=da\left[2-x-xy-d(1-x)\bigl(a+(1-a)y\bigr)\right]. \tag{1}
\]
At \(t_1=t_2\), this also agrees with \(\Pr\{X(t_1)=1\}(2d-d^2)\), so no artificial independence of occupancies is being assumed.

**Step 2: the second survey is always terminal.** Holding \(t_1\) fixed, \(y=e^{-g(t_2-t_1)}\) strictly decreases with \(t_2\). Differentiating (1) yields
\[
 \frac{\partial P(t_1,t_2)}{\partial t_2}
 =dag\,y\bigl[x+d(1-x)(1-a)\bigr]>0.
\]
Thus every global optimum necessarily satisfies \(t_2=H\), and for each fixed \(t_1\) any smaller \(t_2\) is strictly inferior.

**Step 3: strictly concave one-variable optimization.** Write \(h=e^{-gH}\in(0,1)\). Since \(t_2=H\), we have \(y=h/x\) and \(x\in[h,1]\). Formula (1) simplifies exactly to
\[
 \frac{P(t_1,H)}{da}=
 2-h-da+d(1-a)h -(1-da)x-\frac{d(1-a)h}{x}. \tag{2}
\]
The derivative with respect to \(x\) vanishes uniquely at
\[
 x_0=\sqrt{\frac{d(1-a)h}{1-da}}=\sqrt{rh},
\]
and the second derivative is \(-2d(1-a)h/x^3<0\). Hence (2) is strictly concave. As \(0<r\le1\) and \(0<h<1\), one has \(x_0<1\). The stationary point is feasible exactly when \(x_0\ge h\), or \(h\le r\), equivalently \(H\ge H_c\). If \(H<H_c\) the strict maximum is at \(x=h\), namely \(t_1=H\); otherwise it is at the unique stationary point, which corresponds to
\[
 t_1=-\frac1g\log\sqrt{rh}=\frac{H+H_c}{2}.
\]
The boundary equality yields the same terminal pair. Strict concavity and Step 2 prove uniqueness among **all** admissible pairs.

**Step 4: the exact gain.** The terminal pair corresponds to \(x=h\), whereas for \(h<r\) the maximizer is \(x_0=\sqrt{rh}\). Subtracting (2) at the two points and completing the square yields
\[
 P^*-P(H,H)=da(1-da)(\sqrt r-\sqrt h)^2\quad(h<r).
\]
For \(h\ge r\), Step 3 shows that the terminal pair is optimal, and the difference vanishes. Combining the regimes gives the displayed positive-part formula and completes the proof. \(\square\)

## Verification

The standalone `checker.py` can be run using `python3 checker.py` with the Python standard library. It verifies the probability identity (1) against an independently constructed two-state transition-matrix and two-survey survival calculation at 2,500 exact rational parameter quadruples; it then compares the analytic optimizer against every pair in a 21-point time grid for 100 independent continuous-parameter designs, and separately checks the gain formula. This gives 30,800 passed assertions. The rational checks confirm identities for those cases only; the global theorem for all real parameters is established by the preceding calculus proof.

For \(c=e=1\), \(d=1/2\), and \(H=2\), the exact threshold is \(H_c=(\log3)/2\approx0.549306144334\). The unique optimal pair is \((1+(\log3)/4,2)\approx(1.274653072167,2)\). The probability of at least one detection is approximately \(0.404764869381\), compared with approximately \(0.368131635417\) for two independent attempts at time \(2\); the gain is approximately \(0.036633233964\).

## Relationship to prior work

MacKenzie et al. (2003) provide the motivating ecological framework of patch occupancy, colonization, extinction, and imperfect detection. MacKenzie and Royle (2005) explicitly discuss multiple independent surveys within one visit versus across visits, but their full-text sampling-design optimization primarily minimizes occupancy-estimation variance under a closed-occupancy approximation. Pagendam and Pollett (2009), in a fully inspected open proceedings paper, optimize observation times in a stochastic metapopulation model for *parameter-estimation Fisher information*, not for first detection in a known initially empty reversible single-patch process. Guillera-Arroita et al. (2014) analyze an invasive-species survey terminated after detection, with a different static-occupancy/cost objective. These different estimands do not give the strict one-switch two-attempt horizon classification above.

General multistate search theory, including Discenza and Stone (1981), is an important broader antecedent. Only its accessible abstract was inspected; the full text was unavailable, so its implications for two instantaneous imperfect tests were not definitively excluded. The same limitation applies to the inaccessible full text of MacKenzie et al. (2003) and some related survey-design articles. The novelty comparison is therefore limited to the specified checked material rather than a claim of historical uniqueness.

## Limitations

The result assumes one site, known initial vacancy, time-homogeneous constant rates, independent same-quality tests with perfect specificity, no survey-induced state change, and the option to make both tests simultaneously. Unknown initial occupancy, false positives, unequal detection probabilities, persistent correlated detectability, non-Markovian residence times, travel costs, and constraints prohibiting simultaneous visits are not covered. It optimizes probability of at least one observation before a fixed horizon, not welfare, eradication, ecological persistence, or inference quality. No ecological field validation or independent proof audit is claimed.

## References

1. MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G. and Franklin, A. B. (2003), *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*, Ecology 84, 2200–2207. First public date 2003-08-01. https://doi.org/10.1890/02-3090
2. MacKenzie, D. I. and Royle, J. A. (2005), *Designing occupancy studies: general advice and allocating survey effort*, Journal of Applied Ecology. https://doi.org/10.1111/j.1365-2664.2005.01098.x
3. Pagendam, D. E. and Pollett, P. K. (2009), *Robust optimal observation of a metapopulation*, MODSIM 2009, pp. 1781–1787. https://mssanz.org.au/modsim09/F2/pagendam.pdf
4. Guillera-Arroita, G. et al. (2014), *Optimal surveillance strategy for invasive species management when surveys stop after detection*, Ecology and Evolution. https://doi.org/10.1002/ece3.1056
5. Discenza, J. H. and Stone, L. D. (1981), *Optimal Survivor Search with Multiple States*, Operations Research 29(2), 309–323. https://doi.org/10.1287/opre.29.2.309
6. Kendall, W. L. et al. (2013), *Relaxing closure assumption in occupancy models: staggered arrival and departure times*. https://doi.org/10.1890/12-1720.1
