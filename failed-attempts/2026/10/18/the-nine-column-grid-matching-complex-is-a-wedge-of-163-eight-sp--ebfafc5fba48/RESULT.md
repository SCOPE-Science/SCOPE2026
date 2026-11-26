# The nine-column grid matching complex is a wedge of \(163\) eight-spheres

## Finding
Let \(G=P_3\square P_9\) be the Cartesian three-row, nine-column grid, and let \(\mathcal M(G)\) be its simplicial matching complex. There is an integral homotopy equivalence
\[
\mathcal M(G)\simeq\bigvee^{163}S^8.
\]
In particular, \(\widetilde H_8(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{163}\), all other reduced integral homology vanishes, and there is no torsion. The statement concerns this precise finite grid, not arbitrary widths.

## Assumptions and scope
The vertex set of \(G\) is \(\{(r,c):0\le r<3,\ 0\le c<9\}\); edges join vertices at Manhattan distance one. Its \(42\) graph edges are ordered column-first: in each column the two vertical edges come first, followed by that column's three rightward edges if a following column exists. A simplex of \(\mathcal M(G)\) is any set of pairwise vertex-disjoint graph edges. It has \(7{,}594{,}361\) faces counting the empty face, as independently checked by a width-three transfer recurrence.

## Proof
**1. Construct an acyclic matching tree.** Work in the line graph, with the ordered \(42\) grid edges as vertices. A node specifies an independent set already forced and an allowed vertex set \(A\), disjoint from that forced set and its neighbors. Choose an allowed pivot \(p\) of minimum degree within \(A\); among tied pivots maximize the sum of their neighbors' degrees within \(A\), and finally choose the smallest edge index. If an isolated pivot exists, choose the first isolated pivot. For faces selecting no neighbor of \(p\) within \(A\), pair the two faces differing by \(p\). Every remaining face omits \(p\) and selects some neighbor of \(p\). Split these faces according to their smallest selected neighbor \(q\), using increasing edge index. In the child for \(q\), force \(q\), and delete from \(A\) the pivot, \(q\), the earlier neighbors of \(p\), and all neighbors of \(q\). Recurse. If \(A\) is empty, the forced set is critical.

This pairs each noncritical face exactly once. To prove acyclicity rather than infer it from a count: at any node, an upward matched step never changes whether its face belongs to the toggleable class or to one of the ordered first-neighbor branches. An unmatched downward step can move from a branch only to a later branch or to the toggleable class, never in the reverse direction; from the toggleable class it cannot reach a branch. Therefore a directed gradient cycle would have to lie within one class. The toggleable class is paired by one vertex and has no gradient cycles, while the branches are acyclic inductively. The same argument applies at every finite depth. The empty face is paired with one vertex in the augmented matching; when the empty face is omitted, retain that vertex as one critical zero-cell.

The fully specified deterministic tree yields exactly \(182\) critical cells of dimension \(8\) and \(19\) critical cells of dimension \(9\), as well as the critical zero-cell. No other cells are critical.

**2. Compute the signed Morse boundary.** Orient every simplex by increasing edge index. For a codimension-one face \(\sigma\subset\tau\), let \(\varepsilon(\sigma,\tau)=(-1)^j\), where \(j\) is the zero-based position of the deleted edge in \(\tau\). In computing the reduced boundary of a critical nine-cell, a critical eight-face contributes its basis vector; an eight-face that is the upper member of a lower-dimensional pair contributes zero. If an eight-face \(\sigma\) is the lower member of the pair \((\sigma,\tau)\), substitute
\[
R(\sigma)=-\varepsilon(\sigma,\tau)^{-1}
\sum_{\substack{\sigma'\subset\tau\\\sigma'\ne\sigma}}\varepsilon(\sigma',\tau)R(\sigma').
\]
Acyclicity makes the recursion terminating. The resulting integral cellular boundary is a \(182\)-by-\(19\) matrix with \(159\) nonzero entries, each of absolute value at most \(2\). Its ordered critical-cell masks and every nonzero matrix entry appear in the accompanying exact certificate.

**3. Exhibit integral unimodularity.** In the certificate's zero-based row ordering, the rows
\[
(0,6,7,17,19,31,32,33,46,47,48,50,59,61,76,77,78,95,107)
\]
form a square \(19\)-by-\(19\) submatrix with determinant \(+1\). This is checked exactly by fraction-free integer elimination. Thus the boundary map has rank \(19\) and a primitive image. Equivalently, its nonzero Smith invariants are all \(1\).

**4. Recover homotopy, not merely homology.** The acyclic matching supplies a CW model with one zero-cell, \(182\) eight-cells and \(19\) nine-cells. A map from an eight-sphere to a wedge of eight-spheres is classified by its degree vector, since \(\pi_8(\bigvee S^8)\) is free on the wedge inclusions. The displayed unimodular minor permits integral basis changes in the eight-cell attaching degrees and elementary cancellation of the \(19\) nine-cells against \(19\) eight-cells. The remaining CW model is a wedge of \(182-19=163\) eight-spheres.

## Verification
Run `python verification/verify.py` with Python 3.10 or later; no external packages are required. The checker regenerates the full matching-tree policy, the critical-face lists, every signed Morse boundary column and the determinant-one submatrix from `verification/certificate.json`. An independently coded transfer recurrence counts matchings by cardinality and verifies the reduced Euler characteristic \(163\). The recorded execution result is in `verification/verification_output.txt`.

## Relationship to prior work
The withdrawn 2021 paper of Goyal, Shukla and Singh originally proposed an all-width wedge classification, but its 2025 corrigendum specifically identifies incorrect inclusion-map arguments and reports only that the nine-column homology is concentrated in dimension eight. Neither the withdrawn all-width claim nor that homology computation proves the present integral homotopy decomposition and exact rank. The September 2026 paper of Chauhan, Sharma and Shukla proves general lower homology vanishing and nonvanishing in the first allowed degree, and motivates understanding whether higher-dimensional classes appear. The new result resolves the nine-column homotopy type by an independent, reproducible acyclic matching and unimodular integer boundary.

## Limitations
This is a finite-width result. It does not give an arbitrary-width matching-complex homotopy theorem. The full text of the September 2026 paper could not be obtained in this review; its accessible abstract and an extended descriptive review were read. That access limitation leaves a residual possibility that a numerical nine-column calculation was already included, although an empirical Betti table would not itself supply the homotopy certificate established here.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1, first posted 2026-09-23, https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), DOI:10.37236/10496; withdrawn, with corrigendum submitted 2025-03-01, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p16/pdf/.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
4. M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, Journal of Algebraic Combinatorics 27 (2008), 423–450, DOI:10.1007/s10801-007-0096-x (background on matching-tree techniques).
