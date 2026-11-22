# Optimal strong odd coloring census and symmetry of \(S(K_5)\)

## Finding

Let \(G=S(K_5)\) be obtained from the five-vertex complete graph by subdividing each of its ten edges exactly once. A *strong odd coloring* is a proper vertex coloring such that, for every vertex and every color appearing in its open neighborhood, the number of neighbors of that color is odd. Colorings are *optimal* if they use the fewest colors, and a color partition is a coloring modulo permutation of color names.

**Theorem.** There are exactly \(201\) optimal strong odd color partitions of \(G\). The chromatic minimum is \(\chi_{\mathrm{so}}(G)=5\), already established in the literature. Exactly \(6\) of the \(201\) partitions are proper square colorings of \(G\), while \(195\) are strong odd but not square colorings. The \(201\) partitions split into exactly **six** orbits under graph automorphisms, of sizes \(6,15,30,30,60,60\). With a fixed palette of five named colors there are exactly \(5!\cdot201=24{,}120\) optimal colorings.

The root-neighborhood multiplicity-profile census is:

| Number of original vertices with profile \((1,3)\) | Number of optimal partitions | Automorphism orbit sizes |
|:--:|--:|:--|
| 0 | 6 | 6 |
| 2 | 90 | 30, 60 |
| 4 | 45 | 15, 30 |
| 5 | 60 | 60 |

All other profile counts are zero. Every original vertex has either four singleton neighbor colors (profile \((1,1,1,1)\)) or two neighbor colors appearing once and three times (profile \((1,3)\)).

## Assumptions and scope

Work with a fixed labelled root set \(V=\{0,1,2,3,4\}\). The ten subdivision vertices are \(x_{ij}\) for \(0\le i<j\le4\), each adjacent to precisely original vertices \(i,j\). There are no edges between original vertices, nor between subdivision vertices. Unless expressly stated, counts of partitions retain root-vertex labels but disregard color-name permutations; the automorphism-orbit counts additionally identify graphs under permutations of the five roots. A *square coloring* is a proper coloring of \(G^2\), equivalently a proper coloring where every open neighborhood has pairwise different colors.

The first-public motivating source, Kwon--Park (2024-01-22), defines strong odd coloring. Caro--Petruševski--Škrekovski--Tuza, arXiv:2509.20763, Proposition 17(i), already proves \(\chi_{\mathrm{so}}(S(K_n))=n\) except at \(n=2,4\). That chromatic-number formula is **not** a novelty claim here. The new scope is the exact optimal-partition census, its square-coloring comparison, local profiles and six symmetry orbits specifically at \(n=5\).

## Proof

**1. Forced normalization.** For every original pair \(i\ne j\), subdivision vertex \(x_{ij}\) has the two original vertices as its entire open neighborhood. If the originals had equal colors, that color would appear twice, forbidden by strong oddness. Hence five original vertices have distinct colors. At least five colors are necessary. Normalize them uniquely so that original vertex \(i\) has color \(i\); every subdivision vertex \(x_{ij}\) must then have one of the other three colors, because it is adjacent to originals \(i,j\). The exhibited representative of the six-member square-coloring orbit, with ten subdivision colors \((2,3,4,1,4,0,3,1,0,2)\), in lexicographic edge order below, is valid, proving five colors suffice. Thus counting normalized colorings is exactly counting optimal color partitions, with no overcounting by color names.

**2. Exact class correspondence.** For any color \(c\in V\), form an edge set \(F_c\subseteq E(K_5-\{c\})\) by putting \(ij\in F_c\) precisely when \(x_{ij}\) has color \(c\). The properness condition is precisely that edges of \(F_c\) avoid root \(c\). At original root \(i\), the multiplicity of subdivision color \(c\) is exactly \(\deg_{F_c}(i)\). Every nonzero such degree must be odd, so on the four roots other than \(c\), \(F_c\) is exactly one of \(\varnothing\), a single edge \(K_2\), a disjoint two-edge matching \(2K_2\), a claw \(K_{1,3}\), or all of \(K_4\). Indeed, if no degree is three, all positive degrees are one and the graph is a matching. A degree-three vertex forces all its neighbors to have odd degree, hence either no edges among its neighbors (a claw) or a triangle among them (the whole \(K_4\)); any other arrangement leaves an even-degree neighbor.

There are respectively \(1,6,3,4,1\) eligible edge sets of these five kinds, so exactly \(15\) possible \(F_c\) for each color. Conversely, five eligible sets \((F_0,\ldots,F_4)\) define a valid normalized strong odd coloring exactly when they partition the ten edges of \(K_5\) disjointly. This is a **bijection**, not a sampling argument.

**3. Finite exact-cover recurrence.** Write \(E=E(K_5)\) and let \(\mathcal F_c\) be those fifteen allowed edge sets for color \(c\). Define integers \(D_0(\varnothing)=1\), \(D_0(U)=0\) otherwise, and for \(j=0,1,2,3,4\) and all \(U\subseteq E\), set

