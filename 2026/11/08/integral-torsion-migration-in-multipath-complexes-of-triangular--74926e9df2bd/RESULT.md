# Integral torsion migration in multipath complexes of triangular books

## Finding
Let \(B_m\) be the undirected triangular book with vertices \(u,v,w_1,\dots,w_m\) and edges \(uv,uw_i,vw_i\) for \(1\le i\le m\). Replace each edge by both opposite directed arcs and let \(X_m\) be its multipath simplicial complex: vertices of \(X_m\) are these \(4m+2\) arcs, and a face is a subset inducing a vertex-disjoint union of directed simple paths (isolated vertices permitted). For exactly \(m\in\{3,4,5,6\}\), the integral homotopy types are
\[
\begin{aligned}
X_3&\simeq\mathbb{RP}^2\vee\bigvee^7S^2,\\
X_4&\simeq M(\mathbb{Z}/2,2)\vee\bigvee^{17}S^2,\\
X_5&\simeq M(\mathbb{Z}/2,2)\vee\bigvee^{22}S^2\vee\bigvee^{31}S^3,\\
X_6&\simeq\bigvee^{38}S^2\vee\bigvee^{169}S^3.
\end{aligned}
\]
Here \(M(\mathbb{Z}/2,2)=S^2\cup_{\deg 2}e^3\) is the degree-two Moore space. This is a complete classification for the four specified books, not an assertion for every page count. In particular, the integral homology two-torsion appears in degree one at \(m=3\), in degree two at \(m=4,5\), and is absent at \(m=6\).

## Assumptions and scope
The graph is simple before doubling its arrows. The two hubs \(u,v\) are adjacent; they are **not** merely the two vertices of the nonadjacent bipartition in \(K_{2,m}\). Paths cannot repeat vertices; the empty arc set is a face of dimension \(-1\). Every arc is incident to a hub, and any multipath contains at most four arcs: each hub has indegree at most one and outdegree at most one. All homotopy equivalences and homology are integral, and all complexes are finite.

## Proof
Number the hubs \(0,1\), leaves \(2,\dots,m+1\), and directed arcs in the order \((0,1),(1,0)\), followed for each leaf \(j\) by \((0,j),(j,0),(1,j),(j,1)\). Identify an arc subset with the bit mask of its ordered arcs. Validity is equivalent to three constraints: each vertex has indegree and outdegree at most one, and the directed graph has no directed cycle. An exhaustive depth-first enumeration maintaining incoming/outgoing bits and union-find connected components constructs **every** face; the union-find exclusion is valid because with indegree/outdegree at most one, any newly closed undirected component would be a directed cycle. A separately implemented subset enumeration corroborates these face sets and their modular homology.

For each \(m\), apply the deterministic sequence of element matchings with arc-index order specified in `verify_book.py`: whenever both a current face \(F\) not containing arc \(i\) and \(F\cup\{i\}\) remain unmatched, pair them and remove the pair from later stages. The empty-face pairing is discarded from the ordinary CW matching, leaving its paired vertex critical. All nonempty Hasse incidences are oriented downwards except these matched covers, which are oriented upwards. The verifier reconstructs **all** covers and performs a topological sort of the entire resulting directed graph; the sort visits every face in each of the four cases, certifying acyclicity of the discrete-Morse field.

The complete critical-cell counts after this construction are:

| Pages \(m\) | Faces incl. empty | Nonempty Hasse covers | Matched pairs | Critical cells by dimension |
|---|---:|---:|---:|---|
| 3 | 141 | 336 | 65 | one in 0, one in 1, eight in 2 |
| 4 | 355 | 984 | 167 | one in 0, eighteen in 2, one in 3 |
| 5 | 773 | 2340 | 358 | one in 0, twenty-three in 2, thirty-two in 3 |
| 6 | 1503 | 4812 | 647 | one in 0, thirty-eight in 2, 169 in 3 |

