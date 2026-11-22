# Complete largest-simplex locus and four-volume spectrum of the orthogonal double pentagon

## Finding
Let \(A_i=(\cos(2\pi i/5),\sin(2\pi i/5),0,0)\) and \(B_j=(0,0,\cos(2\pi j/5),\sin(2\pi j/5))\) for \(i,j\in\{0,1,2,3,4\}\), and put \(P=\operatorname{conv}(\{A_i\}\cup\{B_j\})\). Among **all** four-dimensional simplices with five arbitrary points in \(P\) as vertices, the exact largest four-volume is
\[
 M=\frac{5(1+\sqrt5)}{192},\qquad
 \frac{M}{\operatorname{vol}_4(P)}=\frac{\sqrt5}{25}.
\]
Among the \(\binom{10}{5}=252\) unordered five-element subsets of the distinguished vertices, the complete simplex-volume spectrum, including degeneracies, is

| Four-volume | Number of vertex subsets |
|---|---:|
| \(0\) | 52 |
| \(5(\sqrt5-1)/192\) | 50 |
| \(5/96\) | 100 |
| \(5(1+\sqrt5)/192\) | 50 |

The 50 vertex-supported maximizers are exactly the sets comprising three vertices forming a *large* triangle of one regular pentagon and an **adjacent pair** of the other pentagon, together with the interchanged choices of factors. Here a large pentagon triangle is any rotation of the index triple \(\{0,1,3\}\).

More strongly, modulo permuting the five simplex vertices, the **entire** maximizing locus is a connected, one-dimensional trivalent graph. Its 50 nodes are the vertex-supported maximizers; its 75 edges are precisely the continuous families obtained by moving exactly one simplex vertex along a segment joining two distinguished vertices while fixing the other four. There are no other maximizing simplices, no two-parameter maximizing families, and no isolated nonvertex maximizers. Exactly 25 family edges move between the two compositions (three \(A\)-vertices versus three \(B\)-vertices), and 50 remain within one composition.

## Assumptions and scope
The ambient metric is ordinary Euclidean four-volume in \(\mathbb R^4\). All ten points are distinct, all selected five-point maximizers are nondegenerate, and interior points of \(P\) are **allowed**. Equalities are statements about unordered geometric simplices, without identifying distinct simplices under any isometry. The full four-volume of the containing body is \(\operatorname{vol}_4(P)=25(5+\sqrt5)/192\), as established independently for this body in the cited ten-vertex extremal-volume paper.

## Proof
**Step 1: determinant factorization.** Put \(s=\sin(2\pi/5)\) and \(t=\sin(\pi/5)\). For a five-subset consisting of \(A_i,A_j,A_k\) in increasing index order and \(B_l,B_m\), expansion of the affine \(5\times5\) determinant by the two orthogonal coordinate blocks gives
\[
 24\operatorname{vol}_4\bigl(\operatorname{conv}(A_i,A_j,A_k,B_l,B_m)\bigr)
 = 2\operatorname{area}(A_iA_jA_k)\,|\det(B_l,B_m)|.
\]
The analogous identity holds for a two/three split. Any other split has affine rank at most three and hence zero four-volume. The regular pentagon has five triangles of area \(T_+=(s+2t)/2\) (the large class), and five of area \(T_-=s-t/2\); its ten pairs have \(\lvert\det\rvert=s\) for adjacent pairs and \(t\) for diagonal pairs, each occurring five times. The four products divided by \(12\) satisfy
\[
 \frac{T_+s}{12}=\frac{5(1+\sqrt5)}{192},\quad
 \frac{T_-t}{12}=\frac{5(\sqrt5-1)}{192},\quad
 \frac{T_+t}{12}=\frac{T_-s}{12}=\frac5{96}.
\]
Thus in each of the two choices of a three-vertex factor there are 25 maxima, 25 minima among positive volumes, 50 intermediate volumes, and 26 degeneracies, yielding the table. The large triangles are exactly the rotations of \(\{0,1,3\}\), equivalently \(\{013,023,024,124,134\}\) in compressed index notation. In particular the vertex maximum is \(M\). Division by the known volume of \(P\) gives the stated fraction.

**Step 2: the global bound and equality support rule.** For arbitrary \(x_0,\ldots,x_4\in P\), write \(x_r=\sum_v\lambda_{r,v}v\) with \(\lambda_{r,v}\ge0\) and \(\sum_v\lambda_{r,v}=1\). The signed affine determinant \(D(x_0,\ldots,x_4)\), divided by \(4!\), is separately affine in each argument, hence
\[
 D(x_0,\ldots,x_4)
 =\sum_{v_0,\ldots,v_4}\Bigl(\prod_{r=0}^4\lambda_{r,v_r}\Bigr)D(v_0,\ldots,v_4).
\]
Every vertex tuple has signed determinant in \([-24M,24M]\), including repeated vertices which give zero. Hence \(|D|\le24M\). Equality holds **if and only if** every tuple with positive product of weights has the same extreme signed determinant \(+24M\) (or all \(-24M\)). This is a necessary and sufficient condition, not a mere local stationarity test.

