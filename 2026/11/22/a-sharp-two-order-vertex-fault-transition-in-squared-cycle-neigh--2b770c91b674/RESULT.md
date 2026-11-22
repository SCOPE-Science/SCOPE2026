# A sharp two-order vertex-fault transition in squared-cycle neighborhood complexes

## Finding
For \(n\in\{8,9\}\), let \(C_n^{(2)}\) be the simple graph with vertices \(\mathbb Z/n\mathbb Z\), where distinct vertices are adjacent exactly when their cyclic distance is one or two. Delete any one graph vertex to obtain \(H_n\). For the *open* Lovász neighborhood complex \(\mathcal N(H_n)\), whose nonempty simplices are vertex sets with a common adjacent graph vertex, one has the integral homotopy equivalences
\[
\mathcal N(H_8)\simeq S^1,\qquad
\mathcal N(H_9)\simeq S^1\vee S^1\vee S^1.
\]
These two orders straddle the first stable toroidal case of the intact squared-cycle family, showing that a single-vertex fault has a different loop response across that boundary. The assertion is **only** for orders eight and nine.

## Assumptions and scope
All graphs are simple, loopless and undirected. Graph deletion removes the selected vertex and its incident edges; the open-neighborhood complex is then reconstructed from the resulting graph, rather than taking an induced simplicial subcomplex of the original neighborhood complex. Rotational symmetry allows the deleted graph vertex to be residue zero. Statements concern ordinary integral homotopy type, and therefore also every coefficient field. No assertion is made for other cycle orders or about inclusion-induced maps.

## Proof
Write the remaining graph vertices as \(1,\dots,n-1\). Enumerate the complex exactly as the union of simplices on
\[
N_{H_n}(c)=\{w\in\{1,\ldots,n-1\}:w\ne c,\ \min((w-c)\bmod n,(c-w)\bmod n)\le2\},
\quad 1\le c\le n-1.
\]
This definition enumerates **all** faces: a set belongs to the complex if and only if it is contained in at least one such neighborhood.

Apply the following completely specified acyclic matching on the nonempty face poset. Initially mark every nonempty face unmatched. For successive pivots \(p=1,\ldots,n-1\), consider every currently unmatched pair of faces \((\sigma,\sigma\cup\{p\})\) with \(p\notin\sigma\), in increasing order of \((|\sigma|,\mathrm{sorted}(\sigma))\); if both are still unmatched, pair and remove them from the unmatched pool. This finite rule depends only on the displayed graph and is replayed by `checker.py`.

For \(n=8\), the procedure matches 22 pairs among 46 nonempty faces, leaving precisely the critical vertex \(\{1\}\) and edge \(\{2,3\}\). For \(n=9\), it matches 27 pairs among 58 nonempty faces, leaving precisely vertex \(\{1\}\) and edges \(\{2,3\},\{2,6\},\{4,8\}\). The attached exact checker constructs the complete face Hasse diagram, reverses precisely the matched cover relations, and verifies by an exhaustive topological sort that the resulting directed graph is acyclic in each case. Thus these are genuine discrete Morse matchings, not merely proposed pair counts.

Forman's discrete Morse theorem gives a CW model with exactly one zero-cell and respectively one or three one-cells, and no cells of higher dimension. The attaching maps of one-cells to a single zero-cell are necessarily constant, so the two CW models are respectively a circle and a three-circle wedge. This establishes the stated integral homotopy types.

## Verification
Run `python3 checker.py` with the Python standard library. It independently enumerates every neighborhood simplex, pairs cells, checks that every cell is used at most once, checks the complete directed Hasse graph for cycles, and compares the exact critical-cell lists. The expected output includes `PASS 8 nonempty_faces 46 matched_pairs 22` and `PASS 9 nonempty_faces 58 matched_pairs 27`. Exact finite certificates establish precisely the two orders claimed; no experimental extrapolation is used.

## Relationship to prior work
The open-neighborhood complex and the intact 4-regular circulant family were studied by Shukla (first publicly available February 13, 2018). The intact \(n=8\) and \(n=9\) cases lie on opposite sides of the exceptional-order versus stable-torus boundary. Those results do not calculate the neighborhood complexes after graph-vertex deletion. The present two-case classification concerns that altered graph and has separate explicit Morse certificates. General classifications of unpunctured cycle powers do not imply the asserted punctured homotopy types without a deletion analysis.

## Limitations
No general \(n\ge9\) formula, induced map on homology, equivariant action, or independent external validation is claimed. The exact certificates depend on the chosen standard cyclic labeling, but graph rotation makes the selected deletion representative of every graph vertex. An unindexed equivalent computation may exist.

## References
- Samir Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first posted February 13, 2018; Electronic Journal of Combinatorics 26(2) (2019), P2.4, https://arxiv.org/abs/1802.04526 and https://doi.org/10.37236/7549.
