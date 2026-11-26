# Integral critical group of the Pascal-line Steiner–Kirkman concurrence graph

## Finding
Let six ordered points on a smooth conic over \(\mathbb C\) have sixty distinct Pascal lines and eighty pairwise distinct distinguished concurrence points (twenty Steiner and sixty Kirkman). Assume each distinguished point belongs to **exactly its three prescribed Pascal lines**. These conditions hold on a nonempty Zariski open set of ordered sextuples. Form the **Pascal concurrence graph** \(G\), with one vertex per Pascal line and an edge between two distinct vertices precisely when the corresponding lines pass through the same distinguished point. (Unmarked intersections of Pascals are not edges.) Then \(G\) is a connected simple eight-regular graph with sixty vertices and 240 edges, and

\[
\begin{aligned}
K(G)\cong{}&(\mathbb Z/2\mathbb Z)^7\oplus\mathbb Z/22\mathbb Z
\oplus\mathbb Z/88\mathbb Z\oplus\mathbb Z/176\mathbb Z\\
&\oplus(\mathbb Z/528\mathbb Z)^5
\oplus(\mathbb Z/2640\mathbb Z)^4
\oplus(\mathbb Z/5280\mathbb Z)^4.
\end{aligned}
\]

Here \(K(G)\) is the degree-zero chip-firing divisor class group, equivalently the cokernel of any reduced integer Laplacian of \(G\). Its order, equal to the spanning-tree count, is
\[
|K(G)|=\tau(G)=2^{71}3^{13}5^8 11^{16}.
\]
Its exponent is \(5280\). The Laplacian characteristic polynomial is
\[
\chi_{L}(t)=t(t-2)^5(t-6)^{14}(t-8)^{15}(t-10)^9(t-11)^{16}.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). Distinctness alone does not suffice for the graph defined by actual geometric incidence: on the conic parametrized by \([1:t:t^2]\), the sextuple \((0,65,195,585,1755,9)\) has sixty distinct Pascal lines and eighty distinct named points, but one of those points is on four Pascal lines and the actual incidence-based graph has 243 edges. The hypotheses also exclude such additional incidences at marked points. Unmarked incidences are irrelevant. No assertion is made about arbitrary positive characteristics or geometric Jacobians or Picard groups of the conic.

A labelled Pascal is an unoriented Hamiltonian six-cycle on the six labels. Thus the vertex set \(\mathcal H\) is the set of cyclic orderings of \(\{0,1,2,3,4,5\}\) modulo dihedral reversal and rotation; it contains \(6!/12=60\) vertices. For each cycle \(h\), denote by \(E(h)\) its six unordered consecutive pairs. The Kirkman triple assigned to \(h\) is the three cycles \(h'\) satisfying \(E(h')\cap E(h)=\varnothing\). The twenty Steiner triples are the three-element fibres of the map sending a six-cycle \(c\) to the unordered inverse pair \(\{c^2,c^{-2}\}\), where both members have permutation type \((3,3)\). The geometric validity of both triple-concurrence relations is classical, with labelled instances in Baralić–Spasojević (2012), Propositions 3.2 and 3.3. Those two incidence families, and **no other intersections**, define the graph.

## Proof
First, direct enumeration of all cyclic words modulo the dihedral action gives exactly sixty vertices. The squared-six-cycle map has twenty fibres of size three. For every hexagon, exactly three other hexagons have disjoint edge sets; these give sixty distinct Kirkman triples. The two families have no common vertex-pair. Each hexagon participates in one Steiner and three Kirkman triples, contributing \(2+6=8\) distinct neighbours. Hence \(G\) is a simple eight-regular graph with \((60\cdot8)/2=240\) edges. Independently, take the \(S_6\)-orbits of the two explicit triple patterns in the 2012 paper: these yield precisely the above twenty and sixty triples. The orbit construction proves independence of the labelling and establishes the match with the named geometric incidences. The Kirkman-only subgraph has six connected components, each of size ten; each Steiner triple meets three different Kirkman components. Their union is connected, as verified by exhaustive integer adjacency traversal.

Let \(L=8I-A\), where \(A\) is the symmetric zero-diagonal adjacency matrix determined by those eighty triples. Fix any root and delete its row and column to obtain a \(59\)-by-\(59\) integer matrix \(L_r\). Exact fraction-free Bareiss elimination gives
\[
\det L_r=2^{71}3^{13}5^8 11^{16}.
\]
The same determinant is obtained for roots \(r=0,17,59\). An independent exact characteristic-polynomial calculation for the full Laplacian gives the polynomial displayed above, and the matrix-tree theorem independently yields the same determinant.

