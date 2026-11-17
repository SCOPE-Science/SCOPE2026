# The Heawood induced-forest complex is a wedge of eight \(8\)-spheres

## Finding
Let \(H\) be the Heawood graph, realized as the point–line incidence graph of the Fano plane. Its **vertex-induced forest complex** is
\[
\mathcal F(H)=\{S\subseteq V(H): H[S]\text{ is a forest}\}.
\]
Then the integral homotopy type is
\[
\boxed{\mathcal F(H)\simeq\bigvee^{8} S^{8}.}
\]
In particular, the only nonzero reduced integral homology is \(\widetilde H_8\cong\mathbb Z^8\). The complex is nonpure: it has \(168\) facets of dimension \(8\) and \(70\) facets of dimension \(9\). The latter confirms that its maximum induced forest contains ten vertices.

## Assumptions and scope
Vertices \(0,\dots,6\) are the seven points in \(\mathbb Z/7\mathbb Z\). Vertex \(7+t\), \(0\le t\le6\), represents the line
\[L_t=\{t,t+1,t+3\}\pmod7.\]
An edge \(\{p,7+t\}\) exists precisely when \(p\in L_t\). There are \(14\) vertices and \(21\) edges. Every pair of distinct points belongs to exactly one of these seven three-point lines, so this is the Fano Levi graph (Heawood graph). A simplicial face is a vertex subset inducing an acyclic graph; the empty subset is included in the complex but is not a vertex of the face poset used in the matching.

## Proof
Represent each nonempty subset by an integer mask from \(1\) through \(2^{14}-1\), with bit \(v\) indicating whether vertex \(v\) is included. Enumerate all masks and retain exactly those for which adding the induced edges never closes a cycle (disjoint-set forest test). A logically separate test verifies the equality \(|E(H[S])|=|S|-c(H[S])\), where \(c\) counts components by flood fill; the two tests agree for all \(2^{14}\) masks.

There are exactly \(12,791\) nonempty faces. Their dimension-count vector in degrees \(0\) through \(9\) is
\[(14,91,364,1001,2002,2975,3208,2254,812,70).\]

Construct the following finite partial matching on the nonempty face poset. Start with every nonempty face unmatched. For \(v=0,1,\ldots,13\), pair **each** currently unmatched face \(S\) avoiding \(v\) with \(S\cup\{v\}\), provided the latter is also currently unmatched. Remove both from subsequent stages. At each stage these pairs are disjoint because their upper member contains \(v\) and their lower member does not. The numbers of pairs at successive stages are
\[(5831,280,128,66,37,22,22,0,0,2,3,0,0,0).\]
Thus \(6391\) pairs exhaust all but nine nonempty faces. The unmatched masks are exactly
\[(1,15288,15308,15336,15796,15844,16268,16280,16328).\]
The first is one critical vertex; each of the other eight masks has nine set bits, hence is an eight-dimensional critical simplex.

For the acyclicity test, form every covering edge \(T\supset S\) where \(|T|=|S|+1\) in the nonempty face poset. Orient matched edges from lower face to upper face and all other coverings from upper face to lower face. All \(81,634\) directed coverings are generated. Kahn's topological-sort algorithm removes all \(12,791\) face vertices, so the matching has no closed gradient path. This completes a finite exhaustive proof that it is an acyclic discrete-Morse matching.

By Forman's discrete-Morse theorem, the geometric realization has the homotopy type of a CW complex containing exactly one zero-cell and eight eight-cells, with no cells in any intermediate dimension. Since every eight-cell attaches to the one-point seven-skeleton by a constant map, this CW complex is a wedge of eight eight-spheres. This proves the stated **integral homotopy equivalence**, not just an equality of Betti numbers.

## Verification
Run `python3 verify_heawood_forest.py` using Python \(3.9\) or newer; no third-party library is needed. The provided output file records the exact results. A separate mod-two simplicial boundary reduction has ranks
\[(13,78,286,715,1287,1688,1520,734,70)\]
in boundary degrees \(1\) through \(9\), yielding only \(\widetilde\beta_8=8\). This independently checks face enumeration and homology but is not used to infer the integral homotopy type. The Euler characteristic is \(9\), consistent with \(\bigvee^8S^8\). The complete Hasse-edge acyclicity check and critical-cell count are the homotopy certificate.

## Relationship to prior work
Taylan's 2015 public preprint develops the general devoid-complex framework and matching-tree techniques; the forest complex is expressible as a devoid complex forbidding all cycles, but its explicit calculations there concern path/cycle families and forests as underlying graphs, not this incidence graph. Carnero Bravo's forest-filtration paper defines the vertex-induced acyclic complex in the same sense and classifies paths, cycles, cactus graphs, joins, certain multipartite graphs and graph products; the Heawood graph is not among the classified cases. The subsequent polyhedral-join paper concerns selected lexicographic graph products and does not give this Heawood classification. Other indexed calculations for the Heawood graph study ordinary independence, matching, cut, neighborhood, Čech or Vietoris–Rips complexes with different face conditions. Their numerical coincidences do not imply the present forest-complex homotopy theorem.

## Limitations
The theorem applies to the specific fourteen-vertex Fano incidence graph. It does not establish homotopy types for incidence graphs of arbitrary finite projective planes, equivariant homotopy representations, or canonical sphere-basis classes. The computation is exhaustive and independently checkable, but independent mathematical review and definitive publication-priority assessment have not been performed. No exhaustive claim about all unpublished or unindexed literature is made.

## References
1. Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1 (first publicly submitted 2015-01-27), https://arxiv.org/abs/1501.06754.
2. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first submitted 2023-07-25), https://arxiv.org/abs/2307.13271.
3. Andrés Carnero Bravo, *Polyhedral Joins and Graph Complexes*, arXiv:2307.14321, https://arxiv.org/abs/2307.14321.
4. Wolfram MathWorld, *Heawood Graph*, https://mathworld.wolfram.com/HeawoodGraph.html.
