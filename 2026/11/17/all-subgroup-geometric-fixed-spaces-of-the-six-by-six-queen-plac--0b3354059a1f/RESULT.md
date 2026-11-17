# All-subgroup geometric fixed spaces of the six-by-six queen-placement complex

## Finding
Let \(Q_6\) be the graph on the thirty-six squares \((i,j)\), \(0\le i,j\le5\), of an ordinary nonperiodic chessboard; two different squares are adjacent if they have a common row, column, or diagonal. Write \(K=\operatorname{Ind}(Q_6)\) for the complex of every partial nonattacking-queen placement (including the empty face). The natural square-symmetry group \(D_4=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle\), where \(r(i,j)=(j,5-i)\) and \(s(i,j)=(i,5-j)\), acts simplicially.

**The complete classification of actual geometric subgroup-fixed spaces** is as follows:

| Subgroup \(H\) | Geometric fixed-space homotopy type |
|---|---|
| Trivial subgroup | \(M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{19}S^3\) (previously known) |
| Central half-turn \(\langle r^2\rangle\) | \(\bigvee^7S^1\) |
| Quarter-turn subgroup \(\langle r\rangle\) | Six discrete points |
| Either diagonal-reflection subgroup \(\langle rs\rangle,\langle r^3s\rangle\) | Six discrete points |
| Either horizontal/vertical-reflection subgroup \(\langle s\rangle,\langle r^2s\rangle\) | Empty |
| Either Klein-four subgroup \(\langle r^2,s\rangle,\langle r^2,rs\rangle\) | Empty |
| Entire \(D_4\) | Empty |

In particular, the half-turn fixes a connected space with nontrivial free integral first homology of rank seven, despite the ambient complex having only two-torsion in integral second homology and free homology in dimension three. This classification is at the level of **geometric fixed points**, not the fixed vertices alone or the rational character.

## Assumptions and scope
A subset \(F\) of the thirty-six squares is a face if and only if every two different squares \((i,j),(u,v)\in F\) satisfy \(i\ne u\), \(j\ne v\), and \(|i-u|\ne|j-v|\). The group acts on the geometric realization through permutation of vertices. The theorem covers all ten subgroups of \(D_4\) (including the trivial subgroup and the full group), over integral coefficients where homology is discussed. The known nonequivariant homotopy type in the first row is cited background, not the claimed new result.

## Proof
**Orbit realization lemma.** For any subgroup \(H\le D_4\), let \(\mathcal O_H\) consist of all orbits of squares that are faces of \(K\), and let a set of these orbits be a simplex exactly when their union is a face of \(K\). A point of \(|K|\) is uniquely represented by barycentric coefficients on its occupied vertices. It is fixed by \(H\) if and only if the coefficients are constant along each \(H\)-orbit. Therefore the orbit-barycenter map gives an affine-on-simplices PL-homeomorphism \(|K|^H\cong_{\mathrm{PL}}|\mathcal O_H|\). In particular an orbit containing an attacking pair cannot contribute a geometric fixed simplex.

**Subgroup exhaustion and the elementary cases.** The eight elements have representatives \(r^as^b\), \(0\le a\le3\), \(b\in\{0,1\}\). Closure of one- and two-generator subsets gives precisely ten subgroups, as shown by the independent complete group table in the verifier. For either axis reflection, every two-element square orbit shares a row or column, and no square is fixed on the even board. Thus the orbit complex is void. Every subgroup containing such a reflection also has empty geometric fixed space. Each diagonal reflection fixes exactly six squares of a single diagonal, which mutually attack, and every off-diagonal orbit has an attacking pair: its orbit complex is six isolated vertices. The quarter-turn has exactly six square orbits whose internal four-square arrangements are nonattacking, and no compatible pair of these orbits; it too has six isolated vertices. The remaining Klein-four subgroup contains both a diagonal reflection and the central half-turn: the half-turn freely interchanges the six fixed points of the reflection, so its simultaneous fixed space is empty.

