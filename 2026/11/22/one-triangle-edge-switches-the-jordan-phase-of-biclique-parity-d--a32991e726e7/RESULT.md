# One triangle edge switches the Jordan phase of biclique parity dynamics

## Finding

Let \(a\ge 3\), \(b\ge 2\), and \(N=a+b\). Begin with the simple, undirected complete bipartite graph \(K_{a,b}\) and add exactly one edge between two distinguished vertices in the shore of size \(a\). On \(\mathbb F_2^N\), apply the **synchronous, self-exclusive neighbor-XOR** rule \(F(x)_v=\sum_{w\sim v}x_w\pmod 2\). Let \(J_s(\lambda)\) denote the size-\(s\) Jordan block with eigenvalue \(\lambda\) over \(\mathbb F_2\). The complete similarity classification, **for every admissible pair of sizes**, is

\[
\begin{array}{c|l|c|c}
(a\bmod2,b\bmod2)&\text{Jordan form of }F&\text{periodic dimension}&\text{sharp entry time}\\\hline
(0,0)&J_2(1)\oplus J_2(0)^{\oplus2}\oplus J_1(0)^{\oplus(N-6)}&2&2\\
(0,1)&J_1(1)^{\oplus2}\oplus J_3(0)\oplus J_1(0)^{\oplus(N-5)}&2&3\\
(1,0)&J_2(1)\oplus J_3(0)\oplus J_1(0)^{\oplus(N-5)}&2&3\\
(1,1)&J_4(1)\oplus J_1(0)^{\oplus(N-4)}&4&1
\end{array}
\]

Here *entry time* is the smallest \(t\ge0\) at which a state belongs to a periodic temporal orbit; the sharp entry time is its maximum over all starting configurations. These are precise block decompositions and not just lists of possible periods. In particular, **three primitive four-cycles occur exactly when both shores have odd size**. Adding the edge also creates nonzero periodic states in all three cases where the unedited complete bipartite rule is nilpotent.

Writing \(P_d\) for the number of configurations with **least** temporal period \(d\), all other periods are absent and

\[
\begin{array}{c|rrr}
(a\bmod2,b\bmod2)&P_1&P_2&P_4\\\hline
(0,0)&2&2&0\\
(0,1)&4&0&0\\
(1,0)&2&2&0\\
(1,1)&2&2&12
\end{array}.
\]

