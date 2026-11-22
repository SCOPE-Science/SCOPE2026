# Anti-aligned hubs dominate ternary plurality fixed points on quadrilateral books

## Finding
For every integer \(m\ge1\), consider the quadrilateral book \(B_m=K_{1,m}\mathbin{\square}K_2\), with two adjacent hubs and \(m\) four-cycle pages, and synchronous three-opinion *open-neighbor unique-plurality updating*. A vertex changes to the uniquely most numerous neighbor opinion if one exists; whenever the largest neighbor count is tied, it retains its present opinion. Let \(E_m\) be the number of labelled fixed configurations. There are explicit finite coefficient formulas for integers \(U_m,V_m\) such that
\[
E_m=3U_m+6V_m,
\]
where \(U_m\) counts fixed configurations for one specified agreeing pair of hub colors and \(V_m\) counts them for one specified distinct ordered pair. Put
\[
r=\sqrt{2/3},\quad \rho=\frac{1+2\sqrt6}{6},\quad
\sigma^2=\frac{2\sqrt6}{1+2\sqrt6},\quad
c=\frac{r}{(1-r)\sqrt{2\pi\sigma^2}}.
\]
Then, as \(m\to\infty\),
\[
\boxed{E_m=6^{m+1}-\frac{12c(1+2\sqrt6)^m}{\sqrt m}
+o\!\left(\frac{(1+2\sqrt6)^m}{\sqrt m}\right).}
\]
In particular, a uniformly selected fixed configuration has **distinct hub opinions** with probability tending to one, and at most \((1/2+o(1))(5/6)^m\) probability of agreeing hubs. For a uniformly chosen initial three-opinion state, the probability of *already being fixed* is asymptotic to \(\frac23(\frac23)^m\); this is not a claim about eventual attraction basins.

## Assumptions and scope
The vertices are \(h_0,h_1,a_1,b_1,\ldots,a_m,b_m\). The edges are \(h_0h_1\) and, for every page \(i\), the three edges \(h_0a_i\), \(a_ib_i\), \(b_ih_1\). All three opinions \(0,1,2\) are named. A state is fixed if one simultaneous update returns the entire state unchanged. The incumbent wins every tie for the maximum even when its color is *not* one of the tied maximal neighbor colors. This is not equivalent to requiring a pure Nash equilibrium in a coordination game.

To define the exact finite formulas, use independent indeterminates \(X_0,X_1,X_2,Y_0,Y_1,Y_2\) and set
\[
P_{=}=X_0Y_0+X_1Y_1+X_1Y_2+X_2Y_1+X_2Y_2,
\]
\[
P_{\ne}=X_0Y_0+X_0Y_1+X_0Y_2+X_1Y_1+X_2Y_1+X_2Y_2.
\]
Let \(\Phi_j(z_0,z_1,z_2)\) be one unless there is a unique index maximizing the three counts and that index differs from \(j\); in the exceptional case it is zero. With \(\mathbf e_j\) the standard coordinate vector, \(|\mathbf a|=a_0+a_1+a_2\), and \([X^{\mathbf a}Y^{\mathbf b}]\) denoting coefficient extraction, define
\[
U_m=\sum_{|\mathbf a|=|\mathbf b|=m}
[X^{\mathbf a}Y^{\mathbf b}]P_=^m\,
\Phi_0(\mathbf a+\mathbf e_0)\Phi_0(\mathbf b+\mathbf e_0),
\]
\[
V_m=\sum_{|\mathbf a|=|\mathbf b|=m}
[X^{\mathbf a}Y^{\mathbf b}]P_{\ne}^m\,
\Phi_0(\mathbf a+\mathbf e_1)\Phi_1(\mathbf b+\mathbf e_0).
\]
Each sum is finite and consists entirely of nonnegative integers. Powers in these two formulas enumerate the \(m\) **labelled** pages; no orbit quotient or automorphism division is taken.

## Proof
**1. Peripheral stabilization.** Fix hub colors \((u,v)\) and a page colors \((x,y)\) at vertices \((a_i,b_i)\). Because each peripheral vertex has exactly two neighbors, it stays unchanged precisely when
\[
(y=u\implies x=u)\quad\text{and}\quad(x=v\implies y=v).
\]
For \((u,v)=(0,0)\), these pairs are exactly \((0,0),(1,1),(1,2),(2,1),(2,2)\), producing \(P_=\). For \((u,v)=(0,1)\), they are exactly \((0,0),(0,1),(0,2),(1,1),(2,1),(2,2)\), producing \(P_{\ne}\). All named equal-color hub pairs are equivalent by color relabelling, and all named distinct ordered pairs are likewise equivalent. Thus their multiplicities are three and six, respectively. The two \(\Phi\) factors state exactly that both hubs are fixed, since the opposite hub supplies one additional neighbor of its own color. This proves the coefficient formulas and \(E_m=3U_m+6V_m\), without appealing to computation.

**2. A sharp dominant event.** Fix hubs \((0,1)\) and choose each of the six admissible page types uniformly and independently. Then \(V_m/6^m\) is the probability both hubs remain fixed. Write \(A_j\) for the number of left leaves with color \(j\), and \(B_j\) for the right leaves with color \(j\). From the six page types, one page contributes to \(A_0-A_2\) the value \(+1\) with probability \(1/2\), the value \(-1\) with probability \(1/3\), and \(0\) with probability \(1/6\). Write \(S_m=A_0-A_2\). By right-left/color symmetry, \(B_1-B_2\) has the same distribution.

