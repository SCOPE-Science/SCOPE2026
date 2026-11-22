# The four-by-four knight symmetry quotient is a three-sphere

## Finding

Let \(K\) be the independence complex of the ordinary nonperiodic knight-attack graph on the \(4\times4\) square board, and let \(D_4\) act through its eight geometric rotations and reflections. For the **ordinary geometric quotient** (not the Borel quotient),
\[
\boxed{|K|/D_4\simeq S^3.}
\]
In particular, its fundamental group vanishes, its reduced integral third homology is \(\mathbb Z\), and every other reduced integral homology group vanishes. The space \(|K|\) itself has been classified as a wedge of five three-spheres in previous work; the integral **orbit-space homotopy type** is the additional result.

## Assumptions and scope

Squares are pairs \((r,c)\) with \(0\le r,c<4\). Distinct squares attack exactly when their absolute row and column differences are \(1\) and \(2\), in either order. A simplex of \(K\) is any set of squares containing no attacking pair, not merely a maximal placement. There is no toroidal identification. The group \(D_4\) acts on squares by square-board isometries. Its quotient is taken after geometric realization and is not asserted to be a quotient simplicial complex on vertex-orbits.

## Proof

**A regular cell model.** Enumerate every nonempty independent face as a 16-bit integer mask. There are 24 knight-attack edges and exactly 1,364 such faces. Their simplex-dimension counts are
\[
(16,96,276,412,340,170,48,6).
\]
Barycentrically subdivide \(K\): a simplex is a nonempty strictly increasing chain of nonempty faces. Every group element preserving a chain fixes each face of that chain individually, since the face cardinalities are distinct. Thus every chain stabilizer fixes its barycentric simplex pointwise. The orbits of chains consequently give a regular-cell description of \(|K|/D_4\). The face maps delete one element from the chain, and the canonical representative is its lexicographically least image under the eight group elements. The signed cellular boundary has coefficient \((-1)^j\) on the face obtained by deleting the element in position \(j\). Two different deletion positions cannot identify the same face-orbit because they delete different cardinalities.

The exact counts of chain-orbit cells in dimensions zero through seven are
\[
(217,4801,35910,126666,239340,249840,136080,30240).
\]
An independent Burnside count, averaging the numbers of fixed chains for the eight group elements, yields the same vector.

**Topological reductions.** In the orbit-chain cell complex, repeatedly choose a codimension-one cell with exactly one incident higher-dimensional cell, of signed incidence \(\pm1\), and remove this free face and its unique coface. The executable enumerator specifies every such choice deterministically by its queue order and checks adjacency in the finite cell structure. There are exactly 411,365 such elementary collapses. The remaining three-dimensional subcomplex has cell counts
\[
(c_0,c_1,c_2,c_3)=(22,102,160,80)
\]
and no higher-dimensional cells. These removals preserve the ordinary homotopy type, not merely its homology.

**Integral homology.** The surviving signed cellular boundary matrices satisfy \(\partial^2=0\). Exact integral eliminations using only unit coefficients \(\pm1\), with the required row and column operations, cancel 21 degree-one pairs, 81 degree-two pairs, and 79 degree-three pairs. This leaves one degree-zero generator, one degree-three generator, and no other generators or nonzero differentials. The reductions are unimodular, so they preserve integral torsion information: \(H_0\cong\mathbb Z\), \(H_3\cong\mathbb Z\), and \(H_i=0\) for all other positive degrees.

**The fundamental group.** On the surviving three-dimensional subcomplex, choose a spanning tree of the 22-vertex, 102-edge one-skeleton. Its 21 tree edges disappear from the standard edge-path presentation, leaving 81 generators. The 160 triangular two-cells give the relators \(e_{ab}e_{bc}e_{ac}^{-1}\), interpreted through the orbit identifications and with tree edges set to the identity. Every one of the 81 generators is eliminated by a Tietze move in which its chosen relator contains that generator exactly once; in this calculation the selected relators have length one after previous eliminations. All remaining relators freely reduce to the empty word. Hence \(\pi_1(|K|/D_4)=1\). The executable group-presentation check reconstructs the edge endpoints and triangle incidences from orbit-chain representatives, rather than inferring simple connectivity from homology.

