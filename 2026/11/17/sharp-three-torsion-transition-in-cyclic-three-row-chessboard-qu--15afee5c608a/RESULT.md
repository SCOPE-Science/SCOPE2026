# Sharp three-torsion transition in cyclic three-row chessboard quotients

## Finding

Let \(\Delta_{3,n}\) be the ordinary chessboard complex of nonattacking rook placements on three labeled rows and \(n\) labeled columns. Let \(C_3\) rotate the three **rows** and fix every column, and set \(Q_n=|\Delta_{3,n}|/C_3\). For every integer \(n\ge3\):

\[
Q_3\simeq S^1\vee S^1,\qquad Q_4\cong T^2.
\]

For every \(n\ge5\),

\[
\pi_1(Q_n)\cong\mathbb Z/3\mathbb Z,\qquad
H_i(Q_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3\mathbb Z,&i=1,\\
\mathbb Z^{n(n-2)(n-4)/3-1},&i=2,\\
0,&i\ge3.
\end{cases}
\]

The order-three torsion is new in the orbit space: for \(n\ge5\), the covering chessboard complex is simply connected and has torsion-free integral homology. The classification identifies the sharp transition from a two-circle wedge, through a torus, to spaces with finite cyclic fundamental group and unbounded free second homology. Its integer-cell presentation below independently establishes the first-homology transition for all widths.

## Assumptions and scope

A simplex of \(\Delta_{3,n}\) is a subset of \(\{0,1,2\}\times\{1,\ldots,n\}\) containing at most one square of each row and each column. A nonempty simplex contains one, two, or three squares. The group generator sends \((r,j)\mapsto(r+1\pmod3,j)\), not a rotation of columns. All quotient spaces mean ordinary geometric realizations modulo this action. Chain groups and homology are over \(\mathbb Z\) unless otherwise specified. No identification with an orbit *poset* is used. There is no assertion of a full homotopy decomposition for \(n\ge5\).

## Proof

**Free action and quotient cells.** Any nonidentity row rotation moves the unique row selected in each occupied column; hence it cannot preserve a nonempty rook-placement simplex setwise. Thus the group acts freely on the geometric realization. Every face orbit gives a genuine quotient simplex cell, oriented by increasing column indices. The numbers of quotient cells in dimensions zero, one and two are respectively

\[
c_0=n,\qquad c_1=n(n-1),\qquad
c_2=2\binom n3=\frac{n(n-1)(n-2)}3.
\]

There are no cells above dimension two. Consequently

\[
\chi(Q_n)=n-n(n-1)+\frac{n(n-1)(n-2)}3
=\frac{n(n-2)(n-4)}3.
\]

**Signed integer boundary and all widths.** Name the orbit vertices \(v_i\), with one for each column. For each \(1\le i<j\le n\) there are two edges \(e^+_{ij},e^-_{ij}\), according as the row of the rook in column \(j\) differs from that in column \(i\) by \(+1\) or \(-1\) modulo three. In either case \(\partial e^\pm_{ij}=v_j-v_i\). For \(i<j<k\), there are precisely two two-cells, with ordered rows \((0,1,2)\) and \((0,2,1)\) modulo simultaneous rotation; denote them \(T^+_{ijk}\) and \(T^-_{ijk}\). Their integral boundaries are

\[
\partial T^+_{ijk}=e^+_{jk}-e^-_{ik}+e^+_{ij},\qquad
\partial T^-_{ijk}=e^-_{jk}-e^+_{ik}+e^-_{ij}.
\]

These descriptions derive directly from all the face orbits and do not rely on rational approximation.

The integral cycle lattice \(\ker\partial_1\) has a unimodular basis consisting of

\[
d_{ij}=e^+_{ij}-e^-_{ij}\quad(1\le i<j\le n),\qquad
t_{ij}=e^+_{ij}-e^+_{1j}+e^+_{1i}\quad(2\le i<j\le n).
\]

Indeed, the \(e^+\) edges form a complete graph on the quotient vertices; the \(t\) cycles constitute its fundamental-cycle basis for the star spanning tree at vertex \(1\), while each remaining \(e^-\) edge differs integrally from its \(e^+\) edge by a \(d\) cycle. The two boundaries associated with columns \(1,i,j\) give the relations

\[
t_{ij}+d_{1j}=0,\qquad t_{ij}-d_{ij}-d_{1i}=0.
\]

They eliminate every \(t_{ij}\) and \(d_{ij}\) with \(i\ge2\). Put \(x_i=d_{1i}\) for \(2\le i\le n\). Both boundaries for a triple \(2\le i<j<k\le n\) then reduce, up to sign, to the single relation

\[
x_i+x_j+x_k=0.
\]

This gives an exact integral presentation

\[
H_1(Q_n;\mathbb Z)
\cong\big\langle x_2,\ldots,x_n\ \big|\ x_i+x_j+x_k=0\quad(2\le i<j<k\le n)\big\rangle.
\]

For \(n=3\) there are no relations, and for \(n=4\) there is just one primitive relation, giving \(H_1\cong\mathbb Z^2\) in both cases. For \(n\ge5\) there are at least four generators. Subtracting two triple relations sharing a pair forces all \(x_i\) equal; a triple relation then says \(3x=0\). Conversely mapping every \(x_i\) to \(1\in\mathbb Z/3\mathbb Z\) respects all relations, so the common generator has *exactly* order three. Thus \(H_1\cong\mathbb Z/3\mathbb Z\), without any assumption about higher homology or the fundamental group.

**Boundary cases.** At \(n=3\), the quotient has two triangles and six edges, each edge belongs to exactly one triangle. The two triangles collapse along distinct free edges, leaving a connected graph with first Betti number two, hence \(Q_3\simeq S^1\vee S^1\). At \(n=4\), the original \(\Delta_{3,4}\) is a triangulated torus by the classical chessboard-complex analysis [1]. The free order-three row action preserves orientation, since the orientation sign homomorphism of an odd-order group to \(\{\pm1\}\) is trivial. Therefore the quotient is a closed orientable surface with Euler characteristic zero, hence \(Q_4\cong T^2\).

**All \(n\ge5\).** The classical chessboard connectivity theorem [1, Theorem 1.1] states that \(\Delta_{m,n}\) is \((\nu-2)\)-connected for \(\nu=\min\{m,n,\lfloor(m+n+1)/3\rfloor\}\). At \(m=3\) and \(n\ge5\), this gives simple connectivity. Thus the free row action presents a regular covering with deck group \(C_3\), and \(\pi_1(Q_n)\cong C_3\). The quotient is connected. As \(\ker\partial_2\) is a subgroup of a free abelian cellular chain group, \(H_2(Q_n;\mathbb Z)\) is free. It has rank \(\chi(Q_n)-1\) because \(H_1\) is finite. The claimed formula follows, with higher homology zero by dimension.

## Verification

The accompanying standalone script `verify_row_cyclic.py` independently reconstructs every labeled matching and row-rotation orbit in dimensions zero through two for \(3\le n\le8\), checks that both boundary maps compose to zero, transforms the two-cell boundaries to an explicitly unimodular integer cycle basis, and computes exact Smith normal forms. It reports the free ranks and all torsion factors. Its output, `verification_output.txt`, records six successful widths; the finite checks are corroboration, not a substitute for the all-width integer presentation or the published connectivity theorem.

## Relationship to prior work

The 1994 chessboard-complex paper [1] proves the connectivity bound and identifies the original \(3\times4\) complex as a torus; it does not assert this three-row cyclic *quotient* homology classification. The 2004 preprint [2] concerns torsion and connectivity in original matching/chessboard complexes. The later 2026 preprint [3] explicitly studies homotopy types of the original generalized chessboard complexes, not a row-rotation quotient in the accessible abstract. Published mathematical records of column-rotation quotients concern a different group action and do not imply the displayed row-rotation orbit-cell boundaries. The present exact computation is about a free threefold quotient, not the column-permutation or full-row-symmetric quotients. The rank formula can partly be deduced from classical connectivity plus Euler characteristic; the explicit integral orbit presentation and complete boundary-to-stable transition are stated to identify precisely the additional conclusion.

## Limitations

The theorem is limited to exactly three rows, a cyclic permutation of those rows, and \(n\ge3\). It neither classifies the full homotopy type for \(n\ge5\) nor treats arbitrary row/column subgroups. A later generalized-chessboard paper [3] was available by abstract only; its full text could not be compared, leaving a bounded bibliographic originality risk. Matching mathematical terminology or absence of search hits alone does not prove publication priority. The computation uses neither experimental extrapolation nor any assumption about inaccessible literature.

## References

[1] A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39. DOI: https://doi.org/10.1112/jlms/49.1.25. Full text author-posted at https://www.researchgate.net/publication/245653497_Chessboard_Complexes_and_Matching_Complexes.

[2] J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public preprint 2004-09-03), https://arxiv.org/abs/math/0409054.

[3] I. Limonchenko and S. Yu, *Homotopy Types and Torsion in Homology of Generalized Chessboard Complexes*, arXiv:2610.37827 (first public preprint 2026-10-27), https://arxiv.org/abs/2610.37827.
