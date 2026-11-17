# A one-edge parity reversal in sequential XOR dynamics on triangular books

## Finding

For each integer \(k\ge1\), let \(Q_k=K_{2,k}\) have distinguished vertices \(a,b\) in the two-vertex shore and labelled leaves \(w_1,\ldots,w_k\) in the other shore. Let \(B_k\) be the *triangular book* obtained from \(Q_k\) by adding the single edge \(ab\). All states are in \(\mathbb F_2^{k+2}\). Updating a vertex \(v\) changes its state according to
\[
 x_v\longleftarrow x_v+\sum_{u\sim v}x_u\pmod2,
\]
using the *current* (possibly previously updated) neighbor states. A macro-step scans each labelled vertex exactly once in a fixed order \(\pi\), repeated indefinitely. Write \(T_{B,\pi}\) and \(T_{Q,\pi}\) for the respective macro-step maps. Let \(t=t(\pi)\in\{0,\ldots,k\}\) be the number of leaves encountered from \(a\) to \(b\) while reading the update order cyclically, beginning just after \(a\).

**Theorem (all scans and exact graph-edit response).** The maps are invertible, so every configuration is periodic from time zero. Their \(\mathbb F_2\)-linear similarity types are as follows. Here \(J_s(1)\) denotes one size-\(s\) unipotent Jordan block, and \(C_3\) is the companion matrix of \(z^2+z+1\).

| Number of pages and cyclic gap | Triangular-book normal form | Complete-bipartite normal form |
|---|---|---|
| \(k\) odd (every \(t\)) | \(J_3(1)\oplus I_{k-1}\) | \(J_3(1)\oplus I_{k-1}\) |
| \(k\) even, \(t\) even | \(C_3\oplus I_k\) | \(J_2(1)\oplus J_2(1)\oplus I_{k-2}\) |
| \(k\) even, \(t\) odd | \(J_2(1)\oplus J_2(1)\oplus I_{k-2}\) | \(C_3\oplus I_k\) |

Thus an edge between the two hubs is **dynamically invisible up to linear conjugacy for every scan when \(k\) is odd**, but **interchanges the two- and three-step nonfixed orbit regimes for every scan when \(k\) is even**. This is an exact single-edge response, not a claim that either pair of update maps is literally equal on the labelled states.

For the triangular book, the exact populations of states of primitive period \(d\), with omitted periods having zero population, are
\[
\begin{array}{c|rrrr}
& P_1&P_2&P_3&P_4\\\hline
 k\text{ odd}&2^k&2^k&0&2^{k+1}\\
 k\text{ even},\ t\text{ even}&2^k&0&3\cdot2^k&0\\
 k\text{ even},\ t\text{ odd}&2^k&3\cdot2^k&0&0.
\end{array}
\]
Dividing \(P_d\) by \(d\) gives the number of distinct primitive \(d\)-cycles. The complete-bipartite populations are identical in the odd case and exchange the last two lines in the even case.

For even \(k=2m\), **exactly**
\[
 (m+1)(k+2)k!\quad\text{of the }(k+2)!\text{ labelled scanning orders}
\]
produce primitive three-cycles on \(B_k\), while the other \(m(k+2)k!\) produce primitive two-cycles. On \(Q_k\) these frequencies are reversed. Thus the single added edge flips the cycle class of every labelled scan, but it does not merely permute the two class frequencies: it reverses which class occurs more often. For odd \(k\), all \((k+2)!\) scans have the same \(1,2,4\) period census on both graphs.

## Assumptions and scope

The result is over \(\mathbb F_2\), on finite simple undirected graphs with \(k\ge1\), with all \(k+2\) vertices labelled. The local rule includes the existing value at the updated site (self-inclusive XOR), has no threshold, and each scan is a permutation with one visit per site; the same scan repeats. The graph \(B_k\) has \(k\) triangles sharing the spine \(ab\); \(Q_k\) is obtained by deleting that spine. This result does not claim an analogue for synchronous updates, multiple visits in a scan, or general finite fields.

A primitive period is the least strictly positive integer \(d\) for which \(T^d(x)=x\). The order of a map is the least positive \(d\) such that \(T^d=I\) on the full state space. A Jordan form here is a rational canonical classification over \(\mathbb F_2\), and its existence does not imply that a graph isomorphism realizes the conjugation.

## Proof

**1. Reduction of an arbitrary order.** Every vertex update is a linear involution: its neighbors are unaffected while that vertex is updated, so a second update cancels the same neighbor parity. Hence a scan is invertible. Cyclically moving the first update to the end conjugates the full product of invertible updates. All leaves are pairwise nonadjacent and have the same neighbor set, so their local updates commute. A cyclic rotation and commuting leaves therefore reduce the proof of the complete primitive orbit census for any labelled scan to the order
\[
 a,\quad A=(w_1,\ldots,w_t),\quad b,\quad D=(w_{t+1},\ldots,w_k),
\]
with \(t\) leaves in \(A\), \(s=k-t\) leaves in \(D\). The cyclic rotation is a *linear* conjugation and commuting leaves does not change the map. Relabelling leaves is also a linear conjugation. Thus this reduction preserves Jordan forms and counts, not merely possible period lengths.

