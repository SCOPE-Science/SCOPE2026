# All \(2\)-plexes of Cartesian products of complete graphs

## Finding

**Theorem (line–square–distance decomposition).** Fix integers \(d\ge2\) and \(n_1,\ldots,n_d\ge2\), and put
\[
G=K_{n_1}\square\cdots\square K_{n_d},\qquad N=\prod_{i=1}^d n_i.
\]
A vertex set \(S\) is a **\(2\)-plex** when every vertex of \(G[S]\) has at most one nonneighbor in \(S\). In particular, no connectivity requirement is imposed. Write \(A_G(z)\) for the enumerator of all \(2\)-plexes, including the empty set, and \(M_G(z)\) for the enumerator of inclusion-maximal \(2\)-plexes. Define
\[
Q=\sum_{1\le i<j\le d}\frac{N}{n_i n_j}\binom{n_i}{2}\binom{n_j}{2},
\quad
D=\frac N2\left(N-1-\sum_i(n_i-1)-\sum_{i<j}(n_i-1)(n_j-1)\right).
\]
Then the following **two exact polynomials** hold:
\[
\boxed{A_G(z)=1+Nz+\binom N2z^2+4Qz^3+Qz^4
+\sum_{i=1}^d\frac N{n_i}\sum_{t=3}^{n_i}\binom{n_i}{t}z^t,}
\]
\[
\boxed{M_G(z)=Dz^2+Qz^4+
\sum_{\substack{1\le i\le d\\n_i\ge3}}\frac N{n_i}z^{n_i}.}
\]
Every inclusion-maximal \(2\)-plex is **exactly one** of: (i) a pair at Hamming distance at least three; (ii) the four vertices of an axis-aligned coordinate square; (iii) a complete coordinate line of size at least three. The three classes are disjoint as sets even if their cardinalities coincide. In particular, the support of \(M_G\) consists of \(4\), of all factor sizes \(n_i\ge3\), and additionally \(2\) precisely when \(d\ge3\).

For a homogeneous Hamming graph \(H(d,q)\) with \(d\ge3\), \(q\ge6\), the only inclusion-maximal \(2\)-plex sizes are \(2,4,q\). Therefore the \(q-5\) consecutive sizes \(5,6,\ldots,q-1\) never occur. This is an unbounded gap as \(q\) grows.

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled by coordinate tuples. Each factor has at least two vertices and there are at least two factors. Two tuples are adjacent in \(G\) exactly when they differ in one coordinate. A coordinate line is the set of all tuples with all but one coordinate fixed. An axis-aligned square is obtained by choosing two coordinates, two distinct symbols in each, and fixing the other coordinates. Hamming distance is the number of differing coordinates. Inclusion-maximal means inclusion-maximal among all \(2\)-plexes; it does not mean maximum cardinality. The empty set is included only in \(A_G(z)\), by vacuous satisfaction of the condition.

## Proof

**Common-neighbor observation.** If tuples \(u,v\) are nonadjacent and have Hamming distance exactly \(2\), their common neighbors are exactly the two tuples obtained by changing either one of the two differing coordinates of \(u\) to the corresponding coordinate of \(v\). If their distance is at least \(3\), they have no common neighbor. This follows directly from the one-coordinate adjacency rule. All cliques of size at least three are contained in a single coordinate line: if \(u,v,w\) are pairwise adjacent, the changed coordinate from \(u\) to \(v\) must equal that from \(u\) to \(w\); the same argument applies to every additional clique vertex.

**Exhausting all \(2\)-plexes.** Let \(S\) be a \(2\)-plex and let \(u,v\in S\) be nonadjacent. Because each of \(u,v\) already has one nonneighbor in \(S\), every vertex of \(S\setminus\{u,v\}\) must be adjacent to both. If \(|S|\ge3\), the pair therefore has distance exactly \(2\), and \(|S|\le4\). If \(|S|=4\), the other two vertices are the two common neighbors, giving exactly a coordinate square; conversely such a square induces a \(4\)-cycle and is a \(2\)-plex. If \(|S|=3\), the nonclique triple is a three-vertex path, uniquely completed to that coordinate square. If \(S\) has no nonadjacent pair and \(|S|\ge3\), it is a clique contained in one coordinate line. Every one- or two-element set is automatically a \(2\)-plex. Thus all cases are exhausted and disjoint at the level of the displayed set types.

