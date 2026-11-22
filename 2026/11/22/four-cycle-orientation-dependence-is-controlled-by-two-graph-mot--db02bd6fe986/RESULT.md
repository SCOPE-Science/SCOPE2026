# Four-cycle orientation dependence is controlled by two graph motifs

## Finding
Let \(G=(V,E)\) be any finite simple undirected graph. Independently orient each edge with probability \(1/2\) in either direction. For each *unoriented* simple four-cycle \(C\) (identified up to rotation and reversal), set \(I_C=1\) if its four edges form a consistently directed cycle in either cyclic direction, and otherwise set \(I_C=0\). Let \(Z=\sum_C I_C\). Write \(c_4(G)\) for the number of distinct simple four-cycles; \(k_4(G)\) for the number of four-vertex complete subgraphs; and \(b_{2,3}(G)\) for the number of edge-distinct, not necessarily induced, subgraphs isomorphic to \(K_{2,3}\).

For two *distinct* four-cycles \(C,D\), their indicator covariance is exactly
\[
\operatorname{Cov}(I_C,I_D)=
\begin{cases}
-1/64,& C\cup D\text{ is a }K_4\text{ and their edge overlap has size }2,\\
+1/64,& C\cup D\text{ is a }K_{2,3}\text{ and their edge overlap has size }2,\\
0,&\text{if their edge overlap has size }0\text{ or }1.
\end{cases}
\]
These are the only possibilities. Consequently the family \((I_C)_C\) is **pairwise independent if and only if** \(G\) contains neither \(K_4\) nor \(K_{2,3}\) as a (not necessarily induced) subgraph. Moreover,
\[
\mathbb E Z=\frac{c_4(G)}8,\qquad
\operatorname{Var}(Z)=\frac{7c_4(G)+6b_{2,3}(G)-6k_4(G)}{64}.
\]

Pairwise independence does **not** imply three-wise independence: in the three-dimensional cube graph \(Q_3\), every pair of distinct four-cycle indicators is independent, but the three square faces through any fixed vertex cannot all be directed cycles simultaneously. Each of their individual probabilities is \(1/8\), each two-face joint probability is \(1/64\), and their three-face joint probability is \(0\).

## Assumptions and scope
The graph is fixed, finite and simple; no connectedness, regularity, planarity or bipartiteness is assumed. All orientations of distinct edges are independent fair coins. A four-cycle is an edge-subgraph, not an induced graph; different cycles on the same four vertices are distinct when their edge sets differ. Both orientations of a single undirected four-cycle are included in its event \(I_C=1\). The copy count \(b_{2,3}(G)\) treats two subgraphs with different edge sets as distinct even if they use the same five vertices. No claim is made about mutual independence of the entire family.

## Proof
**1. One-cycle law.** Each four-cycle uses four independent fair edges. Exactly two of its sixteen orientations are consistently cyclic. Hence \(\mathbb P(I_C=1)=1/8\) and \(\operatorname{Var}(I_C)=7/64\).

**2. Edge overlaps.** Distinct simple four-cycles cannot share three edges: any three-edge path of a four-cycle determines the closing edge. If they share no edges, their indicator variables are independent by independence of edge orientations. If they share exactly one edge, conditioning on its orientation leaves three free edges for each cycle, and exactly one assignment of these three edges completes each directed cycle. Thus each conditional success probability equals \(1/8\) regardless of the shared edge, and the two events are conditionally independent; the unconditional joint probability is \(1/64\).

If two distinct four-cycles share precisely two edges, those shared edges are either adjacent or opposite along either cycle. If adjacent, the union contains five vertices and is exactly a \(K_{2,3}\) edge-subgraph: the two degree-three vertices are the endpoints of the shared two-edge path and the three common neighbors are the middle vertex and the two additional cycle vertices. Conditional on the two shared edge directions, both cycles can close cyclically precisely when the two directions form a directed path. This happens for two of the four equiprobable shared orientations, and each cycle then has exactly one favorable choice for its remaining two edges, with independent choices for the two cycles. Therefore
\[
\mathbb P(I_C=I_D=1)=\frac12\cdot\frac14\cdot\frac14=\frac1{32},
\]
so the covariance is \(1/32-1/64=1/64\).

If the two shared edges are opposite, both cycles use the same four vertices and their union is \(K_4\). The shared edges appear with incompatible relative cyclic directions: any orientation that makes the first four-cycle directed prevents the second from being directed. Thus the joint probability is zero, and the covariance is \(-1/64\). These exhaust all cases.

