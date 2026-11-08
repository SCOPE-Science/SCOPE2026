# Parity classification and topology of geodesic shattering on finite cycles

## Finding
Let \(C_n\) be the simple cycle on \(n\ge3\) vertices, with every edge of length one. Let \(\mathscr P_n\) consist of the **vertex sets of every shortest path between any pair of vertices**, retaining both paths when the endpoints are antipodal; a singleton is also a shortest path. A support \(S\subseteq V(C_n)\) is VC-shattered when each subset of \(S\) is the trace of some member of \(\mathscr P_n\). Let \(\Delta_n\) be the simplicial complex of shattered supports.

**Exact classification.** Every support of size at most two is shattered. A three-point support is shattered if and only if \(n\) is even and the support contains an antipodal pair. No support of size at least four is shattered. In particular,
\[
\Phi_n(z)=1+nz+\binom n2z^2+
\begin{cases}
0,&n\text{ odd},\\
\dfrac{n(n-2)}2z^3,&n\text{ even},
\end{cases}
\qquad
\operatorname{VCdim}(\mathscr P_n)=
\begin{cases}2,&n\text{ odd},\\3,&n\text{ even}.
\end{cases}
\]

**Homotopy classification.** The geometric realization of the full shattered-support complex satisfies
\[
|\Delta_n|\simeq
\begin{cases}
\displaystyle\bigvee^{\binom{n-1}{2}}S^1,&n\text{ odd},\\[5pt]
\displaystyle\left(\bigvee^{\binom{m-1}{2}}S^1\right)
\vee\left(\bigvee^{\binom m2}S^2\right),&n=2m\ge4.
\end{cases}
\]
Here a wedge with zero summands is a point. These formulas determine the integral homology groups without torsion.

## Assumptions and scope
The ground set is the **vertices** of an unweighted, undirected, simple cycle. The hypotheses are actual shortest **paths**, not geodesically convex vertex sets, graph balls, shortest walks, arbitrarily chosen unique representatives, or unions of paths. All tied shortest paths are included. Distances are graph distances. The statement applies to every integer \(n\ge3\); no limiting argument or generic-position assumption is used.

For even \(n=2m\), an antipodal pair is a pair of vertices at distance \(m\). A path has at most \(\lfloor n/2\rfloor\) edges, and whenever the distance between its endpoints is strictly less than \(n/2\), the shortest path is unique.

## Proof
**1. All pairs.** A singleton is realized positively by its one-vertex path and negatively by a different singleton. For two distinct vertices \(u,v\), a shortest \(u\)-to-\(v\) path realizes the positive-positive trace; their singleton paths realize the two mixed traces, and a singleton at a third vertex realizes the empty trace. Thus every one- and two-element support is shattered.

**2. Necessity for triples.** Suppose \(S=\{a,b,c\}\) is shattered. In particular, some shortest path \(P\) contains all three points, say in path order \(a,b,c\). The subpath from \(a\) to \(c\) is shortest. If its length were strictly less than \(n/2\), the cycle would have a unique shortest path from \(a\) to \(c\), and it would contain \(b\). Every shortest path containing both \(a,c\) contains their unique shortest subpath, so the trace \(\{a,c\}\) that excludes \(b\) would be impossible. Therefore the distance from \(a\) to \(c\) is exactly \(n/2\), which requires even \(n\) and an antipodal pair.

**3. Sufficiency for triples.** Let \(n=2m\), and choose antipodes \(a,c\) and another vertex \(b\). Exactly one of the two \(m\)-edge semicircular geodesics joining \(a\) and \(c\) has \(b\) in its interior. That semicircle realizes the full trace; the opposite semicircle realizes \(\{a,c\}\). Its two proper subpaths from \(a\) to \(b\) and from \(b\) to \(c\) realize \(\{a,b\}\) and \(\{b,c\}\). Singletons realize the three one-point traces. Since \(n\ge4\), a singleton outside \(S\) realizes the empty trace. Hence this triple is shattered.

**4. No four-point support.** If four vertices were shattered, some shortest path \(P\) would contain all four; write them \(a,b,c,d\) in path order. The segment of \(P\) from \(b\) to \(d\) has strictly fewer than \(\lfloor n/2\rfloor\) edges, so it is the unique shortest path from \(b\) to \(d\) and contains \(c\). Every shortest path containing both \(b\) and \(d\) must therefore contain \(c\), excluding the trace \(\{b,d\}\). This is a contradiction. By downward closure of shattering, no larger support is shattered.

**5. Coefficients.** There are \(n\) singletons and \(\binom n2\) pairs. If \(n=2m\), the \(m\) disjoint antipodal pairs each extend to a shattered triple by choosing any of the other \(n-2\) vertices. A triple cannot contain two distinct antipodal pairs. Consequently there are exactly \(m(n-2)=n(n-2)/2\) shattered triples. Odd cycles have none. This proves the polynomial and the VC dimensions.

