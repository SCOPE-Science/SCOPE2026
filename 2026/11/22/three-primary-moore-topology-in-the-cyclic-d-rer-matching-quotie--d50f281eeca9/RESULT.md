# Three-primary Moore topology in the cyclic Dürer matching quotient

## Finding
Let \(G=\operatorname{GP}(6,2)\) be the Dürer graph, let \(K=\mathcal M(G)\) be its edge-matching complex, and let \(C_6\) act by simultaneous rotation of its outer and inner six-indexed graph vertices. The ordinary geometric quotient has the **integral homotopy type**
\[
 |K|/C_6\simeq M(\mathbb Z/3\mathbb Z,2)\vee\bigvee^{4}S^3,
\]
where \(M(\mathbb Z/3\mathbb Z,2)\) is the mapping cone of a degree-three self-map of \(S^2\). It is simply connected, its sole nonzero positive-dimensional integral homology groups are \(H_2\cong\mathbb Z/3\mathbb Z\) and \(H_3\cong\mathbb Z^{4}\), and it has no additional reduced homology. The quotient is an ordinary orbit space, not a homotopy orbit space or a vertex-orbit quotient of the original simplicial complex.

## Assumptions and scope
Write \(V(G)=\{u_i,v_i:i\in\mathbb Z/6\mathbb Z\}\) and
\[
 E(G)=\{u_i u_{i+1},\ u_i v_i,\ v_i v_{i+2}:i\in\mathbb Z/6\mathbb Z\}.
\]
All graph edges are undirected and all indices are modulo six. The eighteen edges of \(G\) are the vertices of \(K\); a face of \(K\) is a collection of mutually vertex-disjoint graph edges. The generator \(r\) of \(C_6\) sends \(u_i\) to \(u_{i+1}\) and \(v_i\) to \(v_{i+1}\). All homology statements use integer coefficients. The orbit space is formed on geometric realizations, with all fixed simplices retained. This claim is solely about this specified graph, matching complex and six-element subgroup.

## Proof
**Complete geometric quotient cell model.** The graph has twelve vertices and eighteen edges. Exhaustive matching enumeration gives 1,037 nonempty faces, with the dimension vector \((18,117,334,402,156,10)\). The barycentric subdivision of \(K\) has 166,087 simplices, each an increasing chain of nonempty matchings. The rotation action preserves each vertex rank of such a chain, so no group element reverses or permutes vertices inside a chain. Orbits of these chains therefore give a valid cellular decomposition of \(|K|/C_6\), with 27,703 cells and dimension counts \((180,2205,7550,10448,6120,1200)\). A cell's oriented boundary is the alternating sum of its chain-deletion faces, taking orbits after deletion. Even if two cells of the same dimension have the same orbit vertices, they are kept as distinct cell orbits; no invalid vertex-orbit identification is used.

**Exact geometric collapses and integral chains.** `certificate.json` lists 12,488 elementary free-face pairs in the quotient subdivision. `verify_cyclic_quotient.py` regenerates every orbit and checks, at the instant of each deletion, that the listed face has exactly one currently present codimension-one coface, with one attaching incidence. The remaining regular CW subcomplex has dimensions \((94,673,1268,692)\), with nothing above dimension three. Its cellular boundary operators square to zero over the integers. The certificate then supplies 1,360 signed integral unit-pivot chain cancellations, each rechecked against the current exact boundary matrices. The remaining cellular chain complex has one zero-cell, one two-cell and five three-cells. Exactly one three-cell has boundary three times the two-cell; the other four boundaries vanish. Consequently
\[
H_0\cong\mathbb Z,\qquad H_2\cong\mathbb Z/3\mathbb Z,\qquad H_3\cong\mathbb Z^4,
\]
and all other positive-degree homology vanishes. These last unit-pivot operations establish chain homotopy, not simplicial collapsibility; they are not misrepresented as geometric collapses.

**Fundamental group.** The independent, geometrically collapsed two-skeleton has 94 vertices, 673 edges and 1,268 two-cells. The certificate gives a spanning tree of 93 edges, with 580 complementary edge generators. Each two-cell is an oriented triangle in the barycentric orbit complex, and its attaching word is the product of its three oriented edge loops after contracting the spanning tree. A checked sequence of 580 one-occurrence Tietze eliminations leaves the empty set of generators and only empty relators. Thus \(\pi_1(|K|/C_6)=1\). The fundamental-group proof does not rely on the homological cancellations.

**Homotopy-type upgrade.** The quotient is a simply connected three-dimensional CW space. By Hurewicz, its second homotopy group is the cyclic group of order three. A generator gives an \(S^2\)-map whose triple is nullhomotopic, hence extends over the degree-three Moore space. The Whitehead exact sequence for simply connected three-complexes gives a surjection \(\pi_3\twoheadrightarrow H_3\cong\mathbb Z^4\); choose four sphere maps representing an integral homology basis. Their wedge with the Moore-space map is a homology equivalence between simply connected CW complexes, and hence a homotopy equivalence by Whitehead's theorem. This proves the asserted wedge decomposition.

## Verification
The two standalone files `verify_cyclic_quotient.py` and `certificate.json` are included here. From their directory, run:

```bash
python3 verify_cyclic_quotient.py certificate.json
```

Python 3 with standard library is sufficient. The verifier reconstructs all graph edges, all six rotations, all 1,037 matchings, all 166,087 flags, the exact quotient cells and boundaries, 12,488 geometric collapses, 1,360 integral unit pivots, the quotient two-skeleton and 580 group-presentation eliminations. Its success marker is `DURER_CYCLIC_MATCHING_QUOTIENT_MOORE_THREE_TORSION_OK`. The certificate is finite and exhaustive for this fixed graph. No claim about an infinite parameter family is inferred from it.

## Relationship to prior work
Shareshian and Wachs analyze integral torsion in matching complexes of complete and complete bipartite graphs, not the ordinary sixfold orbit space of this specific graph. Ehrenborg and Hetyei develop independence-complex collapses; applying their terminology to the line graph gives the matching-complex viewpoint but not this quotient classification. The exact Dürer matching-complex calculation listed in the references determines the **unquotiented** wedge of twenty-two three-spheres and the rational character of its full dihedral symmetry. That character predicts four invariant rational third-homology classes under rotations, but neither detects the three-torsion in second homology nor proves simple connectivity. The published eight-vertex octahedral-carrier classification concerns integral cycles in the covering complex, not this orbit-space Moore summand. Outerplanar matching-complex wedge theorems do not apply because the Dürer graph is three-regular and three-connected, hence not outerplanar.

## Limitations
The conclusion is an ordinary homotopy equivalence, not a claimed PL homeomorphism or simple-homotopy collapse onto a Moore wedge. It is restricted to one finite graph and one sixfold subgroup. Computation certificates establish exact finite statements but not general results for other generalized Petersen graphs. Originality comparisons cover identified indexed and accessible publications; unindexed equivalent work remains possible. Independent mathematical audit has not been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first public arXiv posting 2004-09-03, https://arxiv.org/abs/math/0409054.
2. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, available online 2005-11-28, https://www.ms.uky.edu/~jrge/papers/independence.pdf.
3. *The Dürer matching complex: an integral sphere wedge and its full dihedral character*, published exact-object study, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-d-rer-matching-complex-an-integral-sphere-wedge-and-its-full--29af2a0878b2.
4. *Shortest octahedral carriers and integral orbit obstructions in the Dürer matching complex*, published exact-object study, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-shortest-octahedral-carriers-and-integral-orbit-obstructions-in--2058dcbfce11.
5. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, first posted 2024-11-07, https://arxiv.org/abs/2411.04601.
