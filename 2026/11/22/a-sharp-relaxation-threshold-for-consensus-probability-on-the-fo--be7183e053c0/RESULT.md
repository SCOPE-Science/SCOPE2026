# A sharp relaxation threshold for consensus probability on the four-person median ring

## Finding
Consider four people situated on the undirected four-cycle. Each listens with weight \(1/2\) to each of the two adjacent people and with zero weight to themselves. At every synchronous step each selects the point of the weighted-median interval closest to their current opinion and moves a fraction \(\gamma\in(0,1)\) toward that point. Initially the four opinions are independent and uniformly distributed on \([0,1]\).

Write \(P_\gamma\) for the probability that all four opinions converge to one common value. Then the exact sharp threshold is
\[
P_\gamma=\frac13\quad(0<\gamma\le\tfrac12),
\qquad 0\le P_\gamma<\frac13\quad(\tfrac12<\gamma<1).
\]
More precisely, for \(0<\gamma\le1/2\) and any initial state having four distinct entries, consensus occurs if and only if the two lowest opinions occupy *opposite* sites. On that event the eventual consensus opinion is exactly the midpoint of the two middle initial order statistics,
\[
\lim_{t\to\infty}x_i(t)=\frac{x_{(2)}(0)+x_{(3)}(0)}2\quad\text{for all }i.
\]
For every \(\gamma>1/2\), an open set of initially opposite-low configurations instead becomes permanently separated into two adjacent low/high pairs after just one update. Thus the probability drop is strict for any independent common initial law with a strictly positive density on an interval, in particular the uniform law.

## Assumptions and scope
Index vertices cyclically by \(0,1,2,3\), with edges \(01,12,23,30\). For a state \(x\in\mathbb R^4\), set \(m_i(x)=\operatorname{med}\{x_{i-1},x_i,x_{i+1}\}\), indices modulo four. The evolution is
\[
x_i(t+1)=(1-\gamma)x_i(t)+\gamma m_i(x(t)),\qquad 0<\gamma<1.
\]
This is exactly the nearest-current-point weighted-median response for two neighbors each carrying weight \(1/2\): the median interval is the closed interval between the neighbors, and projection of the current value onto it equals the median of the three listed values. The same \(\gamma\) is used at all four sites. The probability assertion uses independent \(\mathrm{Unif}[0,1]\) initial opinions; equality ties occur with probability zero. Statements about individual initial configurations exclude ties only where specified.

## Proof
**1. Adjacent-low patterns cannot reach consensus.** Suppose the two smallest, distinct initial values occupy adjacent vertices, say \(0,1\). Set \(S=\{0,1\}\), \(T=\{2,3\}\). The two neighbors of any site consist of one partner within its pair and one outside. Thus its weighted-median interval, whose endpoints are the two neighbor opinions, intersects the opinion range of its own pair. Projecting its own opinion onto that interval stays inside the pair's old opinion range. Convex interpolation with its own opinion stays there too. Inductively, each pair's range remains inside its initial range. Since the two initial pair ranges are strictly disjoint, all future ranges remain separated by a positive gap. The same reasoning covers any cyclic rotation and either orientation of the two adjacent low sites.

