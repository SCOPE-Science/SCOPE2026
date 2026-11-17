# The first integral torsion in rotation-fixed triangle-free graph complexes

## Finding
For each integer \(n\geq 3\), let \(\mathcal T_n\) be the simplicial complex of all triangle-free spanning subgraphs of the complete simple graph on \(\mathbb Z/n\mathbb Z\). A simplex is an edge set; the geometric cyclic group \(C_n\) acts by rotating vertex labels. Let \(F_n=|\mathcal T_n|^{C_n}\).

**Theorem.** The first \(n\geq3\) for which \(F_n\) has torsion in its integral homology is \(n=21\). For every \(3\leq n\leq20\) all integral homology groups are torsion-free; \(F_3\) is empty. Moreover, \(F_{21}\) is PL-homeomorphic to the Klein bottle. In particular,
\[
H_0(F_{21};\mathbb Z)\cong\mathbb Z,\quad H_1(F_{21};\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z,\quad H_j(F_{21};\mathbb Z)=0\quad(j\geq 2).
\]
The complex realizing \(F_{21}\) has precisely nine vertices, twenty-seven edges, and eighteen triangles.

## Assumptions and scope
The graph's edge set, *not* its vertex set, is the vertex set of \(\mathcal T_n\). Triangle-free means absence of a simple three-cycle; isolated vertices of the spanning graph are permitted. Fixed points refer to the geometric realization, rather than merely individually fixed vertices. The cyclic group rotates all \(n\) graph vertices simultaneously, including possible diametrical edge orbits when \(n\) is even. For \(F_3\), the geometric realization is empty; the conventional degree-minus-one homology of an empty complex does not constitute torsion.

For \(1\leq d\leq\lfloor n/2\rfloor\), let \(O_d\) be the orbit consisting of unordered edges \(\{i,i+d\}\), with indices modulo \(n\). A distance set \(D\) represents the union of edge orbits \(\bigcup_{d\in D}O_d\). Let \(\Sigma(D)=\{d,-d:d\in D\}\subset\mathbb Z/n\mathbb Z\).

## Proof
**Orbit-fixed PL model.** Every point of the geometric realization is a vector of nonnegative barycentric weights indexed by the edges and summing to one. It is fixed by all rotations precisely when its weights are constant on each edge orbit \(O_d\). Its support is a face exactly when the union of the selected orbits is triangle-free. The affine map sending the barycentric mass at \(O_d\) to \(|O_d|\) times the common edge weight gives a piecewise-linear homeomorphism from \(F_n\) onto the realization of the simplicial complex \(K_n\) of admissible nonempty distance sets \(D\). Its inverse splits each orbit mass equally among its edges; the statements hold without change for antipodal orbits.

**Additive characterization.** An ordered triangle \((a,b,c)\) has oriented nonzero step differences \(x=b-a\), \(y=c-b\), and \(-z=a-c\), with \(x+y=z\) in \(\mathbb Z/n\mathbb Z\). Conversely, any \(x,y,z\in\Sigma(D)\) with \(x+y=z\) gives three distinct vertices \(a,a+x,a+z\) (because \(x,y,z\neq0\)). Its edges belong to the selected distance orbits. Therefore
\[
D\in K_n\quad\Longleftrightarrow\quad
\text{there do not exist }x,y,z\in\Sigma(D)\text{ with }x+y=z\pmod n.
\]
Repetitions among the step *values* are permitted: this is the standard sum-free condition, not the distinct-element convention. Equivalently, \(K_n\) is the geometric inversion-fixed complex of the three-zero-sumfree complex on \(\mathbb Z/n\mathbb Z\), since \(x+y+z=0\) is the same forbidden relation after applying inversion to one summand in a symmetric set.

**Finite exact cutoff.** For every \(3\leq n\leq21\), the included verifier independently evaluates the previous condition both by enumerating all triples of distinct polygon vertices and by checking all sums of signed distances. It enumerates *all* \(2^{\lfloor n/2\rfloor}\) distance subsets, constructs the full augmented simplicial chain complex, and calculates the integer Smith normal forms of every boundary. For \(3\leq n\leq20\), each nonzero invariant factor of each boundary is \(1\). Since a subgroup of a free abelian chain group is saturated exactly when its cokernel has no torsion, and since the image of the preceding boundary lies in the corresponding kernel, these reductions imply every integral homology group is torsion-free. This is a finite exhaustive argument, not an extrapolation.

At \(n=21\), the admissible single distances are \(1,2,3,4,5,6,8,9,10\) (distance \(7\) alone creates triangles). The full list of facets is the following eighteen triples; no higher-dimensional faces exist:

```
(1,3,5) (1,3,8) (1,4,6) (1,4,9) (1,5,9) (1,6,8)
(2,3,8) (2,3,10) (2,5,6) (2,5,9) (2,6,10) (2,8,9)
(3,4,5) (3,4,10) (4,5,6) (4,9,10) (6,8,10) (8,9,10)
```
Every one of the twenty-seven edges occurs in exactly two facets. The link of every vertex is a connected six-edge cycle, and the entire complex is connected. Hence \(K_{21}\) triangulates a closed connected surface with Euler characteristic \(9-27+18=0\). A signed orientation-propagation check on the triangle adjacency graph exhibits a contradiction, proving nonorientability. The classification of compact connected surfaces identifies \(|K_{21}|\) with the Klein bottle independently of the integer homology calculation.

For an independent integral check, the matrices built with incidence signs \((-1)^j\) for deleting the \(j\)-th vertex have Smith invariant lists
\[
\operatorname{SNF}(\partial_1):1^{\times8},\qquad
\operatorname{SNF}(\partial_2):1^{\times17},2.
\]
Thus \(\operatorname{rank}\partial_1=8\), \(\operatorname{rank}\partial_2=18\), and \(\widetilde H_1(K_{21};\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z\). No top-dimensional cycle survives because \(\partial_2\) is injective.

## Verification
Run `python verify_trianglefree_fixed.py` with the version of SymPy listed in `requirements.txt`; compare with `verification_output.txt`. The program enumerates all simple-graph triangles, all distance subsets and all oriented simplicial boundary matrices for \(3\leq n\leq21\); it separately tests the equivalent sum-free predicate. It checks vertex links, edge incidences, connectedness and an orientation-sign obstruction at \(n=21\). All integer Smith factors are computed exactly, not numerically approximated. The source code, full output and software dependency are included. The finite calculation exhausts exactly the stated bounded range and proves no assertion for \(n\geq22\).

## Relationship to prior work
Green and Ruzsa establish the standard sum-free framework, especially extremal density and enumeration, not the integral topology of the sign-symmetric family. Adams, Hall and Stucky define the general three-zero-sumfree simplicial complexes and an enumeration algorithm, and report calculations through \(n\leq19\); the inversion-fixed subcomplex and the homological cutoff here are additional questions. Datta and Upadhyay classify degree-regular Klein-bottle triangulations: existence of nine-vertex Klein triangulations is *known*, not claimed as a new triangulation. The distinctive statement is its realization as a rotational fixed set in a canonical graph-property complex and its sharp first integral-torsion threshold. Jonsson's graph-complex treatment provides background; only accessible previews were examined. No assertion is made that the Klein-bottle simplicial isomorphism class is new.

## Limitations
Only full cyclic-rotation fixed spaces of triangle-free graph complexes are considered; neither other subgroups nor all graph properties are classified. The proof shows a sharp cutoff through \(n=21\), not a formula at larger orders. Integral homology does not determine the entire homotopy type in general; the Klein-bottle identification instead follows from the surface criteria. A not-yet-found equivalence in older topological or additive-combinatorial literature remains a priority risk. No independent mathematical validation has been performed.

## References
1. B. Green and I. Z. Ruzsa, *Sum-free sets in abelian groups*, first public version 2003-07-10, arXiv:math/0307142, https://arxiv.org/abs/math/0307142.
2. A. Adams, C. Hall and E. Stucky, *Classifications of \(\ell\)-Zero-Sumfree Sets*, 2019, arXiv:1904.08989, https://arxiv.org/abs/1904.08989.
3. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, first public version 2004-03-25, arXiv:math/0403433, https://arxiv.org/abs/math/0403433.
4. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008 (bibliographic and preview material only).
