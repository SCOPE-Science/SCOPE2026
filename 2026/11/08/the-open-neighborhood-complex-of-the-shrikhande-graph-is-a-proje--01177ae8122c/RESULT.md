# The open neighborhood complex of the Shrikhande graph is a projective plane with fifty-five sphere summands

## Finding
Let \(S\) be the Shrikhande graph on \((\mathbb Z/4\mathbb Z)^2\). Let \(\mathcal N(S)\) denote the **open** Lovász neighborhood complex: its simplices are precisely the vertex subsets that have a common adjacent vertex, where no vertex is adjacent to itself. Then the complete integral homotopy type is
\[
\boxed{\mathcal N(S)\simeq\mathbb {RP}^{2}\vee\bigvee^{55}S^{2}.}
\]
In particular, \(\pi_1(\mathcal N(S))\cong\mathbb Z/2\mathbb Z\) and
\[
\widetilde H_i(\mathcal N(S);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&i=1,\\
\mathbb Z^{55},&i=2,\\
0,&\text{otherwise}.
\end{cases}
\]
The nontrivial integral two-torsion distinguishes this complex from a wedge of spheres and from the **closed** neighborhood complex of the same graph.

## Assumptions and scope
Write the vertices as pairs \((a,b)\in(\mathbb Z/4\mathbb Z)^2\), numbered \(4a+b\) using representatives \(0,1,2,3\). Two distinct vertices are adjacent if and only if their difference belongs to
\[
D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
The graph is six-regular on sixteen vertices and has forty-eight edges. Any two distinct vertices have exactly two common neighbors. Its open-neighborhood complex is the union of the sixteen closed simplices on the six-element sets \(N(v)\), NOT the simplices on \(\{v\}\cup N(v)\). For each nonempty vertex set \(\sigma\), the face condition is \(\sigma\subseteq N(v)\) for at least one vertex \(v\). The empty face is included in the abstract complex. The claim concerns ordinary nonequivariant integral homotopy, not graph embeddings or closed neighborhoods.

## Proof
**1. Exhaustive, independently checked face description.** The stated differences give sixteen bit-mask neighborhoods of size six. Enumerating all their subsets yields exactly 809 faces including the empty face, with face counts in dimensions zero through five
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,320,240,96,16).
\]
An independently coded scan of all \(2^{16}=65,536\) vertex subsets using the common-neighbor predicate gives precisely the same face set. The complete one-skeleton follows also from the exact two-common-neighbor property. The Euler characteristic is 56.

**2. Explicit elementary collapse to dimension two.** Represent a face by its sixteen-bit mask. In a remaining finite simplicial complex, choose a nonempty face \(\tau\) with precisely one immediate coface \(\sigma\) of dimension one higher; remove \(\tau\) and \(\sigma\). Choose among all such pairs by decreasing cardinality of \(\tau\), then by increasing integer mask. Recompute immediate cofaces after every removal. This deterministic procedure makes exactly 256 elementary collapses. Its remaining complex has face counts \((16,120,160)\) in dimensions zero, one and two and no higher faces. An independently selected reverse-mask tie-breaking rule makes 256 collapses to another such two-complex. Every removed pair is checked as a genuine free-face pair, and downward closure is checked at termination, so both procedures are integral homotopy equivalences.

**3. A complete cellular presentation with unimodular cancellations.** The resulting two-complex contains the complete graph on sixteen vertices. Collapse its fifteen-edge star spanning tree \(\{\{0,i\}:1\le i\le15\}\) to the base point. The quotient is homotopy equivalent to the original, with 105 oriented loop generators (the nontree edges) and 160 two-cells. For each triangular face, form its oriented boundary word, omit tree edges, freely and cyclically reduce. This is a cellular attaching-word presentation, not merely a presentation of the abstract fundamental group.

Repeatedly choose a two-cell whose attaching word contains some loop generator exactly once (allowing inverse orientation), solve that relator for the generator, substitute this word in all other attaching maps, and cancel the corresponding loop/two-cell pair. Cyclic conjugation and free reduction are attaching-map homotopies; the substitution is a cellular change of basis followed by an elementary homotopy cancellation, hence preserves the full homotopy type. The precise deterministic tie-breaking and substitutions are specified and executed in `verify_shrikhande.py`.

