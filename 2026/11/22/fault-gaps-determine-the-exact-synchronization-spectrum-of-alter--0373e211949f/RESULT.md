# Fault gaps determine the exact synchronization spectrum of alternating matching NOR networks

## Finding

For a cycle of \(2m\) sites, \(m\ge2\), apply open-neighborhood NOR synchronously using the even-edge perfect matching at even time steps and the odd-edge matching, possibly with a fixed set of deleted edges, at odd time steps. With no deleted edges, every configuration is recurrent: for each \(d\mid m\) the number of two-update temporal orbits of primitive period \(d\) is
\[
P_d=\frac1d\sum_{e\mid d}\mu(d/e)4^e.
\]
With at least one deleted odd-matching edge, there is exactly one recurrent orbit in the time-phase-extended system: the all-one state at even phase alternating with the all-zero state at odd phase. The full dynamics is synchronized sharply after \(L\) two-update rounds, where \(L\) is the greatest cyclic gap between successive deleted edges.

More precisely, if the cyclic gap lengths between the \(k\ge1\) deleted odd-matching edges are \(g_1,\ldots,g_k\), summing to \(m\), put \(q_t=\sum_{i=1}^k\max(g_i-t,0)\). Then for every \(0\le t\le L\), exactly \(4^{m-q_t}\) of the \(4^m\) labelled even-phase initial configurations have entered that recurrent orbit by two-update round \(t\). Hence the exact first-entry distribution is \(H_0=1\) and
\[
H_t=4^{m-q_t}-4^{m-q_{t-1}} \quad(1\le t\le L),
\]
and \(H_t=0\) for \(t>L\). If exactly \(h\) deleted-edge gaps have maximum length \(L\), the fraction needing the maximal \(L\) rounds is exactly \(1-4^{-h}\). A single deleted edge therefore turns a fully reversible \(4^m\)-state two-update permutation into a unique attracting two-phase orbit, with sharp time \(m\) rounds and exactly three quarters of initial states still outside the attractor after round \(m-1\).

If each odd-matching edge is independently deleted with a fixed probability \(p\in(0,1)\), then conditional on at least one deletion, the synchronization time \(L\) obeys
\[
\frac{L}{\log m/(-\log(1-p))}\longrightarrow1
\]
in probability as \(m\to\infty\). The exceptional no-deletion probability equals \((1-p)^m\).

## Assumptions and scope

Number sites \(0,\ldots,2m-1\) cyclically. Let \(M_0=\{\{2j,2j+1\}:j\in\mathbb Z/m\mathbb Z\}\) and \(M_1=\{\{2j-1,2j\}:j\in\mathbb Z/m\mathbb Z\}\). For a set \(J\subseteq\mathbb Z/m\mathbb Z\) of fault positions, delete from \(M_1\) exactly the edges indexed by \(J\), writing the residual matching \(M_1(J)\). For a graph \(G\), define \(F_G(x)_v=1\) exactly when all neighbors of \(v\) have Boolean value zero, with the empty-neighborhood convention giving one. At even phase apply \(F_{M_0}\); at odd phase apply \(F_{M_1(J)}\); \(S_J=F_{M_1(J)}\circ F_{M_0}\) is the two-update return map on even-phase states. First-entry time here is measured in iterations of \(S_J\); each such iteration consists of two synchronous updates. The phase is tracked as part of the time-dependent system, and a recurrent two-phase orbit is not confused with a fixed point of a phase-forgetting time map.

## Proof

Write even-phase coordinates \(a_j=x_{2j}\) and \(b_j=x_{2j+1}\). Since \(M_0\) is perfect, its NOR update gives \(y_{2j}=1-b_j\) and \(y_{2j+1}=1-a_j\). At the next step, the edge \(\{2j-1,2j\}\) is absent if \(j\in J\), so both endpoints are isolated and become one; if present, their outputs are the complements of their partners' \(y\)-bits. Consequently
\[
(S_Ja)_j=\begin{cases}1,&j\in J,\\a_{j-1},&j\notin J,\end{cases}
\qquad
(S_Jb)_j=\begin{cases}1,&j+1\in J,\\b_{j+1},&j+1\notin J.\end{cases}
\]
Here indices are modulo \(m\). Thus the two \(m\)-bit streams are oppositely directed, independently shifted, and reset to one at each fault.

If \(J=\varnothing\), the two streams are independent rotations of length \(m\), so every state is periodic. The number fixed by \(S_J^d\) is \(4^{\gcd(m,d)}\); Möbius inversion gives \(P_d\), for each \(d\mid m\). These are primitive orbits of the two-update map; retaining the phase doubles their temporal lengths.

