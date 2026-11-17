# Canonical classification and exact triangle census for two-read deletion graphs

## Finding
Let \(q\ge2\) and \(n\ge1\) be integers, and let \(\Sigma\) be an alphabet of size \(q\). For a word \(x\in\Sigma^n\), write \(D(x)\) for the **set of distinct** words obtained by deleting exactly one coordinate. Let \(G_{q,n}\) join distinct vertices \(x,y\in\Sigma^n\) if \(|D(x)\cap D(y)|=2\). Then the number \(T_q(n)\) of unordered triangles in \(G_{q,n}\) is exactly
\[
T_q(n)=q(q-1)\sum_{L=4}^{n}(n-L+1)(L-3)q^{n-L},
\]
where an empty sum is zero. Equivalently,
\[
\sum_{n\ge1}T_q(n)z^n=\frac{q(q-1)z^4}{(1-z)^2(1-qz)^2}.
\]
For the binary alphabet, this simplifies for every \(n\ge1\) to
\[
T_2(n)=(n-5)2^{n-1}+2n+2.
\]
More strongly, **every triangle has a unique pivot**: exactly one of its three vertices \(x\) has two adjacent, nonoverlapping intervals \(I=[i,j]\), \(J=[j+1,k]\), both of length at least two, on which it differs from the other two vertices respectively. On each interval \(x\) alternates between the same two distinct symbols \(\alpha,\beta\); at the junction \(x_j=x_{j+1}\). The two other triangle vertices are obtained by exchanging \(\alpha\) and \(\beta\) in \(I\) and \(J\), respectively, leaving all other positions untouched. Conversely every such choice forms a triangle, and its pivot and intervals are unique.

## Assumptions and scope
The graph concerns **two distinct single-deletion reads**. Deletion descendants are counted without multiplicity. For two distinct equal-length source words, a one-deletion intersection has size at most two; hence equality to two is the confusability threshold for a code reconstructed from two distinct reads. The theorem is valid for every finite alphabet of size at least two, including the empty-sum lengths \(n<4\). A triangle means three pairwise confusable source words, **not** three sources sharing the same two deletion descendants.

## Proof
We use the established Type-A characterization for single-deletion reconstruction (Cai–Kiah–Nguyen–Yaakobi): distinct \(x,y\in\Sigma^n\) have two distinct common one-deletion descendants exactly when there is a unique interval \([a,b]\), of length at least two, outside which the words agree, and on which they are opposite phases of a two-symbol alternating word. The interval is exactly the first-to-last difference interval, and each of its positions differs.

Fix a triangle with vertices \(x,y,z\). Let \(I\) be the difference interval of \(x,y\) and \(J\) the difference interval of \(x,z\). Each has length at least two. The two symbols on the alternating interval of an edge form an unordered pair \(P_{xy}\), respectively \(P_{xz}\).

We first establish a common alphabet pair for all three edges. If \(I,J\) overlap in at least two consecutive positions, the word \(x\) alternates there; those two positions exhibit both distinct symbols in both pairs, forcing \(P_{xy}=P_{xz}\). If they overlap in exactly one position, both intervals have exclusive portions. At any position belonging only to \(I\), the differing pair \(y,z\) is exactly the pair \(x,y\), whereas at any position only in \(J\) it is \(x,z\). Since \(y,z\) is a Type-A edge and both positions differ, these pairs must coincide with its fixed pair \(P_{yz}\). If \(I,J\) are disjoint, the same exclusive-portion argument applies. Thus all three edges use the same unordered pair. In particular, at positions of \(I\cap J\), the two symbol swaps cancel between \(y\) and \(z\). Therefore the difference set of \(y,z\) is precisely the symmetric difference \(I\mathbin\triangle J\).

The symmetric difference of two intervals of length at least two is a single interval of length at least two exactly in the relevant distinct-word configurations when (i) the intervals are disjoint and adjacent, or (ii) one properly contains the other and they share a left endpoint or a right endpoint. Crossing intervals with nonempty overlap, or strict interior containment, leave two separated pieces; nonadjacent disjoint intervals do too. If the intervals coincide, the swapped neighbors are identical, contradicting three distinct vertices. The condition remains necessary when one overlap has length one, by the same fixed-pair argument.

