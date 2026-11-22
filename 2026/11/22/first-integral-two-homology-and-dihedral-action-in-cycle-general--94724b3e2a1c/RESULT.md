# First integral two-homology and dihedral action in cycle general-position complexes

## Finding
For every integer \(3\le n\le12\), let \(C_n\) be the cycle on vertices \(0,\ldots,n-1\), and let \(\mathrm{GP}(C_n)\) be the simplicial complex of all vertex subsets such that no three selected vertices lie on any common shortest path of \(C_n\). Its **complete reduced integral homology** is torsion-free and is concentrated in dimensions \(1\) and \(2\), with ranks in this table (zero denotes the zero group):

| \(n\) | Number of two-faces | \(\operatorname{rank}\widetilde H_1\) | \(\operatorname{rank}\widetilde H_2\) |
|---:|---:|---:|---:|
| 3 | 1 | 0 | 0 |
| 4 | 0 | 3 | 0 |
| 5 | 5 | 1 | 0 |
| 6 | 2 | 8 | 0 |
| 7 | 14 | 1 | 0 |
| 8 | 8 | 13 | 0 |
| 9 | 30 | 1 | 3 |
| 10 | 20 | 16 | 0 |
| 11 | 55 | 1 | 11 |
| 12 | 40 | 19 | 4 |

Consequently, \(C_9\) is the first cycle whose general-position complex has nonzero integral second homology, and \(C_{12}\) is the first *even* cycle with this property. For \(C_9\), rotation \(r(i)=i+1\pmod9\) has order three on its rank-three integral second homology, while reflection \(s(i)=-i\pmod9\) has trace \(1\). The reduced rational homology of the ordinary dihedral quotient is
\[
\widetilde H_j\bigl(|\mathrm{GP}(C_9)|/D_9;\mathbb Q\bigr)\cong
\begin{cases}\mathbb Q,&j=2,\\0,&j\ne2.\end{cases}
\]
The claim is about **homology**, not a wedge-of-spheres homotopy equivalence.

## Assumptions and scope
Graphs are simple and unweighted; a shortest path is an ordinary graph geodesic. The full graph-geodesic definition is used, including *all* equally short paths in even cycles. A subset is a face precisely when every triple of its vertices avoids geodesic collinearity. The finite statement covers every labelled cycle of size \(3\) through \(12\) and makes no assertion about later orders. The quotient is the ordinary topological orbit space of the geometric realization, not a homotopy quotient. All homology is unreduced in degree zero and reduced otherwise; since these complexes are connected, \(\widetilde H_0=0\).

## Proof
Order each three-set as \(a<b<c\) and set its cyclic gaps to \(b-a\), \(c-b\), and \(n-c+a\). This triple is in graph-geodesic general position **if and only if** each gap is strictly less than \(n/2\): a gap of at least half the circle makes the other two gaps together a shortest or tied-shortest route between the bounding vertices and puts the remaining vertex on that route. Conversely, if a selected vertex lies on a shortest path between the other two, the complementary cyclic gap has length at least half the circle. The attached verifier checks this equivalence independently using all three shortest-path distance equations for each labelled triple. For every \(3\le n\le12\), an exhaustive four-subset check shows no four-set is a face. Every vertex and pair is a face; thus the complex has chain groups \(C_0=\mathbb Z^n\), \(C_1=\mathbb Z^{\binom n2}\), and \(C_2=\mathbb Z^{f_2}\), with no higher cells.

Using lexicographic orders for vertices, edges and admissible triples, build the signed boundary matrix \(B_n=\partial_2\) whose column for \((a,b,c)\) is \([b,c]-[a,c]+[a,b]\). In each of the ten cases, exact integral elementary row/column operations, using only pivots \(\pm1\), reduce \(B_n\) to \(\operatorname{diag}(I_{r_n},0)\). The ranks \(r_n\), in increasing \(n\), are \(1,0,5,2,14,8,27,20,44,36\). This is a unimodular reduction, so every nonzero Smith invariant factor is one, not just a rational or mod-two rank calculation. In particular \(\operatorname{im}\partial_2\) is primitive in \(C_1\), and the first integral homology has no torsion. The complete one-skeleton gives \(\operatorname{rank}\ker\partial_1=\binom{n-1}{2}\). Therefore
\[
\widetilde H_1\cong\mathbb Z^{\binom{n-1}{2}-r_n},\qquad
\widetilde H_2\cong\mathbb Z^{f_2-r_n}.
\]
The exhaustive face and Smith computations, including zero residual matrices and boundary signs, are independently reconstructible from `verify.py`. Finite enumeration is a complete proof **for the explicitly bounded ten orders only**.

