# The Fano incidence two-independence complex is \(\bigvee^{13}S^5\), with a full symmetry character

## Finding
Let \(V=\mathbf F_2^3\setminus\{0\}\), with seven nonzero vectors. The Heawood graph \(H\) has point vertices \(p_x\), line vertices \(\ell_y\), and exactly the incidences \(p_x\sim\ell_y\) for \(x,y\in V\) satisfying \(x\cdot y=0\) in \(\mathbf F_2\). Set \(K=\operatorname{Ind}_2(H)\): a set of graph vertices is a simplex if and only if every induced connected component has at most two vertices (equivalently, induced maximum degree at most one).

Then, integrally,
\[
K\simeq\bigvee^{13}S^5,\qquad
\widetilde H_i(K;\mathbb Z)=\begin{cases}\mathbb Z^{13},&i=5,\\0,&i\ne5.\end{cases}
\]
Let \(G=\operatorname{Aut}(H)\), and let \(B\cong\operatorname{GL}_3(\mathbf F_2)\) be its index-two subgroup preserving point and line classes. Let \(\varepsilon:G\to\{\pm1\}\) be the character with value \(+1\) on \(B\) and \(-1\) outside \(B\). Let \(U\) denote the six-dimensional augmentation representation of \(B\) on the seven nonzero vectors of \(\mathbf F_2^3\). Then the **complete rational symmetry representation** is
\[
\widetilde H_5(K;\mathbb Q)\cong
\varepsilon\oplus\operatorname{Ind}_{B}^{G}U.
\]
In particular, for a class-preserving symmetry represented by \(M\in B\), with \(f(M)=|\{x\in V:Mx=x\}|\), its trace is \(2f(M)-1\); every class-exchanging symmetry has trace \(-1\). The full-group invariant homology vanishes, so \(\widetilde H_*(K/G;\mathbb Q)=0\). This is not a claim that the quotient is contractible.

## Assumptions and scope
The field, graph, simplicial faces, homology coefficients, and group actions are exactly those just defined. Index the fourteen graph vertices by integers \(0,\ldots,13\), with point \(p_x\) assigned index \(x-1\) and line \(\ell_y\) index \(y+6\), where nonzero three-bit integers represent elements of \(V\). A face is represented by its fourteen-bit subset mask. All enumerations cover every one of the \(2^{14}\) masks; no random sampling is involved. The stated homotopy type is non-equivariant; only the induced homology action is calculated equivariantly.

The group \(B\) consists of all invertible linear maps on the points, acting on covectors as the contragredient \(M^{-T}\). The polarity \(d(p_x)=\ell_x\), \(d(\ell_x)=p_x\) exchanges the classes. The unique bipartition of the connected incidence graph shows that every automorphism either preserves or exchanges them; a class-preserving automorphism is a collineation of the binary projective plane, hence is linear. Thus \(|G|=2|\operatorname{GL}_3(\mathbf F_2)|=336\), with \(|B|=168\).

## Proof
**1. The complete face set.** For each mask \(s\), check every selected vertex \(i\): the bit count of the intersection of \(s\) with its graph-neighbor mask must be at most one. Independently, enumerate all connected components of the induced graph and require cardinality at most two. These predicates agree on all \(16384\) masks. There are \(2256\) nonempty faces, with dimensions zero through six having counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(14,91,322,651,728,392,58).
\]

**2. A complete acyclic matching.** On the poset of nonempty faces, visit pivot vertices \(0,1,\ldots,13\) in that order. At a pivot \(v\), pair every still-unmatched face \(s\) not containing \(v\) with \(s\cup\{v\}\) when the latter is also still unmatched; remove both and proceed. These are cover pairs of the full face poset. The algorithm produces exactly \(1121\) disjoint pairs, leaving one critical vertex (mask \(1\)) and exactly thirteen critical five-simplices. Their masks, in ascending order, are
\[
1008,3300,5460,6712,8064,9826,10600,12160,12504,14208,15232,15744,16000.
\]
To verify acyclicity without assuming a property of the greedy procedure, orient each Hasse cover upward if matched and downward otherwise. Every cover between nonempty faces is included, giving exactly \(10150\) directed edges. Kahn's topological sort removes all \(2256\) vertices. Hence no directed cycle exists, and the matching is acyclic. The matching and the complete acyclicity test are reproduced by the accompanying checker.

**3. Integral homotopy.** Forman's discrete Morse theorem provides a CW homotopy model with one zero-cell and thirteen five-cells and no other cells. Every five-cell is attached to the unique zero-cell, because there are no intermediate-dimensional cells. Thus its attaching map is nullhomotopic and the CW complex is the stated wedge of thirteen five-spheres. In particular there is no integral torsion. Independent mod-two boundary reduction gives ranks \((13,78,244,407,321,58)\) in dimensions one through six, and reduced Betti vector \((0,0,0,0,0,13,0)\), corroborating but not replacing the integral Morse argument.

