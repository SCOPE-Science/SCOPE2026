# Six symmetry types among the 416 optimal strong edge-colorings of the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, equivalently the point-line incidence graph of the Fano plane. A *strong edge-coloring* partitions the edges into induced matchings, meaning that distinct edges of the same color have pairwise disjoint endpoints with no edge of \(H\) between the endpoints of two selected edges.

There are exactly **416** partitions of the 21 edges of \(H\) into seven nonempty, unlabelled strong color classes. Every class has three edges, and seven is the minimum possible number of colors. With a fixed palette of seven distinct colors, there are therefore exactly \(416\cdot7!=2{,}096{,}640\) optimal colorings. The 416 color-class partitions form exactly **six** orbits under the full graph automorphism group, with orbit sizes

\[
8,\quad16,\quad56,\quad112,\quad112,\quad112.
\]

Their respective automorphism stabilizer orders are \(42,21,6,3,3,3\). This is a complete finite classification of optimum strong edge-colorings **up to color permutation** and, separately, up to graph automorphism. It does not purport to classify arbitrary nonoptimal colorings or projective planes of higher order.

## Assumptions and scope

Encode the seven points of \(\mathrm{PG}(2,2)\) by the nonzero bit-vectors \(1,\ldots,7\) in \(\mathbb F_2^3\). The seven lines are the triples \(\{a,b,a\oplus b\}\), with distinct nonzero \(a,b\), where \(\oplus\) means bitwise XOR. Construct \(H\) with point-vertices \(p\), line-vertices \(\ell\), and one edge for each incident point-line pair \((p,\ell)\). The order of points, lines and edges is deterministic and implemented in the attached scripts.

A color class is a subset of the **original incidence edges**; colors are interchangeable when counting the 416 partitions. In the stated six-orbit classification the acting group is the **full** automorphism group of the incidence graph, including automorphisms that interchange the point and line parts.

## Proof

**Induced matchings.** Two distinct incidence edges \((p,\ell)\) and \((q,m)\) can share a strong color if and only if \(p\ne q\), \(\ell\ne m\), \(p\notin m\), and \(q\notin\ell\). These four conditions are necessary and sufficient: they assert that their four endpoints induce precisely two independent edges. Exhaustively checking all \(\binom{21}{3}\) triples by this criterion yields 84 induced three-edge matchings, exactly 12 through each incidence edge. Checking all \(\binom{21}{4}\) quadruples yields no induced four-edge matching; any larger induced matching would contain one. Hence seven colors are necessary for 21 edges, and a seven-coloring must consist of seven disjoint members of the enumerated list of 84 triples.

**Exact covers.** For each remaining incidence edge \(e\), let \(\mathcal T(e)\) be the enumerated triples containing \(e\) and contained in the set \(R\) of remaining edges. The recursion chooses a remaining edge with the fewest eligible triples and branches once for each eligible triple, removing its three edges. If no eligible triple exists the branch is rejected; if no edges remain the sorted unordered seven-triple partition is recorded. Every partition is visited because its unique triple containing the chosen edge appears among the branches. No partition can be visited twice, since the triple containing the first chosen edge is unique and the argument repeats at each descendant. Direct execution visits 5531 recursion nodes and produces exactly 416 distinct solutions. The executable `verify_heawood.py` contains this entire finite enumeration, with asserted boundary checks and a SHA-256 checksum of the canonical solution encoding; `verification_main.json` preserves the computed outputs.

**Full symmetry.** A graph automorphism of connected bipartite \(H\) either preserves the two parts or swaps them. A part-preserving automorphism permutes the points while preserving their lines. Because the Fano plane lines are exactly dependent triples of distinct nonzero vectors in \(\mathbb F_2^3\), such a permutation extends uniquely to a linear automorphism. There are \((2^3-1)(2^3-2)(2^3-2^2)=168\) such maps. The standard orthogonality polarity sends a point \(p\) to the line \(\{q\ne0:p\cdot q=0\}\), and reciprocally a line to its normal point. It exchanges the parts and preserves incidence, so the full group has exactly 336 elements.

