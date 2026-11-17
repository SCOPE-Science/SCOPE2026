# Half-turn-fixed noncrossing forest complexes through twelve vertices

## Finding

Let \(\mathcal N_{2m}\) be the simplicial complex whose vertices are the edges (boundary sides and diagonals) of a regular convex \(2m\)-gon, and whose faces are collections of straight edges forming a crossing-free graph without cycles. The half-turn \(h\) sends polygon vertex \(i\) to \(i+m\pmod{2m}\). For every integer \(m\) with \(2\le m\le6\), its actual geometric fixed-point space has the following integral homotopy type:

\[
|\mathcal N_{2m}|^{\langle h\rangle}\simeq\bigvee^{b_m}S^{m-1},\qquad
(b_2,b_3,b_4,b_5,b_6)=(1,5,23,109,524).
\]

The result concerns **geometric fixed points**, not the orbit space or Borel homotopy fixed points. In particular, the dodecagon's half-turn-fixed space is a wedge of 524 five-spheres.

## Assumptions and scope

All crossings are intersections of relative interiors of straight chords; shared polygon endpoints are allowed. A forest includes isolated vertices. The empty chord set is the empty face of the simplicial complex. For a half-turn orbit \(O\) of chords (of size one for a diameter and two otherwise), let \(\bar O\) denote the barycenter of the vertices indexed by \(O\) in \(|\mathcal N_{2m}|\). The fixed-point complex \(K_m\) has one vertex \(\bar O\) for each chord orbit whose union is a face, and has an orbit-indexed face \(\{O_1,\ldots,O_k\}\) precisely when \(O_1\cup\cdots\cup O_k\) is a noncrossing forest.

For \(m\in\{2,3,4,5,6\}\), the numbers of chord orbits are \(m^2\), and the exact face counts, by increasing dimension, are:

| \(2m\) | \(f_0\) | \(f_1\) | \(f_2\) | \(f_3\) | \(f_4\) | \(f_5\) |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | — | — | — | — |
| 6 | 9 | 24 | 21 | — | — | — |
| 8 | 16 | 78 | 160 | 120 | — | — |
| 10 | 25 | 190 | 660 | 1100 | 715 | — |
| 12 | 36 | 390 | 2000 | 5445 | 7644 | 4368 |

No statement is asserted for \(m\ge7\) or for rotations other than a half-turn.

## Proof

**1. Fixed-point triangulation.** On each original simplex, the half-turn permutes barycentric coordinates in its orbits. A point is fixed exactly when coordinates are constant on each orbit. Such a fixed simplex is the convex hull of the orbit barycenters for the orbits contained in its support. Any two such simplices intersect face-to-face. Thus \(|K_m|\) is PL-homeomorphic to \(|\mathcal N_{2m}|^{\langle h\rangle}\). This argument includes invariant simplices with setwise-swapped vertices; discarding such simplices would incorrectly compute the fixed locus.

**2. Complete finite generation.** Number the original polygon vertices \(0,\ldots,2m-1\). Enumerate unordered chords lexicographically and group each chord with its image under \(i\mapsto i+m\). Sort the resulting chord orbits lexicographically and number them \(0,\ldots,m^2-1\). A subset of these orbits forms a simplex exactly when its union of chords (a) has no pair with alternating four distinct endpoints and (b) has no graph cycle. The executable certificate uses exact integer endpoint comparisons and a disjoint-set forest test. Since both properties are hereditary, building subsets in increasing orbit order enumerates every simplex without omissions. For \(m\le5\), a second enumeration over **all** subsets of each permitted cardinality independently confirms the face counts.

