# A parity-sharp Euclidean diameter and complete antipodal-pair census for complete acyclic flow polytopes

## Finding

Let \(F_N\) be the polytope of nonnegative unit flows from the first to the last vertex of the transitively oriented complete graph on \(N\geq3\) ordered vertices, equipped with the ordinary Euclidean metric in its full directed-edge coordinate space. Its **exact squared Euclidean diameter** is

\[
\operatorname{diam}_2(F_N)^2=N+\left\lfloor\frac{N-3}{2}\right\rfloor=\left\lfloor\frac{3(N-1)}2\right\rfloor.
\]

Every diametral pair consists of two distinct directed source-to-sink path indicator vectors. An unordered pair of paths is diametral **if and only if** (i) every internal vertex belongs to at least one path, (ii) their common internal vertices form a maximum independent set among the ordered vertices \(3,\dots,N-2\), and (iii) every other internal vertex belongs to exactly one of the paths. Thus the number of unordered diametral pairs is

\[
A_N=\begin{cases}
2^{k-1},&N=2k+1,\\
(k-1)2^{k-1},&N=2k.
\end{cases}
\]

The odd formula holds for \(k\ge1\) and the even formula for \(k\ge2\). These are **all** maximizers, including among nonvertex points of the continuous polytope. In particular the odd-order common-vertex core is forced, while in even order there are \(k-1\) possible maximum cores.

## Assumptions and scope

Fix \(N\ge3\). Let \(K_N^{\uparrow}\) be the acyclic directed graph on \(\{1,\ldots,N\}\) with an arc \((i,j)\) for every \(i<j\). In \(\mathbb R^{\binom N2}\), let \(F_N\) consist of arc-coordinate vectors \(f\ge0\) with net outflow one at vertex \(1\), net inflow one at vertex \(N\), and zero netflow at all other vertices. The norm is the standard edge-coordinate \(\ell_2\) norm; it is **not** the Euclidean norm of an alternative permutation-matrix realization. A directed path is determined by the increasing list of internal vertices it visits. Its vector is \(\mathbf1_{E(P)}\).

For \(N=3\), the admissible common-internal-vertex set is empty; for \(N=4\), it is empty as well. Whenever a range of vertices has its starting index above its ending index, interpret it as empty. The maximum independent set in the path induced by \(\{3,\ldots,N-2\}\) has size \(\lfloor(N-3)/2\rfloor\), including these two boundary cases.

## Proof

**Path vertices.** Any nonnegative unit flow on a finite directed acyclic graph decomposes into a convex combination of source-to-sink path flows: repeatedly follow a positive outgoing arc from the source, use flow conservation to continue, and subtract the minimum flow on that path. Conversely, every zero-one path vector is an extreme point: if it is a proper convex combination of zero-one path vectors, coordinates equal to zero or one force every constituent to agree with it on every arc. Thus the vertices of \(F_N\) are exactly the path indicators. Since squared Euclidean distance is strictly convex in either argument separately, all farthest pairs in \(F_N\times F_N\) are vertex pairs.

**Distance identity.** For two paths \(P,Q\), the squared distance of their indicator vectors is \(|E(P)\triangle E(Q)|=|E(P)|+|E(Q)|-2|E(P)\cap E(Q)|\). Write \(S,T\subseteq\{2,\dots,N-1\}\) for their internal vertex sets. If an internal vertex \(i\notin S\cup T\), insert it into the first path, replacing its unique edge \((a,b)\) with \((a,i),(i,b)\). The second path avoids \(i\), so neither new edge occurs in it. The symmetric-difference cardinality rises by one if \((a,b)\) was private, and by three if it was common. Consequently every maximizing pair has \(S\cup T=\{2,\dots,N-1\}\).

For such a pair, write \(C=S\cap T\). A shared edge can only join numerically consecutive vertices \(j,j+1\), since otherwise the intervening vertex (present in the union) would force one of the paths to break the edge. Its two endpoints must belong to both paths, where the endpoints \(1,N\) are included in both by convention. Therefore the number \(c\) of shared edges is exactly the number of adjacent common-vertex pairs along the ordered path \(1,2,\dots,N\), and

\[
\|\mathbf1_{E(P)}-\mathbf1_{E(Q)}\|_2^2=N+|C|-2c.
\]

