# Sharp batch-exchange thresholds and glued-cube geometry for minimum triangle transversals

## Finding

Let \(A,B,C\) be three **specified, disjoint, labelled** nonempty vertex classes with sizes \(2\le a\le b\le c\), and let \(G=K_{a,b,c}\). A *triangle edge transversal* is a set \(D\subseteq E(G)\) meeting every triangle. A maximum triangle-free spanning subgraph is \(G-D\) with \(D\) a minimum triangle edge transversal.

**Theorem (optimal-state exchange geometry, using an explicit minimum-cover description).** The minimum triangle-transversal size is \(ab\), so
\[
\operatorname{ex}(K_{a,b,c},C_3)=ac+bc.
\]
The minimum transversals, with the vertex classes fixed and labelled, are exactly:

1. **Strict largest-class inequality \(b<c\):** the single edge set \(E(A,B)\).
2. **Two equally large classes \(a<b=c\):** for each subset \(S\subseteq A\), the edge set \(E(S,B)\cup E(A\setminus S,C)\). There are exactly \(2^a\) such sets.
3. **Three equally large classes \(a=b=c=n\):** for any one of the three classes \(X\), divide \(X\) into an arbitrary subset and its complement, and delete all incident edges to one of the other classes from one subset and all incident edges to the remaining class from the complement. The three resulting families of \(2^n\) sets have pairwise intersections consisting of the corresponding full bipartite side, with no triple intersection. There are exactly \(3\cdot2^n-3\) distinct sets.