**2. Exact two-hub and leaf-parity update.** Let \(a,b\in\mathbb F_2\) be hub states, \(U=\sum_{w\in A}x_w\), \(V=\sum_{w\in D}x_w\), and \(\alpha=t\bmod2\), \(\beta=s\bmod2\). Write \(L=a+U+V\). One triangular-book scan has precisely the following form:
\[
\begin{aligned}
 a'&=b+L, & b'&=a+\alpha L,\\
 U'&=U+\alpha L, & V'&=V+\beta\bigl(a+b+(1+\alpha)L\bigr).
\end{aligned}
\]
More precisely, **every** leaf in \(A\) is changed by the common bit \(L\), and **every** leaf in \(D\) is changed by \(a+b+(1+\alpha)L\). These formulas follow successively by updating \(a\), then the \(A\)-leaves, then \(b\), then the \(D\)-leaves; they remain valid when either group is empty (its sum and its leaf-update clause are then vacuous).

For comparison, on the graph without the spine, write \(R=a+b+U+V\). The corresponding exact formulas are
\[
\begin{aligned}
 a'&=a+U+V, & b'&=b+U+V+\alpha R,\\
 U'&=U+\alpha R, & V'&=V+\beta\bigl(U+V+(1+\alpha)R\bigr),
\end{aligned}
\]
with each leaf in \(A\) changed by \(R\) and each leaf in \(D\) changed by \(U+V+(1+\alpha)R\). All formulas are identities in characteristic two, not approximate orbit descriptions.

**3. Exact periods of the book.** There are only four parity pairs \((\alpha,\beta)\). Substitution of the formulas in Step 2 into themselves gives:

- For \((0,0)\), the third iterate returns the two hub states and both leaf groups unchanged, so \(T_{B,\pi}^3=I\).
- For \((1,1)\), the second iterate returns all states unchanged, so \(T_{B,\pi}^2=I\).
- For \((0,1)\), the second iterate changes precisely the two hubs and *every* leaf of \(D\) by the common bit \(a+U+V\), and does not change the \(A\)-leaves. A further two iterates return every state; hence \(T_{B,\pi}^4=I\) and \(\operatorname{rank}(T_{B,\pi}^2-I)=1\).
- For \((1,0)\), the second iterate changes precisely the two hubs and *every* leaf of \(A\) by the common bit \(a+b\), and does not change the \(D\)-leaves. Again \(T_{B,\pi}^4=I\) and \(\operatorname{rank}(T_{B,\pi}^2-I)=1\).

The two rank-one assertions are genuine: for \((0,1)\) the group \(D\) is nonempty, and for \((1,0)\) the group \(A\) is nonempty; each displayed linear functional is nonzero on the full state space. Since \(\alpha+\beta=k\bmod2\), odd \(k\) gives precisely the two order-four cases; even \(k\) gives the order-three case for even \(t\) and the order-two case for odd \(t\).

For every \(k\), the fixed states satisfy \(a=b=\sum_i x_{w_i}\). Indeed, a full scan can fix the state only if no individual site changes: each vertex is visited only once, so a site cannot flip and subsequently flip back during that scan. The leaf conditions give \(a+b=0\); the hub conditions then give \(a=b=\sum_i x_{w_i}\). These are two independent linear constraints, hence \(\dim\ker(T_{B,\pi}-I)=k\).

For even \(k\) and even \(t\), the map has order three and fixed-space dimension \(k\). The nonfixed dimension is two and must be one irreducible two-dimensional order-three summand, giving \(C_3\oplus I_k\). For even \(k\) and odd \(t\), the map has order two, so \((T-I)^2=0\), and its rank is two. Thus it has two Jordan blocks of size two and \(k-2\) of size one. For odd \(k\), \((T-I)^4=0\) and \(\dim\ker(T-I)=k\), while the displayed rank-one formula for \(T^2-I=(T-I)^2\) leaves exactly one size-three block and \(k-1\) size-one blocks. This proves the triangular-book normal forms and, by kernel-counting, the stated primitive-period populations.

**4. Exact edge-completion comparison.** For \(Q_k\), the formulas of Step 2 give the opposite even-page dichotomy: \((\alpha,\beta)=(0,0)\) implies \(T_{Q,\pi}^2=I\), whereas \((1,1)\) implies \(T_{Q,\pi}^3=I\). The fixed-state conditions are \(a=b\) and \(U+V=0\), which again give \(k\) fixed dimensions. If \(k\) is odd, the two remaining cases have \(T_{Q,\pi}^4=I\), \(\operatorname{rank}(T_{Q,\pi}^2-I)=1\), and \(\dim\ker(T_{Q,\pi}-I)=k\). The same Jordan-block argument as in Step 3 yields the three displayed complete-bipartite normal forms. In particular the edge-completion comparison is a statement of *linear conjugacy type* for all scans, and is not inferred merely from a coincident list of periods.

