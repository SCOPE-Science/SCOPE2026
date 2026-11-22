# Two peripheral affine types in optimal weak three-colourings of the nine-point plane

## Finding
Let \(H\) have vertex set \(\mathbb F_3^2\) and the twelve affine lines as its three-vertex hyperedges. A *proper weak colouring* of \(H\) has no monochromatic hyperedge. In the graph \(\mathcal R\), vertices are proper assignments of three **named** colours to the nine points, and two assignments are adjacent exactly when they differ at one point.

**Theorem.** The weak chromatic number of \(H\) is three. Its full named-colour counting polynomial is
\[
P_H(q)=q^9-12q^7+66q^5-72q^4-4q^3+27q^2-6q
=q(q-1)(q-2)(q^6+3q^5-5q^4-21q^3+13q^2+9q-3).
\]
Consequently \(\mathcal R\) has exactly \(3,762\) vertices and \(16,848\) edges and is connected, with radius \(9\) and diameter \(10\). Exactly \(306\) unordered colouring pairs are at distance ten.

Write \(r_i(c)\) for the number of rainbow (three-distinct-colour) lines in the \(i\)-th of the four parallel classes, and sort the four numbers. The full orbit classification under the affine point symmetries \(\operatorname{AGL}(2,3)\) and permutations of the three colour names is:

| Orbit size | Sorted colour-class sizes | Sorted rainbow counts per direction | Recolouring degree | Eccentricity |
|---:|---|---|---:|---:|
| 144 | \((3,3,3)\) | \((0,0,0,3)\) | 9 | 10 |
| 162 | \((1,4,4)\) | \((0,0,0,0)\) | 8 | 10 |
| 864 | \((3,3,3)\) | \((0,1,1,1)\) | 9 | 9 |
| 1,296 | \((2,3,4)\) | \((0,0,0,2)\) | 9 | 9 |
| 1,296 | \((2,3,4)\) | \((0,0,1,1)\) | 9 | 9 |

Thus **a colouring is peripheral (eccentricity ten) if and only if** either it has a singleton colour class, or its three colour classes each have size three and its three rainbow lines are parallel. The other \(3,456\) colourings have eccentricity nine. Every one of the \(306\) peripheral colourings has exactly two antipodes at distance ten.

## Assumptions and scope
Points are the nine ordered pairs \((x,y)\) with \(x,y\in\{0,1,2\}\), arithmetic modulo three, in lexicographic order. The twelve lines are \(ax+by=c\), with directions \((a,b)\in\{(1,0),(0,1),(1,1),(1,2)\}\) and \(c\in\mathbb F_3\). Each line has three distinct points. A colouring is valid when the three values on every line are not all equal. All colour names are distinguished, as are the nine labelled points; graph distances count one changed point per step with every intermediate colouring proper. An antipode of \(c\) is a colouring at maximum possible distance ten from \(c\). The theorem is about this particular finite plane, not all affine planes.

## Proof
**Lower bound on the palette.** A colour class without a monochromatic line is a cap, containing no three collinear points. Suppose a cap contained five points. Through any one cap point pass four lines, and each of these would contain one of the other four cap points, so no line meeting this cap would meet it in exactly one point. An exterior point exists and its four incident lines partition the five cap points into intersections of even size (zero or two), a contradiction. Thus every cap contains at most four points. Two cap colour classes cannot cover nine points, proving that two colours are impossible. Three colours are possible: a concrete valid assignment, in the specified lexicographic point order, is \(0,0,1,0,2,2,1,2,1\). This witness can also be checked line by line.

**Complete polynomial.** For each subset \(S\) of the twelve lines, unite the points on every line in \(S\), and let \(k(S)\) count the equivalence classes. Inclusion-exclusion over monochromatic-line events gives
\[
P_H(q)=\sum_{S\subseteq\mathcal L}(-1)^{|S|}q^{k(S)}.
\]
The exhaustive, standalone `verify_orbits.py` performs all \(2^{12}=4,096\) unions and obtains coefficients \((k,a_k)=(9,1),(7,-12),(5,66),(4,-72),(3,-4),(2,27),(1,-6)\). This proves the displayed polynomial for every positive integer palette size, not just three. In particular \(P_H(3)=3,762\).

**Exhaustive colour-orbit certificate.** Any two distinct points \(u,v\in\mathbb F_3^2\) lie on the unique triple \(\{u,v,-u-v\}\). The Python checker independently constructs the twelve lines by this formula and enumerates all \(3^9=19,683\) named assignments. It tests every line directly and retains exactly \(3,762\). It enumerates all \(48\) invertible two-by-two matrices over \(\mathbb F_3\), their nine translations, and all six palette permutations. Each of these \(2,592\) transformations maps lines to lines and hence induces an automorphism of \(\mathcal R\). Partitioning all assignments into full transformation orbits gives exactly the five rows in the table; the sizes sum to \(3,762\). Computing neighbour counts directly gives \(162\) vertices of degree eight and \(3,600\) of degree nine, and thus \((162\cdot8+3,600\cdot9)/2=16,848\) edges.

