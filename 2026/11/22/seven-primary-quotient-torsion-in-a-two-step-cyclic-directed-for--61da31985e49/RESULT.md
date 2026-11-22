# Seven-primary quotient torsion in a two-step cyclic directed-forest complex

## Finding

Let \(D=\operatorname{Cay}(\mathbb Z/7\mathbb Z;\{1,2\})\) be the directed Cayley graph with arcs \(i\to i+1\) and \(i\to i+2\), and let \(X=\operatorname{DF}(D)\) be its directed-forest complex. Sevenfold vertex translation acts simplicially on \(X\); write \(Y=|X|/(\mathbb Z/7\mathbb Z)\) for the *geometric* orbit space. Then

\[
|X|\simeq\bigvee^{29}S^5,\qquad \pi_1(Y)\cong\mathbb Z/7\mathbb Z,
\]

and the full integral quotient homology is

\[
H_j(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/7\mathbb Z,&j=1,3,\\
\mathbb Z^5,&j=5,\\
0,&\text{otherwise}.
\end{cases}
\]

Moreover the action on rational top homology is

\[
\widetilde H_5(X;\mathbb Q)\cong
\mathbb Q\oplus\mathbb Q[\mathbb Z/7\mathbb Z]^{\oplus4}
\]

as a rational representation of the rotation group. This exhibits order-seven torsion in degrees one and three of a quotient whose covering complex has free integral homology.

## Assumptions and scope

Here a directed forest is a selected set of directed arcs with **at most one entering arc per graph vertex and no directed cycle**. Isolated vertices are permitted. The simplices are exactly these arc sets; their subfaces inherit the same conditions. The empty set is used in the augmented face-poset computation. The group \(C_7=\mathbb Z/7\mathbb Z\) acts by simultaneous addition to the source and target of each selected arc. The quotient is a geometric CW orbit space, **not** the simplicial complex formed merely from vertex orbits. All homology is singular homology with indicated coefficients. No statement is made about other cyclic moduli or generators.

## Proof

**1. Complete enumeration and acyclic matching.** Order the 14 arcs lexicographically as the pairs \((i,j)\), with \(i\in\{0,\ldots,6\}\) and \(j=i+1\) or \(i+2\) modulo seven. An arc subset is admissible exactly when every target appears at most once and following predecessor pointers never creates a directed cycle. Testing all \(2^{14}=16384\) masks therefore provides an exhaustive oracle, not a sample. There are 1849 faces, including the empty face, with cardinality enumeration

\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)=(1,14,84,280,553,616,301).
\]

On the augmented face poset, process the seven \(+1\) arcs in increasing source order, followed by the seven \(+2\) arcs in increasing source order. At each pivot, pair every *currently unmatched* face not containing that arc with its arc-added face whenever both are still unmatched. The prescribed matching has 910 pairs, leaving precisely 29 unpaired faces, all six-element simplices (dimension five). To certify Forman acyclicity, direct each Hasse incidence of the full augmented poset from the higher to the lower face, reversing the matched incidences. The supplied standalone verifier topologically sorts this **entire** 1849-vertex incidence digraph, finding no directed cycle. Each pivot pairing is also structurally acyclic: a reversed incidence can insert only the current pivot, while every other incidence removes an earlier fixed or later variable vertex, and the complete check eliminates any cross-pivot ambiguity. The empty face is paired with a vertex; after unaugmenting, the standard discrete-Morse CW structure has one zero-cell and 29 five-cells and no cells in dimensions one through four. All five-cell attaching maps land in the zero-cell, so \(|X|\simeq\bigvee^{29}S^5\) over the integers.

**2. Free cyclic action.** Every nonzero translation in \(C_7\) generates the whole group. Its 14-arc action has exactly two orbits, each of length seven, namely the complete \(+1\) orbit and the complete \(+2\) orbit. A nonempty invariant simplex would contain a whole such orbit, hence a directed Hamiltonian 7-cycle, contradicting admissibility. Thus no nontrivial rotation stabilizes any nonempty face setwise and the induced action on \(|X|\) is free. Because \(|X|\) is simply connected, \(|X|\to Y\) is the universal seven-sheeted cover and \(\pi_1(Y)\cong C_7\).

**3. Low quotient homology.** Since the cover is a wedge of five-spheres, its reduced integral homology vanishes below degree five. The Cartan–Leray homology spectral sequence for a free action consequently gives \(H_j(Y;\mathbb Z)\cong H_j(C_7;\mathbb Z)\) for \(0\le j\le4\). A period-two free resolution of the trivial \(\mathbb Z[C_7]\)-module alternates multiplication by \(g-1\) and by \(1+g+\cdots+g^6\); after tensoring with \(\mathbb Z\), these become zero and multiplication by seven. Thus the groups in degrees one and three are \(\mathbb Z/7\mathbb Z\), those in degrees two and four vanish, and degree zero is \(\mathbb Z\).

