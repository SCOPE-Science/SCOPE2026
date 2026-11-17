# Exact one-step catapult-severity laws and sign-switch separation for a quartic gradient map

## Finding
For the quartic loss \(L(x)=(x^2-1)^2/4\), fixed-step gradient descent is \(G_a(x)=x(1+a-ax^2)\). Fix \(0<a<1\) and let \(R_a=\sqrt{1+2/a}\). Choose \(X\) uniformly on \((-R_a,R_a)\), and define its one-step relative loss multiplier \(H=L(G_a(X))/L(X)\), with arbitrary values on the probability-zero set \(X=\pm1\). Define \(b_a=a+a^2/4\) and the already-known catapult threshold \(a_c=2\sqrt2-2\).

For \(a_c<a<1\), the **complete first-step amplification exceedance law** is
\[
\Pr_X(H>t)=\begin{cases}\sqrt{1-2\sqrt{1+\sqrt t}/(a+2)},&1\le t<b_a^2,\\0,&t\ge b_a^2.\end{cases}
\]
Consequently the exact probability of any strict initial loss increase is \(\sqrt{1-2\sqrt2/(a+2)}\), and the largest relative first-step multiplier is exactly \(b_a^2\). For \(0<a\le a_c\), the strict increase probability is zero.

Under the distinct **uniform-residual initialization** \(Z=a(X^2-1)\sim\operatorname{Unif}(-a,2)\) with either sign of \(X\), the entire tail is instead
\[
\Pr_Z(H>t)=\frac{\sqrt{\max\{a^2+4a-4\sqrt t,0\}}}{a+2},\qquad t\ge1.
\]
Every loss-increasing first update also **preserves the sign** of the weight. Under uniform weights, first-step sign reversal occurs with probability \(1-\sqrt{(a+1)/(a+2)}\); these two events are disjoint. The severity-tail probabilities under both priors have a sharp square-root endpoint and a square-root onset at \(a_c\), but different constants.

## Assumptions and scope
This is a statement about exactly **one update** of the specified one-dimensional gradient map, for \(0<a<1\). The interval \((-R_a,R_a)\) is its known bounded initialization region; almost all of these initial points eventually converge to one of the minima, as established in the cited literature. No claim concerns the largest loss over an entire trajectory. A uniform residual \(Z\) does not induce a uniform physical weight \(X\): the two laws are separately defined, and choosing the sign of \(X\) does not change \(H\). Earlier work already determines the map, initial interval and catapult threshold; those are premises and are not claimed as new.

## Proof
Put \(r=x^2-1\in[-1,2/a]\). Exact expansion gives
\[
G_a(x)=x(1-ar),\qquad r'=G_a(x)^2-1=rq_a(r),\quad q_a(r)=1-2a+(a^2-2a)r+a^2r^2.
\]
Therefore \(H=q_a(r)^2\) whenever \(r\ne0\). The convex quadratic has \(q_a(-1)=q_a(2/a)=1\), its minimum lies at \(r_*=(2-a)/(2a)\), and \(q_a(r_*)=-a-a^2/4=-b_a\). Thus \(q_a\le1\) on the entire initialization interval, so for \(t\ge1\), the event \(H>t\) is precisely \(q_a(r)<-\sqrt t\). This is possible if and only if \(b_a>\sqrt t\). The latter at \(t=1\) is equivalent to \(a>a_c\).

For \(a_c<a<1\) and \(1\le t<b_a^2\), the solution set is \(r_-(t)<r<r_+(t)\) with
\[
r_\pm(t)=\frac{2-a\pm\sqrt{a^2+4a-4\sqrt t}}{2a}.
\]
Both endpoints lie in \((-1,2/a)\). Under uniform weights, the event consists of two symmetric intervals of total relative measure
\[
\frac{\sqrt{1+r_+(t)}-\sqrt{1+r_-(t)}}{\sqrt{1+2/a}}.
\]
Since \((1+r_+)+(1+r_-)=(a+2)/a\) and \((1+r_+)(1+r_-)=(1+\sqrt t)/a^2\), squaring simplifies exactly to the stated uniform-weight tail. Under uniform residuals, the interval has length \(a(r_+-r_-)\) out of the total residual length \(a+2\), giving the second exact tail.

The multiplier reaches \(b_a^2\) at \(r=r_*\); it is an essential supremum for each absolutely continuous initialization law. The upper-tail laws have the sharp endpoint asymptotics
\[
\Pr_X(H>t)\sim \frac{\sqrt{b_a^2-t}}{(a+2)\sqrt{b_a}},\qquad
\Pr_Z(H>t)\sim \frac{\sqrt{2/b_a}\,\sqrt{b_a^2-t}}{a+2},\qquad t\uparrow b_a^2.
\]
At onset, \(\Pr_X(H>1)\sim2^{-3/4}\sqrt{a-a_c}\) and \(\Pr_Z(H>1)\sim2^{-1/4}\sqrt{a-a_c}\) as \(a\downarrow a_c\), by expanding their exact expressions.

Finally, sign reversal means \(xG_a(x)<0\), or \(r>1/a\). Every increasing-loss event is contained in \(r<r_+(1)\). But \(r_+(1)<1/a\) for \(a_c<a<1\), because \(\sqrt{a^2+4a-4}<a\). At smaller \(a\) no increase exists. Hence loss increase and sign reversal are disjoint. The sign-reversal probability is the relative length of \(\{x:1+1/a<x^2<1+2/a\}\), as claimed.

## Verification
The standalone `check_exceedance.py` checks the polynomial recurrence using exact rational arithmetic, both tail formulas against independently computed interval lengths, and independent midpoint-count estimates of exceedance probabilities for multiple \(a,t\). The finite checks corroborate but do not prove the universal statement; the quadratic discriminant and interval-length proof above supply the proof. Run `python3 check_exceedance.py`.

## Relationship to prior work
Hofmann (2026) develops this identical cubic gradient map and its post-edge state-space envelope, and expressly credits Chen et al. (2023) for the known exact monotone-loss threshold. Chen et al. use the affinely equivalent cubic residual recursion and uniform-residual initialization, and classify the phase threshold but do not state the full arbitrary-severity one-step probability laws. The new result uses their model to calculate all superlevel-set measures, compare two coordinate priors, and separate sign reversal from the spike event. Chen and Bruna (2022/2023) analyze the same quartic loss, but principally stable period-two behavior for learning rates above one, not these first-update distributions for \(0<a<1\). Previous bifurcation thresholds, maps and sign-change boundaries are not claimed as novel.

## Limitations
No assertion is made about cumulative maximum loss, noise, multidimensional networks, arbitrary priors or long-time invariant measures. The formulas depend on two *explicitly specified* sampling laws. The asymptotic behavior holds only at the stated boundaries. Historical priority is provisional: the calculation is short and an older equivalent exceedance identity may have escaped search. Independent mathematical validation has not been performed.

## References
1. T. Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, arXiv:2607.04993v1 (first posted 2026-07-06), https://arxiv.org/abs/2607.04993 (especially §§2.1–2.10).
2. X. Chen, K. Balasubramanian, P. Ghosal and B. Agrawalla, *From Stability to Chaos: Analyzing Gradient Descent Dynamics in Quadratic Regression*, arXiv:2310.01687v1 (first posted 2023-10-02), https://arxiv.org/abs/2310.01687 (Theorem 2.1, Lemma 1, Appendix A).
3. L. Chen and J. Bruna, *Beyond the Edge of Stability via Two-step Gradient Updates*, arXiv:2206.04172v1 (first posted 2022-06-08), https://arxiv.org/abs/2206.04172 (Theorem 2 and Appendix F).