**Sharp distances.** The Python program performs a full breadth-first search from a representative of each of the five orbits. Each search reaches all \(3,762\) valid states, proving connectedness. The maxima of the five representative distance profiles are respectively \(10,10,9,9,9\). The first two representatives each have two states at distance ten; the other three have none. Graph automorphisms preserve every distance profile, so precisely \(144+162=306\) states have eccentricity ten, each with two antipodes; hence there are \(306\cdot2/2=306\) unordered diametral pairs. The direction-rainbow and colour-class signatures shown in the table characterize these two peripheral orbits, giving the intrinsic criterion. The independent `verify_all_pairs.cpp` reconstructs the affine lines with linear equations, explicitly builds the complete reconfiguration graph, and performs all \(3,762\) breadth-first searches, reproducing the same radius, diameter, eccentricity multiplicities, and total diametral pairs.

These are finite exhaustive proofs: the checker loops cover exactly the bounded domains in the definitions; no statistical inference or unbounded extrapolation is used.

## Verification
Run `python3 verify_orbits.py` using only the standard library; this checks the lines, colours, affine automorphisms, orbit completeness, five representative distance searches, number of edges, colour polynomial and diametral pairs. Independently compile with `g++ -std=c++17 -O2 verify_all_pairs.cpp -o verify_all_pairs` and run `./verify_all_pairs`. Expected machine output is embedded in `all_pairs.out`. The C++ program enumerates all states and performs every-source BFS. Full unordered pair-distance distribution, for distances one through ten, is
\[
(16848,79704,263088,663768,1290438,1859112,1784592,923184,193401,306).
\]
The ten counts sum to \(\binom{3762}{2}\). Both implementations were executed from the packaged source files and agreed on their overlapping results. No external libraries or downloaded papers are needed to replay the checks.

## Relationship to prior work
Kozik and Shabanov (arXiv:1409.6921, first posted 24 September 2014) investigate proper hypergraph colourings and general sufficient degree bounds for simple uniform hypergraphs. Their colouring notion coincides with the weak colouring used here, but those bounds do not count colourings or analyze the nine-point affine-plane solution graph. Bonsma and Paulusma (arXiv:1509.06357, 2015) study single-vertex recolouring solution graphs for ordinary graphs; their general motivation does not determine the hypergraph configuration space here. Bhattiprolu, Guruswami and Lee (arXiv:1506.06444, 2015) study complexity and approximation of proper hypergraph colouring rather than this exact instance.

Erskine, Griggs and Širáň (2021, doi:10.1002/jcd.21773) discuss weak colouring of symmetric three-uniform configurations, including the eight-point configuration obtained by deleting one point and its incident lines from this affine plane. Their investigated incidence structure differs from the full nine-point, twelve-line hypergraph. An indexed mathematical record on *lean colourings* of finite affine planes (identifier ending `d7d2f7c0a1ae`) uses a different admissibility condition; its displayed result neither states this proper-colouring polynomial nor the reconfiguration distances. That complete external record was not available for full-text inspection, and an unreported implication cannot be ruled out solely from its summary. No claim of a globally exhaustive literature search is made.

## Limitations
The exact result concerns one finite hypergraph, a fixed named three-colour palette and one-point recolourings. The five-orbit classification and distances are established by exhaustive, replayable enumeration rather than a short closed-form argument applying to higher-order affine planes. The scientific priority assessment rests on inspected primary texts and indexed summaries; inaccessible or unindexed prior work may contain equivalent data. The computation has not received independent scholarly validation.

## References
- J. Kozik and D. Shabanov, *Improved algorithms for colorings of simple hypergraphs and applications*, arXiv:1409.6921 (first public version, 24 September 2014), https://arxiv.org/abs/1409.6921.
- P. Bonsma and D. Paulusma, *Using Contracted Solution Graphs for Solving Reconfiguration Problems*, arXiv:1509.06357 (21 September 2015), https://arxiv.org/abs/1509.06357.
- V. V. S. P. Bhattiprolu, V. Guruswami and E. Lee, *Approximate Hypergraph Coloring under Low-discrepancy and Related Promises*, arXiv:1506.06444 (22 June 2015), https://arxiv.org/abs/1506.06444.
- G. Erskine, T. Griggs and J. Širáň, *Colouring problems for symmetric configurations with block size 3*, Journal of Combinatorial Designs 29 (2021), 397–423, https://doi.org/10.1002/jcd.21773.
