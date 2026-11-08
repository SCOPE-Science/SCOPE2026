# Second-independence homotopy distinguishes the Shrikhande and rook graphs

## Finding
Let \(S\) denote the Shrikhande graph and \(R\) the four-by-four rook graph. For the higher independence complex \(\operatorname{Ind}_2(G)\), in which every induced connected component has at most two vertices, the exact integral homotopy types are
\[
\operatorname{Ind}_2(S)\simeq\bigvee^{57}S^3,
\qquad
\operatorname{Ind}_2(R)\simeq\bigvee^{105}S^3.
\]
The pair has the same strongly regular parameters \((16,6,2,2)\), but its nonflag second-independence homotopy invariants differ.

## Assumptions and scope
Take finite, simple, undirected graphs with vertex set \(\{0,\ldots,15\}\), writing \(v(i,j)=4i+j\) for \(0\le i,j<4\). Vertices \((i,j)\) and \((k,l)\) are adjacent in \(S\) if their difference in \((\mathbb Z/4\mathbb Z)^2\) is in
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\};
\]
they are adjacent in \(R\) exactly when \(i=k\) or \(j=l\), and distinct. For either graph \(G\), a face of \(\operatorname{Ind}_2(G)\) is a vertex subset \(A\) such that \(\max_{v\in A}\deg_{G[A]}(v)\le1\) (with the empty face included). This degree condition is equivalent to all components having one or two vertices, and to forbidding every three-vertex path as a not-necessarily-induced subgraph. The theorem concerns the ordinary non-equivariant homotopy type of the geometric realization, over the integers, not a statement of simplicial homeomorphism.

## Proof
**Graph structure.** Both edge rules are undirected and loop-free. Exhaustive adjacency checks give sixteen vertices, degree six at each vertex, and two common neighbors for every pair of distinct vertices. The open neighborhood of a Shrikhande vertex induces a six-cycle, whereas a rook-graph neighborhood induces two disjoint triangles. Thus these are distinct graphs with identical strongly regular parameters \((16,6,2,2)\).

**All faces.** Represent a subset by a sixteen-bit integer \(m\) in the full range \(0\le m<2^{16}\). A set is a face precisely when it contains no triple comprising a vertex and two of its neighbors. The independent direct criterion is that each selected vertex has at most one selected neighbor. Both tests agree on every mask. The nonempty face vectors, in dimensions zero upward, are
\[
 f(S)=(16,120,384,544,240,32),\qquad
 f(R)=(16,120,384,528,144),
\]
with respectively \(1336\) and \(1192\) nonempty simplices.

**Acyclic matchings.** On the face set with the empty face adjoined, start with all faces unmatched. Visit pivots in order \(0,1,\ldots,15\) for \(S\); for \(R\) use \(v_j=5j\pmod {16}\), \(0\le j<16\). At each pivot \(v\), traverse all bit masks in increasing order and pair every still-unmatched face \(m\) without \(v\) with the still-unmatched face \(m\cup\{v\}\), when both are faces. The resulting unique pair involving the empty face is \((\varnothing,\{0\})\). Discard just this pair, leaving \(\{0\}\) as an ordinary critical zero-cell. These are deterministic coverings and disjoint pairs.

For \(S\) the ordinary nonempty-face matching has \(638\) pairs, one critical zero-cell, one critical two-cell (bit mask \(82\)), and \(58\) critical three-cells. For \(R\) it has \(543\) pairs, one critical zero-cell and \(105\) critical three-cells. The directed Hasse graph orients every codimension-one covering downward, reversing each matched incidence. The verifier constructs every one of the \(4960\) (respectively \(4224\)) nonempty-face coverings and removes all \(1336\) (respectively \(1192\)) vertices in a topological sort. Thus no directed cycle exists and these are genuine acyclic discrete-Morse matchings.