If any two adjacent ordered vertices are common, at least one is internal. Remove that internal vertex from the first path, but retain it in the second. This removes one path edge overall and at least one shared edge; the new bypassing edge cannot belong to the second path because that path still visits the removed vertex strictly between the bypass edge endpoints. Hence the squared distance increases by at least one. Every diametral pair therefore has \(c=0\). In particular \(2\) and \(N-1\) cannot be common, and \(C\) is an independent subset of \(\{3,\dots,N-2\}\). Conversely every such independent common set and every assignment of all remaining internal vertices to exactly one path yields \(c=0\) and distance \(N+|C|\).

The largest independent set in a linear path on \(N-4\) vertices has \(\lfloor(N-3)/2\rfloor\) members. This proves the diameter formula and all equality conditions. The cases \(N=3,4\) follow directly from the empty permitted common set.

**Exact pair count.** Put \(N=2k+1\). Among \(3,\dots,N-2\) there are \(2k-3\) vertices and exactly one maximum independent set, the alternating set containing both its endpoints (for \(k=1\), the permitted set is empty and unique). There are exactly \(k\) remaining private internal vertices, each assigned to either \(P\) or \(Q\). Swapping the labels identifies two ordered assignments; because the paths differ, this yields \(2^{k-1}\) unordered pairs. Put \(N=2k\), \(k\ge2\). The \(2k-4\) eligible vertices form a path with exactly \(k-1\) independent sets of maximum size \(k-2\), by the standard gap-placement count \(\binom{(2k-4)-(k-2)+1}{k-2}=k-1\). Again there are \(k\) private vertices, so the total is \((k-1)2^{k-1}\). The common set is recovered uniquely from each pair, hence no double counting between cores. This completes the proof.

## Verification

The included `flow_diameter_checker.py` independently encodes each arc as a bit in a complete ordered graph and exhaustively compares all unordered pairs of path vertices for \(3\le N\le13\), covering 2,794,155 unordered pairs. It checks both the distance maximum and the exact equality classification/count. It also checks 4,800 random pairs for larger orders up to \(N=200\), with a fixed seed. The analytic path-replacement and independent-set argument, not finite testing, proves the assertions for every integer \(N\ge3\).

To reproduce: `python3 flow_diameter_checker.py`. The expected final line begins with `ORDERED_FLOW_DIAMETER_PASS`.

## Relationship to prior work

Dugan's preprint *On the f-vectors of flow polytopes for the complete graph* (first posted September 23, 2024; arXiv:2409.15519v1) studies exactly the relevant complete directed flow family, gives its face-enumeration framework, and in Proposition 5.1 recovers the known path-vertex bijection. Its main theorems determine face numbers, not Euclidean lengths between vertices or the classification of diametral path pairs. The earlier Chan–Robbins–Yuen and Corteel–Kim–Mészáros studies focus on volume and lattice enumeration. The separate shortest-path-polytope literature on *monotonic diameter* concerns paths in the polytope's one-skeleton, a different metric. Related recorded results on Euclidean **inballs** and Minkowski asymmetry of directed flow polytopes do not determine maximum pairwise Euclidean chords. No claim of exhaustive historical priority is made.

## Limitations

The theorem uses the full arc-coordinate Euclidean metric and the complete **transitive** orientation, with unit netflow from first to last. It does not assert a corresponding formula for arbitrary directed acyclic graphs, other netflows, or the different ambient Euclidean metric after an affine identification with a permutation-matrix polytope. Exhaustive and randomized computations are corroborations, not infinite certificates. The independent mathematical audit and any comprehensive historical priority assessment remain outstanding.

## References

1. William T. Dugan, *On the f-vectors of flow polytopes for the complete graph*, arXiv:2409.15519v1 (September 23, 2024), https://arxiv.org/abs/2409.15519 ; later Canadian Journal of Mathematics, DOI:10.4153/S0008414X2510151X.
2. Clara S. Chan, David P. Robbins, David S. Yuen, *On the Volume of a Certain Polytope*, Experimental Mathematics 9 (2000), 91–99, DOI:10.1080/10586458.2000.10504639.
3. Sylvie Corteel, Jang Soo Kim, Karola Mészáros, *Flow polytopes with Catalan volumes*, Comptes Rendus Mathématique 355 (2017), 248–259, DOI:10.1016/j.crma.2017.01.007.
4. *The monotonic diameter of the perfect matching and shortest path polytopes*, Discrete Applied Mathematics (1992), DOI:10.1016/0167-6377(92)90018-X, for the distinct one-skeleton metric.