**Step 3: exact endpoint compatibility and nonvertex classification.** Label the ten distinguished vertices \(0,\ldots,9\), with \(0,\ldots,4\) representing \(A\) and \(5,\ldots,9\) representing \(B\). The signed determinant of an increasing-index extremal quintuple is determined by the orientation of its two-vertex factor: positive if the difference of its two increasing indices is one or two, negative if three or four. Swapping positions flips the sign. This follows from the determinant factorization and the positive orientation of increasing pentagon triangle triples. For each of the 50 maximum five-subsets, inspect replacing exactly one of its five entries with one of the five unused labels while retaining the original positional ordering and the determinant sign. Exactly three such single replacements preserve the extreme signed determinant, each in a **different** simplex position; no pair of these replacements performed simultaneously preserves that sign. The complete finite verification is supplied by `verify_pentagon_simplex.py`. It checks every one of the 50 representative quintuples using only cyclic adjacency, the five large-triangle triples, and permutation parity, so no numerical sign tolerance enters the classification. Equivalently, one can check the reference quintuple \((0,1,3,5,6)\), with allowed changes \(0\mapsto4\), \(1\mapsto2\), and \(3\mapsto8\), and transfer this calculation through the dihedral symmetries of both pentagons and exchange of the two orthogonal planes; these symmetries act transitively on the 50 maximum subsets.

By the equality support rule in Step 2, more than one nontrivial coordinate support would require a same-sign extreme determinant after simultaneous replacements, which was just excluded. Thus at most one simplex vertex can be non-distinguished, and its support consists of the two endpoints of **one** of the three allowed replacement segments. Conversely, determinant affinity proves every point on each such segment attains volume \(M\). Every one of the 50 vertex maximizers has exactly three incident segment families. Each family is counted twice at its two endpoints, so there are \(50\cdot3/2=75\) distinct families. The checker additionally establishes 25 inter-composition and 50 same-composition edges and a single connected component; the interiors of distinct families cannot coincide, since a nondegenerate simplex has a unique five-vertex set. This proves the graph description and exhaustiveness.

## Verification
Run the self-contained standard-library Python 3 script `python3 verify_pentagon_simplex.py`. The checker enumerates all 252 five-subsets, derives every volume class from exact combinatorial formulas, checks all same-sign one-coordinate and two-coordinate replacements, and counts the 75 maximal segment families, including their composition types. All assertions passed. An independent floating-coordinate computation of the 252 direct \(4\times4\) determinants agreed with the exact symbolic levels to within \(10^{-12}\), and numerical convex-hull four-volume agreed with the reference volume. The analytic multilinearity argument, not finite sampling of interior points, is what proves the assertion for **all** interior points.

## Relationship to prior work
Csaba Medgyes determined the unique maximizing ten-vertex spherical four-polytope and its exact body volume (arXiv:2611.14674v1, Theorem 4.5). This construction is exactly that body. The original theorem does **not** give a largest contained four-simplex, its complete vertex-quintuple spectrum, or its 75 continuous maximizing families. The preceding nine-vertex paper (arXiv:2611.10078v1) studies a square–pentagon orthogonal join, proving the containing-polytope volume; a separately available nine-vertex four-simplex spectrum is a closely related but different geometric object. The present claim specifies the ten-vertex double pentagon and includes nonvertex optimizer rigidity, not a repackaging of the ambient volume optimum.

## Limitations
This result does not identify the largest contained simplex in arbitrary ten-vertex four-polytopes, nor does it optimize the simplex-to-body-volume ratio over other polytopes. It classifies four-simplices *within the fixed double-pentagon polytope only*. The proof treats continuously varying vertex locations by multi-affine extremality; the finite checker certifies a discrete compatibility table and is not by itself a proof over the continuum. Prior-art search is substantial but cannot exclude all unpublished or unindexed computations. No independent mathematical audit has been performed.

## References
- C. Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1 (first posted 2026-11-10), https://arxiv.org/html/2611.14674v1 . Relevant: Section 2.3 and Theorem 4.5.
- C. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (first posted 2026-11-06), https://arxiv.org/html/2611.10078v1 . Relevant: Sections 3 and 5, Theorem 7.1.
- *The five-level four-simplex spectrum of the extremal nine-vertex four-polytope* (published mathematical finding, 2026-11-17). This is a distinct nine-vertex square–pentagon comparator, not the ten-vertex theorem proved here.
