# Fixed-duration transient-episode monitoring has a sharp algebraic-to-exponential detection transition

## Finding

Suppose a single episode begins at an exponential arrival time and lasts for an independent exponential duration, both with rate \(\lambda>0\). A monitor can be activated in exactly \(n\ge1\) predetermined disjoint windows of a prescribed common duration \(w>0\), and detects the episode perfectly when any window intersects the presence interval. There is no fixed deadline. Put \(x=e^{-\lambda w}\), define \(v_0=0\), and iterate

\[
v_j=\exp[-x(1-v_{j-1})],\qquad j=1,2,\ldots,n.
\]

The **unique** global maximizing calendar has, in chronological order, the initial idle gap and subsequent gaps

\[
 g_i=\frac{x(1-v_{n-i})}{\lambda},\qquad i=1,\ldots,n,
\]

with an active interval of length \(w\) after every gap. All gaps are strictly positive and strictly increase toward the last window. The exact maximal interception probability is \(v_n\).

For fixed positive window duration, the optimally missed probability obeys the sharp asymptotic

\[
1-v_n\sim C(x)x^n,\quad 0<C(x)<1,
\quad C(x)=\prod_{j=0}^{\infty}\frac{1-e^{-x(1-v_j)}}{x(1-v_j)}.
\]

The optimal **total idle time** remains bounded as \(n\to\infty\), strictly below \(x/[\lambda(1-x)]\). By contrast, in the limiting instantaneous-observation model \(w=0\), the same optimality recurrence satisfies \(n(1-v_n)\to2\) and total idle time is asymptotic to \(2\log n/\lambda\). Hence every fixed positive window duration changes the large-count miss rate from algebraic to exponential. For the same active monitoring time \(nw\), continuously monitoring from time zero misses the event with probability \(x^n\), a strictly larger miss probability; the asymptotic optimal-to-contiguous miss ratio is exactly \(C(x)\). This comparison permits the optimized calendar to finish later than the contiguous calendar.

## Assumptions and scope

Let \(A\sim\mathrm{Exp}(\lambda)\) be the unique arrival time, and independently \(L\sim\mathrm{Exp}(\lambda)\) be the unique presence duration. The species or event is present on \([A,A+L)\) only; it neither reappears nor generates later events. Choose deterministic \(g_1,\ldots,g_n\ge0\), let \(T_0=0\), and define recursively \(T_i=T_{i-1}+g_i+w\). Monitoring window \(i\) is \([T_{i-1}+g_i,T_i]\). Endpoint conventions affect no probabilities because \(A,L\) are continuous. An episode is recorded if and only if its presence interval has nonempty positive-length intersection with any window. The detection mechanism has perfect sensitivity for any positive overlap, with no background, no molecular degradation, no read noise, and no false positives. All times are measured from an origin known to precede the episode. There is no horizon, switching penalty, travel time, budget for elapsed inactive time, or adaptive change after nondetection. We optimize only over nonnegative idle gaps for fixed \(n,w,\lambda\); no optimization over window lengths is claimed.

## Proof

**1. One-window interception.** For a window \([s,s+w]\), detection comes either from an arrival before \(s\) surviving to \(s\), or an arrival during the window. Independence and equal exponential rates give

\[
\begin{aligned}
F(s,w)&=\int_0^s\lambda e^{-\lambda a}e^{-\lambda(s-a)}\,da
  +\int_s^{s+w}\lambda e^{-\lambda a}\,da\\
&=e^{-\lambda s}(\lambda s+1-e^{-\lambda w}).
\end{aligned}
\]

**2. Exact disjoint-first-detection law.** If the first intercepted window is \(i\), the episode must arrive after the preceding window ends at \(T_{i-1}\). Arrivals during or before earlier windows that survive to a later window would already have been intercepted earlier. Exponential arrival memorylessness and the one-window expression therefore imply

\[
P(g_1,\ldots,g_n)=\sum_{i=1}^n e^{-\lambda T_{i-1}}F(g_i,w),
\qquad T_{i-1}=\sum_{j<i}(g_j+w).
\]

These first-detection events are disjoint and exhaust success.

**3. Bellman maximization.** Set \(x=e^{-\lambda w}\). If \(v\in[0,1)\) is the best conditional chance from future windows after the current window ends, then placing the current window after a gap \(g\) produces total conditional chance

\[
F(g,w)+e^{-\lambda(g+w)}v
=e^{-y}(y+1-x+xv),\qquad y=\lambda g\ge0.
\]

Its derivative with respect to \(y\) is \(e^{-y}[x(1-v)-y]\). This is strictly positive before, and strictly negative after, the **unique** optimum \(y=x(1-v)>0\); the value at that optimum is \(e^{-x(1-v)}\). Starting from no remaining windows \(v_0=0\), induction proves the recursion, exact value and unique calendar. The unique maximizing gaps, viewed backward by the number of remaining windows, are \(x(1-v_{j-1})/\lambda\).

**4. Gap order and limit.** The map \(u\mapsto e^{-x(1-u)}\) is strictly increasing and, for \(0\le u<1\) and \(0<x\le1\), exceeds \(u\), since \(e^{-x(1-u)}>1-(1-u)=u\). Consequently \(0=v_0<v_1<v_2<\cdots<1\); its only fixed point in \([0,1]\) is 1. Chronological gaps \(g_i=x(1-v_{n-i})/\lambda\) strictly increase. Writing \(\epsilon_j=1-v_j\) gives

\[
\epsilon_0=1,\qquad\epsilon_{j+1}=1-e^{-x\epsilon_j},\qquad
0<\epsilon_{j+1}<x\epsilon_j.
\]