**2. Opposite-low patterns converge for \(\gamma\le1/2\).** The only other strict rank arrangement puts the two lowest values on the opposite pair \(A=\{0,2\}\) or \(B=\{1,3\}\). By symmetry assume that all values on \(A\) are initially smaller than all values on \(B\). Put \(a_-(t)=\min_{i\in A}x_i(t)\), \(a_+(t)=\max_{i\in A}x_i(t)\), and similarly \(b_-(t),b_+(t)\). Whenever \(a_+(t)\le b_-(t)\), both sites in \(A\) have their current opinions below the minimum neighbor, so their median response is \(b_-(t)\); the two sites in \(B\) respond to \(a_+(t)\). Consequently
\[
\begin{aligned}
a_-'&=(1-\gamma)a_-+\gamma b_-,& a_+'&=(1-\gamma)a_++\gamma b_-,\\
b_-'&=(1-\gamma)b_-+\gamma a_+,& b_+'&=(1-\gamma)b_++\gamma a_+.
\end{aligned}
\]
In particular, the gap \(g=b_--a_+\) obeys \(g'=(1-2\gamma)g\), and both within-pair widths are multiplied by \(1-\gamma\). For \(0<\gamma\le1/2\), the interval ordering is preserved (weakly at equality). The sum \(a_++b_-\) is invariant, hence \(a_+,b_-\) converge to their initial average \(c=(a_+(0)+b_-(0))/2\). The shrinking pair widths imply convergence of all four opinions to \(c\). At \(\gamma=1/2\), the first step makes \(a_+=b_-=c\); those two values then remain fixed and the other two approach \(c\) geometrically. In the original four-value ordering, \(a_+(0)=x_{(2)}(0)\) and \(b_-(0)=x_{(3)}(0)\). Interchanging \(A,B\) covers the opposite orientation.

**3. Exact probability.** For independent continuous identically distributed opinions, each of the six unordered positions of the smallest two ranks has probability \(1/6\). Exactly two of these six pairs are opposite in the four-cycle. Steps 1 and 2 therefore yield \(P_\gamma=2/6=1/3\) for \(0<\gamma\le1/2\). Step 1 gives the upper bound \(P_\gamma\le1/3\) for every \(0<\gamma<1\).

**4. Strict probability loss when \(\gamma>1/2\).** Fix \(1/2<\gamma<1\), a positive gap \(g\), and positive widths \(a,b\) satisfying
\[
a,b>\frac{2\gamma-1}{1-\gamma}g.
\]
Start from the opposite-low ordering \(x(0)=(0,a+g,a,a+g+b)\). The exact first iterate is
\[
x(1)=\bigl(\gamma(a+g),\ a+(1-\gamma)g,\ a+\gamma g,\ a+(1-\gamma)(g+b)\bigr).
\]
The width inequalities imply the strict ordering \(x_0(1)<x_1(1)<x_2(1)<x_3(1)\), with a gap \(x_2(1)-x_1(1)=(2\gamma-1)g>0\). Vertices \(0,1\) and \(2,3\) now form two adjacent pairs with disjoint ranges. Step 1 proves they remain separated forever. All inequalities are strict and the map is continuous, so a nonempty open neighborhood of this initial condition also fails consensus, despite having initially opposite low values. Translation and positive scaling put that neighborhood inside \((0,1)^4\). Hence its probability under four independent uniform values is positive, and \(P_\gamma<1/3\) for every \(\gamma>1/2\). This proves the sharp threshold.

**5. Smallest-cycle boundary.** On the three-cycle, the two neighbors of each vertex are the other two vertices. Every site therefore selects the same three-entry global median as its response. The initially middle opinion stays fixed, while each initially extreme opinion moves a fraction \(\gamma\) toward that fixed median at each step; hence all three converge to consensus for every initial state and every \(0<\gamma<1\). Thus the four-cycle is the smallest simple cycle on which this relaxation-dependent consensus-probability phenomenon can occur.

## Verification
The standalone standard-library checker `verification/check.py` independently implements the projected-median update, compares the theorem to all 24 permutations of four distinct initial integers for three subcritical or critical relaxation values, checks the conservation identity and the closed-form limit numerically, and verifies the first-step strict ordering with exact rational arithmetic for multiple supercritical values. It also tests that the explicit \(\gamma=2/3\) witness has a persistent gap. These finite tests are supplementary: the all-parameter proof is Steps 1–4 above.

A convenient exact supercritical example is \(\gamma=2/3\) and \(x(0)=(0,3,2,5)\). Initially the two lowest opinions are opposite, but
\[
x(1)=(2,7/3,8/3,3).
\]
The adjacent pairs \(\{0,1\}\) and \(\{2,3\}\) thereafter retain an opinion gap of at least \(1/3\). Under \(\gamma=1/2\), the same initial state instead converges to consensus opinion \(5/2\).

## Relationship to prior work
Cheng and Mei (2026) establish global convergence of the synchronous mixed weighted-average/weighted-median model and the necessary-and-sufficient structural criterion for consensus from **every** initial state (their Theorems 9 and 11). Their work permits different adjustment coefficients and includes the all-median specialization, but does not give this four-cycle's initial-condition basin probability, exact consensus-value selection, or a sharp relaxation-dependent probability threshold. The distinction matters: their *universal-consensus* property depends on network and types, whereas the *probability of consensus from random initial data* can depend on \(\gamma\). Here the same four-cycle fails universal consensus for every \(\gamma\), but exhibits a strict change in its random-initial consensus probability at \(\gamma=1/2\).

Mei, Hendrickx, Chen, Bullo and Dörfler (2022) analyze an asynchronous weighted-median model and cohesive-set criteria; synchronous convex-relaxation basin probabilities are a different problem. Related publicly indexed results on opinion rings concern strictly direction-biased median sites and closed influence classes, rather than equal-half-weight tie intervals with variable relaxation. These precedents motivate the structural invariance argument but do not supply the update-dependent probability conclusion proved here.

## Limitations
No exact formula is claimed for \(P_\gamma\) when \(1/2<\gamma<1\); only the sharp strict bound is established. The result assumes a four-cycle, neighbor weights exactly \(1/2\), identical relaxation at all nodes and the nearest-point tie convention. It is a deterministic opinion-dynamics result with a probability over initial states, not a stochastic updating model or an empirical claim about social behavior. Historical novelty is assessed against accessible literature and indexed records, not independently certified.

## References
1. J. Cheng and W. Mei, *Equilibria and consensus in discrete-time opinion dynamics with mixed weighted-averaging and weighted-median mechanisms*, arXiv:2610.16406 (first public version October 12, 2026), https://arxiv.org/abs/2610.16406.
2. W. Mei, J. M. Hendrickx, G. Chen, F. Bullo and F. Dörfler, *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808 (2022), https://arxiv.org/abs/2212.08808.
3. *Exact consensus reliability from directional runs in mixed-median opinion rings*, publicly indexed published-finding corpus record, November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-consensus-reliability-from-directional-runs-in-mixed-media--2e44dd8b777b (full text was not accessible during comparison).