**The central half-turn.** Exactly twelve square-pair orbits are internally nonattacking. Index them by the lexicographically ordered first representatives
\[(0,1),(0,2),(0,3),(0,4),(1,0),(1,2),(1,3),(1,5),(2,0),(2,1),(2,4),(2,5).\]
The partner of \((i,j)\) is \((5-i,5-j)\). Pairwise queen-compatibility of complete orbits gives exactly twenty-two edges and exactly four triangles, indexed
\[(0,6,11),\ (1,7,9),\ (2,4,10),\ (3,5,8).\]
No higher face exists. The four edges \((0,6),(1,7),(2,4),(3,5)\) each belong to precisely their displayed triangle, so removing these four free edge–triangle pairs is a sequence of elementary simplicial collapses. The remaining graph has twelve vertices, eighteen edges, and is connected: one explicit spanning tree has edges
\[(0,7),(0,8),(0,11),(11,1),(11,3),(11,6),(6,9),(3,4),(4,10),(10,2),(10,5).\]
Its cycle rank is \(18-12+1=7\), proving the asserted wedge of seven circles. Since all ten subgroups have already been exhausted, the classification follows.

## Verification
The standalone `verify_queen_fixed.py` needs only Python's standard library. It constructs all eight square permutations, closes all pairs of generators to obtain exactly ten subgroups, and separately constructs fixed orbit complexes in two logically distinct ways: (a) direct compatible orbit-clique enumeration and (b) invariant faces of the independently enumerated original 2,635-face complex. Their entire face sets agree for each subgroup. It confirms the full face-number vector of the original complex \((1,36,340,1024,982,248,4)\), the half-turn orbit-complex vector \((1,12,22,4)\), all four free collapses and an eleven-edge spanning tree. All eight signed simplicial Lefschetz sums agree with the reduced Euler characteristics of the corresponding geometric fixed spaces, and reproduce the established rational dihedral character \((19,-5,7,-5,1,1,-5,-5)\) in its stated element order. The archived `verify_output.txt` is deterministic; run `python3 verify_queen_fixed.py` to reproduce its final marker `SIX_BY_SIX_QUEEN_ALL_D4_FIXED_SPACES_PASS`.

## Relationship to prior work
Chaiken–Hanusa–Zaslavsky (first posted 2013 and 2014) study the counts of nonattacking queen placements, not topology of the geometric fixed spaces. A previously published exact computation for the six-by-six queen complex proves the ambient Moore-space wedge and its complete rational dihedral character; that character gives reduced Euler characteristics by Lefschetz theory, **but does not imply** that the half-turn fixed locus is connected, collapses to a graph, or has free first homology, nor does it determine the other subgroup-fixed homotopy types. A separate five-by-five queen-complex computation concerns a different board. The present theorem adds the complete actual all-subgroup geometric fixed-space homotopy classification. Symmetry-fixed queen-placement *counts* likewise do not imply these homotopy types.

## Limitations
This is a finite, exact theorem for the ordinary six-by-six board only. It does not determine fixed spaces on larger boards, integral homology of symmetry quotients, or a general equivariant homotopy decomposition. The nonequivariant Moore-space homotopy is credited to earlier work. The novelty comparison excludes the most relevant retrieved results but cannot rule out uncatalogued equivalent literature; independent validation has not been conducted.

## References
1. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A q-Queens Problem. I. General Theory*, initial arXiv posting 2013-03-08, https://arxiv.org/abs/1303.1879.
2. S. Chaiken, C. R. H. Hanusa, T. Zaslavsky, *A q-Queens Problem. II. The Square Board*, initial arXiv posting 2014-02-20, https://arxiv.org/abs/1402.4880.
3. *A Moore-space summand in the six-by-six queen-placement complex*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-moore-space-summand-in-the-six-by-six-queen-placement-complex--709883c6625b (comparison of the full `RESULT.md`).
4. *The five-by-five nonattacking-queen complex is a circle with seventeen two-spheres*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-five-by-five-nonattacking-queen-complex-is-a-circle-with-sev--9242cf0d005d (comparison of the full `RESULT.md`).
