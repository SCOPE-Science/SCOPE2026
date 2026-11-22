# A sharp eccentricity dichotomy in Petersen two-dynamic four-colouring reconfiguration

## Finding

Let \(P=\operatorname{KG}(5,2)\), whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with disjoint pairs adjacent. A *two-dynamic proper colouring* \(c:V(P)\to\{0,\dots,k-1\}\) is proper and uses at least two different colours on the three neighbors of each vertex. Adjacent valid named colourings differ at exactly one vertex; let \(\mathcal R^{\mathrm{dyn}}_k(P)\) be their single-vertex recolouring graph. The palette names are fixed, not identified.

**Exact constrained-distance theorem.** The two-dynamic chromatic number of \(P\) is exactly \(4\). There are exactly \(5760\) named minimum-palette two-dynamic colourings, in precisely four orbits under \(\mathfrak S_5\times\mathfrak S_4\) (graph automorphisms and colour permutations). The four orbits are distinguished by their sorted colour-class sizes as follows:

| Colour-class sizes | Number of colourings | Recolouring degree | Eccentricity |
|:--|--:|--:|--:|
| \((1,2,3,4)\) | 1440 | 9 | 15 |
| \((1,3,3,3)\) | 480 | 9 | 15 |
| \((2,2,2,4)\) | 960 | 6 | 16 |
| \((2,2,3,3)\) | 2880 | 6 | 16 |

The graph \(\mathcal R^{\mathrm{dyn}}_4(P)\) is connected, has exactly \(20160\) edges, radius \(15\), and diameter \(16\). A minimum-palette colouring has eccentricity \(15\) if and only if its colour-class sizes include a singleton; otherwise its eccentricity is \(16\). Exactly \(12960\) unordered pairs of valid colourings are at distance \(16\).

The complete unordered-pair distance distribution, for distances \(1,\ldots,16\), is
\[
(20160,72000,174480,334800,568800,896400,1309440,1734000,
2042880,2233680,2412480,2323680,1614240,684000,151920,12960).
\]
The sum is \(\binom{5760}{2}\).

## Assumptions and scope

The graph is the ordinary ten-vertex Petersen graph, with no loops or parallel edges. All assertions concern proper vertex colourings, not edge colourings; each fixed colour label is distinct. The *open* neighborhood is used, with the local requirement \(\lvert c(N(v))\rvert\ge2\). Reconfiguration changes one vertex colour at a time and requires every intermediate colouring to remain proper and two-dynamic. The distance is the shortest number of such changes. A colour need not be used by definition, but every valid four-palette colouring in the theorem uses all four colours. No claim is made for larger graphs or for palettes larger than four.

Because the Petersen graph is cubic, a proper two-dynamic colouring is equivalently a proper open-neighborhood conflict-free colouring: among three neighbour colours, at least two distinct values appear precisely when one value occurs exactly once. This equivalence is specific to the stated degree-three setting.

## Proof

We give an exhaustive, finite and independently reproducible proof. The size is deliberately small: ten vertices, at most four colours, and a graph of \(5760\) valid states. The two included standalone implementations use distinct graph models and enumeration approaches.

**1. Exhaustive enumeration without omitted cases.** Order the ten vertices as
\[
01,02,03,04,12,13,14,23,24,34.
\]
Their three neighbours are exactly the disjoint pairs. For any \(k\in\{3,4\}\), a partition of these ten vertices into exactly \(k\) nonempty independent colour classes has a unique *restricted-growth* coding: start the first label at zero; thereafter a label is at most one greater than the largest preceding label. The program `verify_kneser.py` visits every such restricted-growth string by incrementally extending a proper prefix. It rejects a prefix only if the new label agrees with the label of an already assigned adjacent vertex, which cannot be repaired by later assignments. Thus its completed strings are in bijection with unlabelled proper \(k\)-class partitions. A complete string is two-dynamic if and only if each of the ten open neighbourhoods has at least two different labels.

The exact table returned by this exhaustive partition test is

| Nonempty classes | Proper partitions | Two-dynamic partitions |
|--:|--:|--:|
| 3 | 20 | 0 |
| 4 | 520 | 240 |

There is no proper colouring with fewer than three colours since \(P\) contains five-cycles. Hence no two-dynamic three-colouring exists. Every one of the \(240\) four-class dynamic partitions has exactly \(4!=24\) named realizations, yielding \(5760\), and proves \(\chi_2(P)=4\). The complete proper four-palette count is \(520\cdot24+20\cdot24=12960\), where the second term gives proper colourings using exactly three of the four labels.

**2. Complete symmetry classification.** Permuting the five underlying symbols preserves disjointness, and permuting the four colour names preserves all validity conditions and recolouring edges. For every computed colour-class-size profile, the Python certificate explicitly applies all \(5!\cdot4!\) such group operations to a representative, forms the orbit as a set of distinct named colourings, and checks equality with the entire exhaustively enumerated profile class. The four representatives in the vertex order above are

| Sizes | Representative string |
|:--|:--|
| \((1,2,3,4)\) | `0000111223` |
| \((1,3,3,3)\) | `0001222311` |
| \((2,2,2,4)\) | `0000112323` |
| \((2,2,3,3)\) | `0001221313` |

These orbit equalities prove both completeness and the asserted sizes. They also show that the recolouring degree, eccentricity, and each distance-shell count are constant within a listed class, since the operations act by graph automorphisms on the recolouring graph.

**3. Exact graph distances.** Form a dictionary containing every valid named colouring. For each state and each of its ten vertices, try the other three labels; add the move if and only if the modified string is in the dictionary. This rule enumerates all and only one-vertex legal recolourings. The program checks the adjacency relation is undirected. Its degree totals are \(3840\) vertices of degree six and \(1920\) of degree nine, so the number of edges is \((3840\cdot6+1920\cdot9)/2=20160\).

