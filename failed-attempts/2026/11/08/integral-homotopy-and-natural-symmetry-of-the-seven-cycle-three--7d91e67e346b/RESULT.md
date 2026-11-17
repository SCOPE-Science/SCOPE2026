# Integral homotopy and natural symmetry of the seven-cycle three-color categorical product

## Finding

Let \(G=C_7\times K_3\) be the **categorical** graph product, and let \(I=\operatorname{Ind}(G)\) be its ordinary independence complex. Then
\[
I\simeq S^3\vee S^4\vee S^4\vee S^4.
\]
In particular, \(\widetilde H_3(I;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_4(I;\mathbb Z)\cong\mathbb Z^3\), and all other reduced integral homology vanishes.

Moreover, for the natural \(D_7\times S_3\) action (cycle dihedral symmetries and simultaneous permutations of the three colors), the complete rational homology representations are
\[
\widetilde H_3(I;\mathbb Q)\cong\epsilon_D\boxtimes\operatorname{sgn}_3,
\qquad
\widetilde H_4(I;\mathbb Q)\cong\mathbf1_D\boxtimes(\operatorname{sgn}_3\oplus\operatorname{Std}_3).
\]
Here \(\epsilon_D\) is trivial on rotations and negative on reflections; \(\operatorname{sgn}_3\) is the sign character of color permutations, and \(\operatorname{Std}_3\) is their two-dimensional standard rational representation. Thus all seven-cycle rotations act trivially on homology, reflections act by \(-1\) in degree three and \(+1\) in degree four, and the \(D_7\times S_3\)-invariant reduced rational homology is zero.

## Assumptions and scope

The graph is simple, with 21 vertices \((i,c)\), where \(i\in\mathbb Z/7\mathbb Z\) and \(c\in\{0,1,2\}\). Vertices \((i,c)\) and \((j,d)\) are adjacent precisely if \(j-i\equiv\pm1\pmod7\) and \(c\ne d\). This is not the Cartesian or strong product. Set \(v=3i+c\in\{0,\ldots,20\}\), and represent a simplex by the binary mask \(\sum_{v\in\sigma}2^v\). An independent set, including the empty set for augmented chains, is a subset with no graph edge. The theorem concerns this single 21-vertex graph; no all-parameter statement is made.

## Proof

**Exhaustive finite complex.** The verifier starts with the empty mask. At index \(v=0,\ldots,20\), it adds \(2^v\) to exactly the previously generated independent masks whose selected vertices avoid the neighbors of \(v\). It therefore enumerates each independent subset exactly once by induction on the index. There are 5,281 nonempty faces; the face numbers in dimensions \(0,\ldots,8\) are
\[
(21,168,658,1365,1554,1022,402,84,7).
\]

**Acyclic matching and Morse cells.** For \(v=0,1,\ldots,20\) in order, scan presently unmatched nonempty faces by ascending integer mask, and match each face \(\sigma\) missing \(v\) with \(\sigma\cup\{v\}\) if both remain unmatched; remove both from further consideration. The empty face is not paired. This specifies 2,635 distinct cover relations. Reverse these and orient all other covers downward. The complete directed augmented Hasse diagram has 5,282 vertices and 25,242 directed edges; Kahn topological sorting processes all 5,282 vertices. Hence there is no directed cycle, even when the empty face is included. The unmatched nonempty faces are one vertex, four three-simplices and six four-simplices. Discrete Morse theory gives a CW model with exactly one zero-cell, four three-cells and six four-cells, and no other cells.

**Exact integral attaching data.** Orient simplices by ascending vertex index; deleting vertex \(v\) gives incidence \((-1)^{|\{u\in\sigma:u<v\}|}\). The critical degree-three masks, in order, are
\[
12312,\;12328,\;20504,\;20520,
\]
and the critical degree-four masks are
\[
299152,\;299296,\;598088,\;598304,\;1196104,\;1196176.
\]
Compute the integral Morse differential by signed gradient-path elimination. A critical three-simplex projects to its basis vector. A three-simplex paired as the upper member with a two-simplex projects to zero. If a three-simplex \(\tau\) is matched above by the four-simplex \(\eta\), let \(\varepsilon(\sigma,\eta)\in\{+1,-1\}\) denote its oriented simplicial incidence. Its projection is computed recursively from
\[
P(\tau)=-\varepsilon(\tau,\eta)
\sum_{\substack{\sigma\subset\eta,\;|\sigma|=4\\\sigma\ne\tau}}
\varepsilon(\sigma,\eta)P(\sigma).
\]
The verified absence of directed gradient cycles proves termination. Applying \(P\) to each oriented critical four-cell boundary yields the following integer \(4\times6\) differential, with critical three-cells indexing rows:
\[
\partial_4^{\mathrm{Morse}}=
\begin{pmatrix}
-1&0&-1&-1&0&-1\\
0&0&0&1&0&1\\
0&0&0&1&0&1\\
0&-1&0&-1&-1&-1
\end{pmatrix}.
\]
The second and third rows coincide, so its rank is at most three. The minor in zero-based rows \((0,1,3)\), columns \((0,1,3)\), has determinant \(-1\), so its rank is exactly three and its nonzero Smith factors are \(1,1,1\). This is an integral statement, not an inference from finite fields.

The Morse three-skeleton is a wedge of four three-spheres; the homotopy classes of attaching maps for the six four-cells are completely determined by the displayed degree matrix because \(\pi_3(\bigvee^4S^3)\cong\mathbb Z^4\). Unimodular changes of bases of these groups arise from homotopy equivalences and elementary cell slides. Cancelling the three degree-one pairs leaves one three-sphere and three four-spheres, proving the asserted homotopy equivalence over \(\mathbb Z\).

**Symmetry character.** A natural element is \((i,c)\mapsto(ai+b,\pi(c))\), where \(a\in\{+1,-1\}\), \(b\in\mathbb Z/7\mathbb Z\), and \(\pi\in S_3\). For a simplicial automorphism \(g\), the reduced Lefschetz trace equals the signed alternating sum of all fixed simplices, including the empty simplex in degree \(-1\):
\[
\widetilde L(g)=\sum_{\substack{\sigma\in I\cup\{\varnothing\}\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
The verifier evaluates this sum exactly for all 84 elements and obtains the following table. The columns are color-permutation classes: identity, transposition, and three-cycle. The rows are a dihedral rotation and a reflection, respectively:
\[
\begin{array}{c|rrr}
&1&(12)&(123)\\\hline
\text{rotation}&2&0&-1\\
\text{reflection}&4&-2&1
\end{array}.
\]
Every rotation has identical values for its row, and every reflection has identical values for its row.

Since rational representations of a cyclic group of order seven have irreducible dimensions one or six, its rotations act trivially on both homology groups (of dimensions one and three). Thus the action factors through \(C_2\times S_3\). Write \(\chi_d\) for the degree-\(d\) homology character, so the table records \(-\chi_3+\chi_4\). The reflection/identity entry \(4\) forces \(\chi_3(\text{reflection})=-1\) and \(\chi_4(\text{reflection})=3\) by the dimensions and order-two eigenvalues. Consequently reflections act by a scalar on both groups as claimed. Each one-dimensional rational \(S_3\)-representation is trivial on three-cycles, and the rotation/three-cycle entry \(-1\) forces \(\chi_4((123))=0\). A three-dimensional rational \(S_3\)-module with three-cycle trace zero must be a one-dimensional summand plus the two-dimensional standard module. The rotation/transposition entry \(0\) and reflection/transposition entry \(-2\) force the one-dimensional summand and the degree-three module both to be the sign representation. This establishes the two displayed rational representation decompositions without assuming that the Morse matching preserves symmetry.

## Verification

Execute `python3 verify.py` using only the Python standard library. The program regenerates the graph, all faces, the face-poset orientation, all gradient projections and the signed integral Morse differential. It checks the determinant \(-1\) of the explicit maximal-rank minor. An independent bitset Gaussian elimination of the **original simplicial boundaries over \(\mathbb F_2\)** in all dimensions gives Betti numbers \((1,0,0,1,3,0,0,0,0)\); this is corroboration, not the integral proof. The program independently checks adjacency preservation and oriented Lefschetz sums for each of the 84 proposed automorphisms. Full expected output is recorded in `verification_output.txt`.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (arXiv:2307.12401v2, Theorem 23 and Question 24, pp. 25–27) prove that these cycle–complete product complexes have homology in at most two consecutive dimensions, possibly with Moore-space summands, and explicitly list \(C_7\times K_3\) among examples having free homology in both degrees. Their statement does not provide the present integral attaching matrix, eliminate possible torsion for this case, or give its dihedral-and-color homology character. Their question asks if all such complexes are torsion-free; this result settles only one named instance.

A separately published computation identifies \(\operatorname{Ind}(C_7\times K_4)\simeq\bigvee^3S^3\vee\bigvee^6S^4\); four colors are a different graph and do not imply this three-color homotopy or its natural \(D_7\times S_3\)-action. Carnero Bravo (arXiv:2505.06457) analyzes products involving a path factor; that focus is not an explicit determination of this cycle–complete product. Kozlov (arXiv:math/0503613v1, March 28, 2005) provides early finite collapse and simple-homotopy methodology in topological combinatorics, not a graph-product calculation. The 2005 methodological source is the dated archival anchor; the concrete unresolved cycle-product question was articulated publicly in 2023.

## Limitations

The claim is for the single specified graph, not an all-parameter torsion-free theorem. It determines rational symmetry modules for the natural 84-element subgroup, not integral group-ring lattices or an equivariant wedge decomposition. The topological result is proved by an exhaustive finite Morse calculation; it is not certified by independent human validation. Earlier unindexed or indirect results may exist, and priority has not been independently established.

## References

- D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, first public March 28, 2005, arXiv:math/0503613v1. https://arxiv.org/abs/math/0503613
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v2 (2023), Theorem 23 and Question 24, pp. 25–27. https://arxiv.org/pdf/2307.12401
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v2 (2025). https://arxiv.org/pdf/2505.06457
- *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors*, online mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-torsion-free-mixed-dimensional-sphere-wedge-for-the-seven-cycl--50b8be4e4c8f
