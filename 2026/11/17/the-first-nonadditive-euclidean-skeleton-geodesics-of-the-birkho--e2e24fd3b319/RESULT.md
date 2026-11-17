# The first nonadditive Euclidean skeleton geodesics of the Birkhoff polytope

## Finding
For every integer \(n\ge 2\), give each edge of the one-skeleton of the Birkhoff polytope \(\mathcal B_n\) its inherited Frobenius length, and let \(d_n\) be the resulting shortest-path metric on its permutation-matrix vertices. For \(\sigma,\tau\in S_n\), write \(\rho=\sigma^{-1}\tau\), let \(s(\rho)\) be the number of moved symbols, and let
\[
L(\rho)=\sum_{C\text{ a nontrivial cycle of }\rho}\sqrt{2|C|}.
\]
The following sharp boundary holds.

1. If \(s(\rho)\le5\), then \(d_n(P_\sigma,P_\tau)=L(\rho)\): separate moves around the disjoint cycles are shortest.
2. If \(n\ge6\) and \(\rho\) is a product of three disjoint transpositions (fixing all other symbols), then
\[
d_n(P_\sigma,P_\tau)=\sqrt6+\sqrt{12}<6=L(\rho).
\]
There are **exactly 32 distinct shortest vertex paths** between these vertices, all with two edges. Exactly 16 use a three-cycle move followed by a six-cycle move, and exactly 16 use the reverse order. Every shortest path fixes all symbols outside the six-point support.

Thus six moved symbols are the *least possible support size* at which the natural disjoint-cycle edge-length sum fails to equal the intrinsic weighted skeleton distance.

## Assumptions and scope
\(\mathcal B_n=\{X\in\mathbb R_{\ge0}^{n\times n}:X\mathbf1=\mathbf1,\ X^{\mathsf T}\mathbf1=\mathbf1\}\) with its standard ambient Frobenius metric \(\|A-B\|_F\). Its vertices are permutation matrices \(P_\sigma\). Distances here are measured **along polytope edges**, not across the polytope interior. The known one-skeleton adjacency criterion states that \(P_\sigma\) and \(P_\tau\) are joined by an edge exactly when \(\sigma^{-1}\tau\) is a single cycle of length \(k\ge2\). That edge has length \(\sqrt{2k}\), since the matrices differ in exactly \(2k\) unit entries. Relabeling or translating by a permutation preserves all these lengths. Nontrivial cycles are of length at least two; fixed points do not contribute to \(L\).

## Proof
**Preliminary support lemma.** Let \(\alpha\) and \(\beta\) be nontrivial cycles with respective supports \(A,B\), with nonempty intersection \(I=A\cap B\) of size \(s\). Set \(U=A\cup B\), \(v=|U|\). Every cycle of \(\alpha\beta\), considered as a permutation of \(U\) and including fixed-point cycles, contains an element of \(I\). Indeed, if an \(\alpha\beta\)-orbit avoided \(I\) and contained \(x\in A\setminus B\), its successive orbit points would follow \(\alpha\) through \(A\setminus B\) until hitting \(I\), impossible. If instead the orbit contained only points of \(B\setminus A\), its successive points would follow the single cycle \(\beta\) there until \(\beta\) reached \(I\); the next image under \(\alpha\beta\) would either lie in \(I\) or in \(A\setminus B\), again impossible. Consequently the number \(c_U(\alpha\beta)\) of all cycles on \(U\) is at most \(s\).

**At most five moved symbols.** For a single nontrivial cycle of length \(k\), the direct edge length \(\sqrt{2k}\) is the ambient Euclidean distance between the endpoints, so the triangle inequality proves it shortest. Every nonidentity permutation moving at most five symbols is either a single nontrivial cycle, a product of two disjoint transpositions, or a product of a disjoint transposition and three-cycle. The latter two have evident two-edge paths of lengths \(4\) and \(2+\sqrt6\), respectively. Any path of three or more edges has length at least \(6\), since every edge costs at least \(2\). For the two-transposition case, any two-edge path costs at least \(4\), and no single edge exists. For the two-plus-three case, a two-edge path cheaper than \(2+\sqrt6\) would have to use two transpositions, the only generator pair with smaller summed cost; their product is even, whereas a disjoint two-plus-three permutation is odd. Thus the exhibited paths are optimal for every ambient \(n\).

