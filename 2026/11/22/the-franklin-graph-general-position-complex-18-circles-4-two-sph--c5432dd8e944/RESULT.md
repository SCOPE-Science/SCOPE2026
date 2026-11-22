# The Franklin graph general-position complex: \(18\) circles, \(4\) two-spheres, and a rational quotient sphere

## Finding

Let \(F\) be the Franklin graph on \(V=\mathbb Z/12\mathbb Z\) with cycle edges \(\{i,i+1}\) for \(i\in V\) and chords \(\{2j,2j+5}\) for \(j=0,\ldots,5\), with all indices modulo twelve. Let \(X=\mathrm{GP}(F)\) consist of vertex subsets in graph-geodesic general position. Then

\[
|X|\simeq\bigvee^{18}S^1\vee\bigvee^4 S^2.
\]

For the full graph automorphism group \(G=\operatorname{Aut}(F)\), of order \(48\), the orbit space obeys

\[
\widetilde H_i(|X|/G;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=2,\\0,&i\ne2.\end{cases}
\]

The orbit-space assertion is about rational homology, not its integral homotopy type.

## Assumptions and scope

All graphs are finite, undirected, and simple. For distinct vertices \(a,b,c\), the triple is forbidden exactly when one of \(d(a,b)+d(b,c)=d(a,c)\) and its two analogous equalities holds. A nonempty subset is a face precisely when it contains no forbidden triple; the empty face is included conventionally. The graph \(F\) has twelve vertices, eighteen edges and diameter three. The automorphism group acts simplicially by permuting the graph's vertices. Reduced homology uses integer coefficients for \(X\) and rational coefficients for its orbit space. No other cubic graph or larger-order classification is claimed.

## Proof

**Exhaustive face calculation.** Compute distances by breadth-first search from each of the twelve vertices and iterate over all \(\binom{12}{3}\) unordered triples. Exactly \(144\) satisfy a geodesic equality above. Enumerating all \(2^{12}-1\) nonempty vertex masks and rejecting masks containing any forbidden triple yields the face vector \((12,66,76,45,12,2)\) in dimensions \(0,1,2,3,4,5\). Every iteration and comparison is explicit in `verify_franklin_gp.py`.

**Elementary simplicial collapses.** On the set of active nonempty faces, choose the first codimension-one pair \((\sigma,\tau)\) in descending coface size, then increasing integer mask order, for which \(\sigma\) has precisely one proper active coface, namely \(\tau\). Remove both and repeat until no such pair remains. The checker reconstructs each proper-coface condition directly from the current active set, and asserts \(56\) successive free-face pairs. The remaining two-dimensional complex has \(12\) vertices, \(57\) edges and \(32\) triangles, with no higher faces. Each pair removal is an elementary simplicial collapse and hence preserves homotopy type.

**Fundamental-group and attaching-map cancellation.** Choose a breadth-first spanning tree of the remaining connected one-skeleton from vertex \(0\), exploring neighbors in increasing label order. The checker verifies the tree has \(11\) edges. Contracting that tree preserves the homotopy type of the two-dimensional CW complex: it gives one vertex, \(57-11=46\) oriented loop generators, and \(32\) triangle attaching words. Use the graph edge orientations from smaller to larger endpoint to write each boundary \((a,b)+(b,c)+(c,a)\) as a freely reduced word, deleting tree edges.

Repeatedly choose the shortest attaching relator containing a loop generator \(x\) exactly once (with lexicographically fixed tie breaks). If this relator is \(U x V\), replace \(x\) everywhere by \(U^{-1}V^{-1}\); if it is \(U x^{-1}V\), replace \(x\) everywhere by \(VU\). Freely reduce each substituted word, then remove the selected relator and generator. This is an elementary CW cancellation after a change of free basis: the attaching map crosses the selected \(1\)-cell once with coefficient \(\pm1\), and substitution records the actual attaching words, not just their exponent sums. The checker verifies \(28\) such cancellations, leaving \(18\) loops and exactly \(4\) freely empty attaching words. All four remaining two-cells therefore have nullhomotopic attaching maps. The resulting CW complex is \(\bigvee^{18}S^1\vee\bigvee^4S^2\). This proves the integral homotopy statement and the absence of torsion, without inferring homotopy from Betti numbers alone.

**Full-symmetry quotient.** Enumerate graph automorphisms by an exact vertex-permutation backtracking algorithm, preserving adjacency and nonadjacency. It finds exactly \(48\) automorphisms. In degree \(k\), an invariant rational simplicial chain basis consists of the signed orbit sum of each oriented \(k\)-face whose stabilizer acts orientation-preservingly; an orientation-reversing stabilizer makes the corresponding invariant summand vanish. The checker exhaustively tests these conditions and finds invariant chain dimensions \((1,1,2,0,0,0)\). Direct signed boundary summation shows that the only nonzero invariant differential is from degree \(2\) to degree \(1\), with rank \(1\) (its two basis columns are \(2\) and \(-1\) up to the stated orbit conventions). Thus the invariant rational chain complex has reduced homology one-dimensional in degree \(2\) and zero elsewhere. Since \(G\) is finite and the coefficient field has characteristic zero, the rational chains of the quotient are naturally identified, after equivariant subdivision if needed, with the invariant rational chains. This proves the orbit-space homology formula.

## Verification

The self-contained `verify_franklin_gp.py` uses only the Python standard library and raises an assertion if any stated finite enumeration, free-face property, nonabelian word cancellation, automorphism condition, orbit sign, or invariant boundary rank fails. Running `python3 verify_franklin_gp.py` produces four `PASS` lines. Its checks cover all \(4096\) vertex masks and the complete \(48\)-element automorphism action; they are exhaustive finite certificates for the stated graph, not sampling experiments. Source graph and complex definitions, and the complete deterministic reductions, are included in the source.

## Relationship to prior work

Manuel and Klavžar (2017) introduced the general-position problem for graphs and studied extremal cardinalities. Iršič, Klavžar, Rus and Tuite (2024) studied the counting polynomial of such sets for several graph families. Neither of these inspected articles establishes the Franklin graph's full simplicial-complex homotopy or its symmetry quotient. Published calculations for the Franklin graph's Vietoris--Rips, dissociation, matching, dominance and cut complexes concern **different face predicates**, even when a homology rank happens to coincide. The Franklin graph's intrinsic importance includes its classical appearance in Klein-bottle coloring; the graph identification follows the standard LCF presentation. These comparisons do not establish absolute novelty against unindexed literature.

## Limitations

This is an exact result for a single natural twelve-vertex graph. No general formula for arbitrary cubic graphs, no characterization of larger graph families, no nontrivial Steenrod or multiplicative calculations, and no homotopy-type statement for the orbit space are asserted. The orbit-space calculation is only rational. The published literature search may not cover every unindexed work. All verification is reproducible but not independent external validation.

## References

1. Paul Manuel and Sandi Klavžar, *Graph theory general position problem*, arXiv:1708.09130v1 (first public 2017-08-30), https://arxiv.org/abs/1708.09130 .
2. Vesna Iršič, Sandi Klavžar, Gregor Rus and James Tuite, *General position polynomials*, arXiv:2401.05696v1 (first public 2024-01-11), https://arxiv.org/abs/2401.05696 .
3. Eric W. Weisstein, *Franklin Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/FranklinGraph.html .
4. Publicly indexed related result: *Franklin graph Rips filtration and its four-dimensional homology character*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-franklin-graph-rips-filtration-and-its-four-dimensional-homology--9adbac8c5856 .
5. Publicly indexed related result: *Equivariant integral homotopy of the Franklin two-independence complex*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-equivariant-integral-homotopy-of-the-franklin-two-independence-c--c651b44c82bb .
