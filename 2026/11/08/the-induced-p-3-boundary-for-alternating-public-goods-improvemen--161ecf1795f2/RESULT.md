# The induced-\(P_3\) boundary for alternating public-goods improvement

## Finding

Let \(G=(V,E)\) be any finite, nonempty, simple undirected graph. Each vertex chooses an action in \(\{0,1\}\), with the unique preferred action \(1\) exactly when an even number of its open neighbors choose \(1\). A strict improving move changes one currently non-best-responding vertex to its preferred action. Then:

1. A pure Nash equilibrium exists on **every** such graph. The exact number is \(2^{|V|-\operatorname{rank}_{\mathbb F_2}(I+A_G)}\), where \(A_G\) is the adjacency matrix over \(\mathbb F_2\).
2. **Every** strict-improvement sequence is finite if and only if \(G\) is a disjoint union of cliques (equivalently, \(G\) has no induced three-vertex path \(P_3\)).
3. If \(G\) is a disjoint union of \(c\) cliques, every maximal strict-improvement sequence from a profile \(s\) has exactly \(e(s)\) moves, where \(e(s)\) counts the clique components containing an even number of active vertices initially. Consequently \(e(s)\le c\), and there are exactly \(2^{|V|-c}\) pure equilibria.
4. Otherwise, the strict-improvement graph contains a directed cycle of **four** moves, supported by two moving agents along an induced \(P_3\) while its third agent remains fixed. Four is the minimum possible length of any strict-improvement cycle in this model, and three vertices are the smallest graph order permitting one.

The distinguishing claim is the graph-theoretic **if-and-only-if** finite-improvement boundary with its exact path-length and shortest-cycle witnesses, not the earlier known linear-algebraic method for finding parity-response equilibria.

## Assumptions and scope

Write \(s_v\in\{0,1\}\) for the action of vertex \(v\), and \(k_v(s)=\sum_{u\in N_G(v)}s_u\) for its number of active **open** neighbors. Every vertex has the same best-response function
\[
\operatorname{BR}_v(s_{-v})=\begin{cases}1,&k_v(s)\equiv0\pmod2,\\0,&k_v(s)\equiv1\pmod2.\end{cases}
\]
There are no self-loops, edge weights, ties, or restrictions on which dissatisfied player may move. The result covers arbitrary finite numbers of components and isolated vertices. For a concrete common public-goods utility realization, let the production cost be \(1\), let
\[
B(j)=j+\frac{1-(-1)^j}{4}\quad(j\in\mathbb Z_{\ge0}),
\]
and give player \(v\) utility \(B(s_v+k_v(s))-s_v\). The payoff gain from producing instead of abstaining is \(\tfrac12(-1)^{k_v(s)}\), yielding exactly the stipulated strict best responses. Note that \(B\) is strictly increasing, although its marginal increments alternate.

A *maximal* improvement sequence means one that cannot be extended by another strict-improvement step. The *finite improvement property* (FIP) requires every improvement sequence to terminate, not merely the existence of some terminating schedule or an equilibrium.

## Proof

**Equilibria exist on all undirected graphs.** Over \(\mathbb F_2\), the best-response equations are
\[
(I+A_G)s=\boldsymbol 1.
\]
Let \(M=I+A_G\). For any vector \(z\in\ker M\), symmetry and the zero diagonal of \(A_G\) give
\[
0=z^{\mathsf T}Mz=z^{\mathsf T}z+z^{\mathsf T}A_Gz
=\boldsymbol1^{\mathsf T}z\pmod2,
\]
since each edge contributes twice to the adjacency quadratic form. Thus \(\boldsymbol1\) is orthogonal to \(\ker M^{\mathsf T}=\ker M\), so \(\boldsymbol1\in\operatorname{im}M\). The affine solution set is nonempty and contains exactly \(2^{|V|-\operatorname{rank}M}\) vectors.

**Clique components imply an exact potential and path length.** In a clique component \(C\) let \(h_C(s)=\sum_{v\in C}s_v\). If \(h_C(s)\) is odd, an active player sees an even number of active neighbors and correctly plays \(1\), while an inactive player sees an odd number and correctly plays \(0\); nobody in \(C\) may improve. If \(h_C(s)\) is even, all its agents are dissatisfied: active agents see an odd number and inactive agents an even number of active neighbors. Any single improving flip makes \(h_C(s)\) odd, after which no agent in \(C\) can improve. Therefore
\[
\Phi(s)=\#\{C:\ h_C(s)\text{ is odd}\}
\]
increases by exactly one on each allowed move. Every initially even component moves exactly once, regardless of the update order, and every initially odd component never moves. This proves the exact length \(e(s)\). Each clique of size \(m\) has \(2^{m-1}\) odd-parity binary assignments, giving \(2^{|V|-c}\) equilibria.

