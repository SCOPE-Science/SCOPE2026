# First chord-separation homotopy transition in Möbius-ladder perfect-matching complexes

## Finding
For \(n\ge3\), let \(M_{2n}\) be the graph on \(\{0,1,\ldots,2n-1\}\) with cycle edges \(\{i,i+1\bmod 2n\}\) and antipodal chords \(\{i,i+n\}\), \(0\le i<n\). For \(1\le d\le\lfloor n/2\rfloor\), delete the two chords \(\{0,n\}\) and \(\{d,n+d\}\), obtaining \(G_{n,d}\). Denote by \(\mathcal P(G)\) the simplicial complex whose maximal simplices are the perfect matchings of \(G\).

The complete integral homotopy classification for \(3\le n\le5\) is
\[
|\mathcal P(G_{3,1})|\simeq *,\qquad
|\mathcal P(G_{4,1})|\simeq |\mathcal P(G_{4,2})|\simeq S^0,
\]
\[
\boxed{\ |\mathcal P(G_{5,1})|\simeq S^1\vee S^1,\qquad
|\mathcal P(G_{5,2})|\simeq *\ }.
\]
In particular, \(M_{10}\) is the smallest Möbius ladder whose two-chord-deletion perfect-matching topology depends on the separation of the deleted antipodal chords. The classification is nonequivariant.

## Assumptions and scope
A perfect matching consists of \(n\) pairwise vertex-disjoint graph edges covering all \(2n\) graph vertices. A face of \(\mathcal P(G)\) is exactly a graph matching contained in some perfect matching. Two deleted chords are equivalent under the dihedral graph action precisely when their cyclic distance among the \(n\) chords agrees up to replacing \(d\) with \(n-d\); representatives have \(1\le d\le\lfloor n/2\rfloor\). The stated result makes no assertion for \(n\ge6\).

## Proof
We give finite, exact elementary-collapse certificates, not an extrapolation from homology computations. For each of the five pairs \((n,d)=(3,1),(4,1),(4,2),(5,1),(5,2)\), the accompanying `verify.py` constructs the edges of \(G_{n,d}\) from the formula above. It enumerates every perfect matching twice: once by independent combinations of \(n\) graph edges and once by recursive pairing of the least unused graph vertex. The two exact facet sets must coincide. All faces, including the empty face, are then enumerated as subsets of those facets.

The embedded `collapse_certificate.json` lists a sequence of pairs \((\sigma,\tau)\) of simplices for each case. The verifier checks at each deletion that \(\sigma\subset\tau\), \(|\tau|=|\sigma|+1\), both faces are present, and **\(\tau\) is the only strict coface of \(\sigma\) remaining in the entire complex**. Thus each removal is a genuine elementary simplicial collapse. It verifies equality of the resulting face set with the separately recorded terminal complex and checks that no terminal simplex has dimension above one. These are finite complete certificates: no random sampling and no rank-based inference of homotopy type.

The five certified numbers of collapse pairs are \(3,12,8,64,55\), respectively. Each terminal graph is described by the triple (vertices, edges, connected components): \((7,6,1),(10,8,2),(8,6,2),(13,14,1),(13,12,1)\). A finite graph with \(v\) vertices, \(e\) edges and \(c\) connected components is homotopy equivalent to a disjoint union of wedges of circles, with total circle rank \(e-v+c\). The first terminal graph is a tree; the next two are forests of two trees; the fourth is connected with circle rank \(2\); and the fifth is a tree. Elementary collapses preserve homotopy type, yielding exactly the claimed types.

## Verification
Run `python verify.py` from the package folder containing `collapse_certificate.json` and compare its output with `verification_output.txt`. The program uses Python 3 standard library only. It verifies all five graph constructions, exhaustive perfect-matching facet sets, every simplex removal, all terminal faces and the resulting graph invariants. The observed success sentinel is `DOUBLE_CHORD_MOBIUS_MATCHING_HOMOTOPY_PASS`.

## Relationship to prior work
Agarwal and Basak (2026, arXiv:2608.30601v1, first public August 31, 2026) determine the homotopy types for **unmodified** Möbius-ladder perfect-matching complexes; their section on perfect matchings is inspected. The present theorem asks a different, graph-edge-deletion question: two antipodal chords are removed, and their relative position changes the homotopy type at the first possible ladder order. An existing single-antipodal-chord deletion classification does not imply the double-deletion result, because deleting a graph edge can change the complete set of maximal matchings and all their overlaps. Earlier results on independence complexes after deleting a rung concern a different functor. The novelty claim is restricted to the two-deletion comparison and its sharp small-order threshold.

## Limitations
This is a complete finite classification for \(3\le n\le5\), not an infinite-family theorem. It determines nonequivariant integral homotopy types and does not determine the maps induced by successive graph-edge deletions. The computer-assisted proof is finite and exhaustive, with independently generated facets and replayed elementary-collapse certificates. A differently formulated prior enumeration could exist outside the inspected literature.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1, August 31, 2026, https://arxiv.org/abs/2608.30601 .
2. A. Hatcher, *Algebraic Topology*, 2002, elementary homotopy invariance and graph homotopy type.
