# Minimum isolation on uniform loose hypercycles: type-refined census and exchange connectivity

## Finding

Let \(r\ge3\) and \(m\ge3\) be integers. Construct the labelled \(r\)-uniform *loose hypercycle* \(H_{m,r}\) with hyperedges \(E_i=\{w_{i-1},w_i\}\cup U_i\), indexed by \(i\in\mathbb Z/m\mathbb Z\), where the \(w_i\) are distinct junction vertices and the \(U_i\) are pairwise disjoint private sets of cardinality \(r-2\), disjoint from all junction vertices. A set \(S\) is isolating when its closed hypergraph neighbourhood meets every hyperedge. Put \(k=\lceil m/4\rceil\) and \(\delta=4k-m\in\{0,1,2,3\}\).

**Theorem.** The isolation number is \(\iota(H_{m,r})=k\). The polynomial enumerating all minimum isolating sets by the number of their selected *private* vertices is

\[
\boxed{\displaystyle F_{m,r}(y)=\sum_{\substack{S\subseteq V(H_{m,r})\\|S|=k\text{ isolating}}}y^{|S\cap(\cup_i U_i)|}=\frac{m}{k}[u^{\delta}]\Bigl(1+\bigl(1+(r-2)y\bigr)(u+u^2+u^3)\Bigr)^k.}
\]

Thus the complete number of minima is \(F_{m,r}(1)\), and **every minimum isolating set contains at most three private vertices**, regardless of the number of hyperedges or the rank. Define \(q=1+(r-2)y\). The type-polynomial takes the explicit four-residue form

\[
F_{m,r}(y)=\begin{cases}
4,&\delta=0,\\
mq,&\delta=1,\\
m\bigl(q+\frac{k-1}{2}q^2\bigr),&\delta=2,\\
m\bigl(q+(k-1)q^2+\frac{(k-1)(k-2)}{6}q^3\bigr),&\delta=3.
\end{cases}
\]

Construct a graph \(\mathcal E_{m,r}\) whose vertices are the minimum isolating sets, joining two sets if one vertex is replaced by another. If \(m=4\), the exchange graph is \(K_4\). If \(m\ge8\) and \(4\mid m\), it consists of exactly four isolated vertices. In all other cases \(m\ge3\), the exchange graph is connected. Consequently the minimum-set exchange connectivity has an exact sharp four-periodic obstruction.

## Assumptions and scope

All hypergraphs are finite, simple, labelled, and \(r\)-uniform. A vertex's closed neighbourhood contains itself and all vertices with which it shares a hyperedge; \(N[S]\) is the union for \(v\in S\). An isolating set satisfies \(E_i\cap N[S]\ne\varnothing\) for **every** \(i\); equivalently no hyperedge survives in the induced hypergraph on \(V\setminus N[S]\). The theorem quantifies over **all** \(m\ge3\) and \(r\ge3\). \(F_{m,r}\) counts actual labelled subsets, not rotations or orbit classes. It counts precisely minimum sets, not all or inclusion-minimal nonminimum isolating sets.

## Proof

**Local coverage.** The closed neighbourhood of any private vertex in \(U_i\) is exactly \(E_i\), and therefore meets exactly the cyclic hyperedges \(E_{i-1},E_i,E_{i+1}\) (with duplicates removed in the three-edge boundary case). The closed neighbourhood of a junction vertex \(w_i\) is \(E_i\cup E_{i+1}\), and therefore meets \(E_{i-1},E_i,E_{i+1},E_{i+2}\). These give respectively arcs of three and four consecutive hyperedge positions, both starting at the same position \(i-1\). Each selected vertex thus covers at most four hyperedges, proving \(|S|\ge\lceil m/4\rceil=k\). Conversely, choose \(k\) junction vertices whose arc starts have positive cyclic spacings at most four; their arcs cover all hyperedges. Hence the lower bound is attained.

**Distinct starts and the gap condition.** In a minimum isolating set, no two selected vertices have the same arc start. Indeed, the corresponding arcs are nested (a three-arc lies inside its four-arc, or two three-arcs coincide), so one such selected vertex could be removed without losing coverage, contradicting cardinality minimality. Enumerate its distinct arc starts clockwise as \(a_1,\dots,a_k\), and let \(d_i\ge1\) be the cyclic distance from \(a_i\) to \(a_{i+1}\). Their sum is \(m\). Write \(\ell_i=4\) for a junction or \(\ell_i=3\) for a private vertex. The selected arcs cover the hyperedge positions **if and only if** \(d_i\le\ell_i\) for every \(i\). The forward implication follows because a previous start cannot extend strictly farther right than a later start: starts are separated by at least one position and arc lengths differ by at most one, so their right endpoints are nondecreasing in start order. The backward implication is immediate: each interval of positions from \(a_i\) to just before \(a_{i+1}\) lies in the arc beginning at \(a_i\). For \(m=3,4\), the same statement holds directly on the cyclic positions, including a single start.