For \(n=9\), \(B_9\) has \(30\) columns, rank \(27\), and a three-dimensional integral kernel. In the canonical integral kernel basis obtained by row reduction with lexicographic free triangle-column positions \(14,23,28\) (zero-indexed), the induced maps on \(H_2\) are
\[
R=\begin{pmatrix}-1&-1&0\\1&0&0\\0&-1&1\end{pmatrix},\qquad
S=\begin{pmatrix}0&-1&0\\-1&0&0\\-1&-1&1\end{pmatrix}.
\]
Direct multiplication gives \(R^3=I\), \(S^2=I\), and \(SRS=R^{-1}\). The common \(R\)- and \(S\)-fixed rational subspace is exactly one-dimensional. For reflection the oriented simplicial chain traces in degrees \(0,1,2\) are \(1,-4,-2\), yielding Lefschetz number \(3\). Since its trace on \(H_0\) is \(1\) and on \(H_2\) is \(1\), its trace on the rank-one \(H_1\) must be \(-1\). The order-nine rotation acts as \(+1\) on the rank-one integral \(H_1\). Consequently the full dihedral action has no rational invariants on \(H_1\) and exactly one on \(H_2\). Rational transfer for finite-group actions on simplicial realizations, after barycentric subdivision if necessary, identifies quotient rational homology with these invariant spaces. The construction and matrices are independently reconstructed by `verify_equiv.py` using exact fractions.

## Verification
Run `python3 verify.py` and `python3 verify_equiv.py` in the same directory; both use only the Python standard library. The first independently evaluates shortest-path and cyclic-gap predicates on all labelled triples, rejects all four-faces, constructs every signed boundary matrix, and proves the stated unit Smith reductions by exact integer operations. The second constructs integral two-cycle generators from an exact rational nullspace whose entries turn out to be integers with unit free coordinates, and checks the dihedral matrices, relations, traces, and invariant dimensions. Both scripts were run successfully from their actual packaged paths before acceptance.

## Relationship to prior work
Klavžar, Rall and Yero (first public preprint \(2020\)-05-16, arXiv:2005.08095), especially their cycle section, determine general \(d\)-position *numbers*, not the integral chain homology of the simplicial complex of *all* general-position subsets. Cody and Moore (arXiv:2409.05644, \(2024\)-09-09), especially their cycle theorem, determine generalized maximum cardinalities and maximally even extremizers, not the Smith factors or the dihedral homology of this complex. Related graph-general-position complexes for ladder graphs concern \(P_m\square K_2\), not the ordinary cycles here. These distinctions concern statements and implications, not title similarities.

## Limitations
Only the finite range \(3\le n\le12\) is established. No general formula, shellability, fundamental-group classification, higher-order persistence, or integral quotient homology is claimed. A torsion-free homology calculation does **not** determine the homotopy type. The external literature comparison is necessarily subject to the possibility of unindexed equivalent work; the computational argument makes no claim of independent validation.

## References
1. S. Klavžar, D. F. Rall, I. G. Yero, *General d-position sets*, arXiv:2005.08095 (first posted \(2020\)-05-16), https://arxiv.org/abs/2005.08095; author-hosted full text https://users.fmf.uni-lj.si/klavzar/preprints/2384-11213.pdf.
2. B. Cody, G. Moore, *The k-general d-position problem for graphs*, arXiv:2409.05644 (first posted \(2024\)-09-09), https://arxiv.org/abs/2409.05644.
