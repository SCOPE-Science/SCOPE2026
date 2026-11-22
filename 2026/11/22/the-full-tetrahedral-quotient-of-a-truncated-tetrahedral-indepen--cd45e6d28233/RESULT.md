# The full tetrahedral quotient of a truncated-tetrahedral independence complex is a two-sphere

## Finding
Let \(T\) be the twelve-vertex graph of the ordinary truncated tetrahedron and let \(K=\operatorname{Ind}(T)\) be its independence complex. Its full graph-automorphism group \(S_4\) permutes the four original tetrahedron labels. For the **ordinary geometric orbit space**, rather than the homotopy/Borel quotient, there is an integral homotopy equivalence
\[
\boxed{|K|/S_4\simeq S^2.}
\]
In particular, the quotient is simply connected, has \(H_2\cong\mathbb Z\), and has no other positive-degree integral homology. The claim is for this one natural graph and its full symmetry group.

## Assumptions and scope
Fix \(L=\{0,1,2,3\}\). The vertices of \(T\) are the ordered pairs \((a,b)\) with \(a,b\in L\) and \(a\ne b\). Distinct pairs \((a,b)\) and \((c,d)\) are adjacent exactly if \(a=c\), or if \((c,d)=(b,a)\). Thus there are twelve vertices and eighteen graph edges, comprising four triangular triples and six reversed-pair edges. Independent sets may be empty; nonempty independent sets are simplices of \(K\). The action is \(\pi(a,b)=(\pi(a),\pi(b))\) for \(\pi\in S_4\).

The four triangular triples are exactly the graph's three-cliques. Any graph automorphism permutes these four recognizable triples. Each vertex in one triple has a unique reversed-pair neighbor in one particular other triple, so an automorphism is determined by the permutation of triples. Conversely every permutation of the four labels is an automorphism; therefore the full automorphism group is precisely \(S_4\).

Equivalently, \(K\) is the matching complex of the graph obtained by subdividing every edge of the complete tetrahedral graph \(K_4\) exactly once. It is **not** the ordinary matching complex of \(T\), which has eighteen simplicial vertices.

## Proof
**1. A regular orbit-cell structure.** Index the twelve ordered pairs lexicographically. Direct checking of all independent subsets gives exactly \(162\) nonempty simplices, with face vector \((12,48,72,30)\) in dimensions zero through three. A simplex in the barycentric subdivision \(\operatorname{sd}K\) is a nonempty strict chain of faces \(F_0\subsetneq\cdots\subsetneq F_q\), including chains that skip dimensions. There are \(3342\) such flags.

The group acts simplicially on \(\operatorname{sd}K\). Within each flag, its vertices correspond to faces of *distinct cardinalities*, which the group preserves. Consequently every flag stabilized setwise is fixed vertexwise, and distinct boundary faces of any flag cannot be interchanged by its group action. Thus the orbit flags form a regular CW structure for \(|K|/S_4\): each flag orbit represents one cell and its immediate boundary cells are obtained by deleting one member of its chain. Enumerating all \(24\) permutations and taking lexicographically minimal flag images yields the orbit-cell vector
\[
(c_0,c_1,c_2,c_3)=(11,42,63,30).
\]
These counts are independently confirmed by Burnside's orbit formula in `burnside_check.py`; their alternating sum is \(2\).

**2. Exact elementary collapses.** The `certificate.json` file lists \(60\) ordered lower-cell/upper-cell pairs in this canonical orbit-cell indexing. The standalone `verify.py` reconstructs every face, flag, orbit, and incidence, and for **each pair, at the moment of removal**, verifies that the lower cell has exactly one immediate upper coface, that the upper cell is maximal, and that the incidence is a regular attaching incidence of degree \(\pm1\). Such pairs are elementary regular-CW collapses and preserve the full homotopy type. Removing all \(60\) pairs eliminates all three-cells and leaves a connected two-complex with exactly \(6\) vertices, \(12\) edges, and \(8\) two-cells.