In the forward reduction exactly **104** such cancellations are possible. The resulting one-vertex complex contains one circle generator \(g\) and 56 two-cells: 35 have constant attaching words and 21 attach by \(g^{2}\) or \(g^{-2}\). The opposite-order collapse independently allows 104 cancellations, resulting in 39 constant attachments and 17 attachments of degree \(\pm2\). Neither path assumes a homology calculation to establish the attaching degrees.

**4. Identify the homotopy type.** Reverse orientations of the negatively attached two-cells. Keep one two-cell of degree two. For each other degree-two two-cell, perform a cellular two-cell slide subtracting the first attaching map; its attaching map becomes nullhomotopic in the circle (its winding number becomes zero). Thus the circle with the retained degree-two disk is the standard CW model of \(\mathbb {RP}^{2}\), while the remaining 55 disks attach trivially and contribute fifty-five two-spheres. In the reverse reduction, the same count is \(39+16=55\). This proves the claimed **homotopy equivalence**, rather than inferring it from equal field homology ranks.

## Verification
Run `python3 verify_shrikhande.py` with standard Python 3. The verifier checks the graph and the strong-regularity common-neighbor property by separate coordinate and bit-mask constructions, enumerates all 65,536 subsets by two independent criteria, recomputes both complete elementary-collapse sequences, verifies all free-face and closure requirements, forms full integer attaching words, performs all 104 cellular eliminations for each reduction, and checks the surviving relators literally. Independent simplicial boundary elimination on both resulting two-complexes over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) gives ranks \(104,105,105\) for the degree-two boundary; these are checks, not substitutes for the homotopy proof. See `verification_output.txt` for the exact recorded execution output. No external datasets or mathematical packages are needed.

## Relationship to prior work
Shukla [1] gives homotopy classifications of open neighborhood complexes for graphs of maximum degree at most three and for four-regular circulant graphs. The Shrikhande graph has degree six, so its theorem hypotheses do not cover it; its complete open-neighborhood homotopy type is not stated in the inspected paper. Lovász's original neighborhood construction and the standard equivalence with graph Hom complexes explain the significance of this invariant [1,2], but do not provide this calculation.

A previously reported computation [3] determines the **closed** neighborhood (intrinsic scale-two graph Čech) complex of the Shrikhande graph as a wedge of 23 two-spheres; closed neighborhoods include their center and have a different face condition. The Shrikhande independence-complex calculation [4] concerns independent vertex sets, likewise a distinct complex. A rook-graph result [5] determines high-degree homology and a relative cofiber for the open neighborhood complex of complete Cartesian products, but does not treat the non-rook Shrikhande graph or imply its first integral homology. A general graph-like-neighborhood theorem [6] assumes pairwise edge-disjoint four-cycles. Here an exact enumeration finds sixty four-cycles, with each graph edge in five, so its hypothesis does not apply. These are different assertions even when graph parameters agree; in particular, no one of them implies the present two-torsion or full homotopy type.

## Limitations
This is a finite graph-specific theorem, not a classification of all strongly regular graphs or an equivariant homotopy theorem. The proof is an exact finite constructive homotopy reduction; the accompanying executable is required to independently reproduce the exhaustive cancellation certificates. No claim is made about general neighborhood-complex torsion. Published and indexed searches cannot rule out an equivalent result in unindexed literature. Independent external review has not yet been performed.

## References
1. Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first publicly submitted 2018-02-13. https://arxiv.org/html/1802.04526v2.
2. Takahiro Matsushita, *Fundamental Groups of Neighborhood Complexes*, arXiv:1210.2803, first publicly submitted 2012-10-10. https://arxiv.org/abs/1210.2803.
3. *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, public research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-scale-two-ech-homotopy-distinguishes-the-shrikhande-and-rook-gra--5b6e4436155e/RESULT.md.
4. *Independence complexes of the Shrikhande and four-by-four rook graph have different sphere-wedge homotopy types*, public research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187/RESULT.md.
5. *Row–column boundary spheres control higher neighborhood homology of rook graphs*, public research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45/RESULT.md.
6. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d.