**4. Complete symmetry character.** All \(168\) matrices are enumerated by choosing three linearly independent nonzero binary columns; their dual actions on the lines follow from \(y\cdot x=(M^{-T}y)\cdot(Mx)\). Composing with the point-line polarity gives the other \(168\) graph automorphisms. For each one, the signed simplicial Lefschetz trace is calculated from *all* setwise-fixed faces, including the reduced empty-face contribution. Since homology is concentrated in reduced degree five,
\[
\chi(g)=\sum_{J\subseteq\mathcal C(g):\ \cup J\in K}(-1)^{|J|},
\]
where \(\mathcal C(g)\) is the family of cycles of the permutation of fourteen vertices, and the empty union is admitted. The formula follows by expressing a setwise-fixed face as a union of cycles: the orientation sign of its vertices cancels its alternating face-size sign, leaving one minus sign per chosen cycle. It is also evaluated by an independent fixed-face orientation calculation for every automorphism. Both methods give the same values on all \(336\) elements.

For class-preserving automorphisms, the trace is \(2f(M)-1\). The values are \(13\) for the identity (one element), \(5\) when \(f=3\) (21 elements), \(1\) when \(f=1\) (98 elements), and \(-1\) when \(f=0\) (48 elements). Every one of the \(168\) class-exchanging automorphisms has trace \(-1\). Consequently the full histogram is \((-1:216,\ 1:98,\ 5:21,\ 13:1)\). The full-group character has inner product \(3\) with itself, inner product \(0\) with the trivial character, and inner product \(1\) with \(\varepsilon\).

**5. Representation identification.** The character of the six-dimensional augmentation module \(U\) at \(M\in B\) is \(f(M)-1\). Its conjugate under polarity is the corresponding line-augmentation character and has the same values because a matrix and its inverse transpose have equal fixed-space dimensions over \(\mathbf F_2\). Therefore \(\operatorname{Ind}_B^G U\) has trace \(2(f(M)-1)\) on \(B\) and zero on the other coset. Adding \(\varepsilon\) gives exactly the calculated \(2f(M)-1\) and \(-1\). Maschke's theorem and equality of rational characters establish the rational module isomorphism. By transfer/averaging for a finite group in characteristic zero, rational quotient homology equals the invariant homology, which vanishes in positive degrees; connectedness gives zero reduced degree-zero homology.

## Verification
Run `python3 verify_heawood_two_ind.py` with Python 3.10 or later (standard library only). It exhaustively checks the two face predicates, reconstructs the matching, verifies every directed Hasse cover and topologically sorts the entire graph, calculates independent mod-two boundary ranks, enumerates all invertible binary matrices and all class-exchanging dualities, verifies incidence preservation, and computes each symmetry trace by both oriented fixed faces and cycle-union enumeration. The included `verification_output.txt` is the recorded output of executing that exact script. The run finishes with `ALL_CHECKS_PASS`.

## Relationship to prior work
Taylan's 2015 devoid-complex paper establishes the framework and explicit classifications for paths, cycles, and forests; the Fano incidence graph is none of these. Deshpande and Singh (2020 preprint, later journal article) classify higher-independence complexes of complete multipartite, fully whiskered, path, cycle and perfect-ary-tree graphs, none of which is the Heawood graph. Nilakantan and Shukla study *ordinary* independence complexes of a cyclic-neighborhood bipartite family, not the two-independence complex here. The published ordinary Heawood independence computation \(\bigvee^{6}S^3\) and the Heawood *edge matching* homology character concern different simplicial complexes, and neither implies the present homotopy theorem or its thirteen-dimensional vertex-complex action. A Fano nonincidence two-independence calculation likewise concerns the complementary bipartite incidence relation and does not imply this claim. Indexed comparisons found no covering theorem, though unindexed or differently worded work remains possible.

## Limitations
This proves a homotopy and rational homology-action theorem for one precisely specified fourteen-vertex incidence graph. It does not classify incidence graphs of larger projective planes, assert an equivariant homotopy equivalence, determine an integral decomposition of the symmetry lattice, or determine integral torsion in the quotient. Finite computations are exhaustive for this single graph, not evidence for a general infinite family. Publication priority remains subject to unindexed literature and independent mathematical review.

## References
- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first posted 2015-01-27), particularly the introductory scope and the path/cycle/forest results.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first posted 2020-01-15), particularly the introductory classification list.
- N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1 (first posted 2017-09-14), Theorem 1.2.
- *The Heawood independence complex is \(\bigvee^{6}S^3\)*, public published-finding corpus research record `dbd95019d1e2`, RESULT.md.
- *Full \(\operatorname{Aut}(H)\)-module of the Heawood matching complex*, public published-finding corpus research record `d7a042784870`, RESULT.md.
