# Exact Euclidean degree-zero persistence of partial permutohedron vertices

## Finding

For positive integers \(m,n\), let \(\mathcal P(m,n)\subset\mathbb R^m\) be the partial permutohedron, the convex hull of vectors with entries in \(\{0,1,\ldots,n\}\) and pairwise distinct nonzero entries. Equip its **vertex set** \(V_{m,n}\) with the inherited Euclidean distance, and form the inclusive Vietoris–Rips filtration (an edge is present when its length is at most \(r\)). Put \(p=\min(m,n)\), \(F_k=m!/(m-k)!\) and \(B_k=\binom mk\), for \(0\le k\le p\). Empty sums equal zero.

**Theorem (complete degree-zero barcode).** All zero-dimensional homology classes are born at scale zero; one survives forever. The death lengths of the other \(\sum_{k=0}^p F_k-1\) classes, counted with multiplicity, are exactly:

**(i) \(n\ge m+1\):** \(\sqrt2\) occurs \(\sum_{k=1}^m(F_k-B_k)\) times, and for each \(k=0,\ldots,m-1\), the integer \(n-k\) occurs \(B_k\) times. No other deaths occur.

**(ii) \(1\le n\le m\):** \(1\) occurs \(F_n\) times, \(\sqrt2\) occurs
\[
F_{n-1}-1+\sum_{k=1}^{n-2}(F_k-B_k)
\]
times, and for each \(k=0,\ldots,n-2\), the integer \(n-k\) occurs \(B_k\) times. No other deaths occur.

Equivalently, **every** Euclidean minimum spanning tree on \(V_{m,n}\) has this same multiset of edge lengths. In particular, the exact total Euclidean MST weight is the sum of the listed lengths times their multiplicities, and the smallest radius at which the full vertex cloud becomes connected is exactly \(n\).

For instance, with \((m,n)=(3,4)\) the complete Euclidean graph on 16 vertices has MST edge-length multiplicities \(8\) at \(\sqrt2\), \(3\) at \(2\), \(3\) at \(3\), and \(1\) at \(4\).

## Assumptions and scope

The Euclidean metric is the ordinary ambient \(\ell_2\) distance, not the graph metric of the polytope skeleton. Only **extreme points** of \(\mathcal P(m,n)\) are sampled, not all integer points or all vectors admitted in the initial convex-hull definition. The theorem holds for every \(m,n\ge1\); this includes the simplex case \(n=1\) and the interval case \(m=1\). Its assertion concerns degree-zero Vietoris–Rips persistence, not higher-dimensional persistent homology. Multiplicities in a barcode use half-open finite intervals \([0,r)\).

A rank-\(k\) vertex has precisely the \(k\) positive values \(n,n-1,\ldots,n-k+1\), assigned injectively to \(k\) of the \(m\) positions; there are \(F_k\) such vertices and \(B_k\) possible supports. This previously established vertex characterization is recalled from the cited papers.

## Proof

**1. Exact pairwise separation.** Let \(x\) have rank \(k\) and \(y\) have rank \(\ell>k\). Sorting the coordinates of both points in decreasing order minimizes the squared Euclidean distance among all assignments of their fixed coordinate multisets, by the rearrangement inequality. The canonical sorted vectors agree in the first \(k\) positions, so
\[
\|x-y\|^2\ge\sum_{i=k+1}^{\ell}(n-i+1)^2\ge(n-k)^2.
\]
If two distinct rank-\(k\) vertices have different supports, at least one coordinate belongs exclusively to each support, and each nonzero coordinate has magnitude at least \(n-k+1\). Hence
\[
\|x-y\|^2\ge2(n-k+1)^2.
\]
These bounds apply to **every pair** of vertices, not just polytope edges. Within a fixed rank and support, permutations of successive values give pairwise distances \(\sqrt2\), and these adjacent transpositions connect all \(k!\) orderings. They are the only distance-\(\sqrt2\) links needed below.

**2. Initial events.** Because coordinates are integers, the minimum positive distance is at least \(1\). A pair of distinct vertices at distance \(1\) must differ in exactly one coordinate by one. A fixed rank has a fixed coordinate sum, so this cannot happen within one rank. By the first bound, it can occur only between rank \(n-1\) and rank \(n\), when \(n\le m\); the only such pairs are obtained by deleting the smallest nonzero label \(1\). Every rank-\(n\) vertex has a unique predecessor, giving \(F_n\) mergers at scale \(1\), with no cycles. If \(n\ge m+1\), there are no distance-one pairs.

If \(n\ge m+1\), then just below \(\sqrt2\) every vertex is isolated; at \(\sqrt2\), the rank-\(k\) vertices with each given support become connected by successive-value swaps. As ranks are not linked at these scales, the number of mergers is exactly \(\sum_{k=1}^{m}(F_k-B_k)\), leaving \(\sum_{k=0}^{m}B_k=2^m\) components.