**6. Topology in odd order.** If \(n\) is odd, \(\Delta_n\) is the complete graph \(K_n\), regarded as a one-dimensional simplicial complex. A connected graph with \(n\) vertices and \(\binom n2\) edges is homotopy equivalent to a wedge of \(\binom{n-1}{2}\) circles.

**7. Topology in even order.** Let \(n=2m\) and partition the vertices into the \(m\) antipodal edges \(E_1,\ldots,E_m\), each edge here meaning a pair in the support complex, not necessarily an edge of the original cycle. For each unordered pair \(i<j\), the four vertices of \(E_i\cup E_j\) span a tetrahedral boundary in \(\Delta_n\): each of its four triangular faces contains one of these antipodal pairs. Conversely, every triangle of \(\Delta_n\) belongs to exactly one such tetrahedral boundary. The full one-skeleton is \(K_{2m}\).

Remove the interior of exactly one triangular face from each such tetrahedral boundary, retaining every edge, and call the resulting two-dimensional subcomplex \(X_0\). Each four-vertex tetrahedral boundary minus one open face is a closed topological disk \(D_{ij}\). Its intersections with other such disks are exactly the shared antipodal edges \(E_i\) or \(E_j\), when the index pairs have a common index; otherwise they are disjoint.

Contract each of the \(m\) pairwise disjoint matched edges \(E_i\) to a point. Contracting a contractible CW subcomplex is a homotopy equivalence, one edge at a time. Every disk \(D_{ij}\) remains a disk with two distinguished boundary points \(i,j\), and different disks now meet only at those distinguished vertices. Deformation-retract each disk, fixing the two boundary vertices, onto an embedded arc from \(i\) to \(j\). The result is the complete graph \(K_m\). Hence \(X_0\simeq K_m\simeq\bigvee^{\binom{m-1}{2}}S^1\).

The removed triangular face for \(i<j\) attaches to \(X_0\) along its boundary, which is null-homotopic because it bounds the complementary three-face disk \(D_{ij}\). Attaching one two-cell along a null-homotopic loop wedges on one \(S^2\). The \(\binom m2\) distinct missing faces therefore contribute exactly that many independent sphere summands. This establishes the stated homotopy equivalence.

## Verification
A standalone checker, `check_geodesic_cycles.py`, independently enumerates every shortest path using both cycle arcs whenever their lengths tie, computes every Boolean trace on every support of sizes one through four, and compares each support with the classification above. For \(3\le n\le18\) it also builds the shattered-support boundary matrices and checks the predicted first and second mod-two Betti numbers by exact binary Gaussian elimination. Execute `python3 check_geodesic_cycles.py`. The accompanying `check_output.txt` records the successful run. These finite checks corroborate the universal mathematical proof; the homotopy type and integral torsion statement follow from the explicit disk decomposition, not from mod-two enumeration.

## Relationship to prior work
Abraham, Delling, Fiat, Goldberg and Werneck prove VC dimension at most two for **unique-shortest-path** systems. Deng, Gao, Upadhyay and Wang revisit shortest-path range spaces under a uniqueness assumption, primarily for edge-range privacy queries; Section 6 of their 2023 paper explicitly uses uniqueness in its VC-dimension-two discussion. The present family includes **all** tied geodesics and uses vertex rather than edge queries. On an even cycle, antipodal pairs have two shortest paths, so the unique-path hypothesis is inapplicable and the sharp extra layer of triangles can appear. Their arguments do not enumerate the shattered supports or determine the topology presented here.

The set of all cyclic arcs, the set of all graph balls, and geodesically convex subsets of a cycle are also different hypothesis classes: they generally include arcs not restricted to shortest paths or contain a full-cycle hypothesis. An upper bound of three for unrestricted circular arcs does not imply the parity-sensitive enumeration or the described homotopy type.

## Limitations
The result concerns unweighted simple cycles and vertex-set paths with **every tie retained**. Choosing one shortest path per endpoint pair, allowing arbitrary paths, using weighted edges, or querying edges rather than vertices changes the hypothesis family and may change every coefficient. This work does not compute Littlestone dimension, does not claim a general graph-class classification, and does not assert exhaustive historical priority. No independent mathematical audit has been performed.

## References
1. C. Deng, J. Gao, J. Upadhyay, C. Wang, *Differentially Private Range Query on Shortest Paths*, arXiv:2212.07997 (first public posting 2022-12-15); WADS 2023, Section 6. https://arxiv.org/abs/2212.07997 ; full WADS text: https://sites.rutgers.edu/jie-gao/wp-content/uploads/sites/375/2023/09/DP-Range-shortest-path.pdf
2. I. Abraham, D. Delling, A. Fiat, A. V. Goldberg, R. F. Werneck, *VC-Dimension and Shortest Path Algorithms*, ICALP 2011, 690–699, Theorem 2. https://doi.org/10.1007/978-3-642-22006-7_58
3. C. J. Zhu, K.-Y. Lam, J. K. Y. Ng, J. Bi, *On the VC-Dimension of Unique Round-Trip Shortest Path Systems*, Information Processing Letters 145 (2019), 1–5. https://doi.org/10.1016/j.ipl.2019.01.001