To calculate the integral cellular Morse differential, orient each original face by increasing arc indices. For a matched lower face \(f\) with upper mate \(U\), eliminate \(f\) using \(\partial U=\epsilon f+\sum_{g\ne f}c_g g\), where \(\epsilon=\pm1\). Recursively project \(f\mapsto-\epsilon\sum_{g\ne f}c_g\operatorname{proj}(g)\), send any matched upper face to zero, and retain critical lower faces. Acyclicity makes this recursion terminate. Applying these reductions to boundaries of every critical upper cell gives the exact **signed integer** Morse matrix; this is reproduced from scratch in `verify_book.py`.

For \(m=3\), the only nonzero Morse boundary is from eight two-cells to one one-cell. Exactly three coefficients are nonzero, each \(\pm2\); its Smith invariant is \(2\). Thus the one-skeleton is \(S^1\), and elementary integral changes of its eight attaching loops leave one degree-two attachment and seven null attachments. This CW complex is \(\mathbb{RP}^2\vee\bigvee^7S^2\).

For \(m=4\) and \(m=5\), the Morse one-skeleton is a point and the two-skeleton is a wedge of eighteen and twenty-three two-spheres respectively. By the degree-two Hurewicz isomorphism \(\pi_2(\bigvee S^2)\cong\mathbb{Z}^r\), every three-cell attaching map is determined by its integer incidence vector. For \(m=4\), the matrix has one column and eight nonzero entries \(\pm2\); for \(m=5\), the matrix has one nonzero row and twenty nonzero entries (all divisible by \(2\), with content exactly \(2\)). In each case its rank is one, and all its nonzero Smith invariants consist of a single \(2\). Integral basis changes on two- and three-cells (realized by sphere self-equivalences and cell slides) reduce the attachment to one degree-two map and leave the remaining spheres free. Hence the two Moore-space wedge decompositions above.

For \(m=6\), the CW model has 38 critical two-cells and 169 critical three-cells, and the **entire** Morse boundary is zero. All maps \(S^2\to\bigvee^{38}S^2\) are classified by their degree vectors, so every attachment is nullhomotopic, proving the stated wedge of spheres. These arguments classify homotopy types, not merely field-valued Betti numbers.

## Verification
Run `python3 verify_book.py` using Python 3 (standard library only): it enumerates every multipath, constructs and exhaustively checks the acyclic matching, recomputes all signed gradient-path reductions, checks the rank-one Smith factor \(2\) in cases \(m=3,4,5\), and checks the zero boundary for \(m=6\). Run `python3 independent_book.py` to enumerate all allowed arc subsets independently by combinations and check simplicial homology over fields of characteristics \(2\), \(3\), \(5\). Both programs must print their named success markers; `verification_output.txt` records one verified run.

## Relationship to prior work
Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670, public January 9, 2026), treat bidirected paths and single polygons, including their homotopy/homology. A triangular book with at least three pages has a shared edge and several overlapping triangles and is neither such graph. Caputi, Collari, Di Trani and Smith, *On the homotopy type of multipath complexes* (arXiv:2208.04656), treat line/polygon families, grids and certain one-direction complete-bipartite digraphs, not these fully bidirected triangular books. The edge-absent bidirected \(K_{2,m}\) complexes are distinct: adding the hub edge changes the vertex set of the simplicial complex, its incidence conditions and, at several tested page counts, the integral homology. Exact mathematical overlap was checked against relevant indexed results and available previous claims, but this is not a proof of absolute priority.

## Limitations
Only \(m=3,4,5,6\) are proved. The disappearance of torsion at \(m=6\) does not imply its absence for \(m>6\), and no equivariant splitting, naturality under inclusion, or full arbitrary-book classification is asserted. The mathematical verification is computational but exhaustive for each stated finite complex; independent expert mathematical validation has not been performed.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first submitted 2026-01-09), https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first submitted 2022-08-09), https://arxiv.org/abs/2208.04656.