Apply each of these 336 permutations of incidence edges to each of the 416 exact covers. The resulting orbits have sizes \(8,16,56,112,112,112\), which sum to 416; the scripts assert that no image leaves the computed solution set. A separate Burnside check sums fixed-solution counts to \(2016=336\cdot6\). Orbit representatives are included in `verification_main.json`, fully specifying all six classes. Orbit-stabilizer gives the stated stabilizer orders.

**Independent reconstruction.** `verify_heawood_independent.py` builds the Fano plane instead from the cyclic difference set \(\{i,i+1,i+3\}\) modulo seven, constructs the original graph and its edge-conflict relation directly, enumerates exact covers using a fixed-edge recursion, and exhaustively checks all \(7!\) point permutations together with an explicit point-line duality. It also yields 84 triples, no size-four induced matching, 416 partitions and the identical six orbit sizes. The two constructions use different point/line labelings and different implementations of the group action.

## Verification

With Python 3 (standard library only), run from the directory containing the attached files:

```sh
python verify_heawood.py > check1.json
python verify_heawood_independent.py > check2.txt
```

The scripts use no network access or external data and terminate with assertions if their mathematical census differs from the reported result. Compare the first output with `verification_main.json` and the second with `verification_independent.txt` after accounting for output names. The first output contains the actual 6 orbit representatives, the canonical solution checksum, a 336-automorphism construction and the Burnside sum. The second independently checks the same answers. A finite exhaustive program proves this finite theorem only because the generation rules, exact-cover completeness, and entire bounded enumeration are explicitly supplied; unexecuted logs alone are not offered as evidence.

## Relationship to prior work

The strong edge-coloring definition and general bounds are standard (Zang, first arXiv posting 2015-10-03). Skupień's paper, available by 2021 and published in 2023, proves the *existence* of a seven-class induced-matching decomposition of \(H\) and recalls that its strong chromatic index is seven. It proves unique induced-matching decomposition for the **Petersen** graph, not for the Heawood graph, and does not give the Heawood 416-decomposition census or its six symmetry orbit sizes. These earlier facts are not claimed here. The three ordinary perfect-matching edge partitions described in the Brouwer graph database are different objects: an ordinary matching need not be induced, and such a partition uses three classes rather than seven. The equivalence to proper vertex coloring of the square of the line graph is addressed by counting its proper seven-colorings; the result counts only the first nonempty optimal-color layer, not the entire chromatic polynomial.

## Limitations

This is a finite, explicitly reproducible enumeration for one canonical graph. It does not provide a symbolic closed formula for arbitrary incidence graphs or solve any open strong-edge-coloring upper-bound conjecture. Historical priority is qualified: indexed searches and the most plausible accessible primary full text did not reveal an equivalent enumeration, but inaccessible/unindexed sources, including the full 1993 Brualdi–Massey paper, could affect priority. No independent scholarly audit is asserted.

## References

1. C. Zang, *The Strong Chromatic Index of graphs with maximum degree \(\Delta\)*, first public arXiv posting 2015-10-03, https://arxiv.org/abs/1510.00785 (general definitions and bounds; not the new census).
2. Z. Skupień, *The Petersen and Heawood graphs make up graphical twins via induced matchings*, Discussiones Mathematicae Graph Theory 43 (2023), 677–683, https://doi.org/10.7151/dmgt.2394 (Heawood seven-color existence and Petersen uniqueness, not Heawood orbit enumeration).
3. A. E. Brouwer, *Heawood graph*, https://aeb.win.tue.nl/drg/graphs/Heawood.html (automorphism group and ordinary edge-matching partitions, distinguished from the new strong edge-coloring count).
4. R. A. Brualdi and J. J. Quinn Massey, *Incidence and strong edge colorings of graphs*, Discrete Mathematics 122 (1993), 51–58, https://doi.org/10.1016/0012-365X(93)90286-3 (related foundational work; complete text not inspected).