**Enumeration.** Write \(d_i=4-b_i\), where \(b_i\ge0\). The cyclic spacing sum gives \(\sum_i b_i=4k-m=\delta\le3\). Conversely, any weak composition of \(\delta\) into \(k\) parts gives positive spacings, since each \(b_i\le3\). If \(b_i=0\), then \(d_i=4\) and the corresponding selected vertex must be the unique junction with that arc start. If \(b_i\ge1\), either that junction or any of the \(r-2\) private vertices with the same start can be selected. The latter selection contributes one power of \(y\). Marking \(b_i\) with \(u^{b_i}\), the local weight is therefore \(1+(1+(r-2)y)(u+u^2+u^3)\). Choosing an initial labelled arc start produces \(m\) options; every final minimum set has exactly \(k\) distinguished starts. Double-counting (minimum set, distinguished selected vertex) proves the boxed coefficient formula. Expanding for \(\delta\le3\) yields the four cases. Every private selected vertex requires a positive deficit \(b_i\), so there are at most \(\delta\le3\) of them.

**Exchange connectivity.** For \(m=3\), every singleton is isolating and the exchange graph is complete. For \(m=4\), precisely the four junction singletons are isolating, giving \(K_4\). Assume now \(m\ge5\), so \(k\ge2\). Replacing any selected private vertex in \(U_i\) by junction \(w_i\) preserves isolation, since the four-arc includes the three-arc; by the distinct-start property this is a genuine one-vertex replacement. Repeating yields a minimum set consisting exclusively of junctions. The junction-only minimum sets correspond, via their arc starts, to the minimum isolating sets of the ordinary labelled cycle \(C_m\) (the same cyclic gap condition \(d_i\le4\)). When \(\delta>0\), these are connected under one-vertex replacement: moving a junction by one hyperedge position transports a deficit unit between adjacent gaps, allowing any weak composition of the \(\delta\) deficit units to be reached; transporting one unit around all cyclic gaps translates the labelled configuration by one position. This gives both changes of gap pattern and all rotations. Hence all minimum sets, including those containing private vertices, belong to one connected component. If \(\delta=0\), every gap is exactly four and all chosen vertices are junctions; there are precisely four possible periodic patterns. For \(m=4k\ge8\), each pattern contains at least two vertices, and different patterns are disjoint, so they cannot be adjacent by a one-vertex replacement. They are four isolated vertices. These cases exhaust the parameters.

## Verification

The accompanying standalone `verify_hypercycle.py` constructs the hyperedges and closed vertex neighbourhoods directly, without relying on the cyclic-arc formula. It compares the counts by private-vertex type against an independently implemented coefficient expansion, and constructs the complete one-vertex-exchange graph for small cases. The executed tests checked 44 combinations of ranks \(3\) through \(6\) and cyclic orders \(3\) through \(16\) subject to a 70,000-candidate bound, considering a total of 270,310 candidate minimum-cardinality subsets. Separate exact integer checks cover every order \(3\le m\le699\) and rank \(3\le r\le39\). Output: `VERIFY_OK`. The infinite-parameter result is established by the proof, not the finite tests.

## Relationship to prior work

Borg's 2025 preprint [1] studies clique isolation in general uniform hypergraphs and solves sharp universal upper-bound questions, with extremal classifications. It does not enumerate the optimal isolating sets of loose hypercycles, distinguish junction and private choices, or determine their replacement connectivity. The case of ordinary edge isolation is obtained from Borg's setup by taking the forbidden clique of size equal to the uniform rank.

Caro and Hansberg [2] introduced ordinary graph isolation and gave the cycle isolation number, but a simple graph cycle has no private hyperedge vertices. The closer published result [3] gives the complete enumeration and one-vertex-replacement connectivity for minimum isolating sets of **ordinary simple cycles**. Its cyclic-gap method is relevant and the graph result is credited, not claimed new. The present claim concerns rank \(r\ge3\), adds the new bivariate rank-dependent *type* census and obtains the corresponding exchange geometry of an actual hypergraph. In particular, the graph formula alone does not count the additional \(r-2\) choices at each shortened gap or prove that these added solutions do not alter the connectivity transition. The general hypergraph domination framework of Li, Zhang and Ye [4] concerns bounds rather than the stated minimum-set polynomial and reconfiguration graph.

## Limitations

The classification is restricted to the explicitly defined *loose* hypercycles. It does not hold automatically for tight hypercycles, arbitrary linear unicyclic hypergraphs, or hypertrees with branches. No count of nonminimum isolating sets or replacement-graph diameter is claimed. Comparisons with earlier unindexed work on cyclic domination and hypergraph isolation cannot establish absolute historical priority. A related 2024 hypergraph paper [4] was available here at abstract level only. No independent mathematical audit has been performed.

## References

1. P. Borg, *Solution to a problem on isolation of cliques in uniform hypergraphs*, arXiv:2601.00104v1, first public 2025-12-31. https://arxiv.org/abs/2601.00104
2. Y. Caro and A. Hansberg, *Partial domination—the isolation number of a graph*, arXiv:1504.08055v1, first public 2015-04-30. https://arxiv.org/abs/1504.08055
3. *A four-periodic reconfiguration theorem for minimum isolating sets on cycles*, published 2026-11-02, repository identifier `2026/11/2/SCOPE-a-four-periodic-reconfiguration-theorem-for-minimum-isolating-se--4d710023d8c9`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-four-periodic-reconfiguration-theorem-for-minimum-isolating-se--4d710023d8c9
4. M. Li, S. Zhang and C. Ye, *Partial domination of hypergraphs*, Graphs and Combinatorics 40 (2024), article 109. https://doi.org/10.1007/s00373-024-02840-2
