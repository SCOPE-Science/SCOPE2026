# The dihedral symmetry plane at the second critical cycle-Rips threshold

## Finding
For the shortest-path graph metric on the 15-cycle, set \(K=\operatorname{VR}_{\le6}(C_{15})=\operatorname{Cl}(C_{15}^{6})\). Label vertices by \(\mathbb Z/15\mathbb Z\), let \(r(i)=i+1\), and let \(s(i)=-i\). For \(D_{15}=\langle r,s\mid r^{15}=s^2=1,\ srs=r^{-1}\rangle\), the **complete rational top-homology character** is
\[
\chi(r^a)=\begin{cases}2,&3\mid a,\\-1,&3\nmid a,\end{cases}\qquad \chi(r^as)=0\quad(0\le a<15).
\]
Thus \(\widetilde H_4(K;\mathbb Q)\) is the standard two-dimensional representation of the three-letter dihedral quotient \(D_{15}\twoheadrightarrow D_3\cong S_3\). Its kernel contains the order-five subgroup \(\langle r^3\rangle\); the plane itself is irreducible over \(\mathbb Q\). The original homotopy type \(K\simeq S^4\vee S^4\) is a theorem of Adamaszek and is not claimed as new.

The rational cohomology of the ordinary geometric quotient by the rotation subgroup \(\langle r\rangle\) and by \(D_{15}\) is that of a point. For any reflection \(r^as\), the ordinary geometric quotient has the rational cohomology ring of \(S^4\); this does **not** assert a homotopy equivalence or determine integral torsion.

## Assumptions and scope
The vertex set is exactly \(\{0,1,\ldots,14\}\). A set spans a simplex if, for each pair \(i,j\) within it, the cyclic distance \(\min((i-j)\bmod15,(j-i)\bmod15)\) is at most six. The empty set is included in augmented Lefschetz calculations, and each simplex is oriented by increasing vertex labels. These conventions fix all signs and the inclusive boundary scale. Only the graph's indicated dihedral action is claimed, without assertions about larger graphs or the entire filtration.

## Proof
Adamaszek's Corollary 6.7 (2011) proves that for \(k/n=2/5\), the clique complex of the \(k\)-th power of an \(n\)-cycle is a wedge of \(n-2k-1\) four-spheres. Substituting \((n,k)=(15,6)\) gives \(\widetilde H_4(K;\mathbb Q)\cong\mathbb Q^2\) and zero reduced homology elsewhere.

For an automorphism \(g\), define the signed simplex trace \(T_q(g)\) as the sum of permutation signs on oriented \(q\)-simplices mapped setwise to themselves. The augmented Lefschetz identity and homological concentration imply
\[
\chi(g)=-\sum_{\sigma\in K}(-1)^{|\sigma|}\operatorname{sgn}(g\vert_\sigma),
\]
where the empty face contributes one and its sign is one; terms from faces not preserved setwise are zero. There are exactly 1364 faces, including the empty face. By dimension, their counts are \(1,15,90,275,450,378,140,15\), for dimensions \(-1,0,1,2,3,4,5,6\).

A complete evaluation of the displayed finite sum for all 30 dihedral elements gives \(2\) on the five rotations \(r^{3b}\), \(-1\) on the remaining ten rotations, and \(0\) on each of the fifteen reflections. A logically separate evaluation divides the vertices into cycles of \(g\), enumerates the subsets of cycles whose union is a clique, and adds \(-(-1)^t\) for each surviving subset of \(t\) cycles. The two procedures agree for every element (see the standalone program and its recorded output).

The order-five rotation \(r^3\) has trace two, hence acts identically on the two-dimensional rational homology: its eigenvalues are complex fifth roots of unity, and the only way their sum is two is that both are one. Therefore the action factors through \(D_{15}/\langle r^3\rangle\cong D_3\). The three conjugacy-class values in that quotient are \((2,-1,0)\) on identity, nonidentity cubic rotations, and reflections. These are precisely the irreducible standard two-dimensional character; this identifies the representation, not merely its total dimension.

For a finite group \(H\) acting on a finite complex, rational transfer/averaging gives \(H^*(|K|/H;\mathbb Q)\cong H^*(|K|;\mathbb Q)^H\). Since the average of \(\chi\) over all 15 rotations is \((5\cdot2+10\cdot(-1))/15=0\), the rotation quotient has no positive-degree rational cohomology. The full quotient has none as well. For a reflection, the fixed-subspace dimension is \((2+0)/2=1\), yielding one fourth-degree cohomology class; dimensional reasons force its square to vanish.

## Verification
Run `python3 verify.py` with Python 3 and no third-party modules. The program enumerates all \(2^{15}\) vertex subsets, checks the clique condition, evaluates signed traces on all 30 elements, and independently re-evaluates them using vertex cycles. It verifies the exact character formula and prints `C15_SECOND_CRITICAL_DIHEDRAL_PASS`. The source and its recorded standard output are embedded alongside this document.

## Relationship to prior work
Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433, 2011), Corollary 6.7, **already proves the nonequivariant wedge-of-two-four-spheres**. It provides the key homology-concentration input, not the equivariant character. Adamaszek–Adams–Frick–Peterson–Previte-Johnson, *Nerve complexes of circular arcs* (arXiv:1410.4336, 2014), Proposition 7.2 computes a dihedral action on homology of **arc nerve complexes** and Section 8 addresses their different **clique complexes**. Its Theorem 8.2 gives the nonequivariant clique homotopy type, and Theorem 8.5 supplies a homotopy equivalence to a different-size nerve; it does not assert an equivariant identification under the present 30-element group. The present character comparison is specifically for the graph-metric clique complex and therefore is not implied solely by the different nerve character. Cyclic-power cut-complex and dihedral cycle-matching results concern other simplicial functors.

## Limitations
This determines only the rational action for one canonical 15-point example at the first non-one-dimensional \(2/5\) critical winding-fraction instance. Neither integral homology lattices of its symmetry quotients nor higher-parameter families are classified. An equivalent formulation in other equivariant cyclic-complex literature remains a potential priority risk. The cited nonequivariant theorem is used as published mathematical input; the finite action evaluation is independently reproducible. No independent mathematical audit is claimed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), Corollary 6.7; https://arxiv.org/pdf/1104.0433.
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (2014), Sections 7 and 8; https://arxiv.org/pdf/1410.4336.
