# Rigidity of minimum edge-geodesic transversals in mixed Hamming graphs

## Finding

Let \(d\ge1\) and \(q_1,\ldots,q_d\ge2\) be integers and let the finite simple unweighted graph
\[
H=K_{q_1}\square\cdots\square K_{q_d},\qquad N=\prod_{i=1}^d q_i.
\]
The vertices are tuples in \(\prod_i\{0,\ldots,q_i-1\}\), adjacent exactly when they differ in one coordinate. The coordinate edge class \(E_i\) is the set of all edges that change the \(i\)-th coordinate; thus
\[
|E_i|=\binom{q_i}{2}\prod_{j\ne i}q_j=\frac N2(q_i-1).
\]
A *maximal geodesic* is a shortest path that is not a proper subpath of a longer shortest path. An *edge-geodesic transversal* intersects the edge set of every maximal geodesic.

**Theorem.** With \(q_{\min}=\min_iq_i\),
\[
\operatorname{gt}_e(H)=\frac N2(q_{\min}-1).
\]
Every minimum transversal is exactly \(E_i\) for one index with \(q_i=q_{\min}\), and these are all the minimum transversals. Consequently there are precisely \(|\{i:q_i=q_{\min}\}|\) labelled optimum sets. More strongly, *every* edge set intersecting *each* maximal geodesic in exactly one edge is a complete coordinate class \(E_i\), with no size restriction.

This extends the previously determined numerical invariant on binary hypercubes to all products of complete graphs of unequal orders, while establishing rigidity of every optimal solution. For \(H=Q_d\), there are exactly \(d\) optimum edge transversals (the direction matchings); for \(K_2\square K_3\square K_4\), the unique optimum is the set of 12 edges in the binary direction, despite the other coordinate classes having sizes 24 and 36.

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. Coordinate alphabets are fixed and labelled; the number of minima counts distinct edge subsets, not abstract orbits. Every \(q_i\) is at least two; no claim is made for a factor of order one (which would be deleted from the Cartesian representation). Geodesic maximality is by inclusion as a *path*, not by having locally maximum degree or by inclusion in the vertex set of another path. The assertion includes \(d=1\), in which every edge of the single clique is a maximal geodesic.

For tuples \(x,y\), their distance is the number of coordinates on which they differ. A geodesic changes each differing coordinate exactly once, and changes no other coordinate. A geodesic omitting some coordinate can be extended by one step at its end in that coordinate, preserving the shortest-path property. Hence the maximal geodesics are **exactly** the length-\(d\) paths joining tuples differing in every coordinate. Each such path uses precisely one edge of each coordinate class \(E_i\).

## Proof

**1. A sharp averaging bound.** Choose uniformly at random a maximal geodesic, considering undirected paths as unoriented. The automorphism group that permutes the alphabet in each fixed coordinate acts transitively on the edges within \(E_i\). Since every maximal geodesic contains exactly one edge from \(E_i\), any specified \(e\in E_i\) belongs to a random maximal geodesic with probability \(1/|E_i|\).

For an edge-geodesic transversal \(S\), every maximal geodesic \(P\) satisfies \(|E(P)\cap S|\ge1\). Therefore
\[
1\le\mathbb E|E(P)\cap S|=\sum_{i=1}^d\frac{|S\cap E_i|}{|E_i|}
\le\frac{|S|}{m},\qquad m=\min_i|E_i|=\frac N2(q_{\min}-1).
\]
So \(|S|\ge m\). Each full coordinate class \(E_i\) meets each maximal geodesic *once*, and an \(E_i\) of minimum size achieves equality. In particular, the minimum is \(m\). If \(|S|=m\), the inequalities above are equalities: because \(|E(P)\cap S|\) is a positive integer for every \(P\), it must be **exactly one** for every maximal geodesic. Thus every optimum is an exact-one hitting set.

**2. An exact-one square-exchange lemma.** Let \(S\subseteq E(H)\) meet each maximal geodesic in exactly one edge. Put \(f(e)=1\) if \(e\in S\) and zero otherwise. Fix two different coordinate indices \(i,j\), two distinct letters in each coordinate, and arbitrary letters elsewhere. The resulting four vertices \(A,B,C,D\) form a Cartesian square, with \(AB,CD\) parallel to coordinate \(i\), and \(AC,BD\) parallel to \(j\). Two maximal geodesics that start at \(A\), use \(A-B-D\) or \(A-C-D\), and then change each remaining coordinate in the *same* order have identical edges outside the square. Exact-one hitting therefore gives
\[
f(AB)+f(BD)=f(AC)+f(CD).\tag{1}
\]
Similarly, compare maximal geodesics starting at \(B\), using \(B-A-C\) or \(B-D-C\) and the identical remaining-coordinate suffix. Then
\[
f(AB)+f(AC)=f(BD)+f(CD).\tag{2}
\]
Subtracting gives \(f(BD)=f(AC)\), and substituting gives \(f(AB)=f(CD)\). Every pair of parallel edges in an elementary coordinate square must have the same indicator. The comparison remains valid for \(d=2\), when the common suffix is empty; for \(d=1\), this step is vacuous.

