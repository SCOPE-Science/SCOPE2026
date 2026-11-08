# Line-avoidance homotopy and projective symmetry in \(\mathrm{PG}(2,3)\)

## Finding
Let \(P\) be the thirteen projective points of \(\mathrm{PG}(2,3)\), and let \(\mathcal L\) be its thirteen four-point lines. Define the **line-avoidance complex**
\[
X=\{U\subseteq P: L\not\subseteq U\text{ for every }L\in\mathcal L\}.
\]
Then its *integral homotopy type* is
\[
\boxed{X\simeq S^5\vee\bigvee^{39} S^6.}
\]
Write \(G=\mathrm{PGL}_3(\mathbb F_3)\), of order \(5616\), acting on the thirteen points. It acts trivially on \(\widetilde H_5(X;\mathbb Q)\cong\mathbb Q\); its degree-six rational homology character \(\chi_6\) is given exactly by the table below. A cycle type refers to the permutation of thirteen projective points.

| Point cycle type | Number of group elements | \(\chi_6\) |
| --- | ---: | ---: |
| \(1^{13}\) | 1 | 39 |
| \(1^5 2^4\) | 117 | -1 |
| \(1^4 3^3\) | 104 | 3 |
| \(1^2 2\,3\,6\) | 936 | -1 |
| \(1\,2^2 4^2\) | 702 | -1 |
| \(1\,3^4\) | 624 | 0 |
| \(1\,4\,8\) | 1404 | 1 |
| \(13\) | 1728 | 0 |

In particular, \(\widetilde H_6(X;\mathbb Q)^G=0\) although \(\dim\widetilde H_6(X;\mathbb Q)=39\), and the quotient has reduced rational homology
\[
\boxed{\widetilde H_i(X/G;\mathbb Q)\cong\begin{cases}\mathbb Q,&i=5,\\0,&i\ne5.\end{cases}}
\]
This is a homological conclusion about the quotient, not a claimed homotopy equivalence \(X/G\simeq S^5\).

## Assumptions and scope
Represent a projective point by the unique nonzero vector \((a,b,c)\in\mathbb F_3^3\) whose first nonzero coordinate equals \(1\). Represent lines by equivalently normalized nonzero coefficient vectors \(\ell\), with point \(p\) on line \(\ell\) exactly when \(\ell\cdot p=0\) in \(\mathbb F_3\). There are thirteen points and thirteen lines; each line has four points, each point belongs to four lines, every pair of points belongs to one line, and distinct lines meet at one point.

A face of \(X\) may contain a collinear triple; it is forbidden to contain **all four** points of any projective line. Thus \(X\) is neither the matroid independence complex (which excludes dependent triples) nor the theta/nonblocking complex (which requires a line disjoint from the face). The restriction to the canonical order-three projective plane is essential.

## Proof
**Incidence and complete face set.** Generate the thirteen normalized vectors and their thirteen orthogonal line masks using arithmetic modulo three. A subset is a face precisely when its thirteen-bit mask contains none of the thirteen four-bit line masks. Exhaustively checking all \(8192\) masks yields \(4330\) faces **including the empty face**, with nonempty face counts by dimension \(0,1,\ldots,8\):
\[
(13,78,286,702,1170,1248,702,117,13).
\]
A separate increasing-index recursive generator produces exactly the same mask set. Pair incidence and line-intersection axioms are checked directly.

**Acyclic discrete-Morse certificate.** Starting from all augmented faces, process vertices in increasing label order. At the current vertex \(v\), pair each currently unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both are currently unpaired; remove both. This deterministically gives \(2145\) disjoint pairs and leaves precisely one five-dimensional face and thirty-nine six-dimensional faces. The augmented empty face is paired to a vertex; remove that one pair when returning to the ordinary face poset, retaining its vertex as the unique ordinary critical zero-cell. There are therefore \(2144\) ordinary pairs and exactly \(1,1,39\) critical cells in dimensions \(0,5,6\).

To verify acyclicity **rather than assume it**, orient each codimension-one face relation upward if matched and downward otherwise. The complete augmented face poset has \(23140\) covering incidences. Exhaustive topological sorting visits all \(4330\) faces, so this directed graph has no cycle; deleting the empty node preserves acyclicity. Forman's theorem gives a CW model with a point, one five-cell and thirty-nine six-cells.

**Integral attaching maps.** Orient every simplex using increasing point labels. For a five-face \(f\), define its integral projection \(R(f)\) onto the single critical five-face. For critical \(f\), set \(R(f)=1\); for a five-face paired *downward* with a four-face, set \(R(f)=0\). If \(f\) is the lower member of a matching with six-face \(t\), use the exact signed recurrence
\[
R(f)=-[\partial t:f]\sum_{g\subset t,\,\dim g=5,\,g\ne f}[\partial t:g]R(g).
\]
The acyclic matching guarantees termination. Summing the projections of signed boundaries of all thirty-nine critical six-faces yields the **zero** integer matrix of size \(1\times39\). Consequently every six-cell attaches to the five-sphere with degree zero. Since \(\pi_5(S^5)\cong\mathbb Z\) by Hurewicz, all attaching maps are nullhomotopic, proving the stated wedge decomposition, with no torsion. An independently generated projective coordinate model, reverse-order matching, and second integer boundary computation reproduce the same result.