In case (ii), relabel the triangle to use the vertex obtained by swapping the smaller interval: at that vertex the two difference intervals are the smaller interval and the complementary adjacent interval. They each have length at least two because all edges are Type A. Thus a pivot with adjacent intervals exists in every triangle. When a vertex already has adjacent disjoint intervals, the other two vertices have a nested pair of intervals, so **exactly one pivot** exists.

For a pivot \(x\), the two edges incident to it imply that \(x\) alternates on each block. Since the third edge spans their union and is also Type A, both blocks use the same symbol pair. To make the third pair of words alternating across the junction, the last and first symbols of the two blocks of \(x\) must be **equal**, rather than different. Conversely, these conditions make all three pairs Type A, proving the classification.

Now count uniquely via pivots. The union \(I\cup J\) has some length \(L\ge4\); it has \(n-L+1\) positions and \(L-3\) splits into two lengths each at least two. Choose the first block's first symbol and its distinct alternate symbol in \(q(q-1)\) ways. Internal alternation and the equal junction uniquely determine the union, and the \(n-L\) outside symbols are arbitrary in \(q^{n-L}\) ways. Uniqueness of the pivot precludes double counting, giving the sum. The generating function follows by independently assigning arbitrary left and right contexts (each \((1-qz)^{-1}\)), and a positive pair of block lengths at least two (factor \(z^4(1-z)^{-2}\)). The binary specialization follows by evaluating the rational generating function.

## Verification
The accompanying `verify.py` independently enumerates all words, directly builds each **distinct** deletion-descendant set, and joins pairs having two common descendants. It counts every triangle and verifies that exactly one of its vertices satisfies the stated pivot and alternating-block conditions. It checks all lengths \(1\le n\le11\) for \(q=2\), all lengths \(1\le n\le7\) for \(q=3\), and all lengths \(1\le n\le6\) for \(q=4\). It also verifies the binary closed form through \(n=24\). The program is a finite corroboration; the general proof is the Type-A structural lemma and the exhaustive interval classification above. Run `python3 verify.py` using standard Python 3 only.

## Relationship to prior work
Levenshtein initiated the reconstruction-from-multiple-corrupt-reads problem in 2001. Cai, Kiah, Nguyen and Yaakobi subsequently characterized the pairs of words with exactly two distinct common single-deletion outputs; their Type-A lemma is the principal input here. An exact edge enumeration for the resulting two-read graph counts the Type-A pairs at all lengths and alphabet sizes, but does not determine their mutual incidences or three-vertex cliques. A separate exact triangle enumeration for the **one-read** binary deletion graph counts triples sharing at least one deletion descendant pairwise, which is a different, strictly denser graph; that formula neither states nor directly implies the two-read triple classification or the formula here. The contribution is the canonical pivot classification and complete q-ary triangle enumeration.

## Limitations
The formula gives triangles, not general clique counts, maximum independent sets or optimal codebook cardinalities. It does not assert that three vertices in a triangle share two *common* outputs; only the pairwise intersections are each of size two. An earlier unindexed enumeration or equivalent statement under synchronization terminology may exist. The full original 2001 article was not inspected; accessible bibliographic metadata and abstract establish historical scope but not complete exclusion of prior equivalent results. Correctness uses the published general Type-A lemma; the finite verifier is not a substitute for this general characterization.

## References
1. V. I. Levenshtein, “Efficient reconstruction of sequences,” *IEEE Transactions on Information Theory* **47** (2001), 2–22, DOI 10.1109/18.904499; IEEE publication date 2001-01-31.
2. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:2001.01376, first posted 2020-01-06, and *IEEE Transactions on Information Theory* (2022), DOI 10.1109/TIT.2021.3122798.
3. “Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph,” publicly accessible research result (2026), with explicit Type-A edge count and no triple enumeration.
4. “Exact triangle count in the binary single-deletion graph,” publicly accessible research result (2026), for the distinct one-read graph.
