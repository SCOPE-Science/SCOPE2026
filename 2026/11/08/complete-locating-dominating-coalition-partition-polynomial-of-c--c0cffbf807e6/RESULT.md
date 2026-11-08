# Complete locating-dominating coalition partition polynomial of complete bipartite graphs

## Finding

Let \(m,n\ge 2\), let \(G=K_{m,n}\) be the complete bipartite graph with a fixed labelled vertex set, and put \(N=m+n\). A locating-dominating set \(D\) dominates all vertices outside \(D\), and the intersections of their open neighborhoods with \(D\) are nonempty and pairwise distinct. An **LDC-partition** is an unordered partition of \(V(G)\) into nonempty classes, none individually locating-dominating, in which each class can be joined with at least one other class to form a locating-dominating set. Define the all-partition counting polynomial

\[
\mathcal L_{m,n}(z)=\sum_{\Pi\text{ an LDC-partition of }G}z^{|\Pi|}.
\]

Then for \(N\ge7\),

\[
\boxed{\mathcal L_{m,n}(z)=\left(2^{N-1}-(m+1)(n+1)\right)z^2+\left[\binom m2+\binom n2+mn(N-2)+2\binom m2\binom n2\right]z^3.}
\]

The complete exceptional list (up to interchanging the two part sizes) is

\[
\begin{aligned}
\mathcal L_{2,2}(z)&=z^2+2z^3+z^4,\\
\mathcal L_{2,3}(z)&=4z^2+16z^3,\\
\mathcal L_{2,4}(z)&=17z^2+51z^3,\\
\mathcal L_{3,3}(z)&=16z^2+48z^3.
\end{aligned}
\]

In particular, the maximum number of classes in an LDC-partition is four for \(K_{2,2}\), and three for every other \(K_{m,n}\) with \(m,n\ge2\). For \(N\ge7\), every maximum partition has exactly two classes meeting each bipartition side in at most one vertex; the third class is their complement. The two small classes have one of exactly three forms: (i) two singletons in the same bipartition side; (ii) one singleton and one cross-part pair; (iii) two disjoint cross-part pairs. All these maximum partitions have coalition graph a three-vertex path. The only three-class partitions with a triangular coalition graph are six for \(K_{2,3}\) and six for \(K_{3,3}\). The unique maximum partition of \(K_{2,2}\) has coalition graph a four-cycle.

## Assumptions and scope

All graphs are finite, simple, undirected, with two nonempty fixed labelled bipartition sides of sizes \(m,n\ge2\). Unordered partitions have no class labels; the vertices remain distinguishable. A coalition edge joins two distinct classes precisely if their union is locating-dominating; individual classes must fail this property. The counting variable \(z\) records the number of classes, not their sizes. The exceptional four-, five-, and six-vertex cases are included in the statement and proof; this is not a claim about stars or arbitrary multipartite graphs.

## Proof

**1. The false-twin criterion.** Denote the sides by \(A,B\). Every pair of vertices in the same side has identical open neighborhoods. Therefore an LD-set \(D\) can omit at most one vertex from each side. Conversely, if \(|A\setminus D|\le1\) and \(|B\setminus D|\le1\), then \(D\) meets both sides (because \(m,n\ge2\)). Every omitted vertex has a nonempty neighborhood in \(D\), and omitted vertices from opposite sides have different, nonempty neighborhood traces. Thus \(D\) is locating-dominating if and only if its complement is a **transversal**, namely a set meeting each side in at most one vertex. Every transversal has cardinality at most two. In particular, the minimum LD-set has \(N-2\) vertices.

**2. Possible partition sizes.** If two classes of an LDC-partition form a coalition, all remaining classes lie in the transversal complementary to their union. Hence there are at most four classes. If \(N\ge5\), four classes are impossible: take a coalition between classes \(U,V\); the other two, \(S,T\), must be singletons on opposite sides. Since \(|S\cup T|=2<N-2\), \(S\) must partner with \(U\) or \(V\); take \(U\). Then \(V\) is a singleton on the side opposite \(T\). Both \(S\) and \(V\) are consequently on the same side. The singleton \(T\) can partner neither with \(S\) nor with \(V\), since a two-vertex set cannot be locating-dominating. Partnering \(T\) with \(U\) would require \(S\cup V\) to be a transversal, a contradiction. One class is likewise impossible because the whole vertex set is locating-dominating.

**3. Two-class partitions.** For \(N\ge5\), there are \(2^{N-1}-1\) unordered two-class partitions. One class can be locating-dominating exactly when its nonempty complement is a transversal, giving \((m+1)(n+1)-1\) excluded partitions. Since two LD-sets would each require at least \(N-2\) vertices, they cannot be disjoint for \(N\ge5\); thus no exclusions are double-counted. The answer is \(2^{N-1}-(m+1)(n+1)\). Direct inspection of \(K_{2,2}\) leaves one valid two-class partition, namely its two bipartition sides.