If \(J\ne\varnothing\), the \(k\) fault positions separate the circle into \(k\) runs with lengths \(g_i\). After \(t\) return steps, a forward stream still depends on exactly \(q_t=\sum_i(g_i-t)_+\) distinct original bits; all other coordinates have been overwritten by ones. The backward stream has the same number of independently surviving coordinates, although their locations differ. Since neither shift duplicates a surviving bit, there are exactly \(2q_t\) independent initial coordinates that must equal one for the image at time \(t\) to be the all-one state. The other \(2m-2q_t\) coordinates are free, so precisely \(2^{2m-2q_t}=4^{m-q_t}\) initial states have entered it by that time. A coordinate is never reset to zero, and all ones is a fixed point of \(S_J\); therefore arrival by time \(t\) is equivalent to the above condition. Subtraction of nested arrival sets yields every \(H_t\).

For \(L=\max_i g_i\), one has \(q_L=0\) and \(q_{L-1}=h\), the number of gaps attaining \(L\). This proves sharpness and the exact maximal-depth fraction. An earlier nontrivial recurrent orbit is impossible because every state reaches all ones. From all ones, the \(M_0\)-NOR state is all zeros and the odd-phase step returns all ones, giving the unique phase-resolved two-cycle.

Finally, with independent fault probability \(p\in(0,1)\), write \(r=1-p\). For \(t_+=\lceil(1+\varepsilon)\log_{1/r}m\rceil\), the union bound shows the probability of a cyclic intact run of length \(t_+\) is at most \(mr^{t_+}\to0\). For \(t_-=\lfloor(1-\varepsilon)\log_{1/r}m\rfloor\), partition the \(m\) positions into \(\lfloor m/t_-\rfloor\) disjoint runs; the probability none is completely intact is at most \((1-r^{t_-})^{\lfloor m/t_-\rfloor}\to0\). A fault exists with probability \(1-r^m\to1\); these bounds yield the displayed convergence in probability, as the maximum gap differs by at most one from the longest uninterrupted run of intact edges.

## Verification

Two standalone Python 3 checkers are included. `verify_graph.py` constructs the two actual graph matchings and performs bitwise NOR updates on **every** initial state for every nonempty fault pattern at sizes \(m=2,3,4,5,6\); it verifies the entire entry-time distribution, sharp time, and the no-fault periodic-orbit census. This covers \(119\) fault patterns and \(294128\) checked faulted phase-zero initial states. `verify_transport.py` separately tests the shift-and-reset formula and independent coordinate tracking for \(4697\) fault layouts at lengths \(2\) through \(60\). Both tests are finite checks of the algebraic proof; they are not offered in place of the proof of the all-size statements or probabilistic limit.

## Relationship to prior work

AND-NOT network theory establishes the general signed-conjunctive Boolean setting; see Veliz-Cuba et al. (2012). Work on intersecting asynchronous Boolean cycles, such as Melliti et al. (2013), concerns a different interaction and updating rule. Existing studies of alternating lower approximations on matchings obtain extinction laws, but apply an AND-like rough-set operator, not alternating NOR with complementary reset transport and arbitrary deleted matching positions. Temporal infection under alternating matchings is a monotone propagation system, unlike the NOR complemented matching update. Prior exact NOR attractor classifications on fixed bipartite or rook graphs do not provide the alternating two-matching defect law. These comparisons concern mathematical implications rather than absence of matching titles.

## Limitations

The theorems are for a two-phase, externally prescribed switching between the two perfect matchings of an even cycle with faults fixed only in the odd-phase matching; no assertion is made for arbitrary temporal networks, threshold rules, arbitrary graph deletions or imperfect switching schedules. The long-run fault asymptotic assumes independent, identically distributed edge deletions with fixed probability. Historical novelty is assessed against the inspected literature and recoverable database records, not guaranteed against unindexed publications; an inaccessible contemporary Boolean-network article could not be excluded by whole-text inspection. Independent external audit has not been performed.

## References

1. A. Veliz-Cuba et al., “AND-NOT logic framework for steady state analysis of Boolean network models,” arXiv:1211.5633v1, first public 2012-11-24, https://arxiv.org/html/1211.5633v1 .
2. T. Melliti et al., “Full characterisation of attractors of two intersected asynchronous Boolean automata cycles,” arXiv:1310.5747v1, first public 2013-10-21, https://arxiv.org/abs/1310.5747 .
3. “Non-Deterministic Updates of Boolean Networks,” AUTOMATA 2021, https://drops.dagstuhl.de/storage/01oasics/oasics-vol090-automata2021/OASIcs.AUTOMATA.2021.10/OASIcs.AUTOMATA.2021.10.pdf .