If \(n\le m\), the rank-\(n\) and rank-\((n-1)\) vertices are joined at scale \(1\). At \(\sqrt2\), all these vertices form a *single* component: adjacent swaps of consecutive positive labels, together with swaps of label \(1\) and a zero, connect every rank-\(n\) vertex (the zero labels are indistinguishable). Every rank-\((n-1)\) vertex extends to at least one rank-\(n\) vertex by adjoining label \(1\). The lower rank-\(k\) vertices, \(k\le n-2\), form one component per fixed support, each connected by adjacent positive-label swaps. The component count after \(\sqrt2\) is therefore \(1+\sum_{k=0}^{n-2}B_k\). Subtracting it from the count \(\sum_{k=0}^{n-1}F_k\) after scale \(1\) yields exactly \(F_{n-1}-1+\sum_{k=1}^{n-2}(F_k-B_k)\) mergers. For \(n=1\), the formula gives zero and the rank-one vertices already form a single component with the origin at scale \(1\).

**3. Integer merger stages.** In case (i), after scale \(\sqrt2\), the entire top rank \(m\) is connected (all permutations have full support). In case (ii), the top two ranks are already jointly connected. Proceed by downward induction on \(k\), beginning at \(k=m-1\) in case (i), or \(k=n-2\) in case (ii). Just before scale \(j=n-k\), all ranks greater than \(k\) form one connected core, while the rank-\(k\) vertices form precisely \(B_k\) components indexed by their supports. Indeed, different supports cannot meet below \(j\) by the same-rank bound; rank-\(k\) vertices cannot reach a higher rank below \(j\) by the different-rank bound; and they cannot reach a lower rank below \(j\), since the minimal such distance is at least \(n-k+1>j\). These statements also rule out shortcut paths using nonedges of the polytope.

At scale \(j\), each rank-\(k\) support class is joined to the core: add the value \(n-k=j\) in any currently zero coordinate to a rank-\(k\) vertex. The resulting rank-\((k+1)\) vertex lies exactly distance \(j\) away. Thus precisely \(B_k\) components merge into the core. Repeating down to rank zero establishes the integer multiplicities and exhausts all components.

**4. Persistence and MST equivalence.** Kruskal's algorithm on the complete Euclidean graph merges exactly one pair of components per selected edge. The previous component counts establish the length multiplicities of **every** MST, even when several pairs tie. The degree-zero Vietoris–Rips barcode has identical death multiplicities. The final merger attaches the origin at distance \(n\), and the formulas sum to \(\sum_{k=0}^pF_k-1\), as required.

## Verification

`python3 check_mst.py` independently enumerates the explicit vertices, computes every pairwise squared Euclidean distance using integers, performs Kruskal's algorithm on the *complete* graph, and compares the exact squared-length histogram with the all-parameter formulas. Its recorded run passed 55 parameter profiles, 59,105 exact pair comparisons, and 1,429 cumulatively counted vertices. Examples include the cases \((m,n)=(3,4),(4,2),(4,5),(5,3)\), which cross the branch boundary. Finite checks corroborate, but do not replace, the proof for all positive integers.

## Relationship to prior work

Heuer–Striker characterize partial permutohedron vertices and face lattices; Behrend and collaborators subsequently establish a full face-lattice description and give explicit skeleton edges (notably Proposition 5.7 and Corollary 5.8). The present result concerns the **complete Euclidean metric** on these vertices and the resulting global merge hierarchy. In particular, knowing the convex-polytope edge relation alone does not exclude a shorter nonedge shortcut or determine the all-pairs Vietoris–Rips connectivity thresholds without the pairwise separation argument above.

Cardinal–Steiner study a different invariant: shortest numbers of steps along the one-skeleton between prescribed vertices of general polymatroids. That graph-path optimization does not determine Euclidean minimum spanning trees of the vertex cloud. The previously studied four-permutation Vietoris–Rips filtration uses an adjacent-swap graph distance rather than this Euclidean metric or this infinite two-parameter family. No historical-priority guarantee is claimed.

## Limitations

Only degree-zero persistence and MST length multiplicities are determined. Higher homology, the number of distinct minimum spanning trees, and algorithmic complexity for arbitrary encodings are not evaluated. The assertion is about the standard integer coordinate realization; arbitrary affine deformations need not preserve the lengths. An equivalent formula might exist in work indexed under a different combinatorial terminology; independent historical and mathematical review has not been performed.

## References

1. D. Heuer and J. Striker, *Partial permutation and alternating sign matrix polytopes*, arXiv:2012.09901, first submitted 17 December 2020, especially Section 5. https://arxiv.org/abs/2012.09901
2. R. E. Behrend, F. Castillo, A. Chavez, A. Diaz-Lopez, L. Escobar, P. E. Harris and E. Insko, *Partial Permutohedra*, arXiv:2207.14253, first submitted 28 July 2022, especially Sections 3 and 5, Proposition 5.7 and Corollary 5.8. https://arxiv.org/abs/2207.14253
3. J. Cardinal and R. Steiner, *Shortest Paths on Polymatroids and Hypergraphic Polytopes*, arXiv:2311.00779, first submitted 1 November 2023, Sections 1–2. https://arxiv.org/abs/2311.00779
