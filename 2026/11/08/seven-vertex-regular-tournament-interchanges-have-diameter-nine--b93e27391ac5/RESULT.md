# Seven-vertex regular-tournament interchanges have diameter nine and unique antipodes

## Finding

Let \(\mathcal T_7\) be the set of orientations of the labelled complete graph on \(\{0,1,2,3,4,5,6\}\) in which every vertex has outdegree three. Define \(\mathcal I_7\) to have vertex set \(\mathcal T_7\); two orientations are adjacent when one is obtained from the other by reversing the three arcs of a cyclically directed triangle.

**Theorem.** The graph \(\mathcal I_7\) is connected and has exactly \(2640\) vertices and \(18480\) edges. Its radius is \(8\) and its diameter is \(9\). Its \(720\) vertices of eccentricity \(9\) are precisely the relabellings of the cyclic tournament \(C_7\) defined by arcs \(i\to i+d\pmod7\) for \(d\in\{1,2,3\}\). Every such tournament has **exactly one** vertex at distance \(9\), its complete arc reversal. All other \(1920\) vertices have eccentricity \(8\). Consequently the diameter is attained by exactly \(360\) unordered pairs.

Under the action of the symmetric group on vertex labels there are exactly three orbits of sizes \(720\), \(1680\), and \(240\). The corresponding complete distance profiles from one representative, indexed from distance \(0\), are respectively
\[
(1,14,91,336,721,822,485,147,22,1),
\]
\[
(1,14,91,340,739,853,483,113,6),
\]
\[
(1,14,91,343,749,871,476,92,3).
\]
The numbers of *unordered* vertex pairs at distances \(1\) through \(9\) are
\[
(18480,120120,447720,970200,1116960,637440,158880,13320,360).
\]

## Assumptions and scope

All tournaments are individually **labelled**; no quotient by graph isomorphism is taken when distances are measured. The elementary move is reversal of a *directed* three-cycle, not reversal of an arbitrary triangle, an individual arc, or a larger cycle. Each legal move preserves all outdegrees. The theorem concerns only order \(7\) and does not establish a general formula at larger odd orders.

## Proof

**Degree and representation.** Encode a tournament by a \(21\)-bit word, one bit per lexicographically ordered pair \(i<j\), taking bit \(1\) when \(i\to j\). The regular words are exactly those with seven outdegrees equal to three. In any such tournament the number of transitive triangles is \(\sum_i\binom{3}{2}=21\), because each transitive triangle has a unique source. The remaining \(\binom73-21=14\) triangles are directed cycles. Reversing exactly those three bits gives all and only the neighbours, and each legal move preserves regularity. Thus \(\mathcal I_7\) is a simple \(14\)-regular graph.

**Exhaustive classification lemma.** The two complete, standalone enumerators included in this result establish the following *finite* identities by exhaustive checks, with no probabilistic sampling. First, direct examination of the \(2^{21}\) possible bit words, retaining exactly the seven-outdegree-three cases, gives \(2640\) distinct states. For each retained state examine all \(35\) unordered triples and reverse the three bits exactly when the induced orientation is a directed cycle. All resulting states lie in the retained set, and each of the resulting \(14\) neighbours is distinct. Breadth-first search from all \(2640\) states then gives the claimed radius, diameter, eccentricity histogram, distance distribution, and property that the sole distance-nine target of every peripheral state is its bitwise complement. In a separately constructed enumeration, recursively choose which later vertices are defeated by each labelled vertex, maintaining exact residual scores. This yields the same \(2640\) states. Explicitly apply all \(7!\) relabellings and check that the states are partitioned into exactly three orbits of sizes \(720,1680,240\); breadth-first search from one representative of each orbit yields exactly the three displayed complete distance profiles. Since relabelling is an automorphism of the interchange graph, these profiles determine all source distances. The source code gives the full finite certificate and independently checks every asserted cardinality; it does not assume the desired graph's connectivity.

**Structural lower bound for the cyclic antipode.** In \(C_7\) each arc has cyclic step \(1\), \(2\), or \(3\), with seven arcs of each step. A directed three-cycle has step lengths summing to \(7\): their sum is a positive multiple of seven and lies between three and nine. Its step multiset therefore must be either \(\{1,3,3\}\) or \(\{2,2,3\}\). In particular, it contains either zero or two step-two arcs. If a sequence of seven triangle reversals transformed \(C_7\) to its complete reversal, exactly \(21\) arcs would be toggled by \(7\cdot3=21\) operations. Every arc would consequently be toggled **exactly once**, making the seven reversed triangles edge-disjoint. Since their edges are disjoint, each would already be a directed triangle in the original \(C_7\). But no family of such triangles can partition the seven step-two arcs into blocks of size two. This contradicts the odd number seven. Each legal move toggles three bits, so a path from \(C_7\) to its complete reversal must have odd length, as the endpoints differ in all \(21\) bits. At least seven moves are necessary by edge count; seven is impossible; hence at least **nine** moves are necessary. The finite exhaustive classification above supplies a nine-move route and proves uniqueness of the farthest target throughout the cyclic orbit.

