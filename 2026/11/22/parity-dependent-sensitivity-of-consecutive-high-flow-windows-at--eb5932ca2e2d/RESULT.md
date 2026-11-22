# Parity-dependent sensitivity of consecutive high-flow windows at maximal anti-persistence

## Finding

Consider a stationary two-state wet/dry Markov model with fixed wet-day probability \(\pi\). A notional high-flow passage opportunity is a pair of consecutive wet days. The event probability \(F_N(s)\) within \(N\) observations depends on wet-state persistence \(s\), which may vary while the marginal \(\pi\) stays fixed. At the most anti-persistent admissible chain, the **direction of the response alternates by the parity of the observation horizon**. More precisely, for \(1/2<\pi<1\), let \(r=(1-\pi)/\pi\) and \(s_0=1-r=2-1/\pi\). For every integer \(m\ge1\), the right derivatives at \(s_0\) are

\[
F'_{2m}(s_0+)=r^{m-2}\bigl((3m-2)-(4m-3)\pi\bigr),\qquad
F'_{2m+1}(s_0+)=2m\pi r^m>0.
\]

Thus every odd horizon of at least three days benefits initially from relaxing maximal anti-persistence. For every even horizon \(N=2m\ge4\), the initial effect changes sign exactly at

\[
\pi_m=\frac{3m-2}{4m-3};
\qquad \pi_2=\frac45,
\qquad \pi_m\downarrow\frac34.
\]

For \(\pi<\pi_m\), increasing \(s\) from \(s_0\) initially improves the chance of a wet pair; for \(\pi>\pi_m\), it initially reduces it. Equality means vanishing *first derivative only*, not a uniform statement of local or global optimality.

There are two complementary global results. For **four** days and every \(0<\pi<1\), the unique global optimum is \(s=\max\{3/4,2-1/\pi\}\), interpreted on the admissible interval; it equals maximal anti-persistence exactly when \(\pi\ge4/5\). For **five** days and every \(0<\pi<1\), the event probability is strictly concave in \(s\) on the admissible interval and has a unique *strictly interior* maximizer. Thus the four-day boundary optimum at high wet-day frequency disappears upon adding one observation day.

## Assumptions and scope

Let \(X_1,\ldots,X_N\in\{D,W\}\) have a stationary two-state first-order Markov law with \(\Pr(X_j=W)=\pi\in(0,1)\) and \(s=\Pr(X_{j+1}=W\mid X_j=W)\). Stationarity fixes \(b=\Pr(W\mid D)=\pi(1-s)/(1-\pi)\). Stochasticity requires

\[
\max\{0,2-1/\pi\}\le s\le1.
\]

The endpoints are allowed, with the explicitly stationary initial distribution. Define \(F_N(s)=\Pr(\exists j\in\{1,\ldots,N-1\}: X_j=X_{j+1}=W)\). When \(\pi>1/2\), maximal negative dependence occurs at \(s_0=2-1/\pi\), where \(\Pr(D\mid D)=0\). The assertion concerns *occurrence* of a wet pair, not passage of actual animals or a claim that two days of rain suffice for any species.

## Proof

**Exact avoidance dynamics.** Put \(A_N=1-F_N\), the probability of no \(WW\) pair. After the first observation let \(d_1=1-\pi\), \(w_1=\pi\) denote probabilities of eligible paths currently ending in dry and wet days. Killing each wet-to-wet transition gives

\[
d_{j+1}=(1-b)d_j+(1-s)w_j,\qquad w_{j+1}=bd_j,\qquad A_N=d_N+w_N.
\]

These polynomial/rational expressions also define the derivatives at closed parameter endpoints. They establish \(F_4(s)=\pi s(3-2s)\), independently of the dry-to-wet transition parameter once stationarity is imposed. The parabola has its unique unconstrained maximum at \(s=3/4\). Intersecting with the admissible interval proves the four-day statement, including the threshold \(\pi=4/5\).

**First variation at maximal anti-persistence.** Suppose \(\pi>1/2\), write \(r=(1-\pi)/\pi\), and let \(\delta=s-s_0\ge0\). Then the wet-to-dry and dry-to-wet transition probabilities become \(r-\delta\) and \(1-\delta/r\), while dry-to-dry becomes \(\delta/r\). At \(\delta=0\), a path lacking \(WW\) must alternate strictly. Its derivative comes from (i) differentiating the two alternating strings and (ii) strings with exactly one \(DD\) pair, whose first-order coefficients are counted below. Every other no-\(WW\) string contains at least two \(DD\) transitions and contributes only \(O(\delta^2)\) for fixed \(N\).

For \(N=2m\), the two alternating strings have total first-order coefficient \(-2(2m-1)\pi r^{m-1}\). Exactly one \(DD\) can occur in \(m-1\) strings starting and ending in \(W\), each contributing \(\pi r^{m-2}\), or in \(m\) strings starting and ending in \(D\), each contributing \(\pi r^{m-1}\). Therefore

\[
A'_{2m}(s_0+)=\pi r^{m-2}\bigl((m-1)-(3m-2)r\bigr).
\]