**4. Top quotient group and rational rotation character.** The action is free on all simplices, so the Euler characteristic scales: \(\chi(Y)=\chi(X)/7=(1-29)/7=-4\). The quotient is connected and five-dimensional. Its top integral homology embeds into the free abelian cellular group of top-degree cells, hence has no torsion; the Euler characteristic and the low-degree groups force \(H_5(Y;\mathbb Z)\cong\mathbb Z^5\) and no homology in higher degrees. For each nonidentity translation the Lefschetz number on \(|X|\) vanishes because there are no fixed points. As reduced homology is confined to odd degree five, this gives trace one on \(\widetilde H_5(X;\mathbb Q)\) at every nonidentity group element; the identity trace is 29. Rational irreducible characters of \(C_7\) consist of the trivial character and the six-dimensional cyclotomic character. These traces uniquely determine \(\mathbb Q\oplus\mathbb Q[C_7]^{\oplus4}\).

## Verification

The included `verify.py` uses only the Python 3 standard library and reconstructs both the base simplicial complex and the quotient. It asserts 1849 admissible faces, face vector above, 910 matching pairs, 29 critical five-faces, and complete Hasse-incidence acyclicity; it verifies freedom of all six nontrivial rotations on every nonempty face. It then builds the exact **signed integer cellular boundaries** of the 264-cell orbit CW structure (orbit-cell counts \((2,12,40,79,88,43)\) in dimensions zero through five), checks every boundary composition vanishes, and independently computes field Betti vectors \((1,0,0,0,0,5)\) modulo two and three, and \((1,1,1,1,1,5)\) modulo seven. These field checks are cross-checks; the stated integral torsion orders and homotopy type follow from the proof, not from a field-rank inference. Run `python3 verify.py` from any directory.

## Relationship to prior work

Directed-forest complexes of finite Cayley graphs were studied by Courtney (public seminar in November 2019 and thesis in 2020). The public abstract of the thesis provides the general research framework, not an inspected full text; it therefore cannot be used to assert that the thesis lacks the present example. General results on shellability of directed trees and forest complexes concern structural criteria that do not imply the computed sevenfold orbit-space torsion. The nearest indexed seven-vertex result studies the quadratic-residue **tournament** directed-forest complex, whereas another computes the sevenfold quotient of a cyclic tournament's **multipath** complex, imposing both in-degree and out-degree restrictions; neither statement implies the present homotopy and quotient-homology formula for the sparse two-generator digraph. Results about two isolated shortcuts in an oriented cycle also do not cover an entire second seven-arc translation orbit.

## Limitations

This is a finite, exactly specified digraph, not a theorem for general cyclic groups or arbitrary Cayley generators. The rational symmetry-module is determined; an integral \(\mathbb Z[C_7]\)-module splitting is **not** claimed. The quotient's homology and fundamental group do not determine its full homotopy type. An apparently relevant 2020 Cayley-graph thesis could not be inspected in full because its available download returned an access error; equivalence hidden in that text or unindexed literature remains possible. The results have not received independent external validation.

## References

1. Kennedy Courtney, “The Directed Forest Complex and Shellability,” Boise State topology seminar, November 15, 2019: https://www.boisestate.edu/math/research/seminars/topology/
2. Kennedy Courtney, *The Directed Forest Complex of Cayley Graphs*, master's thesis, Boise State University, May 2020: https://scholarworks.boisestate.edu/td/1684/
3. Duško Jojić, *Shellability of complexes of directed trees*, arXiv:1109.4475: https://arxiv.org/abs/1109.4475
4. Anurag Singh, *Vertex decomposability of complexes associated to forests*, arXiv:2101.05534: https://arxiv.org/abs/2101.05534
5. Priyavrat Deshpande and Rutuja Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936: https://arxiv.org/abs/2602.14936
6. Indexed seven-vertex quadratic-residue tournament forest-complex result: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-directed-forest-topology-and-affine-homology-of-the-seven-vertex--00780bf1e6fb
7. Indexed seven-vertex cyclic-tournament multipath quotient result: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-seven-primary-torsion-in-the-cyclic-tournament-multipath-rotatio--e63367854768
8. Indexed oriented-cycle double-shortcut result: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-adjacency-sensitive-sphere-wedges-from-two-forward-shortcuts-in--6b8bf75ceac4