**3. Explicit acyclic matching.** On the poset of nonempty faces of \(K_m\), initially mark all faces unmatched. For orbit labels \(v=0,1,\ldots,m^2-1\) in order, traverse the current unmatched faces in increasing order of cardinality and then lexicographically. Whenever \(v\notin F\) and both \(F\) and \(F\cup\{v\}\) are unmatched faces, match that cover pair and remove both from the unmatched set. The empty face is never matched. To certify that this matching is *acyclic* rather than merely a pairing, orient every Hasse edge from larger to smaller face except for matched cover edges, which are reversed. The program enumerates **every** such directed edge and verifies that Kahn's topological sort visits all vertices. Therefore no directed cycle, hence no closed discrete-Morse gradient path, exists.

**4. Critical cells and homotopy.** The exact unmatched-cell counts are \(\{0:1,m-1:b_m\}\) in every stated case, with no critical cells in intermediate dimensions. By Forman's discrete Morse theorem, \(|K_m|\) is homotopy equivalent to a CW complex with one zero-cell and \(b_m\) cells of dimension \(m-1\), and no other cells. All such attaching maps are constant, so the resulting CW complex is the stated wedge of spheres. This is a homotopy classification over the integers, not merely a calculation of rational Betti numbers.

## Verification

Run `python3 verify.py` with Python 3 and no third-party libraries. It enumerates all faces, checks the expected face counts and maximal-face dimensions, constructs disjoint matching pairs, and performs an exhaustive directed-Hasse-graph acyclicity check. The verified matched-pair counts for polygons of orders \(4,6,8,10,12\) are respectively \(3,24,175,1290,9679\); the critical top-cell counts are \(1,5,23,109,524\). The exact machine-readable output is `verification_data.json`. Independent all-subset face counts were run through order ten; the order-twelve case is instead checked by the complete hereditary generation and direct validity assertions. Each Euler characteristic agrees with the critical-cell formula.

## Relationship to prior work

The early enumerative theory of noncrossing forests of convex polygons, especially Flajolet–Noy, counts labeled forests and their components, but does not classify geometric rotation-fixed spaces. Chen–Yan study parity involutions on *rooted* noncrossing trees and their relationship with symmetric ternary trees, a different symmetry and a different object. McCammond develops the noncrossing *hypertree* complex and identifies it with a noncrossing-partition link; that complex's face labels and homotopy question differ from the ordinary chord-subset noncrossing-forest complex considered here. Shellability of generalized root-system cluster complexes (Athanasiadis–Tzanaki) does not imply this result without an identification, and the relevant finite complexes do not share the complete type-\(B_3\) cluster-complex facet count: 21 versus 20 in rank three. The prior reflection-fixed model for noncrossing forests is also not a half-turn-fixed model; its orbit relations differ.

## Limitations

Only the five specified even polygon orders have been proved. An infinite uniform formula and a uniform acyclic matching theorem remain unproved. The exact finite certificate is combinatorial and depends on the definitions and the executable code; no independent external mathematical audit has been performed. Bibliographic searches and the primary-source comparisons below cannot exclude an unindexed equivalent theorem. The fixed-point result must not be reinterpreted as the quotient's homotopy type.

## References

1. P. Flajolet and M. Noy, *Analytic combinatorics of non-crossing configurations*, Discrete Mathematics 204 (1999), 203–229. Full text: https://igor-kortchemski.perso.math.cnrs.fr/lecon/Analytic%20combinatorics%20of%20non-crossing%20configurations.pdf
2. W. Y. C. Chen and S. H. F. Yan, *Noncrossing Trees and Noncrossing Graphs*, first public arXiv submission 2005-09-30, arXiv:math/0509715; Electronic Journal of Combinatorics 13 (2006), #N12. https://arxiv.org/abs/math/0509715
3. J. McCammond, *Noncrossing Hypertrees*, manuscript dated 2015-11-18, https://web.math.ucsb.edu/~mccammon/papers/nc-hypertrees.pdf
4. C. A. Athanasiadis and E. Tzanaki, *Shellability and higher Cohen–Macaulay connectivity of generalized cluster complexes*, arXiv:math/0606018 (2006). https://arxiv.org/html/math/0606018v2
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem).