For \(0<x<1\), \(\epsilon_j<x^j\) for all \(j\ge1\), so the total idle time \(\sum_i g_i=(x/\lambda)\sum_{j=0}^{n-1}\epsilon_j\) increases toward a finite limit, strictly less than \(x/[\lambda(1-x)]\).

**5. Sharp exponential miss constant for positive windows.** Divide the exact recurrence by \(x\epsilon_j\):

\[
\frac{\epsilon_n}{x^n}=
\prod_{j=0}^{n-1}\frac{1-e^{-x\epsilon_j}}{x\epsilon_j}.
\]

Every factor is in \((0,1)\), so the products decrease below 1. Their limit is strictly positive: the logarithm of the factor is \(-x\epsilon_j/2+O((x\epsilon_j)^2)\) for small arguments, and \(\sum_j x\epsilon_j\le x/(1-x)\) is finite. Thus the infinite logarithmic sum converges and defines \(0<C(x)<1\). Comparing to one continuous window \([0,nw]\), which detects exactly when \(A<nw\), proves the strict miss improvement and the asymptotic ratio \(C(x)\).

**6. Sharp zero-width boundary.** At \(w=0\), \(x=1\), and \(\epsilon_j\downarrow0\) still holds. Taylor expansion yields \(\epsilon_{j+1}=\epsilon_j-\epsilon_j^2/2+O(\epsilon_j^3)\), hence \(\epsilon_{j+1}^{-1}-\epsilon_j^{-1}\to1/2\). A Cesàro argument gives \(j\epsilon_j\to2\). Finally the sum of the chronological gaps is \(\lambda^{-1}\sum_{j=0}^{n-1}\epsilon_j\sim 2\log n/\lambda\). This boundary is the idealized perfect instantaneous snapshot limit, not a finite-effort molecular measurement.

## Verification

The standalone `verify_transient_windows.py` uses only the Python 3 standard library. It recomputes the Bellman recurrence and optimal gaps; checks the disjoint first-detection expression independently for randomized, perturbed and optimal calendars; independently integrates the one-window arrival-survival probability; and tests monotonicity and asymptotics. The checker reports 16,596 successful assertions. A concrete reproducible example is \(\lambda=1\), \(w=\log 2\), \(n=4\), for which \(v_4\approx0.958186862832\), compared with \(0.9375\) for uninterrupted monitoring from time zero over the same four-window active duration. The chronological optimal gaps are approximately \((0.04271246,0.08929573,0.19673467,0.5)\). Numerical tests are supplementary; the preceding proof establishes the unbounded-count statements.

## Relationship to prior work

Chen et al. (2024) demonstrate that continuous passive eDNA collection can improve detection of rare, transient fauna over instantaneous filtration in their sampled habitats; they do not solve this idealized one-episode fixed-window interception calendar. Yau et al. (2010) analyze recurring stochastic events under periodic on/off monitoring and step or duration-dependent utility, rather than a one-time exponentially arriving episode optimized over a finite, nonperiodic sequence of equally long windows. *Optimal snapshot calendars for a single transient ecological presence episode* (2026) establishes the \(w=0\) point-observation recurrence and algebraic miss law, which the present result uses as an acknowledged boundary case; its assumption of instantaneous observations does not imply the positive-width nested exponential, finite total-idle-time property or exact nonzero window-rate constant. Guillera-Arroita et al. (2014) optimize sampling effort and management costs with a Poisson detection clock at occupied sites; their monitored population does not follow the present one-off arrival-and-departure mechanism. A literature and related-record comparison found no directly covering full positive-window result; that is a best-knowledge finding, not a priority guarantee. The basic Bellman principle and exponential memorylessness are established tools, not claimed as new.

## Limitations

The result does not model molecule capture intensity, eDNA transport or persistence, laboratory sensitivity, empirical occupancy or species recurrence. Perfect detection for arbitrarily brief positive overlap is an idealization; a zero-duration observation is a formal limit. Positive window length is prescribed and equal across windows, and the optimal schedule may finish after a contiguous comparison schedule. Rates of arrival and departure are assumed exactly equal and known. No real-world sampling prescription, sampling-cost optimum or independent empirical validation is claimed. General inspection-scheduling literature is broad, so historical priority cannot be guaranteed, particularly for inaccessible older finite-window formulations.

## References

1. Chen, X., Li, S., Zhao, J., and Yao, M. (2024). *Passive eDNA sampling facilitates biodiversity monitoring and rare species detection*. Environment International 187, 108706. First online 2024-04-26. https://doi.org/10.1016/j.envint.2024.108706 ; https://pubmed.ncbi.nlm.nih.gov/38696978/
2. Yau, D. K. Y., Yip, N. K., Ma, C. Y. T., Rao, N. S. V., and Shankar, M. (2010). *Quality of monitoring of stochastic events by periodic and proportional-share scheduling of sensor coverage*. ACM Transactions on Sensor Networks 7(2), Article 18. https://doi.org/10.1145/1824766.1824774
3. *Optimal snapshot calendars for a single transient ecological presence episode* (2026). Public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-optimal-snapshot-calendars-for-a-single-transient-ecological-pre--b2d028296c40
4. Guillera-Arroita, G., Hauser, C. E., and McCarthy, M. A. (2014). *Optimal surveillance strategy for invasive species management when surveys stop after detection*. Ecology and Evolution 4, 1751–1760. https://doi.org/10.1002/ece3.1056
5. Yu, J., Karaman, S., and Rus, D. (2013). *Persistent Monitoring of Events with Stochastic Arrivals at Multiple Stations*. https://arxiv.org/abs/1309.6041