Each attractor orbit of length \(d\) has an **exactly equal-sized individual basin** of \(d2^{N-r}\) initial states, where \(r=4\) in the odd–odd case and \(r=2\) otherwise. The cumulative first-entry population, \(H(t)=\#\{x:\text{entry time}(x)\le t\}\), is given exactly by

\[
\begin{array}{c|rrrr}
(a\bmod2,b\bmod2)&H(0)&H(1)&H(2)&H(3)\\\hline
(0,0)&4&2^{N-2}&2^N&2^N\\
(0,1)&4&2^{N-2}&2^{N-1}&2^N\\
(1,0)&4&2^{N-2}&2^{N-1}&2^N\\
(1,1)&16&2^N&2^N&2^N
\end{array}.
\]

Thus the full first-entry shell counts are the differences between successive entries of this table, with the time-zero shell equal to \(H(0)\). These identities include every finite boundary in the stated domain.

## Assumptions and scope

The graph has two nonempty parts, with at least three vertices in the *edited* shore and at least two in the other shore. The chosen internal edge is unique, joining two otherwise nonadjacent vertices of the larger-specified shore; all such choices are equivalent under graph relabelling. The update is simultaneous, additive over \(\mathbb F_2\), and excludes the vertex's previous state except through its neighbors. Orbit and basin counts are on **labelled configurations**. No random graph, infinite-size limit or alternative update schedule is assumed. The symbols \(J_s(0)^{\oplus k}\) with \(k=0\) mean an absent block.

## Proof

**Step 1 — four-dimensional exact image.** Label the endpoints of the added edge \(0,1\), the other \(a-2\) vertices of the edited shore \(2,\ldots,a-1\), and the opposite shore \(a,\ldots,N-1\). For any starting state write \(S_A=\sum_{i<a}x_i\) and \(S_B=\sum_{j\ge a}x_j\), with sums in \(\mathbb F_2\). Directly from adjacency,

\[
(Fx)_0=S_B+x_1,\qquad (Fx)_1=S_B+x_0,\qquad
(Fx)_i=S_B\ (2\le i<a),\qquad (Fx)_j=S_A\ (a\le j<N).
\]

All output vectors therefore lie in the subspace \(W\) in which vertices \(2,\ldots,a-1\) have one common value and all vertices in the opposite shore have another common value. This subspace is **four-dimensional**. It is the full image because the four independent input functionals \(x_0,x_1,S_A,S_B\) can be specified arbitrarily when \(a\ge3\) and \(b\ge2\). Hence \(\operatorname{rank}F=4\).

**Step 2 — induced parity matrix.** Write a state of \(W\) as \((p,q,r,t)\), where \(p,q\) are the added edge endpoints, \(r\) is the common value on the remaining edited-shore vertices, and \(t\) is the common value on the opposite shore. Put \(\alpha=a\bmod2\) and \(\beta=b\bmod2\), interpreted as elements of \(\mathbb F_2\). Its next values are

\[
\begin{pmatrix}p'\\q'\\r'\\t'\end{pmatrix}
=M_{\alpha\beta}\begin{pmatrix}p\\q\\r\\t\end{pmatrix},\qquad
M_{\alpha\beta}=
\begin{pmatrix}
0&1&0&\beta\\
1&0&0&\beta\\
0&0&0&\beta\\
1&1&\alpha&0
\end{pmatrix}.
\]

This matrix is valid in every case because the parity of \(a-2\) equals \(\alpha\). In particular, the graph and update operators are determined completely by the size parities **after their one-step image**.

**Step 3 — rank filtration and invertible part.** Direct elimination of these four displayed rows, or substitution of the update formulas, gives

\[
\begin{array}{c|cccc|l}
(\alpha,\beta)&\operatorname{rank}F&\operatorname{rank}F^2&\operatorname{rank}F^3&\operatorname{rank}F^4&\text{invertible restriction}\\\hline
(0,0)&4&2&2&2&J_2(1)\\
(0,1)&4&3&2&2&J_1(1)\oplus J_1(1)\\
(1,0)&4&3&2&2&J_2(1)\\
(1,1)&4&4&4&4&J_4(1)
\end{array}.
\]

For completeness, when \(\beta=0\) one has \(p'=q,q'=p,r'=0,t'=p+q+\alpha r\); after one or two further steps the remaining \(p,q\) swap and \(t=p+q\). When \(\beta=1,\alpha=0\), the map sends \(r'=t,t'=p+q\) and becomes the identity on its two-dimensional stable image after two applications to \(W\). When \(\alpha=\beta=1\), \(M_{11}\) is invertible and \((M_{11}+I)^4=0\), while the kernel dimensions of \((M_{11}+I)^j\) for \(j=1,2,3,4\) are \(1,2,3,4\); thus its single invertible summand is \(J_4(1)\). The rank drops from \(N\) to rank four, and then the displayed subsequent drops, determine the nilpotent Jordan block multiplicities: \((N-6)\) size-one and two size-two blocks in the even–even case; \((N-5)\) size-one and one size-three block in the mixed-parity cases; and \((N-4)\) size-one blocks in the odd–odd case. This proves the full similarity classification.

**Step 4 — temporal populations.** A unipotent \(J_2(1)\) has two points of period one and two points of least period two; \(J_1(1)\oplus J_1(1)\) has four fixed points; and \(J_4(1)\) has exactly two fixed points, four points fixed by the second iterate and sixteen fixed by the fourth. Therefore its least-period populations are \(2,2,12\), respectively for periods \(1,2,4\). The nilpotent summands contribute no nonzero periodic state. The maximum nilpotent block size gives the sharp entry time in the first table: this is attained by selecting a vector at the top of a longest nilpotent block.

To count states that have entered recurrence by time \(t\), use the Fitting direct sum of the invertible part of dimension \(r\) and the nilpotent part. A nilpotent input has vanished after \(t\) updates if and only if it lies in the kernel of the nilpotent power. Consequently

\[
H(t)=2^{N-\operatorname{rank}(F^t)+r},\qquad t\ge0,
\]

where \(F^0=I_N\). Substituting the ranks yields the exact first-entry table. Finally every periodic state has exactly \(2^{N-r}\) initial states in its corresponding eventual-phase fiber, since the projection along the nilpotent summand is a surjective linear map. Summing the fibers of the \(d\) states in a periodic orbit gives its basin size \(d2^{N-r}\). No assumption of numerical uniformity is needed.

**Step 5 — effect of a single edge.** Without the internal edge, after one update the graph has part-constant states, and the induced map is \((u,v)\mapsto(\beta v,\alpha u)\). If either shore is even, this map is nilpotent, so the zero configuration is the only periodic state. If both shores are odd, it is a two-coordinate swap: there are exactly two fixed configurations and one two-cycle. In contrast, the single added edge creates nonzero recurrent states in all formerly nilpotent cases and exactly three four-cycles in the odd–odd case. This is a sharp graph-edit response, not a consequence of the unedited graph's orbit census.

## Verification

The standard-library program `verification/verify.py` independently constructs the full \(N\)-vertex adjacency rule from neighbor masks. It checks the six successive binary ranks for all \(110\) parameter pairs with \(3\le a\le12\), \(2\le b\le12\). For the \(36\) cases having \(N\le12\), it exhaustively traces the entire finite functional graph and compares its periodic populations, first-entry shells and individual orbit basins with the all-size formulas. Six additional unedited graphs are exhaustively evaluated to check the boundary contrast. The reproduced output is in `verification/verify_output.txt`. These finite checks support the bookkeeping; the argument in the proof, not finite testing, establishes the infinite family.

## Relationship to prior work

Ciandrini, Maffi, Motta, Bassetti and Cosentino Lagomarsino study XOR feedback on random Boolean networks, explaining the role of graph topology and linear algebra; their full paper does not classify these single-edge-edited complete bipartite graphs. The published result *Sharp period-four census for complete multipartite parity automata* explicitly proves that **self-exclusive parity on an unedited complete multipartite graph has no genuine period-four states**. That theorem is not contradicted or extended by a parameter substitution here: once the internal edge is added and \(a\ge3\), nonadjacency fails transitivity and the graph is no longer complete multipartite. The new nonzero four-cycle census genuinely requires the defect calculation. The published result *A one-edge parity reversal in sequential XOR dynamics on triangular books* concerns sequential self-inclusive updates on \(K_{2,k}\) with its spine edge, rather than simultaneous neighbor-only updates on the present \(a\ge3\) family; its conjugacy theorem cannot give the present adjacency Jordan form. Kantic, Qureshi, Panario and Legl give general algorithms for linear finite dynamical systems on cyclic Galois-ring modules; those algorithms are broader machinery, but not an explicit graph-edit, all-shore-size Jordan classification.

## Limitations

The theorem is restricted to this one-edge perturbation of a complete bipartite graph, with the edge in a shore of size at least three and with binary synchronous neighbor XOR. It does not address other field characteristics, graph edits involving several edges, asynchronous schedules, or nonlinear thresholds. General finite-field Fitting theory underlies the proof and is not claimed as novel. The literature comparison does not prove historical uniqueness against unindexed sources or alternate representations. The finite verification cannot replace the universal algebraic argument or independent mathematical validation.

## References

1. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526v1, first publicly submitted 2008-09-09, https://arxiv.org/abs/0809.1526.
2. *Sharp period-four census for complete multipartite parity automata*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-period-four-census-for-complete-multipartite-parity-automa--acea41c73be7.
3. *A one-edge parity reversal in sequential XOR dynamics on triangular books*, publicly available RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-one-edge-parity-reversal-in-sequential-xor-dynamics-on-triangu--eb169b398ece.
4. J. Kantic, C. Qureshi, D. Panario and F. Legl, *On the Dynamics of Linear Finite Dynamical Systems Over Galois Rings*, arXiv:2604.01548v1, first publicly submitted 2026-04-02, https://arxiv.org/html/2604.01548v1.
