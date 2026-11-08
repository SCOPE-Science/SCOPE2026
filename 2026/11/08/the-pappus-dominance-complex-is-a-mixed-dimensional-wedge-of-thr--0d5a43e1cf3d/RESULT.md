# The Pappus dominance complex is a mixed-dimensional wedge of three spheres

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, with the explicit graph model below. Its dominance complex is
\[\operatorname{Dom}(P)=\{S\subseteq V(P): V(P)\setminus S\text{ is a dominating set}\}.\]
There is an **integral homotopy equivalence**
\[\boxed{\operatorname{Dom}(P)\simeq S^8\vee S^8\vee S^9.}\]
Thus its only nonzero reduced integral homology groups are \(\widetilde H_8\cong\mathbb Z^2\) and \(\widetilde H_9\cong\mathbb Z\). This is a statement about homotopy, not just field homology or Euler characteristic.

## Assumptions and scope
Number the vertices \(0,1,\ldots,17\). The edges are the cycle \(\{i,i+1\bmod18\}\) for all \(i\), together with the chords \(\{i,i+d_i\bmod18\}\), where the displacement list is the six-term block \((5,7,-7,7,-7,-5)\) repeated three times. Repeated undirected chord descriptions are counted once. This is the standard LCF representation of the cubic bipartite Pappus incidence graph (27 edges). The closed neighborhood \(N[v]\) comprises \(v\) and its three neighbors.

A subset \(S\) is a face exactly when no \(N[v]\) is contained in \(S\); equivalently the complement of \(S\) intersects every closed neighborhood. The empty face is included in the abstract complex, but not as a geometric cell in the Morse calculation. All homotopy and homology statements use the ordinary geometric realization and integral coefficients; no symmetry representation or assertion about all incidence graphs is included.

## Proof
**Finite complex and an explicit matching.** Generate the graph exactly by the displacement list above, and enumerate all \(2^{18}=262144\) vertex subsets as eighteen-bit integers. The two equivalent face criteria are independently implemented and agree for every subset. There are 118562 nonempty faces. The face numbers in dimensions \(0\) through \(12\) are
\[(18,153,816,3042,8316,16953,25650,28134,21422,10575,3042,423,18).\]
The 281 inclusion-maximal faces occur in dimensions \(8,10,11,12\), with multiplicities \(2,72,189,18\), respectively; in particular, the complex is nonpure.

Use the following *exact, deterministic*, face-poset matching. Starting with every nonempty face unmatched, process vertex labels in the order
\[(8,10,16,7,11,13,6,5,1,14,3,4,2,9,0,15,12,17).\]
At each pivot \(v\), pair every still-unmatched face \(S\) not containing \(v\) with the still-unmatched coface \(S\cup\{v\}\), whenever both are faces. Every pair is a cover relation and each face is used at most once. The procedure gives **59279 pairs**, leaving precisely one critical vertex (mask 256), two critical eight-simplices (masks 87637 and 182954), and one critical nine-simplex (mask 187084). Here a mask means the integer \(\sum_{v\in S}2^v\), and dimensions equal cardinality minus one.

**Acyclicity.** Orient every unmatched face-poset cover from larger to smaller face, and reverse each matched cover. Construct this directed graph *on every one* of the 118562 nonempty faces, including all **900162** cover relations. The attached standalone checker uses Kahn's topological-sort algorithm, verifies every oriented indegree and visits all 118562 nodes. Therefore there is no directed cycle; the matching is a valid acyclic discrete-Morse matching in the sense of Forman. This finite exhaustive certificate is substantive: the claim of acyclicity does not come from sampled cases or from a successful timeout.

