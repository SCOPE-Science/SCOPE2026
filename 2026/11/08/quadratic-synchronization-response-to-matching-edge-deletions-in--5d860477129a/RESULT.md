# Quadratic synchronization response to matching-edge deletions in three-state excitable dynamics

## Finding
For integers \(n\ge3\) and \(0\le t\le n\), let \(G_{n,t}\) be the labelled complete bipartite graph \(K_{n,n}\) with \(t\) pairwise disjoint matching edges removed. Start either the synchronous three-colour cyclic cellular automaton (CCA) or synchronous three-state Greenberg–Hastings model (GHM) from any of the \(3^{2n}\) labelled initial colourings. Then the two models have **the same set of synchronizing initial colourings**, whose exact number is
\[
Z_{n,t}=3\left(4^n+2\cdot3^n-2^{n+2}+1+t\,2^{n+1}+t(t-1)\right).
\]
In particular, the number of **additional** synchronizing initial colourings created by deleting a matching of \(t\) edges is
\[
Z_{n,t}-Z_{n,0}=3\left(t\,2^{n+1}+t(t-1)\right).
\]
The successive increments obey
\[
Z_{n,t}-Z_{n,t-1}=3\left(2^{n+1}+2(t-1)\right),\qquad
Z_{n,t}-2Z_{n,t-1}+Z_{n,t-2}=6
\]
for \(1\le t\le n\) and \(2\le t\le n\), respectively. Thus the edge-deletion response is strictly quadratic, with a universal positive pair-interaction term. Uniformly for \(0\le t\le n\), the synchronization probability under independent uniform initial colours satisfies
\[
\frac{Z_{n,t}}{3^{2n}}\sim 3\left(\frac49\right)^n\quad(n\to\infty).
\]

## Assumptions and scope
Let the two sides be \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). Exactly the edges \(a_i b_i\), \(1\le i\le t\), are absent. All other cross-edges are present. The graph is connected when \(n\ge3\), including when \(t=n\).

At every discrete time all vertices update simultaneously. For CCA, colour \(c\in\mathbb Z/3\mathbb Z\) changes to \(c+1\) if some neighbour has colour \(c+1\), and otherwise stays at \(c\). For GHM, colours \(1\) and \(2\) change automatically to \(2\) and \(0\), while a colour-\(0\) vertex becomes \(1\) exactly when some neighbour has colour \(1\), otherwise remaining \(0\). Synchronization means that after some finite time all vertices have the same state at each later time; CCA then has a constant homogeneous state and GHM ultimately reaches all zero.

The theorem counts **initial** colourings, not recurrent configurations, entry-time strata, nonzero excitation rates or primitive periods. Labelled graphs with matching edges removed in different specified positions are isomorphic.

## Proof
**Cycle criterion and a common zero set.** For a directed edge \(uv\), the CCA one-form is the unique integer in \(\{-1,0,1\}\) congruent to \(X(v)-X(u)\) modulo three. The GHM one-form equals \(+1\) on \(0\to1\), \(-1\) on \(1\to0\), and zero on every other ordered colour pair. For any closed directed walk, conservation of departures and arrivals at each of the three colours shows that the net oriented numbers of \(0\to1\), \(1\to2\), and \(2\to0\) edges are equal. Consequently, the CCA integral around that walk equals **three times** its GHM integral. Gravner–Lyu–Sivakoff's finite-graph cycle criterion [1, Theorem 3] states that either model synchronizes exactly when its initial one-form has zero integral around every cycle. Hence the two models synchronize on exactly the same initial colourings.

**Normalized integer lifts.** A CCA colouring has zero integral around every cycle precisely when there exists an integer height function \(h\) on the vertices satisfying \(h(a_1)=0\), \(|h(u)-h(v)|\le1\) on every graph edge, and \(X(v)\equiv X(a_1)+h(v)\pmod3\). Construct it by summing the CCA one-form along a path from \(a_1\); zero cycle integrals ensure path independence. Conversely, such heights have vanishing cycle integrals. Heights with the same root normalization are unique: if two lifts induce the same colouring, their adjacent height differences both lie in \(\{-1,0,1\}\) and are congruent modulo three, hence equal. Since the graph is connected, the lifts coincide. Therefore the desired count is three times the number of normalized heights, one factor for each root colour.

For counting it is more convenient to translate each height so the minimum of its \(A\)-heights is zero. This is a bijective alternative normalization, because every height assignment is considered modulo simultaneous integral translation.

