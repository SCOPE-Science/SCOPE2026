# Cube-optimal Kuhn frames are oriented spanning trees

## Finding
Let \(d\geq 1\), \(C_d=[-1,1]^d\), and \(\Lambda=\mathbb Z^d\). For an unordered set \(F=\{v_1,\ldots,v_d\}\) of \(d\) linearly independent lattice vectors, consider all \(d!\) permutation simplices
\[
\Delta_\pi(F)=\operatorname{conv}\{0,v_{\pi(1)},v_{\pi(1)}+v_{\pi(2)},\ldots,\sum_{j=1}^dv_{\pi(j)}\}.
\]
Each simplex may be placed in its own translate of \(rC_d\); let \(\kappa_F(C_d)\) be the least common \(r\) permitting these placements. The known minimum over frames is \(\kappa(C_d,\mathbb Z^d)=1/2\) [1]. The new result is a **complete classification and exact count of its minimizers**:

**Theorem.** An unordered independent frame \(F\) minimizes \(\kappa_F(C_d)\) if and only if, after ordering its vectors as columns in a matrix \(M\), each ambient-coordinate row contains either exactly one nonzero entry \(\pm1\), or exactly two nonzero entries \(+1,-1\). Such a matrix is the reduced, oriented edge-incidence matrix of a spanning tree on \(d+1\) labeled vertices, with coordinate rows labeling the edges, and every minimizing frame is a lattice basis. The number of distinct unordered minimizing frames, **without quotienting by cube symmetries**, is
\[
\boxed{\ 2^d(d+1)^{d-1}.\ }
\]
For \(d=1,2,3,4\) these counts are respectively \(2,12,128,2000\). The same description holds, after changing coordinates, for a parallelotope \(AC_d\) with its matching lattice \(A\mathbb Z^d\), for any invertible real matrix \(A\).

## Assumptions and scope
The underlying norm is \(\ell_\infty\), the frame is a set of exactly \(d\) linearly independent vectors of the **integer coordinate lattice**, and every permutation simplex has an independently chosen translation. The definition is the original common-frame packet fitting radius of [1], not a radius derived from arbitrary periodic triangulations. Frames are counted as unordered sets of actual lattice vectors, with no identification under coordinate signs, permutations, or other lattice automorphisms. The empty row case is excluded by full rank.

For any ordered frame \(B=(v_1,\ldots,v_d)\) write \(M_{ij}=(v_j)_i\), and define row totals
\[
P_i=\sum_{j=1}^d\max\{M_{ij},0\},\qquad N_i=\sum_{j=1}^d\max\{-M_{ij},0\}.
\]
The stronger exact **fixed-frame formula**, used in the theorem, is
\[
\boxed{\ \kappa_B(C_d)=\tfrac12\max_{1\leq i\leq d}\max\{P_i,N_i\}.\ }
\]

## Proof
**Step 1 — radius of one simplex.** A finite set \(T\subset\mathbb R^d\) lies in a translate of \(r[-1,1]^d\) if and only if its range in every coordinate is at most \(2r\). Indeed, the product of the midpoint intervals between each coordinate minimum and maximum supplies such a translate; conversely, containment implies the range bound. Applying this to the vertices of \(\Delta_\pi(B)\) gives a radius equal to half the maximum coordinate range of its prefix sums.

**Step 2 — maximization over orders.** Fix coordinate \(i\), and abbreviate its row as \(a_j=M_{ij}\). Every difference of two prefix sums in any ordering is a sum over a contiguous block. Such a sum lies between \(-N_i\) and \(P_i\). Therefore every prefix range is at most \(\max(P_i,N_i)\). Conversely, choose a permutation that puts every positive \(a_j\) first; the prefix sums then differ by \(P_i\) between the initial vertex and the end of this positive block. Putting all negative entries first similarly achieves \(N_i\). The largest prefix range over all permutations is exactly \(\max(P_i,N_i)\). The outer maximum over coordinates commutes with the finite maximum over permutations, proving the fixed-frame formula.

**Step 3 — integrality and the optimizer condition.** Every row of an invertible integer matrix is nonzero, so its nonnegative integer totals satisfy \(\max(P_i,N_i)\geq1\). Consequently the fixed-frame radius is at least \(1/2\). The standard coordinate basis attains \(1/2\), recovering the value already given in [1]. Equality for any frame is equivalent to \(P_i\leq1\) and \(N_i\leq1\) for every row. By integrality, a nonzero row must be \(+e_j\), \(-e_j\), or \(e_j-e_k\) for distinct column indices \(j,k\). There are no other possibilities.