**5. Number of labelled update orders.** For each prescribed \(t\in\{0,\ldots,k\}\), choose the position of hub \(a\) in \(k+2\) ways, then place hub \(b\) exactly \(t+1\) positions later around the cyclic order, then arbitrarily permute the \(k\) labelled leaves. Thus each \(t\) occurs in exactly \((k+2)k!=(k+2)!/(k+1)\) schedules. For even \(k=2m\), there are \(m+1\) even choices and \(m\) odd choices of \(t\). Combining these counts with the period cases proves the frequency reversal, including the boundaries \(k=1\) and \(k=2\). This completes the proof.

## Verification

The independent direct-update program `verification/verify_exhaustive.py` checks **every labelled scanning order** and **every binary initial configuration** for \(1\le k\le5\), using the vertex adjacency masks rather than the proof's quotient formulas. Its successful recorded run checks 5,910 labelled schedules and 695,472 schedule-state pairs. Each trajectory is simulated until its least period (at most four) is determined and is checked against the case formula; it also checks the exact parity-class frequency of schedules.

The separate standard-library binary-matrix program `verification/verify_linear.py` constructs every representative ordered scan for \(1\le k\le40\) and \(0\le t\le k\), for both graphs, by applying each update to the standard basis. It computes all fixed-space dimensions of the first twelve powers directly over \(\mathbb F_2\) and checks all cases of the theorem. The successful recorded run checks 20,640 fixed-space-dimension equalities and 5,160 cross-graph comparisons. The recorded outputs are in `verification/exhaustive_output.txt` and `verification/linear_output.txt`.

To reproduce from an extracted package, run `python3 verification/verify_exhaustive.py` and `python3 verification/verify_linear.py` in any working directory. All scripts use only Python's standard library. Finite calculations corroborate the proof but are not used to infer the statements for all \(k\).

## Relationship to prior work

Macauley, McCammond and Mortveit (2007, arXiv:0707.2360) develop update-order invariance, and Macauley and Mortveit (2008, arXiv:0802.4412) establish cycle equivalence under shifts and reflections of update orders *for a fixed graph*. Defant (2015, arXiv:1511.06966) classifies invertible asynchronous Rule 150/105 dynamics on **cycle graphs**. None of those graph scopes yields the specific all-scan, single-edge comparison between the nonbipartite triangular book and its complete-bipartite deletion.

An accessible complete-bipartite parity classification, *A modulo-three scheduling law for sequential parity dynamics on complete bipartite graphs* (public published-finding corpus record `2026/11/2/...--a1fb648a5614`), supplies the full \(Q_k\) side. It does **not** state or imply the triangular-book side without a separate analysis of the changed hub update; that step is proved here. A separate public record, *Dense–sparse cycle equivalence and scan-frequency laws for one-edge-deleted cliques* (`2026/11/2/...--c675021794c5`), addresses a different pair of graphs and different schedule statistics, not this edge-completion theorem. The prior *Exact entrance-time census and parity law for majority dynamics on triangular books* concerns simultaneous strict majority, not sequential XOR. The comparison is based on exact statements and map domains, not title matching alone.

## Limitations

The theorem concerns one graph family, one binary local rule, and fixed simple scanning orders. It does not claim that the same labelled starting state has the same orbit after the spine edge is added; it proves a conjugacy classification. The formula is not a classification of arbitrary finite graphs or arbitrary schedules with repeated site visits. General historical treatments of affine Boolean sequential networks may supply alternative normal-form machinery, and unindexed earlier sources could affect historical priority. The mathematical proof and reproducibility checks do not constitute independent expert validation or independent audit.

## References

1. M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360, first posted 2007-07-16, https://arxiv.org/abs/0707.2360.
2. M. Macauley and H. S. Mortveit, *Cycle Equivalence of Graph Dynamical Systems*, arXiv:0802.4412, first posted 2008-02-29, https://arxiv.org/abs/0802.4412.
3. C. Defant, *Flexible Toggles and Symmetric Invertible Asynchronous Elementary Cellular Automata*, arXiv:1511.06966, first posted 2015-11-22, https://arxiv.org/abs/1511.06966.
4. *A modulo-three scheduling law for sequential parity dynamics on complete bipartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-modulo-three-scheduling-law-for-sequential-parity-dynamics-on--a1fb648a5614 (public mathematical result, accessed by its complete result text).
5. *Dense–sparse cycle equivalence and scan-frequency laws for one-edge-deleted cliques*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-dense-sparse-cycle-equivalence-and-scan-frequency-laws-for-one-e--c675021794c5 (public mathematical result, accessed by its complete result text).
6. *Exact entrance-time census and parity law for majority dynamics on triangular books*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-entrance-time-census-and-parity-law-for-majority-dynamics--260f52d7946d (different local rule).