For each prime divisor \(p\) of that determinant, perform unit-pivot row and column operations over \(\mathbb Z/p^{12}\mathbb Z\). After removing all unit pivots, the remaining block is divisible by \(p\); divide it by \(p\), reduce the modulus correspondingly, and repeat. These are Smith-equivalent operations over the localization at \(p\), and twelve digits exceed every resulting valuation. The complete elementary-divisor valuation counts, including unit factors, are:

| \(p\) | Valuation-zero factors | Positive Smith valuations |
|---|---:|---|
| \(2\) | 36 | valuation 1: 8; valuation 3: 1; valuation 4: 10; valuation 5: 4 |
| \(3\) | 46 | valuation 1: 13 |
| \(5\) | 51 | valuation 1: 8 |
| \(11\) | 43 | valuation 1: 16 |

For each prime, the weighted sum of the listed positive valuations agrees exactly with its exponent in \(\det L_r\). Since the determinant has no other prime divisor, these are all elementary divisors. Sort the \(p\)-power lists into divisibility order, left-pad each to 59 entries with units, and multiply corresponding entries across primes. Removing the 36 invariant factors equal to one yields the 23 nontrivial invariant factors stated in the Finding. This proves the integral group, not merely its order or rational spectrum.

The exhaustive steps are implemented with integer arithmetic in `verify_pascal.py`; two labelling constructions are cross-checked there. `verify_geometry.py` constructs six exact rational points \([1:t:t^2]\) with \(t\in\{0,1,3,9,27,81\}\), verifies all sixty Pascals by the collinearity of the three opposite-side intersections, and verifies that the eighty indicated concurrence points are pairwise distinct and are each on exactly their three expected Pascal lines. Where the line and point coordinates are defined and distinct, excluding any additional flag amounts to a polynomial nonvanishing condition after clearing denominators. The witness therefore proves nonemptiness of the open set. The script also checks the boundary example in the scope paragraph.

## Verification
Run `python3 verify_pascal.py` and `python3 verify_geometry.py` with Python 3 and no external dependencies. The first verifier checks all 720 relabellings of the two published sample concurrence triples, compares them with edge-disjoint and squared-cycle descriptions, checks graph degree/connectivity, computes exact Bareiss cofactors at three roots, and computes complete prime-local Smith valuations at all four relevant primes and three roots. The second tests all marked-point/line pairs both for the generic witness and for the distinctness-only boundary example. The characteristic polynomial provides a separate consistency check; it is not substituted for the integral Smith computation.

## Relationship to prior work
The geometry of Pascal, Steiner and Kirkman concurrence is classical. Baralić and Spasojević, *Illumination of Pascal's Hexagrammum and Octagrammum Mysticum*, arXiv:1209.4795 (first posted September 21, 2012), proves representative triple-concurrence statements (Propositions 3.2 and 3.3), discusses the classical sixty-line incidence, and studies geometric extensions and arrangements, but does not provide the above integral critical-group decomposition. Pisanski and Servatius, *Configurations from a Graphical Viewpoint* (2013), Section 1.1, also treats Pascal lines and distinguished Steiner/Kirkman points, not this combined graph Jacobian.

Earlier related arithmetic work on Pascal–Kirkman incidence flags determines Frobenius permutations of a different 180-element flag set; such permutation cycle information does not imply this integral Laplacian Smith form. Earlier integral work on the Steiner–Plücker incidence graph concerns a different 35-vertex bipartite graph, not this 60-vertex graph. Published searches found no exact equivalent of the present decomposition, but incomplete indexing and uninspected historical graph-isomorphism tables remain a priority risk.

## Limitations
This is an integral graph invariant, not a Picard-group or Jacobian computation of an algebraic curve. The proof uses exact finite enumeration, local Smith elimination and an exact geometric realization; it concerns this fixed configuration, not an infinite family of line arrangements. Special sextuples can introduce accidental Pascal incidences at a marked point and are not covered. The historical priority comparison is provisional.

## References
- Đorđe Baralić and Igor Spasojević, *Illumination of Pascal's Hexagrammum and Octagrammum Mysticum*, arXiv:1209.4795 (first posted September 21, 2012), especially Section 3, Propositions 3.2–3.3; Sections 8–9. https://arxiv.org/abs/1209.4795
- Tomaž Pisanski and Brigitte Servatius, *Configurations from a Graphical Viewpoint*, Birkhäuser/Springer, 2013, Section 1.1. https://doi.org/10.1007/978-0-8176-8364-1
- Alexander Bogomolny, *Pascal Lines: Steiner and Kirkman Theorems*, https://www.cut-the-knot.org/Curriculum/Geometry/PascalLines.shtml, and *Part II*, https://www.cut-the-knot.org/Curriculum/Geometry/MorePascal.shtml (independent geometric explanations).