**A two-unit spread bound.** Write \(u_i=h(a_i)\), let \(s=\max_i u_i-\min_i u_i\), and suppose \(s>2\). Choose indices of a minimum and a maximum and a third, distinct index \(k\), possible because \(n\ge3\). The vertex \(b_k\) is adjacent to both extrema (it can miss only \(a_k\)), requiring its height to lie within one unit of two values more than two units apart. This is impossible. Thus \(s\in\{0,1,2\}\).

For each \(i\), let \(s_i\) be the spread of heights on the \(A\)-vertices adjacent to \(b_i\). If \(i\le t\), this is the spread after deleting \(u_i\); otherwise it is \(s\). Once the \(u_i\) are chosen, the admissible integer heights at \(b_i\) form the intersection of closed unit intervals about the heights of its neighbours. There are exactly \(3-s_i\) choices, independent for different \(i\).

**Case \(s=0\).** There is one translated \(A\)-height pattern. Every \(b_i\) has three choices, contributing \(3^n\) normalized heights.

**Case \(s=1\).** There are \(2^n-2\) binary \(A\)-height patterns containing both values. Every \(b_i\) has two choices unless \(i\le t\) is the unique index at one of the two extrema, when it has three. Because \(n\ge3\), at most one extremum can be represented just once. There are exactly \(2t\) patterns with such a distinguished, deleted extremum. Their extra contribution is \(2t\cdot2^{n-1}=t2^n\). The full contribution is therefore
\[
(2^n-2)2^n+t2^n=4^n-2^{n+1}+t2^n.
\]

**Case \(s=2\).** There are \(3^n-2^{n+1}+1\) words over \(\{0,1,2\}\) containing both extrema. Initially give each word weight one, corresponding to one height choice for every \(b_i\). If a deleted index is the unique occurrence of \(0\) or \(2\), its \(b_i\) acquires at least one extra choice. For each selected extremum there are \(2^{n-1}-1\) eligible completions, giving \(2t(2^{n-1}-1)\) additions. When all other heights equal the opposite extremum, the single exceptional \(b_i\) acquires **two** extra choices rather than one, accounting for another \(2t\). Finally, if distinct deleted indices are the unique occurrences of \(0\) and \(2\), their independent doubled choices yield an additional multiplicative cross term of one, contributing \(t(t-1)\). These cases are exhaustive, because any index other than a unique extreme sees both extrema. The contribution is
\[
3^n-2^{n+1}+1+t2^n+t(t-1).
\]

Summing the three disjoint spread cases yields \(4^n+2\cdot3^n-2^{n+2}+1+t2^{n+1}+t(t-1)\) normalized heights. Multiplying by the three root colours proves the first formula. Subtraction proves the edge-deletion formulas. The asymptotic statement follows because \(t\le n\), so all non-\(4^n\) terms are \(o(4^n)\). This completes the proof.

## Verification
A direct lift-consistency enumerator, `verify_lifts.py`, separately checked all \(n\in\{3,4,5,6\}\) and \(0\le t\le n\) against the closed formula (22 instances and \(4{,}110{,}102\) candidate labelled colourings in total). A direct synchronous-update simulator, `verify_dynamics.py`, independently evolved both CCA and GHM for eight steps on every labelled colouring for \(n\in\{3,4,5\}\) and \(0\le t\le n\) (15 instances, \(390{,}015\) colourings). It confirmed that the two models synchronize on the predicted number of starts. Both programs use only Python's standard library; run `python verify_lifts.py` and `python verify_dynamics.py`. Captured outputs are included. Finite enumeration is a consistency check, not the all-size proof.

## Relationship to prior work
The general finite-graph theorem of Gravner, Lyu and Sivakoff [1] gives the exact cycle-integral criterion, without enumerating synchronizing colourings for the present matching-deletion family. One-edge deletions and intact complete bipartite graphs are special endpoint cases of the formula, so their known behavior is not claimed as an independent novelty. The substantive new calculation is the complete matching-size interpolation, especially the \(t(t-1)\) interaction term and its universal second difference \(6\). Searches of exact synchronization counts, equivalent integer-Lipschitz graph-homomorphism counts and matching-deleted bipartite graph invariants did not identify a statement covering this formula. The lack of an identified source is not proof of historical uniqueness.

## Limitations
Only the synchronization event and its total initial population are determined. The theorem does not classify the distinct non-synchronizing rates, the primitive periods, the transient-entry-time distribution, or dynamics for \(n=2\) at full matching deletion (that graph is disconnected). Historical priority remains conditional on the accessible sources; no independent validation has been performed.

## References
[1] J. Gravner, H. Lyu, D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first posted 2016-10-24, Section 2, Theorem 3, equations (4)–(10). https://arxiv.org/abs/1610.07320