**3. Counting overlapping cycle pairs.** Inside each edge-subgraph \(K_4\) there are exactly three distinct four-cycles, hence three unordered pairs whose union is that subgraph. Conversely, each pair of distinct four-cycles whose union is \(K_4\) uniquely identifies that copy. Analogously a \(K_{2,3}\) contains three four-cycles, one for each choice of two of its three vertices in the larger part, and exactly three unordered pairs sharing a two-edge path. Each such pair uniquely determines its union copy. No pair is counted twice. Summing the individual variances and twice the pairwise covariances yields
\[
\operatorname{Var}(Z)=\frac{7c_4(G)}{64}+2\cdot\frac{3b_{2,3}(G)-3k_4(G)}{64}.
\]
The two obstructions to pairwise independence are exactly the two types of nonzero covariance; if either subgraph is present, choose two of its constituent four-cycles. If both are absent, every covariance vanishes and, because these variables are Bernoulli, every pair is independent.

**4. Cube obstruction.** In \(Q_3\), every vertex has exactly three neighbors; two vertices have at most two common neighbors, and the graph is bipartite. Thus \(Q_3\) contains neither \(K_4\) nor \(K_{2,3}\), so the six square-face indicators are pairwise independent. At one vertex, the three incident faces use the three unordered pairs of its incident edges. For any face to form a directed cycle, exactly one of its two edges incident to the vertex must point inward and the other outward. It is impossible for all three pairs among three binary edge directions to differ. Hence the joint three-face cyclic probability is zero, proving failure of three-wise independence.

## Verification
The standalone standard-library script `verify.py` enumerates every labelled simple graph on four and five vertices, checks all its fair edge orientations, and compares exact pairwise cycle probabilities and the variance to the two-motif formula. Exactly \(486\) of these graphs contain a four-cycle; all pass. It independently checks the complete six-vertex graph, where both motif types occur in many overlapping copies. For the eight-vertex cube, it enumerates its \(4096\) edge orientations and verifies the three chosen incident faces each occur \(512\) times, every pair occurs \(64\) times, and all three never occur together. The script uses exact integer counts and rational arithmetic with no external packages. Run `python3 verify.py`.

These finite checks are corroboration. The proof above covers every finite simple graph without relying on the checked size cutoff.

## Relationship to prior work
Amini, Griffiths and Huc (arXiv:0911.3969, first posted 2009-11-20) examine oriented four-cycles and their extremal existence in arbitrary oriented graphs. Their full open-access text addresses bias and forcing, not the present pairwise covariance taxonomy or exact variance for an independently oriented fixed graph. Griffiths (arXiv:1101.5421, first posted 2011-01-28) gives the four possible oriented-four-cycle types and quasirandomness criteria. Its type-I frequency \(1/8\) is the elementary one-cycle input used here; the inspected sections do not supply the covariance or forbidden-motif classification.

Classical tournament work of Andersson (1998) and Moran (1947), and a later published exact orthogonal decomposition for random tournaments, already cover the **complete-graph special case** of four-cycle count moments. In particular, the complete-graph variance \(3(4n-11)\binom n4/64\) follows from the present formula because \(c_4(K_n)=3\binom n4\), \(b_{2,3}(K_n)=10\binom n5\), and \(k_4(K_n)=\binom n4\). This complete-graph moment is not claimed as new. A published decomposition for tournaments has been inspected in full, but its complete-graph assumption does not yield the arbitrary-underlying-graph motif classification. No directly covering theorem was identified in the searched literature or indexed research, but absence from those searches does not prove priority.

## Limitations
The exact results rely on fair independent edge orientations and need not hold for biased or dependent edge directions. Pairwise independence does not imply full joint independence; the cube example makes the limitation explicit. No full classification of all three-way dependencies is asserted. The extension to arbitrary graphs is elementary once overlap types are enumerated; the contribution is the complete sharp graph-motif statement, not a new general concentration or limit theorem. Andersson's complete primary full text was inaccessible; an implicit more general formula there or in older combinatorial-statistics work remains a historical risk. No independent verification is claimed.

## References
1. O. Amini, S. Griffiths and F. Huc, *Subgraphs of weakly quasi-random oriented graphs*, arXiv:0911.3969 (first posted 2009-11-20), https://arxiv.org/abs/0911.3969.
2. S. Griffiths, *Quasi-random oriented graphs*, arXiv:1101.5421 (first posted 2011-01-28), https://arxiv.org/abs/1101.5421.
3. P. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms **13** (1998), 249–260, DOI: 10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V (abstract accessible; complete text not inspected).
4. *Exact orthogonal decomposition of three- and four-cycle counts in random tournaments*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-orthogonal-decomposition-of-three-and-four-cycle-counts-in--3b4b1b16fef5 (full result inspected for comparison).