The quotient is therefore simply connected and has vanishing second homology, hence \(\pi_2=0\) by Hurewicz. Its third Hurewicz map is an isomorphism onto \(H_3\cong\mathbb Z\). A generator gives a map \(S^3\to|K|/D_4\) inducing an isomorphism on all integral homology groups. The simply connected homological Whitehead theorem makes this map a homotopy equivalence.

## Verification

The standalone files `verify_quotient_cells.cpp`, `verify_integral_homology.py`, `verify_fundamental_group.py`, and `verify_burnside.py` reproduce the construction. From their directory, run:

```sh
g++ -O2 -std=c++17 -o verify_cells verify_quotient_cells.cpp
./verify_cells
python3 verify_integral_homology.py
python3 verify_fundamental_group.py
python3 verify_burnside.py
```

The C++ program writes `quotient_reduced.txt`, whose exact content is also supplied as an independently inspectable finite certificate. The Python programs use the standard library only. The integral program checks signed boundary compositions and every unit cancellation. The fundamental-group program checks every edge and triangle orbit identification before eliminating the generators. The separate Burnside program enumerates all 1,364 independent faces by a different algorithm, recomputes the 24 attack edges, and independently validates every dimension's chain-orbit cell count.

## Relationship to prior work

Bode and Harborth (2000) calculate maximum nonattacking-piece numbers, including exactly six maximal eight-knight placements on the ordinary four-by-four board; this does not determine the topology of the complex of *all* placements, much less its geometric orbit space. Berghammer (2011) independently discusses that same square-board placement census and attack graphs, without computing orbit-space homotopy. Bousquet-Mélou, Linusson and Nevo (2007) establish foundational independent-set topology for nearest-neighbor square-grid graphs; their adjacency relation differs from the knight graph here.

The closest directly relevant subsequent homotopy results identify \(K\simeq\bigvee^5S^3\) and the rational dihedral character \(\mathbf1\oplus2\eta\oplus\rho\). Thus the quotient's rational third Betti number was already one. Neither statement alone determines whether the geometric quotient has integral torsion or nontrivial fundamental group. The present finite cell and presentation calculations resolve those additional possibilities. Analyses of other square-grid matching complexes and of the toroidal knight graph concern different graphs or different group actions and do not imply this classification.

## Limitations

The result is for exactly the ordinary \(4\times4\) knight graph and the full square dihedral group. No statement is made about larger boards, proper subgroups, equivariant homotopy of \(K\), or smooth/PL homeomorphism of the quotient with a round sphere. The proof gives a homotopy equivalence, not a homeomorphism. Computational counts are exhaustive for this finite object and do not establish a general formula. An unindexed equivalent computation remains possible; an independent mathematical audit has not been performed.

## References

1. J.-P. Bode and H. Harborth, *Independent Chess Pieces on Euclidean Boards*, Journal of Combinatorial Mathematics and Combinatorial Computing **33** (2000), 209–223. https://combinatorialpress.com/article/jcmcc/Volume%20033/vol-033-paper%2014.pdf
2. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public submission 2007-01-30. https://arxiv.org/abs/math/0701890
3. R. Berghammer, *Relational Modelling and Solution of Chessboard Problems*, in RAMICS 2011, LNCS **6663**, 92–108. https://www.cs.cornell.edu/courses/cs6861/2024sp/Papers/ramics12.pdf
4. *The first noncontractible square knight-placement complex and its dihedral homology*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-the-first-noncontractible-square-knight-placement-complex-and-it--36a4a95dc753/RESULT.md
5. *First noncontractible square-knight complexes and a dihedral homology transition*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-first-noncontractible-square-knight-complexes-and-a-dihedral-hom--9354f4ac73dc/RESULT.md
