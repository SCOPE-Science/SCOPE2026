# Stable three-sphere bouquets in bidirected complete bipartite multipath complexes

## Finding
For every integer \(n\ge6\), let \(D_n\) be the fully bidirected complete bipartite graph with parts of sizes two and \(n\). Let \(X_n\) be the simplicial complex whose vertices are the directed arcs of \(D_n\) and whose simplices are arc sets that form vertex-disjoint directed simple paths. Then
\[
|X_n|\simeq\bigvee^{\,n^4-8n^3+19n^2-14n+1}S^3.
\]
In particular, the only nonzero reduced integral homology is free and lies in degree three. At \(n=6,7,8\), the sphere multiplicities are respectively \(169,491,1105\). The previously calculated case \(n=6\) is included to state the sharp stable range; the contribution is the unrestricted family.

## Assumptions and scope
There are exactly two vertices on the small side, denoted \(u,v\), and \(n\) leaf vertices \(w_1,\ldots,w_n\). Each undirected edge is replaced by both arrows. Every directed path is vertex-simple, so directed two-cycles and longer directed cycles are excluded. The complex is **not** the ordinary matching complex or the discrete-Morse complex of the underlying graph. Its realization has dimension at most three, since each of the two hubs supports at most one incoming and one outgoing selected arc.

Use the four arc types \(A_i:u\to w_i\), \(B_i:w_i\to u\), \(C_i:v\to w_i\), and \(D_i:w_i\to v\). A face can be encoded by \((a,b,c,d)\in\{0,1,\ldots,n\}^4\), where zero denotes an absent type. This tuple is a face precisely when none of the following holds (zero entries do not participate): \(a=b\ne0\), \(a=c\ne0\), \(b=d\ne0\), \(c=d\ne0\), or \(a=d\ne0\), \(b=c\ne0\) simultaneously. The first four restrictions are the two-cycles and repeated leaf in-/outdegree conflicts. The last condition excludes the directed four-cycle; no longer simple directed cycle exists with only two hubs.

## Proof
**1. Explicit face count.** Every face has at most one arc of each of the four types. The numbers of faces with respectively zero through four arcs are
\[
1,\quad4n,\quad 6n^2-4n,\quad4n(n-1)^2,\quad n(n-1)^2(n-2).
\]
For example, a four-arc face first chooses \(a\ne c\), then chooses \(b\ne a\). If \(b=c\), the fourth index has \(n-2\) choices after excluding the four-cycle; if \(b\ne c\), it again has \(n-2\) choices. This proves the final formula. The two- and three-arc formulas follow by selecting types and imposing the displayed pairwise conflicts.

**2. A universal acyclic matching.** Include the empty face temporarily. Order the arc vertices by all \(A_i\) in increasing \(i\), followed by all \(B_i\), then \(C_i\), then \(D_i\). At each arc vertex, pair every currently unpaired face not containing it with its extension by that vertex, whenever both remain unpaired; remove the two faces. Each such step is a matching along a cover relation. The union of these matches is acyclic: in a hypothetical closed alternating gradient path choose the earliest arc-vertex step used by a matched upward edge. Every face of the path is still present at the beginning of that step. Any downward edge deleting that same arc vertex would then have been paired at that step, impossible. Hence that arc's presence could only increase along the cycle, contradicting closure.

**3. Fresh-tail lemma.** Write \(R_s\) for the unmatched faces after the first \(s\) complete type blocks, with \(R_0\) the initial face set. For \(0\le s\le3\), suppose \(n\ge5s\), \(F\) is a face of at most three arcs, and \(e\) has an as-yet-unprocessed type and uses a leaf \(j>5s\) absent from \(F\). Then
\[
F\in R_s\quad\Longleftrightarrow\quad F\cup\{e\}\in R_s.
\]
Prove this simultaneously with the following pivot bound: whenever \(F\in R_{s-1}\), \(F\) does not contain the type processed at stage \(s\), and \(F\) has at most three arcs, there is an eligible surviving extension at that stage whose leaf index is at most \(5s\) (provided \(n\ge5s\)).

For the induction start \(s=0\), both sets are faces: an arc at a fresh leaf cannot create a directed cycle or repeat an in-/out-port. For the pivot bound at step \(s\), choose a leaf among \(5(s-1)+1,\ldots,5s\) not used by \(F\); at most three leaves are occupied. Appending the stage-\(s\) arc at that fresh leaf preserves membership in \(R_{s-1}\) by the inductive fresh-tail statement. Thus an eligible extension exists in the indicated five-position interval.