For an integer \(k\ge1\), define the *\(k\)-batch exchange graph* \(\mathcal R_k(G)\): its vertices are the minimum transversals \(D\), and distinct \(D,D'\) are adjacent exactly when \(|D\setminus D'|=|D'\setminus D|\le k\). Thus a move replaces at most \(k\) deleted edges by the same number of other deleted edges, retaining a minimum transversal at the endpoints. For every \(k< b\) in case 2, and every \(k<n\) in case 3, this graph has no edges. The first connected exchange graph is:

- In case 2, \(\mathcal R_b(G)\cong Q_a\), the \(a\)-dimensional Boolean cube, of diameter \(a\).
- In case 3, \(\mathcal R_n(G)\) consists of three copies of \(Q_n\), each pair identified at one corner, the two shared corners within each copy being antipodal. It has \(3\cdot2^n-3\) vertices, \(3n2^{n-1}\) edges, and diameter \(\lfloor3n/2\rfloor\).

The case \(b<c\) has one optimum and a one-vertex exchange graph for every \(k\).

## Assumptions and scope

All graphs are finite, simple, undirected, with their three partite classes distinguished and individual vertices labelled. The theorem concerns arbitrary integers \(2\le a\le b\le c\); it does not assert a classification for hosts with four or more partite classes. In the balanced case \(n\ge2\), all three possible choices of source class are counted before deduplication. The exchange graph is a graph **on optimal edge-deletion sets**, not on arbitrary triangle-free graphs. A move is evaluated by the number of edges restored (equally, the number newly deleted), not by the cardinality of the symmetric difference.

## Proof

**Step 1: Exact optimum and equality forcing.** Write \(d_{AB}=|D\cap E(A,B)|\), and similarly define \(d_{AC},d_{BC}\). Every one of the \(abc\) triples \((x,y,z)\in A\times B\times C\) must have at least one deleted edge. An \(AB\)-edge lies in exactly \(c\) host triangles; similarly the incidences for \(AC\) and \(BC\) are \(b\) and \(a\). Thus
\[
abc\le c d_{AB}+b d_{AC}+a d_{BC}\le c(d_{AB}+d_{AC}+d_{BC})=c|D|.
\]
Consequently \(|D|\ge ab\), attained by deleting all \(AB\)-edges. Whenever \(|D|=ab\), *both* inequalities are equalities. Hence every host triangle contains **exactly one** deleted edge, and every deleted edge lies on a side whose incidence multiplier equals \(c\).

If \(b<c\), equality permits deletions only on side \(AB\), giving \(D=E(A,B)\). If \(a<b=c\), equality forbids deletions on side \(BC\), while for each fixed \(x\in A\) the exact-one equations are
\[
1_D(xy)+1_D(xz)=1\qquad(y\in B,z\in C).
\]
Fixing one endpoint and varying the other shows that \(1_D(xy)\) is constant over all \(y\), while \(1_D(xz)\) is its complement and constant over all \(z\). Each \(x\) independently chooses a fully deleted side, yielding exactly \(2^a\) transversals.

**Step 2: Balanced equality classification.** Let \(a=b=c=n\) and write \(p(x,y)=1_D(xy)\) on \(AB\), \(q(x,z)=1_D(xz)\) on \(AC\), and \(r(y,z)=1_D(yz)\) on \(BC\). The exact-one condition says
\[
p(x,y)+q(x,z)+r(y,z)=1\quad\text{for all }x,y,z.
\]
Subtracting the equations for \(x,x'\in A\) shows that \(p(x,y)-p(x',y)\) is independent of \(y\), and its negative is \(q(x,z)-q(x',z)\), independent of \(z\). If two \(AB\) rows differ, then their constant nonzero difference is \(+1\) or \(-1\); one is identically zero and the other identically one. Every other row must also be constant, and the \(AC\) rows are complementary. Substitution yields \(r\equiv0\). This is an \(A\)-split family. If all \(AB\) rows agree but its columns differ, apply the same argument interchanging \(A\) and \(B\): the \(AB\) indicator depends only on the vertex of \(B\), the \(BC\) indicator is its complement, and \(q\equiv0\). This is a \(B\)-split family. Otherwise \(p\) is constant. If \(p\equiv1\), the other two indicators vanish: the full \(AB\) side is deleted. If \(p\equiv0\), then \(q(x,z)+r(y,z)=1\), so for each \(z\in C\), \(q(x,z)\) and \(r(y,z)\) are constant in \(x\) and \(y\) and complementary. This is a \(C\)-split family.

Every construction in these three families clearly deletes exactly one edge of every triangle and has \(n^2\) deleted edges. Each family has \(2^n\) configurations; the only intersections between two families are the three pure-side deletions \(E(A,B),E(A,C),E(B,C)\), each shared by precisely two families. Therefore the number of distinct optima is \(3\cdot 2^n-3\).

**Step 3: Batch moves.** For \(a<b=c\), two choices \(S,S'\subseteq A\) differ in \(b|S\mathbin\triangle S'|\) deleted/restored edges. Therefore no smaller batch connects different optima and \(\mathcal R_b(G)\cong Q_a\).

In the balanced case, two configurations within a fixed split family differ by \(n\) deletions/restorations for each source vertex on which their choices differ, giving a \(Q_n\) induced subgraph at batch size \(n\). To rule out other edges, consider an \(A\)-split configuration at \(p\) source vertices away from the shared pure-\(AB\) configuration, and a \(B\)-split configuration at \(q\) such vertices. A direct count by the three sides yields
\[
|D_A\setminus D_B|=n(p+q)-pq.
\]
For \(p,q\ge1\), this is at least \(2n-1>n\), because \(n\ge2\). If either parameter is zero, one configuration is the common pure-\(AB\) corner; an edge at batch size \(n\) occurs only when the other parameter is one. This shows there are no additional between-family edges, and every within-family cube has its two pure-side corners antipodal. The intersection of the cube families was established in Step 2.

**Step 4: Diameter and edge count.** Each copy of \(Q_n\) has \(n2^{n-1}\) edges; edges of distinct copies are not identified, so the total is \(3n2^{n-1}\). Distances within one cube are Hamming distances, since an excursion through the other two cubes connects its opposite shared corners with length \(2n\), versus \(n\) inside the original cube. For vertices in two different cubes, let \(s\) be the sum of their distances to their unique common corner. One path through that corner has length \(s\). The path around the third cube, via the two other shared corners, has length \(3n-s\). Hence their distance is \(\min(s,3n-s)\), with every integer \(s\in[0,2n]\) possible. Its maximum is \(\lfloor3n/2\rfloor\), larger than or equal to the internal diameter \(n\). This completes the proof.

## Verification

Run `python3 verify.py` from the same directory as this document. The checker uses only Python's standard library; it does not call an external solver or load precomputed certificates.

It tests all edge-deletion subsets up to the claimed optimum size in \(K_{2,2,2}\), \(K_{2,2,3}\), \(K_{2,2,4}\), \(K_{2,3,3}\) and \(K_{2,3,4}\), a total of \(405579\) candidate subsets. It separately enumerates every balanced exact-one solution for \(n=2,3,4\) using the \(AB\)-indicator matrix and solving the remaining forced binary equations. It independently constructs every balanced optimum for \(2\le n\le7\), computes the \(n\)-batch exchange graph and its all-pairs graph distances, and checks four unequal examples with two tied largest classes. Expected final output is `VERIFY_OK`.

These computations are finite cross-checks; the proof above establishes the result for all allowed class sizes.

## Relationship to prior work

Zhao and Li (arXiv:2611.08547, first public 2026-11-05), Theorem 2, give the general edge-regular girth-cycle upper bound \(\operatorname{ex}(K_{n,n,n},C_3)\le2n^2\). This agrees with the balanced value here, but does not describe optimal spanning subgraphs or exchange geometry, and does not determine the unbalanced three-class phase transition.

Amarnani, De Burgos, and Broughton (arXiv:2307.08824, first public 2023-07-17) prove a triangle-packing/transversal min-max theorem for all bilaterally-complete tripartite graphs. Their Section 2 parametrizes **all** triangle transversals via arbitrary deleted edges on one side and vertex covers on the other sides; the listed minimum-cover families can be obtained by specializing that framework to a complete tripartite host and imposing equality. We do **not** claim that this optimizer classification is independent of, or historically novel relative to, that known more-general parametrization. The new contribution here is the exact metric graph on all optimum covers under bounded atomic edge exchanges: its sharp first nontrivial batch threshold, the three-glued-cube structure in the balanced regime, and the exact distance diameter. The inspected source does not discuss these exchange graphs. The earlier minimum-cover equality is also credited to Lakshmanan, Bujtás, and Tuza (2012). The independent new claim is the *sharp optimum-preserving batch-reconfiguration geometry* derived from those minimum-cover families, not the scalar optimum or the general triangle-transversal parametrization.

## Limitations

The classification is only for exactly three nonempty classes of sizes at least two; do not infer its counts for four or more classes. The exchange move permits simultaneous equal-size replacement batches at the endpoints; it does not require valid intermediate minimum transversals during an atomic batch. No independent external mathematical audit has been performed. Prior literature may contain unindexed equivalent exchange-graph theorems, especially in papers on packing/covering triangle transversals; the 2012 paper's full text was not accessible in this review, so priority remains provisional.

## References

1. S.-L. Zhao and Y.-Q. Li, *Upper bound on the size of subgraphs avoiding cycles of girth length in graphs*, arXiv:2611.08547v1 (2026-11-05), https://arxiv.org/abs/2611.08547.
2. N. Amarnani, A. De Burgos and W. J. Broughton, *Packing and Covering Triangles in Bilaterally-Complete Tripartite Graphs*, arXiv:2307.08824v1 (2023-07-17), https://arxiv.org/abs/2307.08824; journal version: *Graphs and Combinatorics* (2024).
3. S. Aparna Lakshmanan, Cs. Bujtás and Zs. Tuza, *Small Edge Sets Meeting all Triangles of a Graph*, *Graphs and Combinatorics* 28 (2012), 381–392, https://doi.org/10.1007/s00373-011-1048-8.
