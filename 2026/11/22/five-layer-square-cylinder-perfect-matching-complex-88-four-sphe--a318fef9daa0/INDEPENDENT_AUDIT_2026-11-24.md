# Independent mathematical audit

## correctness

PASS

The input is the extendibility complex, not all matchings. In an independent exact implementation I generated the coordinate graph and branched on a remaining vertex of minimum remaining degree to enumerate 450 perfect matchings. Their nonempty subfaces number 183,543, all lying in ten-edge facets. A cover-count and XOR-of-covers reconstruction found 88,171 elementary collapse pairs, verifying membership, codimension, uniqueness of the cover and maximality of the upper face. The core has f-vector (36,427,1850,3129,1759). Contracting a spanning tree, the triangle relators eliminate each of the remaining 392 generators; a queue of triangles with one surviving edge rechecked this. Independent sparse integer row operations returned 392, 1458 and 1671 unit pivots for ∂2, ∂3 and ∂4, with zero remainders. Unit Smith factors ensure free cokernels and hence torsion-free homology; the boundary ranks and connectedness leave exactly Z^88 in degree four. With π1 trivial, Hurewicz gives representatives in π4 for a basis, and the resulting wedge map is a homology equivalence between simply connected CW spaces, hence a homotopy equivalence. Nonzero H4 rules out pure dimension-nine shellability. For the symmetry check I enumerated unions of whole edge-permutation cycles lying in some perfect matching, deduplicated across matchings. A nonempty union of c cycles contributes (−1)^(c+1) to the reduced alternating trace, and the empty union contributes −1. This directly reproduces the degree-four character on the original complex without relying on equivariant collapses. The trace pairs in lexicographic (k,s) order are (88,4),(8,4),(0,0),(0,−8),(0,12),(8,4),(0,0),(0,−8). Character inner products give the five stated pairs, including seven copies of the trivial representation.

## originality

PASS

The strongest catalogued neighbors differ in either the graph or the allowed partial matchings. The broader primary theorems treat cubic circular ladders and open three-row grids, neither of which includes the target. The supported distinct claim is the exact wedge and full natural rational character for this extendibility complex; no general family novelty is inferred.

## value

PASS

This canonical periodic analogue of an open four-by-five grid gives an exact benchmark for the extendible-matching topology of noncubic cylinders, where ladder theorems do not apply. The dimension drop from nine to four, pure nonshellability, and full symmetry splitting supply different information. In particular, retaining the path reversal as well as square symmetry distinguishes the two parity sectors and determines the precise seven-dimensional invariant space; a nonequivariant Betti computation would not answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