Breadth-first search from one representative of each of the four verified group orbits visits all \(5760\) states, proving connectedness. The respective maxima of the shortest-path distances are \(15,15,16,16\), proving the exact radius, diameter, and eccentricity classification for every state. For each distance \(d\), multiply a representative's shell count by its orbit size, add across the four profiles, and divide by two for \(d>0\). This gives the complete displayed unordered-pair histogram, including the \(12960\) diametral pairs. There is no unexamined state or pair: orbit transitivity reduces all starting states to four representatives.

**4. Independent reconstruction.** `verify_gp.cpp` builds the Petersen graph instead as \(\operatorname{GP}(5,2)\), with outer pentagon edges, inner star-pentagon edges, and five spokes. It backtracks directly over every named proper colouring with three and four labels, tests the local two-dynamic property, and reconstructs the full legal recolouring graph using base-four integer codes. Unlike the orbit-reduced Python computation, it runs breadth-first search from **every** one of the \(5760\) states and counts pairs directly. The second output reproduces exactly the same profile counts, degrees, eccentricities, radius, diameter, and distance histogram. The two graph descriptions are the standard isomorphic descriptions of the Petersen graph; agreement is an independent check of the finite assertion.

## Verification

The complete sources and their actual reproduced reference outputs are embedded beside this document as `verify_kneser.py`, `verify_kneser_expected.txt`, `verify_gp.cpp`, and `verify_gp_expected.txt`. Run from their containing directory:

```sh
python3 verify_kneser.py
c++ -O2 -std=c++17 verify_gp.cpp -o verify_gp
./verify_gp
```

The Python version uses only the standard library; the C++ version uses only the C++17 standard library. The two methods check the ten-vertex domain by exhaustive finite enumeration, not random sampling. The orbit-reduced and all-sources BFS computations both finish and produce the tabulated values. Exact metrics are certified only for the stated finite graph; there is no extrapolation to graph families.

## Relationship to prior work

Montgomery introduced dynamic colouring in 2001. Kang, Müller, and West's 2014 preprint treats \(r\)-dynamic colourings of rectangular grids, and Jahanbekam, Kim, O, and West's 2016 article treats general bounds and regular graphs. These foundational sources justify the local neighbour-diversity condition but do not in their inspected accessible material give the present complete Petersen four-colouring reconfiguration graph.

The published exact ordinary four-colouring reconfiguration computation for the Petersen graph reports radius \(13\) and diameter \(14\) for *all* proper four-palette colourings. It concerns a larger state space: \(12960\) proper states, of which exactly \(5760\) satisfy the two-dynamic requirement. Its complete eleven-orbit table already supplies the four representative strings used here and, after testing the local two-dynamic predicate on those representatives, implies the four orbit populations and their class-size profiles. **We do not claim novelty for those orbit populations or the four-colour state count:** these are inherited baseline classifications, independently verified here to define the constrained state space. The specific new claim is the induced-state exchange graph, its exact edge total, connectedness, sharp eccentricity split, diameter, and complete pair-distance histogram. Its ordinary shortest paths can leave the dynamic subset, so the present distance values \(15\) and \(16\) are neither a restatement nor a consequence of those ordinary distances. Proper open-neighbourhood conflict-free colouring is an equivalent predicate here, and searches also considered that terminology. Published cycle-prism proper conflict-free enumerators are not results for this graph. The published proper symmetry-breaking Petersen colouring polynomial also gives complete proper four-class partition counts and an orbit classification, but neither it nor the ordinary-reconfiguration census determines shortest paths constrained to remain two-dynamic.

## Limitations

This is a self-contained exact finite graph theorem, not a theorem for an infinite graph family. Proof validity depends on the explicitly supplied exhaustive algorithms, whose finite loops and state spaces are documented, not on a claimed formal theorem prover or an outside certificate. No independent scholarly audit is claimed. The accessible 2001 dissertation abstract was inspected, but its full text could not be retrieved; unindexed historical work and any inaccessible exact Petersen dynamic-colouring enumeration remain residual originality risks. The publisher-hosted 2016 article was available through extracted passages but was not fully inspected as a downloadable article. Searches alone do not establish absolute novelty.

## References

1. B. Montgomery, *Dynamic Coloring of Graphs*, PhD dissertation, West Virginia University (2001), DOI: https://doi.org/10.33915/etd.1397 ; accessible abstract https://researchrepository.wvu.edu/etd/1397/ .
2. R. Kang, T. Müller, D. B. West, *On \(r\)-dynamic Coloring of Grids*, arXiv:1407.3504, first submitted 2014-07-13, https://arxiv.org/abs/1407.3504 .
3. S. Jahanbekam, J. Kim, S. O, D. B. West, *On \(r\)-dynamic coloring of graphs*, Discrete Applied Mathematics 206 (2016), 65–72, https://doi.org/10.1016/j.dam.2016.01.016 .
4. A. Taherkhani, *\(r\)-Dynamic Chromatic Number of Graphs*, arXiv:1401.6470, submitted 2014-01-24, https://arxiv.org/abs/1401.6470 .
5. *Exact Petersen vertex-recolouring geometry at three and four colours*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-petersen-vertex-recolouring-geometry-at-three-and-four-col--83b049512d48 .
6. *The proper symmetry-breaking colouring polynomial of the Petersen graph*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-proper-symmetry-breaking-colouring-polynomial-of-the-peterse--2b49c41819af .
7. *Optimal proper conflict-free colouring census for cycle prisms*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-optimal-proper-conflict-free-colouring-census-for-cycle-prisms--373334d2a6e9 .