**Integral attaching degrees.** Orient every simplex by increasing vertex label. For every matched pair of an eight-face and a nine-coface, use the incidence coefficient \(\pm1\) as an integral unit pivot. Recursively eliminate lower matched eight-faces along the gradient relation; faces paired as upper eight-faces with seven-faces project to zero. Because the matching is acyclic, this recursion terminates. Project the oriented boundary of the unique critical nine-simplex onto the two critical eight-simplices. The resulting **exact integral Morse differential** is
\[\partial_9=(0\quad0).\]
The attached checker computes this row by summing *oriented* contributions and verifies both zeros over the integers, not just modulo a prime. There are no other critical cells in positive dimensions. Forman's theorem therefore provides a CW complex with one zero-cell, two eight-cells and one nine-cell. Its eight-skeleton is \(S^8\vee S^8\). The attaching map of the nine-cell lies in
\[\pi_8(S^8\vee S^8)\cong H_8(S^8\vee S^8;\mathbb Z)\cong\mathbb Z^2,\]
where the first isomorphism is Hurewicz because the eight-sphere wedge is seven-connected. The attaching-map degrees are exactly the Morse differential entries and both vanish, so the attaching map is nullhomotopic. Hence the Morse CW complex, and therefore the original dominance complex, is homotopy equivalent to \(S^8\vee S^8\vee S^9\).

**Separate matching cross-check.** Independently, processing pivots in the natural order \((0,1,\ldots,17)\) gives 59278 pairs, one critical vertex, three critical eight-cells and two critical nine-cells. Its exact integral ninth boundary matrix, written as rows indexed by the two nine-cells and columns by the three eight-cells, is
\[\begin{pmatrix}0&0&-1\\0&0&1\end{pmatrix}.\]
This unimodular rank-one matrix independently yields integral homology ranks \((2,1)\) in dimensions \((8,9)\); the more economical second matching above proves the full wedge statement without requiring a cancellation argument.

## Verification
Execute the included `pappus_dominance_verify.py` with Python 3 (standard library only). It recomputes graph edges, independently tests the domination and neighborhood face predicates for all 262144 subsets, validates all 118562 nonempty faces and their dimensional counts, constructs **both** matchings, and exhaustively verifies acyclicity on all 900162 cover relations for each. Exact signed boundary elimination returns the two matrices displayed above. The expected captured stdout is `pappus_dominance_verify_output.txt`; it concludes `INTEGRAL_PAPPUS_DOMINANCE_WEDGE_CHECK_PASS`. The full script—not just the log—is a reproducible finite certificate. The topological inference uses the discrete-Morse and Hurewicz theorems as stated in the proof.

## Relationship to prior work
The original dominance-complex work of Ehrenborg–Hetyei and Marietti–Testa established spherical behavior for **forests**, and Taylan extended structural results to **chordal** graphs. The Pappus graph is cubic, bipartite, of girth six and therefore is neither a forest nor chordal. Matsushita–Wakatsuki relate dominance complexes to Alexander-dual neighborhood constructions and classify other graph families; that duality does not by itself supply the Pappus homotopy type. The preexisting Pappus results for its matching and graph-Čech complexes use different faces and do not calculate this dominance complex. The mixed-dimensional integer homotopy type is the claimed contribution; no general dominance-complex framework is claimed as new.

## Limitations
This proves the exact homotopy type for the eighteen-vertex Pappus graph in the stated LCF labeling; no infinite-family result, automorphism-module decomposition, explicit equivariant splitting, or simple-homotopy classification is claimed. The computational part is exhaustive for this **one fixed finite** complex and is not a general algorithmic impossibility theorem. Searches of indexed mathematical records and relevant prior papers cannot establish exhaustive publication priority, and equivalent results outside the inspected literature remain possible. Independent mathematical audit has not been performed.

## References
- M. Marietti and D. Testa, *Cores of simplicial complexes*, arXiv:math/0703351v1 (first publicly posted 2007-03-12), Section 8 Theorem 8.1 on dominance complexes of forests. https://arxiv.org/abs/math/0703351
- M. Marietti and D. Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461v1 (first publicly posted 2007-05-10), dominance complexes in Section 4.3. https://arxiv.org/abs/0705.1461
- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first publicly posted 2015-01-27), chordal domination result, Section 5. https://arxiv.org/abs/1501.06754
- T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (first publicly posted 2023-12-05), duality theorem and graph-family applications. https://arxiv.org/abs/2312.02639
- E. W. Weisstein, *Pappus Graph*, MathWorld; standard eighteen-vertex LCF representation. https://mathworld.wolfram.com/PappusGraph.html
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145; the acyclic matching and Morse CW complex theorem.