For fixed coordinate \(i\) and fixed unordered distinct letters \(\{a,b\}\) in that coordinate, arbitrary letters in the other coordinates are connected by a succession of changes in one other coordinate. The square equality just proved shows that \(f\) is constant on all edges labelled by \((i,\{a,b\})\). Write this constant as \(h_i(\{a,b\})\in\{0,1\}\).

**3. Rigidity across letters.** For any independent choice of distinct-letter pairs \(p_i=\{a_i,b_i\}\) in all coordinates, a maximal geodesic from \((a_1,\ldots,a_d)\) to \((b_1,\ldots,b_d)\) changes every coordinate exactly once. Its number of selected edges is therefore \(\sum_i h_i(p_i)=1\). Keeping all other pairs fixed while replacing \(p_i\) with any other edge of \(K_{q_i}\) gives \(h_i(p_i)=h_i(p_i')\). Consequently \(h_i\) is constant on the edges of its entire factor; call that binary constant \(c_i\). The equality \(\sum_i c_i=1\) forces exactly one \(c_i\) to be one. Hence \(S=E_i\) for one coordinate \(i\). This proves the stronger exact-one statement, including \(d=1\).

Finally, an optimum \(S\) has the exact-one property by Step 1, hence equals \(E_i\) by Steps 2–3. Its cardinality is \(m\), so \(q_i=q_{\min}\). Conversely each such \(E_i\) is an optimum. Distinct coordinates have disjoint, nonempty edge classes, proving the labelled census.

## Verification

A separate bounded checker constructs all edges and all maximal geodesics directly from tuple coordinates, without using the proof's averaging or square-exchange characterization. For factor-size tuples \((2)\), \((3)\), \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), and \((2,2,3)\), it enumerates **every** edge subset of the claimed minimum cardinality and verifies that the sole transversal sets are the smallest-coordinate classes. It also tests the exact-one property of each coordinate class for several larger mixed tuples, including \((2,3,4,5)\). Run `python3 verify_hamming_geodesic.py`; the last line must read `VERIFY_OK`.

These bounded checks do not constitute an all-dimensional verification; the unrestricted theorem follows from the proof above.

## Relationship to prior work

Prabha, Sandhiya, and Manuel, *The Edge Geodesic Transversal Problem* (2026), introduce the edge version of geodesic transversals, prove an edge-cut criterion, and compute the numerical optimum \(2^{d-1}\) for binary cubes. Their full preprint provides a binary-coordinate cut attaining that optimum, but does **not** classify all optimizers or treat unequal, nonbinary complete-graph factors. The present theorem proves both properties and in particular determines the exact number of labelled optima.

Brešar, Klavžar, and Manuel's *The geodesic-transversal problem* studies vertex hitting sets, which are a different object. Peterin and Semanišin study vertex covers of maximal shortest paths; neither their parameter nor its implications determine the edge-transversal optimum classification here. General Hamming product geometry, as in *Isometric Hamming embeddings of weighted graphs*, supplies the standard coordinate-distance setting but not this hitting theorem. Results on geodesic distances in Hamming products and geodesic packings are likewise distinct from minimum edge hitting sets. A complete novelty guarantee against unindexed literature is not asserted.

## Limitations

The graph factors must be complete and unweighted. The proof relies on the ability to permute different-coordinate moves and on each maximal geodesic containing exactly one edge of each factor direction; it does not establish analogous rigidity for products of paths, cycles, or arbitrary connected graphs. It also does not count nonminimum transversals, inclusion-minimal transversals of larger size, or transversals of only some geodesics. Historical priority is provisional pending broader human literature verification. No independent mathematical audit is claimed.

## References

1. R. Prabha, B. Sandhiya, P. Manuel, *The Edge Geodesic Transversal Problem*, first public arXiv version 2026-10-27, arXiv:2610.36821v1, https://arxiv.org/abs/2610.36821.
2. P. Manuel, B. Brešar, S. Klavžar, *The geodesic-transversal problem*, first arXiv version 2021-01-20, arXiv:2101.08042, https://arxiv.org/abs/2101.08042.
3. I. Peterin, G. Semanišin, *On the Maximal Shortest Paths Cover Number*, Mathematics 9 (2021), 1592, https://doi.org/10.3390/math9141592.
4. *Isometric Hamming embeddings of weighted graphs*, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10653646/ (background on Cartesian product distance).
