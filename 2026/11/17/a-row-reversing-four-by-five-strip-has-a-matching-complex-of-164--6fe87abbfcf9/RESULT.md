# A row-reversing four-by-five strip has a matching complex of 164 six-spheres

## Finding

Let \(G\) be the four-row, five-column lattice graph with a row-reversing seam as specified below. Its ordinary matching complex, whose vertices are the edges of \(G\), has the exact integral homotopy type

\[
|\mathcal M(G)|\simeq\bigvee^{164}S^6.
\]

In particular, \(\widetilde H_6(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{164}\), with all other reduced integral homology zero. The complex has dimension nine, so this is a nontrivial collapse in dimension.

## Assumptions and scope

This is a claim about one finite simple graph, not an infinite family. Label vertices \(v(r,c)=5r+c\) with \(r\in\{0,1,2,3\}\) and \(c\in\{0,1,2,3,4\}\). There are 35 edges, ordered as follows: first all 15 vertical edges \(\{v(r,c),v(r+1,c)\}\) in increasing \(r\), then increasing \(c\); next all 16 horizontal edges \(\{v(r,c),v(r,c+1)\}\) in increasing \(r\), then increasing \(c\); finally the four seam edges \(\{v(r,4),v(3-r,0)\}\), in increasing \(r\). Only graph edges that share no endpoints may appear together in a face of \(\mathcal M(G)\). The empty face is present and is excluded from the ordinary CW matching.

The row-reversing seam makes the graph bipartite, unlike the odd-column untwisted cylinder; this boundary distinction motivates the comparison. Direct enumeration gives the reduced Euler characteristic \(164\), while the untwisted graph with seam \(\{v(r,4),v(r,0)\}\) has reduced Euler characteristic \(136\). These two Euler computations alone do not establish a homotopy equivalence.

## Proof

**1. Full finite face set.** Encode a matching by a 35-bit integer, with bit \(i\) indicating the \(i\)-th graph edge. Exhaustive recursion adds each edge if and only if neither endpoint is already occupied. It produces exactly \(255300\) faces, including the empty face, with nonempty face vector in dimensions zero through nine:

\[
(35,505,3910,17725,48197,77455,69770,31630,5820,252).
\]

**2. Acyclic face-poset matching.** Reserve the empty face. For each edge bit \(i\), in order \(i=0,1,\ldots,34\), pair every currently unmatched face \(F\) not containing bit \(i\) with \(F\cup\{i\}\), provided the latter is also a currently unmatched face. The resulting pairing has 127550 pairs. The unmatched cells consist of exactly one vertex, 181 six-cells and 17 seven-cells. To verify that the matching is acyclic, form the directed gradient-path graph whose vertices are matched upper faces \(U\), with an arrow from \(U\) to the upper mate of each other matched facet of \(U\). This directed graph has a full topological ordering of all 127550 vertices; hence there is no closed gradient path. All generated pairs are verified to be codimension-one incidences.

**3. Signed integral boundary.** Orient every simplex by the increasing edge-bit order. For each matched lower \(d\)-face \(L\) and upper \((d+1)\)-face \(U\), write the oriented boundary as \(\partial U=\varepsilon L+\sum_{L'\ne L}\varepsilon_{L'}L'\), with \(\varepsilon=\pm1\). Eliminating the pair replaces \(L\), in degree \(d\), by \(-\varepsilon\sum_{L'\ne L}\varepsilon_{L'}L'\), recursively until only critical degree-\(d\) cells remain. A degree-\(d\) face that is the upper member of a degree-\((d-1,d)\) pair projects to zero. The resulting integral Morse boundary from critical seven-cells to critical six-cells is a 181-by-17 signed integer matrix. Its exact entries are supplied as `MORSE_BOUNDARY.tsv`. Integer-only elementary row and column operations exhibit 17 successive unit pivots and a zero residual matrix, establishing that the boundary is a primitive rank-17 map between free abelian lattices.

**4. From the Morse model to homotopy.** Discrete Morse theory gives a CW complex with one zero-cell, 181 six-cells and 17 seven-cells, and no cells of dimensions one through five. Its six-skeleton is \(\bigvee^{181}S^6\), and \(\pi_6\) of this skeleton is its integral degree-six homology by Hurewicz. Therefore the attaching maps of the seven-cells are classified by their integer cellular degrees. The unit-pivot operations can be implemented as changes of basis of the six-sphere wedge and elementary CW cancellations, removing exactly 17 six/seven-cell pairs. The remaining CW complex is \(\bigvee^{164}S^6\), proving the claim.

**5. Second exact check.** Repeating the same toggle procedure in reverse edge order produces one vertex, one five-cell, 166 six-cells and one seven-cell. Acyclicity is checked again for all 127565 matched pairs. The signed five/six and six/seven boundaries each have unit rank one and compose to zero; their homology again gives 164 generators in degree six and none in degrees five and seven. This is a consistency test, independent of the forward matching order; the forward integral CW cancellation is the homotopy proof.

## Verification

Run `python3 verify_twisted_grid.py` with standard Python 3 (no third-party dependencies). Its single JSON output must agree exactly with `EXPECTED.json`. It recomputes all graph edges, all 255300 faces, the two complete matchings, every gradient acyclicity check, both signed Morse reductions, unit pivots, the boundary composition and the untwisted Euler comparison. `MORSE_BOUNDARY.tsv` records each nonzero entry and its critical face identifiers for the forward seven-to-six Morse differential. No numerical sample substitutes for an exhaustive finite check.

## Relationship to prior work

Chauhan, Sharma and Shukla (first public posting September 23, 2026) analyze matching-complex homology of ordinary rectangular three-row grids; their stated family does not contain this four-row twisted-seam graph. Matsushita's earlier work proves sphere wedges for two-row open grid matching complexes and a related generalized line-graph family, with a different graph specification. Agarwal and Basak treat independence and perfect-matching complexes of cubic Möbius ladders, which are distinct in graph and complex from the present ordinary matching complex. Existing indexed computations on three-row cylinders and on ordinary Möbius ladders likewise do not imply a result for the present 20-vertex, 35-edge strip. The conclusion is a finite homotopy classification with a verifiable integral incidence certificate, rather than a general periodicity theorem.

## Limitations

This result does not determine the homotopy types of arbitrary row-reversing grid strips, symmetry representations, or full persistence filtrations. The unit-cancellation certificate is finite and is not an infinite-family proof. The primary September 2026 three-row preprint could not be examined in full; its published object and stated scope are distinct, but unindexed coincident calculations remain a priority risk. Independent mathematical review has not been performed.

## References

- P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first public September 23, 2026. https://arxiv.org/abs/2609.27366
- T. Matsushita, *Matching complexes of small grids*, Electronic Journal of Combinatorics 26(3), P3.1 (2019), DOI:10.37236/8480. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i3p1
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, first public August 31, 2026. https://arxiv.org/abs/2608.30601
