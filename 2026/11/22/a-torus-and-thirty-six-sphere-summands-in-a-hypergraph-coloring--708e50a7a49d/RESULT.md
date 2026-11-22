# A torus and thirty-six sphere summands in a hypergraph coloring counterexample

## Finding
Let \(H\) be the 5-uniform hypergraph on \(\{1,\ldots,9\}\) with exactly the following nine hyperedges, where the notation \(12347\) abbreviates \(\{1,2,3,4,7\}\):

\[
E(H)=\{12347,12358,12369,14567,24568,34569,14789,25789,36789\}.
\]

For the ordinary hypergraph coloring complex \(\Delta_H\) of Breuer--Dall--Kubitzke (2012, Example 23), the complete integral homotopy type is

\[
\boxed{\Delta_H\simeq T^2\vee\bigvee^{27}S^2\vee\bigvee^{9}S^3.}
\]

Here \(T^2=S^1\times S^1\); the wedge is an ordinary unbased homotopy equivalence after choosing compatible basepoints. In particular, \(\pi_1(\Delta_H)\cong\mathbb Z^2\), the reduced integral homology is \(\mathbb Z^2\) in degree 1, \(\mathbb Z^{28}\) in degree 2, and \(\mathbb Z^9\) in degree 3, and zero in all other degrees. The sole nonzero product of positive-degree reduced cohomology classes, up to the graded-ring structure, is the standard degree-one exterior product contributed by the torus.

## Assumptions and scope
The coloring complex is defined as the union of the nine edge-sphere subcomplexes \(Q_F\) in the standard braid subdivision, exactly as in Sections 2--3 and 5 of [1]. The theorem concerns this one hypergraph and ordinary, nonequivariant integral homotopy. It is not an assertion about the full family of uniform hypergraphs. The finite certificate uses zero-based indices in the displayed order of the nine edges.

## Proof
**1. Classify every intersection.** For any nonempty set \(A\subseteq E(H)\), merge vertices of each edge in \(A\) under an equivalence relation; write \(b(A)\) for the number of resulting blocks, counting isolated vertices. The intersection \(\bigcap_{F\in A}Q_F\) is \(S^{b(A)-2}\) when \(b(A)\ge2\), and empty when \(b(A)=1\), by Lemma 17 of [1]. Exhaustively checking all \(2^9-1=511\) choices of \(A\) yields precisely \(36\) distinct nonempty intersections: nine \(S^3\), eighteen \(S^1\), and nine \(S^0\). Exactly \(421\) choices of \(A\) have empty intersection. Different subsets giving the same equivalence partition represent the same intersection, not duplicate poset elements.

**2. Determine the proper lower intervals.** Order distinct nonempty intersections by reverse inclusion, equivalently order their equivalence partitions by refinement. A maximal-dimensional \(S^3\) intersection has an empty strict lower interval. For each of the eighteen \(S^1\) intersections, the lower interval consists of exactly two incomparable \(S^3\) elements, so its order complex is \(S^0\). For each of the nine \(S^0\) intersections, the lower interval consists of four \(S^3\) and four \(S^1\) elements, with its comparability graph a single 8-cycle; its order complex is \(S^1\). The statement is verified from the actual vertex partitions in `verify_hypergraph.py` and does not depend on a drawing.

**3. Identify the top interval as a torus.** Add a formal top element for the empty intersection. By the crosscut description of the intersection poset, its strict lower order complex is homotopy equivalent to the abstract nerve \(N\) on the nine edge spheres, with a face indexed by \(A\) precisely when \(b(A)\ge2\). Enumerating this simplicial nerve gives \(f(N)=(9,36,36,9)\). The attached independent, explicit eighteen-pair elementary-collapse sequence produces a two-dimensional simplicial complex with face counts \((9,27,18)\). Every edge belongs to exactly two triangles, each vertex link is a single cycle, and the surface is connected and admits a coherent orientation. Its Euler characteristic is \(9-27+18=0\). By the classification of closed connected surfaces it is a two-torus. As elementary collapses preserve homotopy, \(N\simeq T^2\).

**4. Apply the established wedge decomposition.** Proposition 19 of [1] is a homotopy-level wedge decomposition, not merely a homology formula. With the standard convention for an empty intersection as the formal top element, the top contribution is \(\Delta(P_{<\hat1})\simeq N\simeq T^2\). The nine \(S^3\) intersections contribute nine copies of \(S^3\). Each of the eighteen \(S^1\) intersections contributes \(S^1*S^0\simeq S^2\), and each of the nine \(S^0\) intersections contributes \(S^0*S^1\simeq S^2\). Their wedge is exactly \(T^2\vee\bigvee^{27}S^2\vee\bigvee^9S^3\). The general wedge lemma already verifies null-homotopy of strict inclusion maps because the intersections are nested spheres of strictly decreasing dimensions. This completes the homotopy, rather than only homology, claim.

## Verification
Run `python3 verify_hypergraph.py` with Python 3 and no external modules. It computes each equality partition independently from the displayed nine hyperedges, checks the 36-element intersection poset and all lower-interval incidence types, forms the entire nerve, verifies all eighteen free-face/coface pairs, checks manifold vertex links and two-sided edge incidences, propagates an orientation across every triangle, and uses the resulting Euler characteristic to identify the connected surface as \(T^2\). It terminates with `HYPERGRAPH_COLORING_TORUS_WEDGE_VERIFIED`. No numerical approximation, timeout assertion, or reliance on a prior-run log enters the proof. The derived cohomology ranks \(2,28,9\) agree with the published integral ranks in Example 23 of [1], which is a useful secondary check but not a homotopy proof by itself.

## Relationship to prior work
Breuer, Dall, and Kubitzke [1], Example 23, introduced these exact hyperedges and proved that the coloring complex is connected but not a wedge of spheres; they already computed reduced integral cohomology groups and a nontrivial cup product. Their Proposition 19 supplies the general wedge decomposition used here. Their paper illustrates toroidal geometry but does not enumerate the entire intersection-poset wedge, identify the top interval by an elementary-collapse certificate, or state the full homotopy decomposition with 27 two-spheres and nine three-spheres. Accordingly, the source's example and all its published numerical results are credited, and only the stronger explicitly resolved homotopy type is offered as an additional conclusion.

## Limitations
This is a complete homotopy classification for one finite, historically motivated hypergraph, not a universal classification or a new general wedge lemma. It relies on the correctness of the published Proposition 19, as used under its stated hypotheses, and on the reproducible finite combinatorial certificate. Finding no exact prior homotopy calculation in searched sources does not demonstrate an absence of unindexed equivalent work. No independent mathematical validation has been performed.

## References
[1] Felix Breuer, Aaron Dall, Martina Kubitzke, *Hypergraph Coloring Complexes*, arXiv:1104.0483v3 (public 28 April 2012; Example 23 and Proposition 19), *Discrete Mathematics* 312 (2012), 2407--2420, doi:10.1016/j.disc.2012.04.027. Full open-access text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3587399/ ; version history: https://arxiv.org/abs/1104.0483 .

[2] G. M. Ziegler and R. Živaljević, homotopy theory of arrangements, Wedge Lemma (as cited and specialized in [1], Section 5). Standard crosscut theorem for finite intersection posets and closed-surface classification are used for the nerve identification.