**Three disjoint transpositions.** By vertex transitivity take \(\sigma\) to be the identity and \(\rho=(a_1b_1)(a_2b_2)(a_3b_3)\). A one-edge path is impossible, and every path with three or more edges has length at least \(6\). Consider a two-edge path corresponding to a factorization \(\rho=\alpha\beta\) into cycles of lengths \(k,l\ge2\). Disjoint supports are impossible, since their product has only two nontrivial cycles. For overlapping supports, let \(v=|\operatorname{supp}\alpha\cup\operatorname{supp}\beta|\ge6\) and \(s=k+l-v\). The product on that union has exactly three two-cycles and \(v-6\) fixed points, hence \(v-3\) cycles. The support lemma implies
\[
v-3\le s=k+l-v,\qquad k+l\ge2v-3\ge9.
\]
Parity gives \(k+l\) odd. For \(k+l\ge11\), the concavity of square root yields
\[
\sqrt{2k}+\sqrt{2l}\ge2+\sqrt{18}>\sqrt6+\sqrt{12}.
\]
If \(k+l=9\), the displayed inequality forces \(v=6\), hence \(s=3\). As \(s\le\min(k,l)\), the only unordered length pairs are \((3,6)\) and \((4,5)\), and
\[
\sqrt6+\sqrt{12}<\sqrt8+\sqrt{10}.
\]
This gives the claimed lower bound for all two-edge paths.

For attainment, choose one element from each of the three transposition pairs and let \(\alpha\) be either orientation of the three-cycle on those elements. Multiplication of the three disjoint two-cycles by \(\alpha^{-1}\) merges the three components into one six-cycle \(\beta=\alpha^{-1}\rho\). Thus \(\rho=\alpha\beta\), a path with cost \(\sqrt6+\sqrt{12}<6\). Necessity and the count follow from the equality-case support analysis: every optimal two-edge factorization has length pair \((3,6)\) or \((6,3)\); the three-cycle uses precisely one element from each of the three transposition pairs. There are \(2^3\) selections and two cyclic orientations, totaling 16 factorizations of each order. Their intermediate permutations are distinct, since a three-cycle cannot equal a six-cycle. No shortest path uses an outside symbol, as \(v=6\) is forced. Translation by \(\sigma\) gives the assertion for arbitrary endpoints. \(\square\)

## Verification
The accompanying standalone standard-library `check.py` generates every single-cycle edge of \(\mathcal B_n\), runs Dijkstra's algorithm with exact-formula floating weights \(\sqrt{2k}\), and checks the theorem for all endpoint permutations in dimensions six and seven. It also independently enumerates ordered optimal two-cycle factorizations of the canonical triple transposition and obtains 16 for each order. Run `python check.py` and optionally `python check.py 7`. The arithmetic proof above, not those finite checks, establishes all dimensions.

## Relationship to prior work
The single-cycle edge criterion and the *unweighted* graph diameter two are established properties of Birkhoff polytopes; they are not new here. Huang, Li, Swartz and Sze (2022) study cliques and independent sets of the cycle-generated Birkhoff graph, and Cardinal and Steiner (2022) study *step-count* shortest paths for bipartite perfect-matching polytopes and their algorithmic difficulty. These results do not imply a Frobenius-edge-weighted shortest-path law or count the 32 length-minimizing two-step paths for triple transpositions. The novelty claim is limited to this weighted six-point onset and its exact geodesic enumeration.

## Limitations
No formula for the full weighted Birkhoff graph metric, for arbitrary permutation cycle type, or for its weighted diameter is claimed. The result does not classify all minimal-cost paths for permutations moving more than six symbols. Historical priority remains subject to independent literature review, including possible equivalent formulations as weighted cycle factorizations or Cayley word metrics. Numerical Dijkstra checks cover only orders six and seven and are not infinite-dimensional proofs.

## References
- Z. Huang, C.-K. Li, E. Swartz, N.-S. Sze, *Cliques and independent sets of the Birkhoff polytope graph*, arXiv:2212.12655, first public version 2022-12-24, https://arxiv.org/abs/2212.12655.
- J. Cardinal and R. Steiner, *Inapproximability of shortest paths on perfect matching polytopes*, arXiv:2210.14608, first public version 2022-10-26, https://arxiv.org/abs/2210.14608.
- R. Cação et al., *Quantum Walk on the Generalized Birkhoff Polytope Graph*, *Entropy* 23(10), 1239 (2021-09-23), https://pmc.ncbi.nlm.nih.gov/articles/PMC8534586/ (different generalized graph and unweighted walk setting).