**Step 4 — tree equivalence and unimodularity.** Introduce a graph with vertices labeled \(0,1,\ldots,d\). Associate to \(+e_j\) or \(-e_j\) the corresponding oriented edge between the special vertex \(0\) and \(j\), and associate to \(e_j-e_k\) the oriented edge between \(j\) and \(k\). Label each edge by the coordinate-row index \(i\). The resulting \(d\times d\) matrix is precisely a reduced oriented incidence matrix, obtained by deleting the column of vertex \(0\) from the full edge-vertex incidence matrix. Its nullspace consists of assignments to nonroot vertices that, upon setting the value at the root to zero, are constant along every edge. Hence full rank is equivalent to the graph being connected. A connected graph on \(d+1\) vertices with exactly \(d\) edges is a tree. Its reduced incidence matrix has determinant \(\pm1\), by repeatedly removing a leaf distinct from the root and expanding along its single incidence entry. Thus every optimizer is a full lattice basis, despite the original definition allowing nonprimitive independent frames. Conversely, any oriented spanning tree with its edges assigned to coordinate rows constructs an invertible matrix whose rows have the permitted form, hence an optimal frame.

**Step 5 — exact enumeration.** By Prüfer-code enumeration there are \((d+1)^{d-1}\) spanning trees on the labeled vertex set \(\{0,1,\ldots,d\}\) (also valid for \(d=1\)). Assigning the \(d\) labeled coordinate rows to the tree edges contributes \(d!\) choices, and orienting the edges contributes \(2^d\). Every such choice gives an ordered column matrix, and every unordered independent frame has exactly \(d!\) distinct column orderings. Permuting the nonroot vertex labels is exactly permuting the frame columns, so division by \(d!\) counts each unordered frame once, yielding \(2^d(d+1)^{d-1}\). Applying an invertible map \(A\) transports containment, lattice frames and minimizers bijectively and proves the affine statement. \(\square\)

## Verification
The standalone `verify.py` uses only exact integer arithmetic. It exhausts every matrix of dimension \(d\leq4\) whose rows satisfy the threshold condition: the number of eligible row patterns is \(d(d+1)\), so the exhaustive search checks \(2,36,1728,160000\) matrices in successive dimensions. Their nonzero determinants are all \(\pm1\); the counts of ordered independent matrices are \(2,24,768,48000\), which equal \(d!2^d(d+1)^{d-1}\). A separate exhaustive check verifies the prefix-range lemma for every row in \(\{-2,-1,0,1,2\}^d\) for \(1\leq d\leq5\), by examining every permutation. It reports `CUBE_PACKET_EXACT_CHECKS_OK 165671`.

To reproduce, execute `python verify.py` with a standard Python 3 interpreter. Computations are finite cross-checks, not a substitute for the proof for arbitrary dimensions.

## Relationship to prior work
Xue [1] introduces the common-frame \(\kappa\)-covering invariant and explicitly computes its value \(1/2\) for standard cubes, as part of the general coordinate \(\ell_p\)-ball formula (3.2). That **numerical value is prior work**, not a new claim here. Lian and Xue [2] study related Kuhn-simplex covering criteria and prescribed-basis tests. Grozev and Nikolov [3] study parallelotope coverings using unit-cube vertices and Balitskiy's triangulation lemma, including an individual simplex containment criterion. These results motivate the fitting question but do not state the full minimizer characterization by signed tree incidence matrices, the all-dimensional basis rigidity, or the enumerator above. The classical spanning-tree enumeration and reduced-incidence unimodularity used in the proof are standard; the geometric optimality characterization is the proposed new connection.

## Limitations
The classification is for the standard cube and its **matched affine lattice** only, not for an arbitrarily fixed lattice and an unrelated parallelotope, nor for general convex bodies or other \(\ell_p\) norms. The frame count distinguishes actual vector sets and changes if symmetry classes are identified. Complete historical novelty has not been independently established; older results on integer incidence matrices, unimodular triangulations and lattice coverings could present an equivalent statement in other terms. No independent mathematical audit has been performed.

## References
1. Fei Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1, publicly posted 2026-10-28. https://arxiv.org/abs/2610.39034 ; see definition (1.1) and equation (3.2).
2. Yanlu Lian and Fei Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584v3, first posted 2026-06-12. https://arxiv.org/abs/2606.14584 ; see Theorem 1.1 and §6.
3. Dragomir Grozev and Nikolai Nikolov, *Lattice coverings by parallelotopes containing cube vertices*, arXiv:2610.21572v1, posted 2026-10-15. https://arxiv.org/abs/2610.21572 ; see Lemma 5.
4. The classical Prüfer coding of labeled trees and the elementary determinant property of reduced incidence matrices are used in standard form; their necessary parts are proved or recalled above.
