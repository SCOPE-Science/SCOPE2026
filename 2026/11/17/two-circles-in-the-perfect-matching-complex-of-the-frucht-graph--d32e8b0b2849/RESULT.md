# Two circles in the perfect-matching complex of the Frucht graph

## Finding
Let \(F\) be the twelve-vertex Frucht graph and \(\mathcal P(F)\) its perfect-matching complex, with graph edges as vertices and a subset as a face exactly when it extends to a perfect matching. There is an **integral homotopy equivalence**
\[
\boxed{|\mathcal P(F)|\simeq S^1\vee S^1.}
\]
Consequently \(\pi_1(|\mathcal P(F)|)\cong \mathbb Z*\mathbb Z\), the free group of rank two, and \(\widetilde H_1(|\mathcal P(F)|;\mathbb Z)\cong\mathbb Z^2\), with all other reduced integral homology zero. The complex is pure of dimension five, yet not shellable. Exactly 29 of the 117 disjoint pairs of Frucht edges do not extend to perfect matchings.

## Assumptions and scope
Number the graph vertices \(0,\ldots,11\). Add edges \(\{i,i+1\}\), with indices modulo twelve, and chords \(\{i,i+s_i\}\), where the Lederberg–Coxeter–Frucht list is
\[
(s_0,\ldots,s_{11})=(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2).
\]
Remove duplicated undirected edges. This is the standard Frucht graph, with eighteen edges and degree three at every vertex. Order the edges lexicographically, starting from edge-label zero. A perfect matching is a six-edge subset covering all twelve vertices once. The perfect-matching complex consists of all subsets of all perfect matchings; **it is not** the ordinary matching complex. This is an exact result about this particular graph, not a family-level assertion or an equivariant classification.

## Proof
**Exhaustive facet enumeration.** Branch on the least unmatched graph vertex, choosing each of its available incident edges, and recurse on the remaining vertices. This lists every perfect matching exactly once: an arbitrary perfect matching contains exactly one incident edge at the chosen vertex. The eight facets, encoded as eighteen-bit sums of edge labels, in the resulting recursion order are
```
168481, 150561, 166026, 140554, 74290, 35026, 9554, 84108
```
A separate search through all \(2^{18}\) edge subsets tests six-edge covers of all twelve vertices and reproduces the same eight masks. The perfect-matching complex has the face counts, **including the empty face**, by cardinality zero through six:
```
1, 18, 88, 147, 118, 48, 8
```
Thus its eight facets all have dimension five, and the complex is pure.

**Exact nerve reduction.** Cover \(|\mathcal P(F)|\) by its eight full five-simplices. The intersection of any nonempty collection is either empty or a full simplex on the common graph edges, and hence contractible when nonempty. The finite simplicial nerve theorem therefore gives a homotopy equivalence between this complex and the nerve \(N\). Index the eight facets by recursion indices \(0,\ldots,7\); represent a simplex of \(N\) by its eight-bit characteristic mask. It is a nerve face exactly when the indexed perfect matchings have a common *graph edge*. The verifier independently constructs the nerve both from intersections of perfect-matching masks and by taking all subsets of the membership-index set of each graph edge. Both methods produce exactly 64 faces including the empty face, with cardinality counts
```
1, 8, 25, 22, 7, 1.
```

**Elementary collapses.** The standalone checker contains an explicit list of 26 ordered pairs of nerve-face masks \((\sigma,\tau)\). Before removing each pair it checks that \(\tau\) is the unique strict coface of \(\sigma\) in the current complex and that their dimensions differ by one. Hence each is a legal elementary simplicial collapse preserving homotopy type. The final complex is one-dimensional; its vertex masks are \(2,16,32,64,128\), and its edge masks are \(18,80,96,130,144,160\). The edge incidences are \((2,16),(16,64),(32,64),(2,128),(16,128),(32,128)\). This is connected, with five vertices and six edges. Every connected graph of cycle rank \(6-5+1=2\) is homotopy equivalent to the wedge of two circles. The nerve theorem and the elementary collapses give the displayed integral homotopy classification.

**Extendibility and shellability.** The ordinary matching complex has 117 unordered pairs of disjoint graph edges; exactly 88 are faces of the perfect-matching complex, leaving 29 nonextendible disjoint pairs. A pure shellable five-dimensional complex has reduced homology only in dimension five; the proved nonzero first homology excludes pure shellability.

## Verification
Execute `python3 verify.py` using Python 3 standard library. It builds the graph without external graph libraries; enumerates perfect matchings twice by independent algorithms; constructs every face of both the original complex and the nerve; checks both nerve definitions; tests each of the 26 proposed elementary collapses against the full surviving face set; and certifies the final connected graph and cycle rank. Its checked output is in `verification_output.txt`, including the exact 26 collapse pairs and remaining simplex masks. These finite exhaustive steps prove the particular finite graph claim; no infinite-family extrapolation or external certification is asserted.

## Relationship to prior work
Chbili (2011) studies the Frucht graph through its Tutte polynomial and graph periodicity; this does not establish perfect-matching-complex homotopy. Bayer, Jelić Milutinović and Vega (2022) define and investigate perfect-matching complexes of honeycomb graphs, not the Frucht graph. A publicly available 2026 Frucht-graph result establishes the distinct **ordinary matching complex** \(\mathcal M(F)\simeq\bigvee^{20}S^3\); its statement explicitly excludes perfect-matching complexes. Published work on the Franklin graph, despite the same number of graph vertices and edges, concerns a different graph and gives \(\bigvee^6 S^2\) for its perfect-matching complex. The present calculation is not a restatement or special case of those results.

## Limitations
This result treats the natural perfect-matching extendibility complex of one fixed twelve-vertex graph. It does not describe perfect-matching complexes of all asymmetric cubic, Halin or planar graphs; nor does it determine maps induced by changes to the graph. The novelty comparison relies on identified accessible literature and an indexed record search, not a proof of comprehensive publication priority. An independent mathematical audit has not been performed.

## References
1. Nafaa Chbili, *The Tutte polynomial and the automorphism group of a graph*, arXiv:1103.6134, publicly posted 2011-03-31. https://arxiv.org/abs/1103.6134
2. Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, 2022-09-06. https://arxiv.org/abs/2209.02803
3. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, 2026-08-31. https://arxiv.org/abs/2608.30601
4. Eric W. Weisstein, *Frucht Graph*, MathWorld, including the explicit LCF code. https://mathworld.wolfram.com/FruchtGraph.html
5. *A perfect Morse model for the Frucht-graph matching complex*, publicly indexed result (2026-10-25), distinguished from perfect-matching extendibility.