To establish the fresh-tail statement at stage \(s\), compare \(F\) with \(F\cup\{e\}\), with \(e\) at index \(j>5s\). Their membership before this stage agrees by induction. If neither contains a stage-\(s\) arc, the pivot bound removes both whenever they were present. Otherwise remove their common stage-\(s\) arc to obtain the respective bases. If the base was already removed, no matching at this stage acts on either face. If it survives, both bases have a least eligible stage-\(s\) pivot, and these least indices are at most \(5s\). Every candidate of index at most \(5s\) is legal for both bases simultaneously: the new arc at the distinct leaf \(j\) cannot create a repeated in-/out-port or directed cycle. By induction the corresponding candidates survive the earlier stages simultaneously. Their least pivots therefore coincide, so the two faces are paired at this stage simultaneously or both survive. This completes the induction. The argument also applies when a base already contains later-type arcs, provided at most four arcs occur after extension.

**4. Uniform stable range.** For \(n\ge20\), at the end of stage \(s\in\{1,2,3,4\}\), every unmatched face contains an arc of type \(s\). Indeed, any still-unmatched face without that type has at most three arcs; the pivot bound supplies an extension with an index in the first \(5s\), forcing its removal at stage \(s\). Previously acquired types cannot be lost by subsequent matching because unmatched faces are only deleted. Consequently the final unmatched faces contain all four types and thus are all three-simplices. This conclusion requires no finite extrapolation.

**5. Bounded initial range and Morse conclusion.** For \(6\le n\le19\), the exhaustive finite procedure in `verify_k2n.py` constructs every possible tuple using the exact five validity tests, executes every specified matching pair, and asserts that only four-arc faces remain. These are finite exhaustive certificates for this bounded range, not a substitute for step 4. The same verifier independently checks direct-path validity and the entire oriented face-incidence graph for \(n=6,7\).

We thus have, for every \(n\ge6\), an acyclic matching on the augmented face poset with no critical cell below dimension three. Delete only the matching between the empty face and the first vertex; this leaves one ordinary critical vertex and all the critical three-cells, without introducing a gradient cycle. Forman's discrete Morse theorem gives a CW model with one zero-cell and only three-cells, hence a wedge of three-spheres. Its sphere multiplicity is the negative reduced Euler characteristic. Using step 1 gives
\[
1-4n+(6n^2-4n)-4n(n-1)^2+n(n-1)^2(n-2)
=n^4-8n^3+19n^2-14n+1.
\]
This proves the theorem integrally.

## Verification
Run `python3 verify_k2n.py` using Python 3 standard library. It checks all fourteen sizes \(6\le n\le19\), their full face counts, all the matching operations, the dimensions and multiplicities of critical cells, and the formula for the final count. For \(n=6,7\) it also independently recognizes faces from graph indegree/outdegree and directed-cycle tests, and topologically sorts the complete directed face-incidence graph. The recorded exact output is in `verification_output.txt`. The uniform step for \(n\ge20\) is proved in step 4 rather than asserted from finite data.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (arXiv:2208.04656v1, August 9, 2022) consider complete bipartite digraphs with **only arcs directed from the first part to the second** (Section 3.2), giving a chessboard matching-complex interpretation. Their one-way construction is different from the fully bidirected object here, which admits paths through both hubs and has directed four-cycle exclusions. Caputi, Collari and Smith (arXiv:2601.05670, originally posted January 9, 2026) study multipath complexes of bidirected paths and cycles and their homology; their Section 1.1 discusses cycle-free chessboard complexes for complete digraphs. Those conclusions do not imply the four-slot complete-bipartite classification here. Deshpande and Sawant (arXiv:2602.14936, February 16, 2026) study directed-linear-forest complexes via conflict graphs and vertex decomposability, with direct independence-complex identifications under 2-acyclicity assumptions. The digraph here has directed four-cycles, so that reduction does not apply. Separately recorded exact finite cases include \(n=4,5,6\); the present result supplies a **uniform** proof for all larger sizes. A Morse complex of the underlying \(K_{2,n}\) and a two-matching complex of \(K_{2,n}\) have different face definitions and do not imply the theorem.

## Limitations
The theorem only concerns the two-hub bidirected complete bipartite family and its nonequivariant integral homotopy type. It does not determine integral permutation representations, arbitrary part sizes, or any directed variant lacking reciprocal arcs. The bounded enumeration is exact for the tested integer range; the infinite range depends on the stated fresh-tail lemma. No independent external mathematical audit has been performed.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (January 9, 2026), https://arxiv.org/pdf/2601.05670.
2. P. Deshpande, R. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1 (February 16, 2026), https://arxiv.org/pdf/2602.14936.
3. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (August 9, 2022), Section 3.2, https://arxiv.org/pdf/2208.04656.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; discrete Morse collapse theorem.
