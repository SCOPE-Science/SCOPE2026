# Exact metric geometry of the eight-arch Dyck two-read reconstruction graph

## Finding
Let \(\mathcal D_8\) consist of all length-\(16\) binary Dyck words, with \(1\) as an up-step and \(0\) as a down-step. For each word \(w\), let \(\Delta(w)\) be the **set** of all distinct length-\(15\) words obtained by deleting exactly one position. Define \(G_8\) to have vertex set \(\mathcal D_8\), joining two distinct words when \(|\Delta(u)\cap\Delta(v)|\ge2\).

**Exact metric classification.** This graph has \(1430\) vertices and \(6733\) edges. Its radius is \(6\) and its diameter is \(12\). Its **unique center** is the word `1101010101010100`. The full eccentricity spectrum, represented by (eccentricity, number of vertices), is \((6,1),(7,68),(8,387),(9,581),(10,320),(11,69),(12,4)\). The four peripheral vertices are `1111111100000000`, `1111111000000010`, `1011111110000000`, and `1011111100000010`.

The numbers of **unordered distinct vertex pairs** at distances \(1,2,\ldots,12\), respectively, are
\[
(6733,33784,106065,213636,274051,223067,115996,38930,8325,1073,73,2).
\]
The only unordered diametral pairs are the two pairs:

- (`1111111100000000`, `1011111100000010`)
- (`1111111000000010`, `1011111110000000`).

These claims concern the exact finite semilength-eight graph, not all Dyck semilengths. Its first graph-size scale above a thousand states makes it a useful fully certified test instance for proposed all-order metric laws.

## Assumptions and scope
Each Dyck word has eight up-steps and eight down-steps, every prefix has nonnegative height, and total height zero. Deletion descendants count distinct **strings**, not deletion positions or a multiset. Graph distance is ordinary unweighted shortest-path distance. Vertices are labeled by their exact bit words; no reversal, complementation, or tree quotient is taken.

## Proof
This is an exhaustive finite proof with two independent realizations. First, every Dyck word is generated recursively by appending an up-step, or (when height is positive) a down-step, with exactly eight up-steps and eight down-steps at the end; each path has precisely one generation route. A binomial independent generator separately chooses eight up-step positions and discards any negative-prefix path. Both give \(1430\) unique words, exhaustively covering the Catalan set.

For the first graph realization, remove each of the 16 positions from each vertex, deduplicate the resulting strings, invert the string-to-parent incidence lists, and count common deletion descendants for each unordered vertex pair. Add an edge if and only if the resulting count is at least two. This is exactly the graph definition, with no unproved classification step. Each edge is undirected. The construction produces \(6733\) edges.

Independently, for every generated Dyck word, enumerate all even-length alternating contiguous intervals and complement the bits on that interval. Keep the resulting word if and only if it is another Dyck vertex. A classical characterization of binary single-deletion two-read overlaps establishes that this exactly generates the same graph: the first-to-last different positions of a qualifying pair form opposite phases of an alternating interval. Equal Hamming weights force an even interval. In this independent construction the resulting graph again has \(6733\) edges, and its complete metric census matches the first method.

For either graph, breadth-first search started at **each** vertex computes all shortest-path distances: the usual queue invariant says each newly visited vertex is reached by a path of its minimal possible length, because every edge has unit weight. Both implementations assert that every vertex is reached. Taking the row maxima computes all eccentricities and the radius and diameter. Counting the entries above the diagonal of the distance matrix computes the unordered pair-distance distribution without double counting. Both full calculations return the same arrays stated above. The pair distribution sums to \(\binom{1430}{2}=1,021,735\); the eccentricity distribution sums to \(1430\). The unique center, four peripheral vertices and two diametral pairs are retrieved directly from the labeled rows. Since every state and every graph neighbor has been examined, this establishes the complete claimed finite result, not a sampling-based inference.

## Verification
Run `python3 verify_dyck_A.py` and `python3 verify_dyck_B.py` using Python 3 and its standard library. The first program builds the graph directly from all distinct deletion outputs; the second independently generates the vertices using combinations and builds the graph by alternating-interval flips. Both exhaust all \(1430\) breadth-first search sources and verify the full pair-distance and eccentricity counts and the unique center. The second method does not import the first method or any data table from it. Re-run both from the files embedded here, not external versions.

## Relationship to prior work
*Cai et al., Coding for Sequence Reconstruction for Single Edits* (2020) gives the general binary two-read overlap characterization. The published 2026 study *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree* gives the complete Dyck edge description, its all-order **edge-count** formula, and a unique maximum-**degree** vertex. The published result does **not** state this graph's radius, diameter, eccentricity distribution, center, or the number of diametral pairs. The previously known edge formula predicts the 6733 edges and is explicitly **not** proposed as new. Eccentricity requires global shortest-path computations and cannot be inferred from the edge count or maximum degree alone. Song, Cai and Quek (2026) motivate reconstruction from erroneous reads but study a different channel with substitutions.

## Limitations
No all-semilength metric theorem is asserted; the linear radius/diameter patterns observed in smaller semilengths remain conjectural outside the proved finite range. The enumerated exact metric is computationally certified by complete exhaustive programs, not by a compact closed-form distance formula. A prior paper already characterizes every edge, so the distinction between an unstated graph metric and an algorithmically derivable corollary is an important residual originality risk. Unindexed equivalent metric computations cannot be ruled out. 

## References
1. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, https://arxiv.org/abs/2001.01376 (2020).
2. *Dyck-restricted two-read deletion graph: a vertex-marked bijection and sharp degree*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dyck-restricted-two-read-deletion-graph-a-vertex-marked-bijectio--3635f93f657f (2026-11-08).
3. W. Song, K. Cai, and T. Q. S. Quek, *On the Sequence Reconstruction Problem for the Single-Deletion Two-Substitution Channel*, arXiv:2601.07547, first released 2026-01-12, https://arxiv.org/abs/2601.07547.