Hub zero has neighbor counts \((A_0,A_1+1,A_2)\). Its failure event differs from \(\{S_m\le-1\}\) only where \(A_0-A_1\le0\): the latter contains every case in which opinion one wins outright, or in which opinion two exceeds opinion zero but is tied by opinion one. The generating function of a one-page increment of \(A_0-A_1\) has multiplicities \((3,2,1)\) for \((+1,0,-1)\). Chernoff's inequality therefore bounds the discrepancy by
\[
\beta^m,\qquad \beta=\frac{2+2\sqrt3}{6}<\rho.
\]
The same argument holds for the other hub.

The two main bad events \(\{A_2>A_0\}\) and \(\{B_2>B_1\}\) can intersect, but their intersection is exponentially smaller. For one page the corresponding pair of increments has the six equally weighted outcomes
\[
(1,0),(1,1),(1,-1),(0,1),(-1,1),(-1,-1).
\]
Put \(t_*=(1/2)\log(2/3)\), \(r=e^{t_*}\). Applying the exponential Markov inequality simultaneously to the two negative deviations bounds their intersection by a constant times \(\mu^m\), where
\[
\mu=\frac{2r+r^2+2+r^{-2}}{6}<\rho.
\]
Consequently,
\[
\frac{V_m}{6^m}=1-2\Pr(S_m\le-1)+O(\beta^m+\mu^m).
\]
This handles incumbent-retaining **multiway ties**, rather than incorrectly treating them as best-response stability.

**3. Exact large-deviation prefactor.** The moment generating function of one increment of \(S_m\) is
\[
M(t)=\frac12e^t+\frac16+\frac13e^{-t}.
\]
Its unique minimizer is \(t_*\), with \(M(t_*)=\rho\). Under the exponentially tilted distribution proportional to \(e^{t_*S_m}\), the increments are centered, aperiodic on the integer lattice, and have variance \(\sigma^2\). The aperiodic lattice local central limit theorem, together with the geometric summability of \(r^j\), gives
\[
\Pr(S_m\le-1)=\rho^m\sum_{j\ge1}r^j
\Pr_{t_*}(S_m=-j)
\sim\frac{r}{(1-r)\sqrt{2\pi\sigma^2}}\frac{\rho^m}{\sqrt m}
=c\frac{\rho^m}{\sqrt m}.
\]
The local limit is used for fixed \(j\), and a uniform \(O(m^{-1/2})\) upper bound controls the summable tail. No finite numerical experiment is being extrapolated to prove this limit.

**4. The agreeing-hub sector.** Every page in this sector has only five admissible color pairs, so \(0\le U_m\le5^m\). Since \(5<6\rho=1+2\sqrt6\), it is negligible even compared with the first large-deviation correction to \(6V_m\). Combining this bound with steps 2–3 proves the boxed asymptotic. In addition \(3U_m/E_m\le(1/2+o(1))(5/6)^m\). Division by the \(3^{2m+2}\) uniformly possible states proves the fixed-state probability assertion.

## Verification
Two different exact integer algorithms were executed: an all-size page-count dynamic program, and a direct exhaustive enumeration of the actual graph vertices with a separately implemented update-stability test. They agreed for all page counts \(1\le m\le5\), covering \(3^{12}=531{,}441\) initial configurations in the largest case. The dynamic program also checked page counts through \(m=10\). The first five total fixed-state counts are \(39,93,531,5109,20979\). A separate exact-integer random-walk recurrence checks the tilted-tail constants and their slow convergence, but is **diagnostic** rather than a proof of the limit. Reproduce with `python verification/count_fixed.py`, `python verification/bruteforce.py`, and `python verification/large_deviation.py` from the package root. The analytic argument above, not the finite checks, establishes the statement for all \(m\ge1\).

## Relationship to prior work
Mossel, Neeman and Tamuz (first public version 2012) study information aggregation and unanimity in majority/plurality social-network dynamics; their theorems do not enumerate stationary configurations of this square-book family or provide the displayed prefactor. Apt, de Keijzer, Rahn, Schäfer and Simon (2015 preprint; later revised) analyze pure and coalitional Nash equilibria of graph coordination games, **not** the incumbent-retaining-tie fixed-state rule here; the two equilibrium notions cannot be identified. Di Ianni (2025) treats different deterministic three-state update rules from a complexity viewpoint, not this graph-family stationary entropy. A 2010 tie-resolution study by Yang and Pan concerns group-based opinion updates, with only an abstract inspected, and so remains a limited source of priority uncertainty. Publicly indexed results on binary-majority square books and three-state excitable dynamics on quadrilateral books have distinct local maps. The present finite coefficient formula and sharp asymptotic have not been found in the inspected sources, but absence from searched records is not a proof of world-wide priority.

## Limitations
The claim concerns **fixed configurations only**. It does not assert that trajectories eventually reach one of those configurations, and it does not compute attraction basins, transient times or other periodic cycles. The graph is unweighted, simple and labelled, and the number of opinions is exactly three. The result does not apply to random tie-breaking, incumbent-best-response tie choice, closed-neighborhood plurality or asynchronous updates. The asymptotic applies as the integer page count tends to infinity. Some relevant historical literature was searched only at abstract level; independent validation and definitive historical priority are not established.

## References
1. E. Mossel, J. Neeman, O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1, first posted 2012-07-04. https://arxiv.org/abs/1207.0893
2. K. R. Apt, B. de Keijzer, M. Rahn, G. Schäfer, S. Simon, *Coordination Games on Graphs*, arXiv:1501.07388v1, first posted 2015-01-29. https://arxiv.org/abs/1501.07388
3. M. Di Ianni, *Three Majority-Based Deterministic Dynamics for Three Opinions*, AppliedMath 5(4), 147 (2025). https://doi.org/10.3390/appliedmath5040147
4. L. Yang and K. Pan, *Solution on Tie in Three-Opinion Dynamics Research*, WMSVM (2010), pp. 98–101. https://doi.org/10.1109/WMSVM.2010.30 (abstract only inspected).