**Maximality.** A distance-at-least-three pair cannot be enlarged: any added vertex would have to be adjacent to both endpoints, which is impossible. A full coordinate line with at least three vertices cannot be enlarged, because any vertex outside it is adjacent to at most one vertex in the line and so has at least two nonneighbors there. A square cannot be enlarged because every \(2\)-plex of size at least five is a clique, whereas the square is not. Conversely, a pair at distance one extends to a three-vertex path by varying any different coordinate (possible since \(d\ge2\)); a pair at distance two extends using one of its common neighbors. Every nonclique three-element \(2\)-plex extends to its unique square. Every clique of size at least three extends to its entire coordinate line unless it already is that line. Singletons and the empty set are not maximal. This proves the classification.

**Enumeration.** There are \(N/n_i\) coordinate lines in direction \(i\), each containing \(n_i\) vertices; a clique of size \(t\ge3\) belongs to exactly one such line. There are \(Q\) coordinate squares, and each has four three-vertex paths, each uniquely square-completable. The empty, singleton, and pair coefficients are \(1,N,\binom N2\). Adding the line cliques of sizes at least three and the three-vertex paths and four-vertex squares proves \(A_G(z)\). A fixed vertex has \(\prod_{i\in J}(n_i-1)\) vertices differing from it exactly on a specified coordinate subset \(J\). Summing over \(|J|\ge3\), using \(N=\prod_i(1+(n_i-1))\), and dividing by two yields \(D\), the number of unordered distant pairs. Counting full lines and squares proves \(M_G(z)\). For homogeneous parameters \(q\ge6\), \(d\ge3\), the three classes have the stated distinct cardinalities and give the asserted missing interval.

## Verification

The accompanying `verify.py` implements \(2\)-plex membership from the coordinate adjacency definition and tests inclusion-maximality by every possible one-vertex addition. It independently generates distant pairs, full coordinate lines, and coordinate squares, compares all proposed maximal sets with brute-force maximal sets, and compares the full \(2\)-plex polynomial with direct subset counts. Across eleven small instances (up to \(18\) vertices), all \(468037\) nonempty subsets were checked; three larger instances received generated-family maximality checks only. The final verifier line is `VERIFY_OK instances=14 tested_subsets=468037 generated_maximal=881 exact_families=PASS all_and_maximal_polynomials=PASS`. The program is finite corroboration, not a proof for all parameters.

## Relationship to prior work

The \(2\)-plex model is established in network community detection and maximal relaxed-clique enumeration. Dai et al. (2022) formulate and algorithmically enumerate general maximal \(k\)-plexes but do not derive Hamming-product-specific coefficients or a line–square–distance classification. Conte et al. (2019) give a general distributed \(2\)-plex enumerator; Jiddou and Manoussakis (2025) give enumeration guarantees in bounded-degeneracy graphs. The general co-\(2\)-plex polynomial of McClosky, Simms, and Hicks (2011), applied to the complement graph, supplies a general recurrence but not the displayed closed Hamming-product polynomials. Klavžar and Peterin (2005) characterize which graphs embed into Hamming graphs, a different question from counting all and all maximal \(2\)-plexes in a specified Hamming product.

## Limitations

Only the case \(k=2\) is addressed. The theorem does not require a \(2\)-plex to be connected; imposing connectivity would delete distant-pair terms. It does not address arbitrary Cartesian products or higher \(k\). No publication-priority guarantee or independently certified verification is asserted. A general embedding paper was checked at abstract level, not in full; search coverage cannot exclude every differently named equivalent source. The proof, rather than the finite checks, carries the universal quantifiers.

## References

1. Q. Dai, R.-H. Li, H. Qin, M. Liao, G. Wang, *Scaling Up Maximal k-Plex Enumeration* (first public preprint 21 March 2022), arXiv:2203.10760.
2. A. Conte, D. Firmani, M. Patrignani, R. Torlone, *Shared-Nothing Distributed Enumeration of 2-Plexes*, CIKM 2019, DOI 10.1145/3357384.3358083.
3. M. Jiddou and G. Manoussakis, *Efficient Enumeration of k-Plexes and k-Defective Cliques*, IPEC 2025, DOI 10.4230/LIPIcs.IPEC.2025.22.
4. B. McClosky, A. Simms, I. V. Hicks, *Co-2-plex polynomials*, Journal of Combinatorial Optimization 22 (2011), 640–650, DOI 10.1007/s10878-010-9313-y.
5. S. Klavžar and I. Peterin, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory 49 (2005), 302–312, DOI 10.1002/jgt.20084.