**Pair classification.** Three orbit sizes and their profiles yield \(720\) ordered pairs at distance nine; divide by two for \(360\) unordered pairs. For each distance, multiply the appropriate profile count by its orbit size and divide by two. The sum of the resulting unordered distance counts is \(\binom{2640}{2}=3483480\), as required.

## Verification

The standalone programs are `verify_full.cpp` (C++17) and `verify_orbits.py` (Python 3 standard library). From their directory run:

```sh
g++ -O2 -std=c++17 verify_full.cpp -o verify_full
./verify_full
python3 verify_orbits.py
```

The first enumerates all \(2^{21}\) labelled orientations, tests regularity, explicitly builds all valid triangle-reversal edges, and performs breadth-first searches from every state; it checks the exact pair-distance histogram and the unique-complement farthest-target condition for every vertex of eccentricity nine. The second uses row-score-constrained recursion, an independent triangle-orientation test, all \(5040\) label permutations, and only the three orbit-representative breadth-first searches. Both must print their respective `CPP_EXHAUSTIVE_PASS` and `PYTHON_INDEPENDENT_PASS` markers. These finite checks are exhaustive within the declared order-seven domain; they do not imply a general-order theorem.

## Relationship to prior work

Brualdi and Li introduced the tournament interchange graph and proved a lower bound of \((n-1)^2/4\) for the diameter of the regular-tournament interchange graph; the conjecture that this is sharp is quoted explicitly in McShine's Remark 2 [1]. For seven vertices, that bound is \(9\). The present theorem verifies sharpness at seven vertices and gives additional orbitwise eccentricities, full distances, and a complete sharp-pair classification; it does **not** claim to introduce the interchange graph, its connectivity, the uniform triangle count, the \(2640\)-state count, or the general conjecture. McShine [1] proves connectivity and rapid sampling, not the specific exact seven-vertex metric. Kolesnik, Mitchell and Przybyłowski [2] study degree structure and Coxeter generalizations, not this full distance distribution. The published census of regular tournaments [3] records three unlabelled order-seven types, not their labelled interchange distances. Guiduli et al. [4] study structural transformations and an unlabelled tournament quotient. Yuster [5] studies cycle-packing and interchange distances in a related but different setting. The older original 1984 Brualdi–Li chapter has not been inspected in full; an unindexed equivalent finite calculation remains a priority risk.

## Limitations

This is an exact **order-seven finite theorem**. Its metric upper bound and complete eccentricity and pair classifications depend on exhaustiveness of the supplied finite programs and their explicitly stated state/edge construction. The structural lower bound for the cyclic antipode is independent of enumeration. No claim is made about all odd orders or about uniqueness of the result in historical literature. Independent external mathematical audit has not been performed.

## References

[1] L. McShine, *Random Sampling of Labeled Tournaments*, Electronic Journal of Combinatorics 7 (2000), R8, published 2000-02-23, DOI: 10.37236/1486. Original full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r8/pdf

[2] B. Kolesnik, R. Mitchell and T. Przybyłowski, *Coxeter Interchange Graphs*, arXiv:2312.04532 (first posted 2023-12-07), later Annals of Combinatorics (2025); DOI: 10.1007/s00026-025-00768-9.

[3] B. D. McKay, *Combinatorial Data: Regular and Semi-regular Tournaments*, https://users.cecs.anu.edu.au/~bdm/data/digraphs.html.

[4] B. Guiduli, A. Gyárfás, S. Thomassé and P. Weidl, *2-Partition-Transitive Tournaments*, Journal of Combinatorial Theory, Series B 72 (1998), 181–196. Open full text: https://users.renyi.hu/~gyarfas/Cikkek/85_2partitiontranstourn.pdf.

[5] R. Yuster, *Packing 4-cycles in Eulerian and bipartite Eulerian tournaments with an application to distances in interchange graphs*, arXiv:math/0310411 (first posted 2003-10-26).

[6] R. A. Brualdi and Q. Li, *The interchange graph of tournaments with the same score vector*, in *Progress in Graph Theory*, 1984, 129–151. Earlier original source; day of first public circulation and complete text were not verified.