**4. Three-class criterion.** If the classes are \(U,V,W\), the coalition \(U\cup V\) exists precisely when the complementary class \(W\) is a transversal, provided each individual class is non-LD. Hence an unordered three-class partition is admissible exactly when none of its classes is LD and at least two of its classes are transversals. Exactly two transversals give a path coalition graph; three give a triangle. For \(N\ge7\), three classes of size at most two cannot cover the vertices, so exactly two classes are transversals, and the third has at least three vertices. They can be (i) two singleton classes, both from the same side so that the remaining class is non-LD; (ii) a singleton and a cross-part pair; (iii) two disjoint cross-part pairs. These cases contribute, respectively,

\[
\binom m2+\binom n2,\qquad mn(N-2),\qquad 2\binom m2\binom n2.
\]

They are mutually disjoint and each class is non-LD. Each pair of small classes individually partners with the remaining class, so all constructions work, proving the general coefficient formula and the path assertion.

**5. The finite boundaries.** For \(N=6\), the profiles of three classes can only be \((4,1,1)\), \((3,2,1)\), or \((2,2,2)\), since at least two classes must be transversals. The first two profiles contribute \(\binom m2+\binom n2\) and \(mn(N-2)\), respectively. For \(K_{2,4}\), the last profile consists of two disjoint cross-part pairs and the two remaining vertices of the four-vertex side; there are \(2\binom22\binom42=12\) such partitions. This gives \(7+32+12=51\) three-class partitions. For \(K_{3,3}\), the last profile consists of three cross-part pairs, precisely the six perfect matchings of the bipartition. Counting each matching once gives \(6+36+6=48\) three-class partitions. The six perfect matchings produce triangles; all the other three-class cases produce paths.

For \(N=5\), necessarily \(G=K_{2,3}\). The \((3,1,1)\) profile contributes \(\binom22+\binom32=4\). For \((2,2,1)\), a singleton on the two-vertex side gives three choices for its cross-part pair and two choices for the singleton, hence six path configurations; a singleton on the three-vertex side leaves two vertices per side and gives two matchings into cross-part pairs, hence six triangular configurations. Thus there are \(4+6+6=16\) three-class partitions.

For \(N=4\), necessarily \(G=K_{2,2}\). There is one valid two-class partition (the two sides), two valid three-class partitions (keep either side together, split the other into singletons), and one valid four-class partition (all singletons). The four singleton coalition graph is \(K_{2,2}\), a cycle of length four. This completes all cases.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The checker constructs the actual open-neighborhood traces rather than using the transversal theorem. It enumerates every unordered vertex partition for all \(2\le m\le n\) with \(m+n\le10\), checks every partition against the original locating-domination definition, and compares counts and three-class coalition-graph types to the theorem. It additionally directly tests each constructed three-class family for five larger parameter pairs, including \((m,n)=(7,8)\). The final output is `VERIFY_OK`. This finite replay corroborates, but does not replace, the unrestricted proof above.

## Relationship to prior work

Chellali, Dobrynin, Foucaud, Golmohammadi, and Valenzuela-Tripodoro introduced locating-dominating coalitions and proved general bounds on the coalition number, as well as formulas for paths and cycles and certain small-order extremal graphs [1]. Their Proposition 2.8 gives \(C_L(K_{m,n})\le4\) from the known minimum LD-set size; their Proposition 4.1 already includes \(K_{2,2}\cong C_4\) among order-four extremal graphs. Those known facts are not claimed as new. The present contribution is the complete partition polynomial for every nontrivial complete bipartite graph, the classification of all maximum partitions, and the precise exceptional triangle-coalition multiplicities. Locating-dominating *domatic* partitions require every class individually to be LD and are not the coalition partitions studied here; see [2]. The literature comparison is provisional, not an independent priority certification.

## Limitations

The formula counts unordered partitions of a labelled graph, not orbits under graph automorphisms. It assumes both part sizes are at least two. No claim is made for stars, general multipartite graphs, or other coalition definitions. Only self-review has been performed; independent assessment and historical priority verification remain outstanding. The finite computational tests alone do not establish the infinite statement.

## References

[1] M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, and J. C. Valenzuela-Tripodoro, *Locating-dominating coalitions in graphs*, arXiv:2602.18760, first public version February 21, 2026, https://arxiv.org/abs/2602.18760 .

[2] F. Foucaud, P. V. Maniya, K. Paul, and D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933, first public version June 15, 2025, https://arxiv.org/abs/2506.12933 .
