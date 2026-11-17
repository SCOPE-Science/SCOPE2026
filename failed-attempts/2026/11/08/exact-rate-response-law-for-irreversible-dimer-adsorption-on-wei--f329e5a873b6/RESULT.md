# Exact rate-response law for irreversible dimer adsorption on weighted fans

## Finding
For each integer \(m\ge 1\) and every real \(\lambda>0\), let \(F_{2m}=K_1\vee P_{2m}\) be a fan with central vertex \(o\) and a path of \(2m\) peripheral vertices. Deposit dimers irreversibly: each path edge attempts adsorption at rate one, each spoke incident with \(o\) at rate \(\lambda\), and an attempt succeeds if and only if both endpoints are vacant. Let \(q_m(\lambda)\) be the probability that the central vertex remains vacant at jamming. Write \(\beta=2(1+\lambda)\). Then
\[
q_0(\lambda)=1,\qquad
q_m(\lambda)=\frac{1}{\beta m-1}\sum_{j=0}^{m-1}q_j(\lambda)q_{m-1-j}(\lambda)\quad(m\ge1).
\]
The generating function \(Q_\beta(z)=\sum_{m\ge0}q_m(\lambda)z^m\) has the exact logarithmic-derivative representation
\[
Q_\beta(z)=-\beta\frac{u_\beta'(z)}{u_\beta(z)},\qquad
u_\beta(z)=1-\sum_{j=1}^\infty a_j(\beta)z^j,
\]
where \(a_1(\beta)=1/\beta\) and
\[
a_j(\beta)=\frac{a_{j-1}(\beta)}{\beta j[\beta(j-1)-1]}\qquad(j\ge2).
\]
The entire function \(u_\beta\) has exactly one zero of smallest modulus, a positive simple zero \(\rho(\lambda)>1\), characterized by \(\sum_{j\ge1}a_j(\beta)\rho(\lambda)^j=1\). There is some \(R(\lambda)>\rho(\lambda)\) such that
\[
q_m(\lambda)=\frac{\beta}{\rho(\lambda)^{m+1}}+O_\lambda(R(\lambda)^{-m}).
\]
The exponential-decay base \(\rho(\lambda)\) is strictly increasing and real-analytic for \(\lambda>0\), with
\[
\rho(\lambda)=2(1+\lambda)-\frac12+O(\lambda^{-1})\qquad(\lambda\to\infty).
\]
Finally, at every fixed \(\lambda_0>0\) and \(s\in\mathbb R\), for \(\lambda_m=\lambda_0+s/m>0\) eventually,
\[
\frac{q_m(\lambda_m)}{q_m(\lambda_0)}\longrightarrow
\exp\left(-s\frac{\rho'(\lambda_0)}{\rho(\lambda_0)}\right),
\qquad \frac{\rho'(\lambda_0)}{\rho(\lambda_0)}>0.
\]
The rate-dependent exponential law and its finite-size \(m^{-1}\) response give exact rare-event sensitivity to the spoke-to-path adsorption-rate ratio.

## Assumptions and scope
The vertices are labeled and the path edges are the \(2m-1\) edges between successive peripheral vertices; every peripheral vertex has one spoke to \(o\). Each edge has an independent exponential first-attempt clock with its assigned positive rate; equivalently, edges with two available endpoints are repeatedly chosen proportionally to rate. A deposited dimer permanently occupies its two endpoints. The event studied is vacancy of \(o\) at terminal jamming, not the expected total adsorption density. For \(\lambda>0\), the hub is vacant at jamming exactly when **every** peripheral vertex is occupied by a path-edge dimer. The identity does not extend to \(\lambda=0\), where the hub is isolated and remains vacant with probability one independently of path coverage. The auxiliary initial value \(q_0=1\) is a recurrence convention.

## Proof
**First successful attempt.** Initially every edge is available. Its total attempt rate is \((2m-1)+2m\lambda=\beta m-1\). If the first successful edge is a spoke, the hub is occupied and the target event fails. If it is path edge \((i,i+1)\), the remaining peripheral vertices split into intervals of lengths \(i-1\) and \(2m-i-1\) (with path edges indexed by \(1\le i<2m\)). Hub survival requires both intervals to be perfectly filled by path dimers, hence both lengths must be even, so \(i=2j+1\). Conditional on the first event, independent memoryless clocks remain on the two intervals. The target event is equivalent to both independent subevents in which no spoke ever succeeds. Their probabilities multiply, giving the stated recurrence.

**Generating function.** The recurrence yields
\[
\beta zQ_\beta'(z)-Q_\beta(z)+1=zQ_\beta(z)^2.
\]
Setting \(Q_\beta=-\beta u'/u\) reduces this Riccati equation to \(\beta^2zu''-\beta u'-u=0\). The initial condition \(Q_\beta(0)=1\) gives \(u(0)=1\), \(u'(0)=-1/\beta\). Coefficient comparison gives the displayed \(a_j\). Its ratio is \(O(j^{-2})\), so \(u_\beta\) is entire.

**Dominant zero.** Every \(a_j\) is positive and \(\sum_{j\ge1}a_jx^j\) increases strictly from zero to infinity as \(x\to\infty\) (the first term alone diverges). There is thus a unique \(\rho>0\) satisfying the zero equation. For \(|z|<\rho\), \(|\sum a_j z^j|<1\). At \(|z|=\rho\), equality can hold only when the positive \(j=1\) and \(j=2\) terms point in the same positive-real direction; thus \(z=\rho\). Moreover \(u'(\rho)=-\sum j a_j\rho^{j-1}<0\), so this is a simple zero. Isolated zeros of the entire function give a surrounding disk with no other zeros. Subtracting the simple pole \(\beta/(\rho-z)\) from \(Q_\beta\) and applying Cauchy's coefficient bound on a slightly larger circle proves the exponential asymptotic. Since \(0\le q_m\le1\), the asymptotic with positive coefficient forces \(\rho>1\).

**Rate response.** On compact positive \(\lambda\)-intervals, the series for \(u_\beta\) and its derivatives converge locally uniformly in \(z\). Each coefficient \(a_j(\beta)\) decreases strictly as \(\beta\) increases, hence the positive zero \(\rho\) increases strictly. The nonzero \(u_\beta'(\rho)\) and implicit-function theorem give real analyticity and strictly positive derivative. Uniform isolation of the simple dominant pole for \(\lambda\) near \(\lambda_0\) gives a uniform exponentially small relative remainder in the coefficient asymptotic. Taylor expansion of \(\log\rho(\lambda_0+s/m)\) then gives the stated finite-size ratio. For the large-rate expansion, note first that at \(z=\beta\) the positive coefficient sum exceeds one, while at \(z=\beta-1\) it equals \(1-1/(2\beta)+O(\beta^{-2})<1\) for sufficiently large \(\beta\). Hence \(\rho=\beta+t\) with \(-1<t<0\). The first two terms of the zero equation are \(z/\beta=1+t/\beta\) and \(a_2 z^2=1/(2\beta)+O(\beta^{-2})\); its remaining terms are \(O(\beta^{-2})\) uniformly for bounded \(t\). This forces \(t=-1/2+O(\beta^{-1})\).

## Verification
The accompanying `check.py` verifies finite sizes \(1\le m\le5\) at five distinct rational spoke rates using an independent exact-rational Markov-state recursion on all remaining-vertex subsets, rather than the splitting argument. It also tests the analytic zero equation, leading-pole asymptotics at three rates, positivity, and root monotonicity. All 52 assertions passed in the prepared package. For the equal-rate check \(\lambda=1\), \(\rho=3.475472691346290\ldots\) and \(q_1=1/3\), \(q_2=2/21\), \(q_3=19/693\). These finite checks are consistency tests; the infinite-size theorem is proved above.

## Relationship to prior work
Penrose and Sudbury (arXiv:math/0503519, initially public 2005-03-24) formulate dimer adsorption on graphs and solve occupancy/correlations on regular trees; the inspected model and Section 4.2 do not state the weighted-fan hub-vacancy probability or its parameter-response law. Pippenger (SIAM J. Discrete Math., 1989, DOI below) analyzes random sequential adsorption on graph families, but only its published abstract could be inspected here, so historical coverage remains a priority risk. Other work on one-dimensional adsorption concerns coverage densities or lattice correlations, not the rare event that every path site is covered before a positive-rate hub spoke succeeds.

The equal-rate wheel \(K_1\vee C_{2m}\) has separately been analyzed via a trace-class transfer operator, with a dominant exponential base numerically equal to \(1/\rho(1)=0.287730645241419\ldots\). **That equal-rate exponential base is not claimed as new here.** The result above concerns all finite fan probabilities, arbitrary positive spoke rates, the full decay-rate function, its strictly monotone response and the \(m^{-1}\) rate window; none follows from the wheel's stated equal-rate cyclic formula. The fan's open path and rate tunability are essential to the present argument.

## Limitations
No claim is made about perfect-matching probabilities on arbitrary graphs, joint terminal vacancy statistics, finite-time coverage or higher-dimensional surfaces. The strict positivity assumption on \(\lambda\) is essential to interpreting hub vacancy as complete path coverage. The verification uses finitely many small graphs and cannot certify infinitely many cases by itself. An inaccessible historical full text and the possibility of differently named equivalent probability-generating functions remain originality risks. Independent historical-priority and scientific validation have not been performed.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889. arXiv:math/0503519v1, https://arxiv.org/abs/math/0503519 (first posted 2005-03-24).
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034.
3. Y. Fan and J. K. Percus, *Asymptotic coverage in random sequential adsorption on a lattice*, Physical Review A 44 (1991), 5099–5103, https://doi.org/10.1103/PhysRevA.44.5099.
