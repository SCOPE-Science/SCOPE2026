# The Heawood dominance complex is a six-sphere with orientation-preserving incidence symmetries

## Finding
Let \(H\) be the fourteen-vertex Heawood graph, the point–line incidence graph of the Fano plane \(\mathrm{PG}(2,2)\). Its dominance complex \(\operatorname{Dom}(H)\), consisting of vertex subsets whose complements dominate \(H\), has the complete integral homotopy type
\[
\operatorname{Dom}(H)\simeq S^6.
\]
Every automorphism of \(H\) acts by degree \(+1\) on the top homology \(\widetilde H_6(\operatorname{Dom}(H);\mathbb Z)\cong\mathbb Z\). Consequently the full 336-element incidence automorphism group acts trivially on this homology group, including point–line dualities.

## Assumptions and scope
Represent the seven Fano points as the nonzero vectors \(1,\ldots,7\) of \(\mathbb F_2^3\). A Fano line is a triple \(\{a,b,a\oplus b\}\), where \(\oplus\) is bitwise addition over \(\mathbb F_2\). The seven lines are
\[
123,145,167,246,257,347,356.
\]
The vertices of \(H\) are the seven points followed by seven lines. A point is adjacent precisely to its three incident lines. A set \(D\) dominates if every vertex lies in \(D\) or is adjacent to a vertex of \(D\). Thus a simplex \(F\) of \(\operatorname{Dom}(H)\) is exactly a subset that does not contain any entire closed neighborhood \(N[v]\). Every \(N[v]\) consists of four vertices. Dimensions refer to ordinary simplices: a nonempty face of size \(k\) has dimension \(k-1\).

## Proof
Enumerate all subsets of the fourteen vertices and retain those avoiding all fourteen four-element closed neighborhoods. This gives 8,851 faces including the empty face, with counts by cardinality \(0,\ldots,10\):
\[
(1,14,91,364,987,1862,2394,1962,931,224,21).
\]
The equivalent condition that the complement intersects every closed neighborhood is checked separately and yields exactly the same face family.

For each vertex in order \(0,1,\ldots,13\), pair every currently unpaired face \(F\) not containing the vertex with \(F\cup\{v\}\), whenever both are currently unpaired faces. Remove every pair and continue through all vertices. This produces 4,425 pairs on the augmented complex, including the empty-face/singleton pair; exactly one seven-vertex face remains unmatched, whose lexicographic bitmask is \(16256\). Discard the empty-face pair to obtain an ordinary matching with 4,424 pairs, exactly one unmatched vertex, and exactly one unmatched six-dimensional simplex. Repeating the construction with the seven line vertices before the seven point vertices yields the same critical-cell dimensions and an unmatched seven-vertex face with bitmask \(127\).

Acyclicity is verified over the entire ordinary Hasse diagram: direct every covering relation from higher to lower face, except for each matching pair, whose arrow is reversed. There are 8,850 nonempty faces and 52,304 covering relations. The actual directed graph, constructed from the reproduced matching, admits a complete topological sorting through all 8,850 vertices (under both matching orders). Therefore the matchings are acyclic. Forman's discrete Morse theorem yields a CW model with one zero-cell and one six-cell, and no cells in dimensions one through five. Since the six-cell attaches to a point, this CW model is \(S^6\). In particular, the statement is an integral homotopy equivalence, not a conclusion from field homology or an incomplete enumeration.

For the symmetry refinement, the 168 invertible linear transformations of \(\mathbb F_2^3\) induce all Fano collineations. The fixed symmetric bilinear form \(a\cdot b\) defines a polarity: send each point to its orthogonal Fano line and each line to its orthogonal point. This exchanges the two parts of the Heawood graph. A connected bipartite graph automorphism either preserves or swaps the parts. Any part-preserver is determined by the images of three noncollinear points, and these have \(7\cdot6\cdot4=168\) possibilities, all realized by invertible linear maps. Thus the 168 collineations and their 168 compositions with polarity exhaust the 336 graph automorphisms.

For each of these 336 permutations \(g\), compute the reduced Lefschetz number from signed fixed faces:
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne F\in\operatorname{Dom}(H)\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
The sign is the parity of the induced vertex permutation on the oriented simplex. Every exact finite evaluation is \(+1\). Because the only nonzero reduced homology lies in even degree six, \(\widetilde L(g)\) equals the trace on the rank-one integral sixth homology. An automorphism of \(\mathbb Z\) has trace \(+1\) exactly when it is the identity, establishing the claimed orientation-preserving action for the entire graph automorphism group.

## Verification
Run `python3 verify_heawood_dominance.py` using only Python's standard library. The program regenerates the Fano lines and graph, checks both definitions of all 8,851 faces, verifies the entire oriented Hasse graph under two independent vertex-order matchings, enumerates all 336 automorphisms, checks adjacency preservation, and computes each signed simplicial Lefschetz trace. The included `verification_output.txt` records the actual result, ending with `ALL_CHECKS_PASS`. These finite calculations support the preceding complete Morse and Lefschetz arguments; neither timeouts nor sampling are used as evidence.

## Relationship to prior work
Taylan's 2015 preprint introduces generalized matching-tree techniques and determines dominance-complex homotopy for chordal graphs, but the Heawood graph has induced six-cycles and is not chordal. Matsushita–Wakatsuki identify the Alexander dual of any dominance complex with the neighborhood complex of the complementary graph and establish connectivity criteria. Their general identity applies here but does not by itself determine this six-sphere or its full integral orientation character.

Previously indexed calculations of the Heawood matching, independence, total three-cut, perfect-matching and graph-homomorphism complexes have different face conditions. General high-girth three-cut theorems apply to three-cut complexes of the original Heawood graph, not automatically to the four-cut complex of its dense complement, which is Alexander-dual to the dominance complex. The latter possible equivalence was considered explicitly when comparing claims. No directly covering archived or indexed result was identified, but mathematical priority remains provisional.

## Limitations
This is an exact statement for the Fano-plane incidence graph only. It neither determines the analogous dominance complexes for larger projective planes nor constructs an equivariant homotopy equivalence with a sphere carrying a specified action. Triviality of the *homology* action is weaker than equivariant homotopy triviality. Independent validation and publication-priority confirmation remain outstanding.

## References
1. Demet Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first publicly posted 2015-01-27, especially §2 and Theorem 5.4. https://arxiv.org/abs/1501.06754
2. Takahiro Matsushita and Shun Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, especially Theorems 1.1, 5.10 and 5.12 and §§4–6. https://arxiv.org/html/2312.02639v2
3. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. Richard Ehrenborg and Gábor Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, DOI:10.1016/j.ejc.2005.04.010 (the earlier forest context).