**3. Exact attaching maps.** In the remaining one-skeleton, the five edge cells with canonical IDs \(12,13,16,17,20\) form a spanning tree. Collapsing this tree preserves homotopy type and leaves one vertex, seven oriented one-cells \(g_1,\ldots,g_7\) (edge-cell IDs \(14,18,19,40,41,42,43\)), and eight triangular attaching relators, in ascending two-cell order \(63,64,66,67,68,69,70,71\):
\[
 g_4,\quad g_4g_1^{-1},\quad g_5,\quad g_6g_2^{-1},
 \quad g_3g_6,\quad g_3g_5,\quad g_7g_1^{-1},\quad g_7g_2^{-1}.
\]
Each word follows the oriented flag triangle boundary, read along the first edge, then the second, then the reverse of the third; tree-edge letters are omitted. This calculation is exhaustively reproduced in the checker and recorded in the certificate.

A one-cell occurring exactly once with exponent \(\pm1\) in an attaching word can be removed along with that two-cell by a homotopy-preserving elementary generator/relator cancellation, substituting its solved word into the remaining attaching maps. Here the sequence \(g_4,g_1,g_5,g_3,g_6,g_2,g_7\) cancels all seven generators. Each substitution reduces to the empty word, and the one remaining two-cell has the empty attaching word. The resulting CW complex has one zero-cell, no one-cells, and one two-cell attached constantly, and hence is precisely \(S^2\). Every step is a homotopy equivalence, proving the stated quotient homotopy type and its integral consequences.

## Verification
In the same directory as `certificate.json`, run `python3 verify.py`; the expected final marker is `TRUNCATED_TETRA_ORBIT_SPHERE_OK`. The checker uses only the Python standard library and reconstructs all \(24\) permutations, \(162\) simplicial faces, \(3342\) flags, \(146\) orbit cells, each claimed free-face pair, the exact remaining one-skeleton, all eight attaching words, and all seven generator/relator cancellations. It compares these computations with the embedded explicit finite certificate rather than trusting a saved execution log.

Run `python3 burnside_check.py` separately. It enumerates faces by bit masks and counts fixed flags under each label permutation using a different recurrence; it obtains the same orbit-cell vector and Euler characteristic. These are finite, exhaustive checks on the specified twelve-vertex object. The topological conclusion uses the cited cellular-homotopy operations; Burnside counts or rational homology alone would not prove it.

## Relationship to prior work
Engström's 2005 work establishes connectivity results for independence complexes of claw-free graphs. Barmak's 2010 work studies star clusters, matching complexes and their connectivity; their inspected full texts do not give the full tetrahedral orbit-space homotopy type here.

The closest publicly available same-object work, *Homotopy and tetrahedral symmetry of a subdivided-complete-graph matching complex* (2026), identifies \(K\simeq\bigvee^5S^2\), computes its rational \(S_4\)-character, and proves **every** subgroup quotient simply connected. It also gives the full quotient's rational second Betti number \(1\). A separate same-object result, *The truncated-tetrahedral independence complex and its rational tetrahedral symmetry module* (2026), establishes these nonequivariant/rational statements. None of these previously stated conclusions determines the **integral homotopy equivalence** of the full quotient: a three-dimensional orbit complex can have torsion or nontrivial higher attaching information even if it is simply connected and has rational homology \(\mathbb Q\) in degree two. The exact \(60\)-collapse/\(7\)-cancellation certificate rules out those alternatives.

The matching complex of \(T\) itself, its two-independence complex, and its graph-metric Rips complexes are different simplicial constructions. A numerical similarity in sphere ranks or rational invariant dimensions does not imply equivalence of their orbit spaces.

## Limitations
This is an exact classification for the full \(S_4\) action on one finite graph, not a theorem for all subgroups or larger truncated simplices. The pre-existing simply-connectedness and rational homology conclusions are credited, not claimed anew. The independent Burnside test checks cell counts, not attaching maps; the full homotopy certificate is verified computationally in one implementation. Indexed searches and full-text comparisons cannot eliminate the possibility of unpublished or unindexed equivalent results. No independent mathematical audit has been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public 2005-12-17, https://arxiv.org/html/math/0512420v1.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, https://arxiv.org/html/1007.0418v1.
3. *Homotopy and tetrahedral symmetry of a subdivided-complete-graph matching complex*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-homotopy-and-tetrahedral-symmetry-of-a-subdivided-complete-graph--eabf618ad7d5.
4. *The truncated-tetrahedral independence complex and its rational tetrahedral symmetry module*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-truncated-tetrahedral-independence-complex-and-its-rational--1ca9caa90c0c.