For \(N=2m+1\), alternating paths contribute \(-2m\pi r^{m-1}(1+r)\), and exactly-one-\(DD\) paths contribute \(2m\pi r^{m-1}\). Therefore \(A'_{2m+1}(s_0+)=-2m\pi r^m\). Taking negatives and substituting \(r=(1-\pi)/\pi\) gives both displayed derivative formulas. For \(m=1\), the even formula is understood with the positive factor \(r^{-1}\) and gives \(F'_2=\pi\). For \(m\ge2\), the threshold is unique; \(\pi_m=3/4+1/[4(4m-3)]\) proves monotonicity and the limit.

**Five days.** Repeatedly applying the avoidance recurrence and differentiating yields

\[
F'_5(s)=-\frac{2\pi}{1-\pi}G_\pi(s),\qquad
G_\pi(s)=2\pi s^3-3\pi s^2-2\pi s+2\pi+3s-2,
\]

with \(G'_\pi(s)=3-2\pi-6\pi s(1-s)\). For \(\pi\le6/7\), \(G'_\pi(s)\ge3-7\pi/2\ge0\), and it is strictly positive throughout the admissible interval. For \(\pi>6/7\), the lower bound \(s\ge s_0>1/2\) makes \(G'_\pi\) increasing, while

\[
G'_\pi(s_0)=\frac{10\pi^2-15\pi+6}{\pi}>0
\]

because the quadratic has negative discriminant and positive leading coefficient. Hence \(F'_5\) is strictly decreasing everywhere admissible. Its left-boundary value is \(4\pi>0\) if \(\pi\le1/2\), or \(4(1-\pi)^2/\pi>0\) if \(\pi>1/2\), whereas \(F'_5(1)=-2\pi<0\). Strict concavity and the intermediate-value theorem give a unique interior maximizer, namely the unique feasible root of \(G_\pi(s)=0\). This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The checker constructs avoidance and first derivatives with exact rational arithmetic and compares the event probability against direct enumeration for up to nine days, multiple stationary wet frequencies and admissible persistence values; checks the exact four-/five-day identities; and checks both all-horizon derivative expressions at the extreme boundary through 121 days. The checker is a finite regression test: the arbitrary-horizon proof is the explicit first-variation enumeration above, not extrapolation from the tests.

## Relationship to prior work

Oh, Park and Kim (2022), Secs. 2.2–2.3, derive Markov-dependent waiting-time and longest-run distribution recurrences for arbitrary transition probabilities; these pre-existing recurrences, and the equivalence of wet-pair occurrence with a length-two waiting-time event, are not claimed to be new. The present classification **optimizes and differentiates while preserving a fixed, unequal stationary wet frequency**, proving an all-horizon even/odd boundary-sensitivity law and a four-/five-day global-optimizer discontinuity in boundary status. The earlier published study “A one-fifth correlation limit for paired-wet-spell risk” fixes the wet frequency exactly at one half and proves different finite- and long-horizon results; it does not assert or imply the present high-wet-frequency anti-persistence threshold from its stated hypotheses. General distribution identities are a priority risk if their authors elsewhere explicitly derive these constrained phase transitions. Jubb et al. (2023) motivate flow-dependent serial passage and report contrasting hydrological years but do not model binary Markov wet runs.

## Limitations

The binary weather model has a fixed stationary wet fraction, one-step memory, and a stipulated two-consecutive-wet-day proxy. Its transition dependence is a mathematical comparison, not a controllable intervention. This proxy is not calibrated to fish, river stage or individual barrier passage. The even-horizon formula is a *local one-sided derivative* at maximum anti-persistence for arbitrary lengths; global optimization is proved only at four and five days. At a vanishing derivative, higher-order behavior may differ by horizon. Full historical priority is uncertain because the full text of some older Markov-run papers was inaccessible; no external independent audit has occurred.

## References

- W. M. Jubb et al., “Understanding the impact of barriers to onward migration; a novel approach using translocated fish,” *Journal of Environmental Management* **335**, 117488 (2023). First online 2023-02-22. https://doi.org/10.1016/j.jenvman.2023.117488 . Open published full text: https://eprints.gla.ac.uk/292685/1/292685.pdf .
- J. Oh, C. Park and S. Kim, “Recurrence algorithms of waiting time for the success run of length k in relation to generalized Fibonacci sequences,” arXiv:2210.08797 (2022), especially Sec. 2.2 and Thm. 2.14. https://arxiv.org/abs/2210.08797 .
- L. Ya. Savelyev, S. V. Balakin and B. V. Khromov, “Covering runs in binary Markov sequences,” *Discrete Mathematics and Applications* **13** (2003), 111–138. https://doi.org/10.1163/156939203322109104 .
- W. Y. Wendy Lou, “On Runs and Longest Run Tests: A Method of Finite Markov Chain Imbedding,” *JASA* **91** (1996), 1595–1601. https://doi.org/10.1080/01621459.1996.10476727 .
- “A one-fifth correlation limit for paired-wet-spell risk,” published research record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-one-fifth-correlation-limit-for-paired-wet-spell-risk--ef8eca4293c6 .