**Projective symmetry and quotient.** The verifier enumerates all invertible \(3\times3\) matrices over \(\mathbb F_3\) modulo scalar matrices, obtaining all \(5616\) distinct projective permutations. Every one preserves the line collection. The natural map \(\mathrm{SL}_3(\mathbb F_3)\to\mathrm{PGL}_3(\mathbb F_3)\) is an isomorphism, since scaling a matrix to determinant one is unique. Elementary transvections generate \(\mathrm{SL}_3(\mathbb F_3)\), and each is a commutator of two elementary transvections in distinct coordinate directions; hence this group is perfect. Its action on the rank-one integral \(\widetilde H_5(X;\mathbb Z)\) must therefore be trivial.

For any \(g\in G\), an invariant face is a union of cycles of its permutation on the thirteen points. If it comprises \(k\) whole cycles, its contribution to the **reduced** signed simplicial Lefschetz number \(\widetilde L(g)\) is \((-1)^{k-1}\), including the empty face's contribution \(-1\). Exhaustively enumerating cycle unions that avoid complete lines gives the table's multiplicities and \(\widetilde L(g)\) values \(\{-2,-1,0,2,38\}\). Since the only reduced rational homology is in degrees five and six,
\[
\chi_6(g)=1+\widetilde L(g).
\]
The sum of all \(5616\) reduced Lefschetz numbers is \(-5616\). Thus the character average \(\frac1{|G|}\sum_g\chi_6(g)\) is zero, and \(\dim\widetilde H_6(X;\mathbb Q)^G=0\). The rational transfer/averaging isomorphism for a finite group acting on a finite simplicial complex identifies rational homology of the quotient with invariant rational homology, completing the proof.

## Verification
Both `verify.py` and `second_check.py` use the Python 3 standard library and reconstruct their geometric input from scratch. Their checked outputs are recorded in `verification_output.txt` and `second_output.txt`, respectively. The first executable verifies the full face set by two enumerators, the complete directed-Hasse topological sort, the exact integral Morse coefficients, independent mod-two boundary ranks, the \(5616\) projective actions, every line-preservation test, the signed Lefschetz character table and its invariant average. The second independently constructs lines by cross products of pairs of projective points, uses reverse pivot order and obtains the same zero integral Morse differential. All assertions completed.

## Relationship to prior work
Conant and Thistlethwaite (arXiv:0808.0739, first public 2008-08-05) developed the theta complex and its relationship to hypergraph independence complexes, including discrete-Morse examples. Their analyzed cubical hypergraphs are not the line hypergraph of \(\mathrm{PG}(2,3)\). Björner and Tancer (arXiv:0710.1172, 2007) prove combinatorial Alexander **homology** duality; this does not determine a dual complex's attaching maps or homotopy type.

The closest directly comparable published calculation is *Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph* (public result ID `c6098fc06928`, 2026-10-11). It computes the **nonblocking/theta** complex \(\Theta=\{U:U\cap L=\varnothing\text{ for some line }L\}\), obtaining \(\Theta\simeq\bigvee^{39}S^4\vee S^5\). The theta complex is the combinatorial Alexander dual of \(X\), not \(X\) itself: its face count is \(3862\) including the empty face, versus \(4330\) for \(X\). Its known homotopy type and Alexander duality imply the *homology ranks* of \(X\), but not the claimed integral homotopy wedge or the rational projective-group character and quotient. The latter conclusions are the new content.

A separate calculation of the line-free and theta complexes of the nine-point affine plane concerns twelve **three-point** affine lines, not the thirteen **four-point** projective lines here. The graph-metric Rips constructions on incidence graphs are likewise different simplicial complexes. Related results are compared by implication, not by similarity of titles or numbers.

## Limitations
This establishes an exact finite-case integral homotopy equivalence and the full rational character under the indicated projective collineation group. It does not assert a general formula for larger projective planes, an equivariant homotopy wedge, an integral decomposition of \(\mathbb Z[G]\)-modules, or a homotopy classification of the quotient. Exhaustive literature searching cannot rule out unpublished or unindexed equivalent work; publication priority remains provisional. Independent external mathematical validation has not been performed.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first version 2008-08-05), especially the definitions and discrete-vector-field examples. https://arxiv.org/abs/0808.0739
2. A. Björner and M. Tancer, *Combinatorial Alexander Duality—A Short and Elementary Proof*, arXiv:0710.1172 (first version 2007-10-05), Theorem 1.1. https://arxiv.org/abs/0710.1172
3. *Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph*, public result dated 2026-10-11, identifier `c6098fc06928`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-complex-homotopy-of-the-ternary-p--c6098fc06928
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for the discrete-Morse CW reduction.