\[
D_{j+1}(U)=\sum_{F\in\mathcal F_j\, :\, F\subseteq U} D_j(U\setminus F).
\]

This recurrence counts exactly the choices of disjoint color classes covering \(U\). The complete recurrence uses at most \(6\cdot2^{10}\) states and only the explicit fifteen sets per color. Direct evaluation in `verify/exact_cover_dp.py` yields \(D_5(E)=201\). To count square colorings, restrict every \(F_c\) to a matching, i.e. only the \(1+6+3\) types with all degrees at most one. The same recurrence returns \(6\). A separate, independent direct evaluation of all \(3^{10}=59{,}049\) assignments to the ten subdivision vertices, applying the full fifteen-vertex neighborhood definition, agrees with both numbers. These are exhaustive finite calculations.

**4. Root profiles and orbits.** Every original root has four subdivision neighbors, so its permissible positive color multiplicities are \((1,1,1,1)\) or \((1,3)\). The direct checker tabulates the profile census shown in the theorem. Since original vertices have degree four while subdivision vertices have degree two, every automorphism of \(G\) permutes the originals, giving \(\mathrm{Aut}(G)\cong S_5\). It acts on normalized assignments by applying the same permutation to root indices and to all five color labels. Exhausting the \(120\) permutations produces six disjoint orbits of lengths \(6,15,30,30,60,60\), whose total is \(201\). Reproducible orbit representatives and the fixed lexicographic edge order are included in `verify/direct_orbits_output.txt`. The independent Burnside fixed-point sum is \(720\), giving \(720/120=6\) orbits; see the verification section.

**5. Named palette.** Every optimal partition uses all five colors because all five originals have distinct colors, so every partition gives exactly \(5!\) assignments of five distinct names. Thus the count is \(201\cdot120=24{,}120\). Likewise, exactly \(6\cdot120=720\) named colorings are square colorings.

## Verification

Run `python3 verify/exact_cover_dp.py` and `python3 verify/direct_orbits.py` with standard Python 3; no external dependencies are required. Exact outputs are preserved in `verify/exact_cover_output.txt` and `verify/direct_orbits_output.txt`. The first algorithm enumerates only admissible odd-degree color classes of \(K_4\) and evaluates a set-partition recurrence; the second constructs all fifteen vertices and twenty edges of \(S(K_5)\) from first principles, directly tests neighborhood parity on every possible normalized coloring, and independently computes its automorphism orbits. These two encodings do not share enumeration logic. The edge order is \((01,02,03,04,12,13,14,23,24,34)\). The complete candidate domain has exactly \(3^{10}\) assignments; there is no unexamined part of this finite search space.

For the six conjugacy types of \(S_5\), the number of permutations and the number of valid normalized assignments fixed by a single permutation are respectively: identity \((1,201)\), transposition \((10,21)\), double transposition \((15,9)\), three-cycle \((20,0)\), three-cycle times transposition \((20,0)\), four-cycle \((30,5)\), and five-cycle \((24,1)\). Thus the Burnside numerator is \(201+210+135+0+0+150+24=720\).

## Relationship to prior work

Kwon and Park, arXiv:2401.11653, introduced strong odd coloring and established general sparsity bounds; their accessible full-text sections do not supply this optimal-coloring census. Caro et al., arXiv:2410.02336, study general, planar, and product-graph strong odd coloring, including the fact that square coloring implies strong odd coloring; the paper does not state this subdivision-five-clique census. More directly, Caro et al., arXiv:2509.20763, Proposition 17(i), completely settles the optimal **number of colors** for \(S(K_n)\) and supplies constructions for both parities. Its statement and inspected proof do not count all optimal colorings, separate square from non-square optima, or describe automorphism orbits. In particular, the numerical fact \(\chi_{\mathrm{so}}(S(K_5))=5\) is covered; the \(201\)-partition census and its six-orbit classification are not consequences of that numerical fact.

Related published studies of completely subdivided complete **bipartite** graphs concern different base graphs and cannot imply the five-clique count by specialization. Classical total-coloring results control square colorings of a subdivision and hence the six square colorings here, but do not rule out or enumerate the additional \(195\) strong odd colorings.

## Limitations

This is a complete finite classification for \(S(K_5)\), not a closed enumeration of optimal colorings for arbitrary \(S(K_n)\). The minimum-color formula for general \(n\) is explicitly existing literature, not newly proved. The exact-cover recurrence and orbit enumeration are finite exhaustive arguments, not a proof for an infinite family. Priority beyond the inspected indexed literature and accessible research records is not guaranteed; independent mathematical review has not been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first publicly posted 2024-01-22), https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (2024-10-03), https://arxiv.org/abs/2410.02336.
3. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763 (2025-09-25), especially Proposition 17(i), https://arxiv.org/abs/2509.20763.