**Signed integral attaching map.** For \(R\), the resulting Morse CW complex has only a point and \(105\) three-cells, all trivially attached. This gives the claimed wedge. For \(S\), its CW model has one point, one two-cell and \(58\) three-cells. The attaching map of a three-cell to the two-sphere is classified by its integral degree. Fix the natural increasing-vertex orientations. For a matched lower face \(\sigma\) and its upper partner \(\tau\), solve the integral boundary relation \(\partial\tau=0\) for \(\sigma\) and recursively eliminate gradient-matched faces. Every incidence coefficient is \(\pm1\). The directed acyclicity guarantees termination, so this is exactly the signed integer Morse boundary. The sole critical two-cell has mask \(82\); the coefficient from the critical three-cell with mask \(340\) is \(+1\). In fact the complete one-row boundary has fifteen nonzero entries: five \(+1\) and ten \(-1\), and all others zero. Its entries therefore have gcd one. An integral change of basis among the \(58\) three-cells transforms the attaching degrees to \((1,0,\ldots,0)\). Attaching one three-cell by a degree-one map to a two-sphere makes a contractible subcomplex, so the remaining \(57\) three-cells yield \(\bigvee^{57}S^3\). No torsion or higher attaching ambiguity remains.

## Verification
Run `python3 verify_shrikhande_rook_ind2.py` with Python 3 standard library. It independently tests the degree condition against all forbidden triples for each of the \(2^{16}\) masks, constructs both complete matchings, verifies all face-poset covering relations and directed acyclicity, and recomputes the signed integer Morse boundary from gradient substitutions. The final marker is `INTEGRAL_MORSE_CERTIFICATE_PASS`.

A second standalone implementation, `python3 verify_homology_shrikhande_rook_ind2.py`, generates the graphs and admissible faces independently, builds each mod-two simplicial boundary matrix, and reduces it over \(\mathbf F_2\). For \(S\), boundary ranks are \((15,105,279,208,32)\) and Betti numbers are \((1,0,0,57,0,0)\); for \(R\), boundary ranks are \((15,105,279,144)\) and Betti numbers are \((1,0,0,105,0)\). This is an independent finite-field check, not a replacement for the integral Morse proof. Exact recorded console outputs accompany both programs.

## Relationship to prior work
Taylan (2015, arXiv:1501.06754) develops matching-tree calculations for forbidden-path devoid complexes; the inspected specific homotopy results cover paths, cycles, and forests, not these strongly regular graphs. Deshpande and Singh (2020, arXiv:2001.05448) treat complete multipartite graphs, fully whiskered graphs, paths, cycles and rooted trees. Their results do not subsume either of these graphs. Deshpande, Shukla and Singh (2020, arXiv:2001.06775) give connectivity constraints and a chordal-graph wedge theorem rather than multiplicities for the two present nonchordal graphs.

Previously recorded results distinguishing \(S\) and \(R\) via their **ordinary independence complexes** (respectively \(23\) versus \(15\) two-spheres) and **closed-neighborhood Čech complexes** (respectively \(23\) versus \(63\) two-spheres) do not imply the second-independence homotopy types: their simplices have different defining conditions. The ordinary open Lovász neighborhood complexes of these graphs have also been calculated, but are yet another construction. The numerical distinction here does not assert that these graphs were previously indistinguishable by all topological invariants.

## Limitations
This is an exact finite classification for two particular sixteen-vertex graphs; it does not give a formula for larger Hamming, Doob, or general strongly regular graphs. The existence of all relevant adjacent constructions was checked, but equivalently formulated unindexed work remains possible. The full homotopy statement uses a reproducible finite discrete-Morse argument with an integral unit coefficient, not homology alone. An independent mathematical audit has not been performed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first public 2015-01-27, https://arxiv.org/abs/1501.06754.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first public 2020-01-15, https://arxiv.org/abs/2001.05448.
3. P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775v1, first public 2020-01-19, https://arxiv.org/abs/2001.06775.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. Prior full-text result: *Independence complexes of the Shrikhande and 4-by-4 rook graphs have different sphere-wedge homotopy types*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
6. Prior full-text result: *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-two-ech-homotopy-distinguishes-the-shrikhande-and-rook-gra--5b6e4436155e.