**Any induced path forces a repeated improvement cycle.** If \(G\) is not a disjoint union of cliques, some connected component is not complete. A shortest path between two nonadjacent vertices supplies three consecutive vertices \(a,b,d\), with edges \(ab,bd\) but no edge \(ad\). Set \(s_d=1\) and every other vertex to \(0\). Keep all vertices outside \(\{a,b\}\) fixed (they need not best-respond). Starting from \((s_a,s_b,s_d)=(0,0,1)\), make these four moves:
\[
(0,0,1)\xrightarrow{a}(1,0,1)\xrightarrow{b}(1,1,1)
\xrightarrow{a}(0,1,1)\xrightarrow{b}(0,0,1).
\]
At the first step, \(a\) sees zero active neighbors; at the second, \(b\) sees its two active path neighbors; at the third, \(a\) sees the active neighbor \(b\); and at the fourth, \(b\) sees only \(d\) active. Hence the moving player strictly improves at each step, independent of any additional edges to the fixed inactive vertices. This directed cycle disproves FIP on every non-cluster graph.

Every improving move flips exactly one bit, so a return to the same profile requires an even number of moves. A two-step return would have to flip the same bit twice without any change in its neighbors between flips; both flips cannot be strict best responses. Thus any improvement cycle has length at least four. Every simple graph on at most two vertices is a disjoint union of cliques, while \(P_3\) itself realizes the four-move witness. This proves both sharpness statements.

## Verification

The accompanying `verify.py` uses the Python standard library and exact integer/bit operations. Running `python3 verify.py` enumerates every labeled simple graph on \(1\) through \(6\) vertices (\(33{,}867\) graphs). It checks the induced-\(P_3\)/clique-union equivalence and tests the four-step witness on every non-cluster graph; for every cluster graph it checks every strategy profile, legal improving move, potential increment, and equilibrium count. The observed totals are \(278\) cluster graphs, \(33{,}589\) non-cluster graphs, \(14{,}946\) cluster profiles, \(43{,}685\) cluster improvement edges, and \(134{,}356\) witness moves. The program prints `VERIFY_OK`.

These finite checks are cross-checks, **not** a substitute for the proof for all finite graphs. The algebraic existence argument and the structural dichotomy above are independent of the enumeration cutoff.

## Relationship to prior work

Papadimitriou and Peng (2021, Lemma 3.3) explicitly reduce alternating binary public-goods equilibrium equations to linear algebra over \(\mathbb F_2\). Gilboa and Nisan (2022) study the decision complexity of binary response patterns. Klimm and Stahlberg (2023, Section 3 and Corollary 3.4) establish convergent best-response dynamics for **decreasing** patterns; their introduction distinguishes the infinite alternating pattern and its equilibrium decision complexity from truncated versions. None of these inspected statements supplies a graph characterization of **unrestricted unilateral strict-improvement convergence** for the alternating pattern, nor do their results imply the induced-\(P_3\) cycle or exact termination length on cluster graphs.

Related mathematical records concerning *synchronous* parity automata study simultaneous updates and periodic-state censuses on specified graph classes. Synchronous parity orbits and arbitrary-schedule unilateral strict improvements are different transition relations, so their period bounds do not cover this theorem.

## Limitations

The FIP classification is specific to the strictly alternating homogeneous rule, undirected unweighted simple graphs, and single-agent strict improvements. It does not assert convergence of synchronous updates, stochastic or fairness-constrained schedules outside the stated model, weighted or directed network versions, or arbitrary monotone/heterogeneous response patterns. The four-step witness demonstrates the **possibility** of cycling, not that all schedules on non-cluster graphs cycle. Unindexed literature using equivalent game terminology could contain the same classification; no claim of exhaustive priority verification or independent audit is made.

## References

1. C. Papadimitriou and B. Peng, *Public Goods Games in Directed Networks*, arXiv:2106.00718, initially public 2021-06-01. https://arxiv.org/html/2106.00718v2 . See Lemma 3.3 and the alternating parity equations.
2. M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238, initially public 2022-07-09. https://arxiv.org/html/2207.04238v1 .
3. M. Klimm and M. J. Stahlberg, *Complexity of Equilibria in Binary Public Goods Games on Undirected Graphs*, arXiv:2301.11849, initially public 2023-01-27. https://arxiv.org/html/2301.11849v3 . See introduction, Section 3, Corollary 3.4.
